import numpy as np

class Graph():

    # static
    SAMP = 1000
    INTERVAL_MILLIS = 5
    MAX_FRAMES = 9999
    XLIMIT = 10

    # changeable
    YLIMIT = 2
    TITLE = "wave"

    # This fucntion is called for every frame. X is the graph x and t is the 
    # time or frame.
    @staticmethod
    def f(x, t):
        sin = Graph.Waves.sin;tria = Graph.Waves.triangle;squa = Graph.Waves.square;saw = Graph.Waves.saw
        return sin(x, .6, .4*(sin(t*.02, w=.5)+1), 0) + .5*saw(x)

    class Waves():

        @staticmethod
        def sin(x, a=1., w=1., p=0.):
            return a*np.sin(2*np.pi*w*x+p)

        @staticmethod
        def triangle(x, a=1., w=1., p=0.):
            return a*(2*np.abs(2*((x*w+p)/(2*np.pi)-np.floor((x*w+p)/(2*np.pi)+.5)))-1)

        @staticmethod
        def saw(x, a=1., w=1., p=0.):
            return a*(2*((x*w+p)/(2*np.pi)-np.floor((x*w+p)/(2*np.pi)+.5)))

        @staticmethod
        def square(x, a=1., w=1., p=0.):
            return a*np.sign(np.sin(2*np.pi*w*x+p))


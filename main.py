import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import myGraph
from myGraph import Graph as gr
import os
import importlib
import time
import threading

def main():
    GRAPH_FILE_PATH = "./myGraph.py"
    QUIT = False

    def hotReload():
        global gr
        fileTStamp = os.path.getmtime(GRAPH_FILE_PATH)
        while True:
            newTStamp = os.path.getmtime(GRAPH_FILE_PATH)
            if (fileTStamp < newTStamp):
                gr = importlib.reload(myGraph).Graph
                fileTStamp = newTStamp
                print("updating graph")
            time.sleep(1)
            if(QUIT):
                break

    x = np.linspace(-gr.XLIMIT, gr.XLIMIT, gr.SAMP)
    y = np.sin(x)
    fig, ax = plt.subplots()
    ln, = ax.plot(x, y)
    plt.plot(x,y)

    def update(frame):
        ax.clear()
        new_y = gr.f(x, frame)
        ax.plot(x, new_y);
        ax.set_title(gr.TITLE)
        ax.set_xlim(-gr.XLIMIT-.2, gr.XLIMIT+.2)
        ax.set_ylim(-gr.YLIMIT, gr.YLIMIT)
        return ln,

    ani = FuncAnimation(fig, update, frames=np.arange(0, gr.MAX_FRAMES), interval=gr.INTERVAL_MILLIS)
    hrt = threading.Thread(target=hotReload)
    hrt.start()
    plt.show()
    QUIT = True

if __name__ == "__main__":
    main()

import pandas as pd
from tkinter import *
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk

libro = "servi.xlsx"
df = pd.read_excel(libro, header=0, delim_whitespace=True)
tabla = df[["media", "humedad", "temperatura", "fechahora"]]

aX=tabla.get("fechahora")
aY=tabla.get("temperatura")
bX=tabla.get("fechahora")
bY=tabla.get("humedad")

class raiz(Tk):
    def __init__(self):
        super(raiz, self).__init__()
        self.title("Tkinter con graficas Matplotlib")
        self.minsize(1280, 700)
        self.matplotCanvas()

    def matplotCanvas(self):
        f = Figure(figsize=(11, 7), dpi=100)
        a = f.add_subplot(211)
        a.plot(aX,aY)
        canvas = FigureCanvasTkAgg(f, self)
        canvas.draw()
        g = Figure(figsize=(11, 7), dpi=100)
        b = f.add_subplot(212)
        b.plot(bX, bY)
        canvas2 = FigureCanvasTkAgg(g, self)
        canvas2.draw()
        canvas.get_tk_widget().pack(side=TOP, fill=X, expand=True)

root = raiz()
root.mainloop()

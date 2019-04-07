#*********************************************************
#           LIBRERÍAS NECESARIAS
#*********************************************************
from tkinter import *
from tkinter import font
from tkinter import messagebox
from tkinter import ttk
import numpy as np
from numpy import *
import matplotlib.backends.tkagg as tkagg
from matplotlib.backends.backend_agg import FigureCanvasAgg
#*********************************************************

#*********************************************************
#          CONFIFGURACIÓN LA VENTANA PRINCIPAL
#*********************************************************
class GUI(Tk):
  def __init__(self, *args, **kwargs):
    self.main = Tk()
    #*****************************************************
    #         APARIENCIA PARA NUESTRA VENTANA
    #*****************************************************
    self.main.title("Holographic Microscope")
    self.main.geometry("1200x480+50+100")
    self.main.minsize(1100, 480)
    self.main.maxsize(1366, 768)
    frame = Frame(self.main, width = 650, height = 20)
    frame.pack(side = "top", anchor = "n")
    #*****************************************************
    #                 TIPOS DE LETRA
    #*****************************************************
    title_font = font.Font(family = "Helvetica", size = 20, weight = "bold", slant = "italic")
    Arial16 = font.Font(family = "Arial", size = 16)
    Arial14 = font.Font(family = "Arial", size = 14)
    Arial12 = font.Font(family = "Arial", size = 12)
    #*****************************************************
    #                  BARRA DE MENU
    #*****************************************************
    barMenu = Menu(self.main)
    menuArchivo = Menu(barMenu)
    menuHelp = Menu(barMenu)
    menuArchivo.add_command(label = "Abrir")
    menuArchivo.add_separator()
    menuArchivo.add_command(label = "Guardar")
    menuArchivo.add_command(label = "Guardar como")
    menuArchivo.add_separator()
    menuArchivo.add_command(label = "Salir", command = quit)
    menuHelp.add_command(label = "Ayuda con la teoría")
    menuHelp.add_command(label = "Acerca de 'Holographic Microscope'")
    barMenu.add_cascade(label = "Archivo", menu = menuArchivo)
    barMenu.add_cascade(label = "Help", menu = menuHelp)
    #*****************************************************
    #              DISEÑO DE LA VENTANA
    #*****************************************************
    label = Label(frame, text = "Holographic Microscope", font = title_font)
    label.pack(side = "top", fill = "x", pady = 10)
    #*****************************************************
    #  NOTA: Ingresar frames para los axis y los botones
    #*****************************************************
    self.main.config(menu = barMenu)
    self.main.mainloop()

  def axis(canvas, figure, loc=(0,0)):
    figure_canvas = FigureCanvasAgg(figure)
    figure_canvas.draw()
    figure_x, figure_y, figure_w, figure_h = figure.bbox.bounds
    figure_w, figure_h = int(figure_w), int(figure_h)
    photo = tk.PhothoImage(master = canvas, width = figure_w, height = figure_h)
    canvas.create_image(loc[0] + figure_w/2, loc[1] + figure_h/2, image = photo)
    tkagg.blit(photo, figure_canvas.get_render()._render, colormode = 2)
    return photo

def mainp():
    my_GUI = GUI()
    return (0)

if __name__ == "__main__":
    mainp()
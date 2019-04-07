#*********************************************************
#           LIBRERÍAS NECESARIAS
#*********************************************************
from tkinter import *
from tkinter import font
from tkinter import messagebox
from tkinter import ttk
import numpy as np
from numpy import *
#*********************************************************

#*********************************************************
#          CONFIFGURACIÓN GENERAL PARA LA GUI
#*********************************************************
class GUI(Tk):
  def __init__(self, *args, **kwargs):
    Tk.__init__(self, *args, **kwargs)
    #*****************************************************
    #                TIPOS DE LETRAS
    #*****************************************************
    type_words = "Arial"
    self.title_font = font.Font(family = "Helvetica", size = 20, weight = "bold", slant = "italic")
    self.font20 = font.Font(family = type_words, size = 20)
    self.font16 = font.Font(family = type_words, size = 16)
    self.font14 = font.Font(family = type_words, size = 14)
    self.font12 = font.Font(family = type_words, size = 12)
    self.font10 = font.Font(family = type_words, size = 10)
    #*****************************************************
    #              APARIENCIEA DE LA GUI
    #*****************************************************
    self.title("Holographic Microscope")
    self.geometry("1366x768+0+0")
    #*****************************************************
    #        CONFIGURACIÓN DE LA BARRA DE MENU
    #*****************************************************
    barMenu = Menu(self)
    menuArchivo = Menu(barMenu)
    menuHelp = Menu(barMenu)
    menuArchivo.add_command(label = "Abrir")
    menuArchivo.add_separator()
    menuArchivo.add_command(label = "Guardar")
    menuArchivo.add_command(label = "Guardar como")
    menuArchivo.add_separator()
    menuArchivo.add_command(label = "Salir", command = quit)
    barMenu.add_cascade(label = "Archivo", menu = menuArchivo)
    barMenu.add_cascade(label = "Ayuda", menu = menuHelp)
    
    helpGUI = Menu(menuHelp)
    help_holography = Menu(helpGUI)
    
    menuHelp.add_cascade(label = "Ayuda para la teoría", menu = helpGUI)
    helpGUI.add_cascade(label = "Holografía")
    menuHelp.add_separator()
    menuHelp.add_command(label = "Acerca de Holographic Microscope")
    
    self.config(menu = barMenu)
    
    #*****************************************************
    #       ALGORTIMO PARA USAR SOLO UNA VENTANA
    #*****************************************************
    container = Frame(self)
    container.pack(side = "top", fill = "both", expand = True)
    container.grid_rowconfigure(0, weight = 1)
    container.grid_columnconfigure(0, weight = 1)
    
    self.frames = {}
    
    for F in (main):
      page_name = F.__name__
      frame = F(parent = container, controller = self)
      self.frames[page_name] = frame
      
      frame.grid(row = 0, column = 0, sticky = "nsew")
    
    self.show_frame("main")
  
  def show_frame(self, page_name):
    '''Show a frame for the give page name'''
    frame = self.frames[page_name]
    frame.tkraise()

class main(Frame):
  def __init__(self, controller):
    Frame.__init__(self, parent)
    controller = self.controller
    label = Label(self, text = "Holographic Microscope", font = controller.title_font)
    label.pack(side = "top", fill = "x", pady = 10)

if __name__ == "__main__":
  app = GUI()
  app.mainloop()
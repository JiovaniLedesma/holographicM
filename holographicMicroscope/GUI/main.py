# **********************************************************************************************************************
#           LIBRERÍAS NECESARIAS
# **********************************************************************************************************************
from tkinter import *
from tkinter import font
from tkinter import messagebox
from tkinter import ttk
import numpy as np
from numpy import *
import matplotlib as mpl
import matplotlib.pyplot as plt
import matplotlib.backends.tkagg as tkagg
from matplotlib.backends.backend_agg import FigureCanvasAgg
from holographicMicroscope.holography_algorithms import *

# from PIL import Image, ImageTk
# **********************************************************************************************************************

# **********************************************************************************************************************
#          CONFIFGURACIÓN LA VENTANA PRINCIPAL
# **********************************************************************************************************************
class GUI(Tk):
    def __init__(self, *args, **kwargs):
        self.main = Tk()
        # **************************************************************************************************************
        #         APARIENCIA PARA NUESTRA VENTANA
        # **************************************************************************************************************
        self.main.title("Microscopio Holográfico Digital")
        self.main.geometry("1200x480+0+0")
        self.main.minsize(700, 380)
        self.main.maxsize(800, 480)
        frame1 = Frame(self.main, width=700, height=30)
        frame1.pack(side="top", anchor="n")
        # **************************************************************************************************************
        #                 TIPOS DE LETRA
        # **************************************************************************************************************
        title_font = font.Font(family="Helvetica", size=16, weight="bold", slant="italic")
        Arial16 = font.Font(family="Arial", size=16)
        Arial14 = font.Font(family="Arial", size=14)
        Arial12 = font.Font(family="Arial", size=12)
        Arial11 = font.Font(family="Arial", size=11)

        color_background = "#B9B9B9"
        # **************************************************************************************************************
        #                  BARRA DE MENU
        # **************************************************************************************************************
        barMenu = Menu(self.main)
        menuArchivo = Menu(barMenu)
        menuHelp = Menu(barMenu)
        menuArchivo.add_command(label="Abrir")
        menuArchivo.add_separator()
        menuArchivo.add_command(label="Guardar")
        menuArchivo.add_command(label="Guardar como")
        menuArchivo.add_separator()
        menuArchivo.add_command(label="Salir", command=self.main.destroy)
        menuHelp.add_command(label="Ayuda con la teoría")
        menuHelp.add_command(label="Acerca de 'Microscopio Holográfico Digital'")
        barMenu.add_cascade(label="Archivo", menu=menuArchivo)
        barMenu.add_cascade(label="Ayuda", menu=menuHelp)
        # **************************************************************************************************************
        #              DISEÑO DE LA VENTANA
        # **************************************************************************************************************
        label = Label(frame1, text="Microscopio Holográfico Digital", font=title_font, bg=color_background)
        label.pack(side="top", anchor="n", pady=10)
        # **************************************************************************************************************
        #                     LOGO
        # **************************************************************************************************************
        # self.logo = Image.open("img/upg.png")
        # resized = self.logo.resize((80,40), Image.ANTIALIAS)
        logoUPG = PhotoImage(file="img/upg_redimensionado.png")
        Label(self.main, image=logoUPG, height=40).place(x=710, y=0)
        # **************************************************************************************************************
        #                 FRAME GRÁFICAS
        # **************************************************************************************************************
        frame2 = Frame(self.main, width=600, height=480)
        frame2.pack(side="bottom", anchor="w")
        # **************************************************************************************************************
        #                     AXES 1
        # **************************************************************************************************************
        w1, h1 = 100, 100
        axes1 = Canvas(frame2, width=w1, height=h1)
        axes1.grid(row=0, column=0, padx=5, pady=5)
        # **************************************************************************************************************
        #               EJEMPLO PARA AXES 1
        # **************************************************************************************************************
        X1 = np.linspace(0, 2 * np.pi, 50)
        Y1 = np.sin(X1)
        fig1 = plt.figure(figsize=(1, 1))
        ax1 = fig1.add_axes([0, 0, 1, 1])
        ax1.plot(X1, Y1)
        fig1_x, fig1_y = 0, 0
        fig1_photo = self.ax(axes1, fig1, loc=(fig1_x, fig1_y))
        fig1_w, fig1_h = fig1_photo.width(), fig1_photo.height()
        axes1.create_line(100, 0, fig1_x + fig1_w / 2, fig1_y + fig1_h / 2)
        # **************************************************************************************************************
        #                LABEL PARA AXES 1
        # **************************************************************************************************************
        Label(frame2, text="Vista de cámara", font=Arial12, bg=color_background).grid(row=1, column=0, padx=5, pady=5)
        # **************************************************************************************************************
        #            SEPARACIÓN ENTRE AXES 1 y 2
        # **************************************************************************************************************
        Label(frame2, text=" ", bg=color_background).grid(row=0, column=1, padx=5)
        # **************************************************************************************************************
        #                     AXES 2
        # **************************************************************************************************************
        w2, h2 = 100, 100
        axes2 = Canvas(frame2, width=w2, height=h2)
        axes2.grid(row=0, column=2, padx=5, pady=5)
        # **************************************************************************************************************
        #               EJEMPLO PARA AXES 2
        # **************************************************************************************************************
        X2 = np.linspace(0, 2 * np.pi, 50)
        Y2 = np.sin(X2)
        fig2 = plt.figure(figsize=(1, 1))
        ax2 = fig2.add_axes([0, 0, 1, 1])
        ax2.plot(X2, Y2)
        fig2_x, fig2_y = 0, 0
        fig2_photo = self.ax(axes2, fig2, loc=(fig2_x, fig2_y))
        fig2_w, fig2_h = fig2_photo.width(), fig2_photo.height()
        axes2.create_line(100, 0, fig2_x + fig2_w / 2, fig2_y + fig2_h / 2)
        # **************************************************************************************************************
        #                LABEL PARA AXES 2
        # **************************************************************************************************************
        Label(frame2, text="Fase\n(Espectro de Fourier)", font=Arial12, bg=color_background).grid(row=1, column=2,
                                                                                                  padx=5, pady=5)
        # **************************************************************************************************************
        #            SEPARACIÓN ENTRE AXES 2 y 3
        Label(frame2, text=" ", bg=color_background).grid(row=0, column=3, padx=10)
        # **************************************************************************************************************
        #                     AXES 3
        # **************************************************************************************************************
        w3, h3 = 100, 100
        axes3 = Canvas(frame2, width=w3, height=h3)
        axes3.grid(row=0, column=4, padx=5, pady=5, sticky="n")
        # **************************************************************************************************************
        #               EJEMPLO PARA AXES 3
        # **************************************************************************************************************
        X3 = np.linspace(0, 2 * np.pi, 50)
        Y3 = np.sin(X3)
        fig3 = plt.figure(figsize=(1, 1))
        ax3 = fig3.add_axes([0, 0, 1, 1])
        ax3.plot(X3, Y3)
        fig3_x, fig3_y = 0, 0
        fig3_photo = self.ax(axes3, fig3, loc=(fig3_x, fig3_y))
        fig3_w, fig3_h = fig3_photo.width(), fig3_photo.height()
        axes3.create_line(100, 0, fig3_x + fig3_w / 2, fig3_y + fig3_h / 2)
        # **************************************************************************************************************
        #            SEPARACIÓN ENTRE AXES 3 y 4
        Label(frame2, text=" ", bg=color_background).grid(row=2, column=4, pady=5)
        # **************************************************************************************************************
        #                     AXES 4
        # **************************************************************************************************************
        w4, h4 = 100, 100
        axes4 = Canvas(frame2, width=w4, height=h4)
        axes4.grid(row=4, column=4, padx=5, pady=2)
        # **************************************************************************************************************
        #               EJEMPLO PARA AXES 4
        # **************************************************************************************************************
        X4 = np.linspace(0, 2 * np.pi, 50)
        Y4 = np.sin(X3)
        # fig4 = mpl.figure.Figure(figsize = (2, 2))
        fig4 = plt.figure(figsize=(1, 1))
        ax4 = fig4.add_axes([0, 0, 1, 1])
        ax4.plot(X4, Y4)
        fig4_x, fig4_y = 0, 0
        fig4_photo = self.ax(axes4, fig4, loc=(fig4_x, fig4_y))
        fig4_w, fig4_h = fig4_photo.width(), fig4_photo.height()
        axes4.create_line(100, 0, fig4_x + fig4_w / 2, fig4_y + fig4_h / 2)
        # **************************************************************************************************************
        #                LABEL PARA AXES 4
        # **************************************************************************************************************
        Label(frame2, text="Reconstruir", font=Arial12, bg=color_background).grid(row=5, column=4, padx=5, pady=5)
        # **************************************************************************************************************
        #             LABEL PARA SLIDER (Z)
        # **************************************************************************************************************
        Label(frame2, text="Z", font=Arial11, bg=color_background).grid(row=3, column=0, columnspan=3, padx=5)
        # **************************************************************************************************************
        #               SLIDER (Z)
        # **************************************************************************************************************
        Slider = Scale(frame2, from_=-100, to=100, length=400, tickinterval=20, orient=HORIZONTAL, bg=color_background)
        Slider.set(0)
        Slider.grid(row=4, column=0, columnspan=3, padx=5, pady=10, sticky="n")
        # **************************************************************************************************************
        #               COMBOBOX PARA SLIDER (Z)
        # **************************************************************************************************************
        unidades = ttk.Combobox(frame2, font=Arial12, width=10)
        unidades.grid(row=4, column=3, padx=5, pady=10, sticky="n")
        unidades["values"] = ["-", "milímetros", "micras"]
        # **************************************************************************************************************
        #               LABEL PARA EL COMBOBOX
        # **************************************************************************************************************
        Label(frame2, text="Unidades:", font=Arial12, bg=color_background).grid(row=3, column=3, padx=5)
        # **************************************************************************************************************
        #                       BOTONES
        # **************************************************************************************************************
        # Label(frame2, text = "", font = Arial11, bg = color_background).grid(row = 1, column = 5, padx = 5, pady = 5)
        btn_iniciar = Button(frame2, text="Iniciar", font=Arial11, width=9, height=1, borderwidth=2, cursor="hand2")
        btn_iniciar.grid(row=1, column=6, padx=5, pady=5)
        # Label(frame2, text = "", font = Arial11, bg = color_background).grid(row = 2, column = 5, padx = 5, pady = 5)
        btn_reconstruir = Button(frame2, text="Reconstruir", font=Arial11, width=9, height=1, borderwidth=2,
                                 cursor="hand2")
        btn_reconstruir.grid(row=2, column=6, padx=5, pady=5)
        # Label(frame2, text = "", font = Arial11, bg = color_background).grid(row = 3, column = 5, padx = 5, pady = 5)
        btn_capturar = Button(frame2, text="Capturar", font=Arial11, width=9, height=1, borderwidth=2, cursor="hand2")
        btn_capturar.grid(row=3, column=6, padx=5, pady=5)
        # Label(frame2, text = "", font = Arial11, bg = color_background).grid(row = 4, column = 5, padx = 5, pady = 5)
        btn_salir = Button(frame2, text="Salir", font=Arial11, width=9, height=1, borderwidth=2, cursor="hand2",
                           command=self.main.destroy)
        btn_salir.grid(row=4, column=6, padx=5, pady=5)
        # **************************************************************************************************************
        self.main.config(menu=barMenu, background=color_background)
        frame1.config(background=color_background)
        frame2.config(background=color_background)
        self.main.mainloop()

    def ax(self, canvas, figure, loc=(0, 0)):
        figure_canvas = FigureCanvasAgg(figure)
        figure_canvas.draw()
        figure_x, figure_y, figure_w, figure_h = figure.bbox.bounds
        figure_w, figure_h = int(figure_w), int(figure_h)
        photo = PhotoImage(master=canvas, width=figure_w, height=figure_h)
        canvas.create_image(loc[0] + figure_w / 2, loc[1] + figure_h / 2, image=photo)
        tkagg.blit(photo, figure_canvas.get_renderer()._renderer, colormode=2)
        return photo

    # ******************************************************************************************************************
    #     Funciones para el funcionamiento de los componentes de la GUI
    # ******************************************************************************************************************
    def iniciar(self, image):
      self.Hog, self.ker, self.lamda = off_axis(image)

    def slider_funtion(self, valor_unidades, valor_slider):
        if valor_unidades == '-': messagebox.showwarning(
            'Precaución", "Revise que esta eligiendo alguna unidad para el Slider')
        if ((valor_unidades != '')or(valor_unidades != '-')):
            if valor_unidades == 'milímetros':
                valor = 1e-3
            if valor_unidades == 'micras':
                valor = 1e-6
            v_slider = valor_slider * valor

            int = slider(v_slider, self.Hog, self.ker, self.lamda)


def mainp():
    my_GUI = GUI()
    return (0)


if __name__ == "__main__":
    mainp()

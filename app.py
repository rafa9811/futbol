from tkinter.ttk import *
from tkinter import *
import sys

sys.path.append("..")
from excel.extract import *
from pdf.createpdf import *

class App():
    def __init__(self):
        self.inicial()

    def inicial(self):
        self.root = Tk()
        self.root.title('RefApp')
        self.root.geometry('350x200')
        lbl = Label(self.root, text="Bienvenido a RefApp", padx=65, pady=10, font=("Helvetica Bold", 20))
        lbl.grid(column=0, row=0)
        btn1 = Button(self.root, pady=10, text="Elaborar previa de partido", command=self.btn1)
        btn2 = Button(self.root, pady=10, text="Introducir datos de jornada", command=self.btn2)
        btn1.grid(column=0, row=1)
        btn2.grid(column=0, row=2)
        self.root.mainloop()

    def principal(self):
        self.wprevia.destroy()
        self.inicial()

    def btn1(self):
        self.root.destroy()
        self.wprevia = Tk()
        self.wprevia.title('RefApp')
        self.wprevia.geometry('350x200')
        lbl = Label(self.wprevia, text='Elaborar previa de partido', padx=50, pady=10, font=("Helvetica Bold", 20))
        lbl.grid(column=0, row=0)

        lblocal = Label(self.wprevia, text='Equipo local')
        combolocal = Combobox(self.wprevia, state='readonly')
        combolocal['values']= tuple(get_teams())
        lblocal.grid(column=0, row=1)
        combolocal.grid(column=0, row=2)

        lbvis = Label(self.wprevia, text='Equipo visitante')
        combovisitante = Combobox(self.wprevia, state='readonly')
        combovisitante['values']= tuple(get_teams())
        lbvis.grid(column=0, row=3)
        combovisitante.grid(column=0, row=4)

        atras = Button(self.wprevia, text="Atrás", command=self.principal)
        atras.grid(column=0, row=6)
        elaborar = Button(self.wprevia, text="Elaborar", command= lambda: createpdf(combolocal.get(), combovisitante.get()))
        elaborar.grid(column=0, row=5)
        self.wprevia.mainloop()

    def btn2(self):
        self.root.destroy()
        wintroduce = Tk()
        wintroduce.title('RefApp')
        wintroduce.geometry('350x200')
        wintroduce.mainloop()


app = App()

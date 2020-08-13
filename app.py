from tkinter.ttk import *
from tkinter import *
from tkcalendar import Calendar, DateEntry
import sys

sys.path.append("..")
from excel.extract import *
from pdf.createpdf import *
from gamedata.gamedata import *

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
        btn2 = Button(self.root, pady=10, text="Obtener datos de jornada", command=self.btn2)
        btn1.grid(column=0, row=1)
        btn2.grid(column=0, row=2)
        self.root.mainloop()

    def principal(self):
        self.wprevia.destroy()
        self.inicial()

    def principal2(self):
        self.wget.destroy()
        self.inicial()

    def btn0(self):
        self.root.destroy()
        self.group = Tk()
        self.group.title('RefApp')
        self.group.geometry('350x200')
        lbl = Label(self.group, text='Seleccione grupo', padx=50, pady=10, font=("Helvetica Bold", 20))
        lbl.grid(column=0, row=0)

        lbgroup = Label(self.group, text='Grupo')
        group = Combobox(self.group, state='readonly')
        group['values']= tuple(['1', '2'])
        lbgroup.grid(column=0, row=1)
        group.grid(column=0, row=2)

        atras = Button(self.group, text="Atrás", command=self.principal)
        atras.grid(column=0, row=3)
        siguiente = Button(self.group, text="Siguiente", command= lambda: self.btn1(group))
        siguiente.grid(column=0, row=4)
        self.group.mainloop()

    def btn1(self):
        self.root.destroy()
        self.wprevia = Tk()
        self.wprevia.title('RefApp')
        self.wprevia.geometry('620x250')
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

        s = Style(self.wprevia)
        s.theme_use('clam')
        lcal = Label(self.wprevia, text='Introduzca la fecha del partido')
        calendar = Button(self.wprevia, text='Abrir calendario', command=self.calendar)
        lcal.grid(column=1, row=1)
        calendar.grid(column=1, row=2)

        atras = Button(self.wprevia, text="Atrás", command=self.principal)
        atras.grid(column=1, row=6)
        elaborar = Button(self.wprevia, text="Elaborar", command= lambda: createpdf(combolocal.get(), combovisitante.get()))
        elaborar.grid(column=0, row=6)
        self.wprevia.mainloop()

    def btn2(self):
        self.root.destroy()
        self.wget = Tk()
        self.wget.title('RefApp')
        self.wget.geometry('350x200')
        get1 = Button(self.wget, text="Cargar grupo 1", command= lambda: gd_toFile('1'))
        get1.grid(column=0, row=1)
        get2 = Button(self.wget, text="Cargar grupo 2", command= lambda: gd_toFile('2'))
        get2.grid(column=0, row=2)
        atras = Button(self.wget, text="Atrás", command=self.principal2)
        atras.grid(column=0, row=3)
        self.wget.mainloop()

    def calendar(self):
        def proc_date():
            self.matchdate = cal.selection_get()
            cal.destroy()
            top.destroy()
            print(self.matchdate)

        top = Toplevel(self.wprevia)
        cal = Calendar(top,
                       font="Arial 14", selectmode='day',
                       cursor="hand1", year=2020, month=8, day=13)
        cal.pack(fill="both", expand=True)
        Button(top, text="Seleccionar", command=proc_date).pack()


app = App()

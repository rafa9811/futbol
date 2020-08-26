from datetime import datetime, timedelta
from tkinter.ttk import *
from tkinter import *
from tkinter import messagebox
from tkcalendar import Calendar, DateEntry
import sys

sys.path.append("..")
from excel.extract import *
from pdf.createpdf import *
from gamedata.gamedata import *

class App():
    def __init__(self):
        self.matchdate = None
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
        def check_create():
            if self.matchdate == None or combolocal.get() == '' or combovisitante.get() == '':
                messagebox.showwarning('Error', 'Antes de elaborar la previa debe seleccionar una fecha, equipo local y equipo visitante.')
            else:
                refteam = [tarb1.get(), tarb2.get(), tarb3.get(), tdel.get()]
                nweek = (datetime.now() + timedelta(days=7)).date()
                today = (datetime.now()).date()
                if nweek <= self.matchdate:
                    r = messagebox.askyesno('Atención', 'Si selecciona una fecha con más de siete días de diferencia: \n\n(1) Puede que los datos no estén actualizados al no haberse completado alguna jornada.\n(2) La previsión meteorológica no estará disponible.\n\n¿Desea continuar?')
                    if r == True:
                        createpdf(combolocal.get(), combovisitante.get(), None, refteam, ttime.get())
                elif today > self.matchdate:
                    messagebox.showwarning('Error', 'El partido no puede jugarse en el pasado.')
                elif today == self.matchdate:
                    r = messagebox.askyesno('Atención', 'No es posible obtener la meteorología del mismo día del partido. ¿Desea continuar?')
                    if r == True:
                        createpdf(combolocal.get(), combovisitante.get(), None, refteam, ttime.get())
                else:
                    createpdf(combolocal.get(), combovisitante.get(), str(self.matchdate), refteam, ttime.get())

        self.root.destroy()
        self.wprevia = Tk()
        self.wprevia.title('RefApp')
        self.wprevia.geometry('850x280')
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
        lcal = Label(self.wprevia, text='Seleccione la fecha del partido')
        calendar = Button(self.wprevia, text='Abrir calendario', command=self.calendar)
        lcal.grid(column=1, row=1)
        calendar.grid(column=1, row=2)

        ltime = Label(self.wprevia, text='Introduzca la hora del partido')
        ttime = Entry(self.wprevia)
        ltime.grid(column=1, row=4)
        ttime.grid(column=1, row=5)

        larb1 = Label(self.wprevia, text='Árbitro')
        tarb1 = Entry(self.wprevia)
        larb2 = Label(self.wprevia, text='Árbitro asistente 1')
        tarb2 = Entry(self.wprevia)
        larb3 = Label(self.wprevia, text='Árbitro asistente 2')
        tarb3 = Entry(self.wprevia)
        ldel = Label(self.wprevia, text='Delegado de partido')
        tdel = Entry(self.wprevia)

        laux = Label(self.wprevia, text='            ')
        laux.grid(column=2, row=1)

        larb1.grid(column=3, row=1)
        tarb1.grid(column=3, row=2)
        larb2.grid(column=3, row=3)
        tarb2.grid(column=3, row=4)
        larb3.grid(column=3, row=5)
        tarb3.grid(column=3, row=6)
        ldel.grid(column=3, row=7)
        tdel.grid(column=3, row=8)

        atras = Button(self.wprevia, text="Atrás", command=self.principal)
        atras.grid(column=1, row=8)
        elaborar = Button(self.wprevia, text="Elaborar", command=check_create)
        elaborar.grid(column=0, row=8)
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

        date = datetime.now().date()
        top = Toplevel(self.wprevia)
        cal = Calendar(top,
                       font="Arial 14", selectmode='day',
                       cursor="hand1", year=date.year, month=date.month, day=date.day)
        cal.pack(fill="both", expand=True)
        Button(top, text="Seleccionar", command=proc_date).pack()


app = App()

import tkinter
from tkinter import ttk
from tkinter import messagebox
from tkinter import filedialog


root = tkinter.Tk()
root.title("Boliglån kalkulator")
root.geometry("1280x720")
root.wm_resizable(width=False, height=False)

def ValError(steg):
    messagebox.showerror(title="Verdifeil", message="""En eller flere verdier er ugyldig eller tømme. Sjekk hva du har skrevet inn og prøv igjen. 
    (Steg""" + str(steg) + ")")

bp = False

def Betalingsplan():
    global bp
    cont = 1
    string = """"""
    try:
        la = float(loanamount.get())
    except ValueError:
        ValError(1)
        cont = 0
    try:
        if cont == 1:
            te = int(terminer.get())
    except ValueError:
        ValError(2)
        cont = 0
    try:
        if cont == 1:
            re = float(renter.get())
            re = re / 100
    except ValueError:
        ValError(3)
        cont = 0
    try:
        if cont == 1:
            bi = int(biler.get())
    except ValueError:
        ValError(4)
        cont = 0
    try:
        if cont == 1:
            ba = int(barn.get())
    except ValueError:
        ValError(5)
        cont = 0
    try:
        if cont == 1:
            eg = float(egenkapittel.get())
    except ValueError:
        ValError(6)
        cont = 0
    if cont == 1:
        if eg >= (la * 0.2):
            string = string + """Du har fått 1% mindre i rente fordi du har egenkapittel som er 20% eller mer av lånbeløpet.
"""
            re -= 0.01
        if ba >= 2.0:
            string = string + """Du har fått 1.5% mer i rente fordi du har 2 barn eller mer.
"""
            re += 0.015
        if bi >= 2.0:
            string = string + """Du har fått 0.5% mer i rente fordi du har 2 biler eller mer.
"""
            re += 0.005
        tb = round(la / float(te), 2)
        rl = la
        string = string + "Du har " + str(round(re * 100, 2)) + """% i rente.
"""
        string = string + "Ditt avdrag for hvert termin skal være " + str(tb) + """kr.
"""
        for termin in range(te):
            string = string + "Termin " + str(termin + 1) + ": " + str(round(rl, 2)) + "kr i restlån, " + str(round(rl * re, 2)) + "kr i rente. Du må betale: " + str(round(tb + (rl * re), 2)) + """kr.
"""
            rl -= tb
        bplan.config(state="normal")
        bplan.delete("1.0", "end")
        bplan.insert("1.0", string)
        bplan.config(state="disabled")
        bp = True

def SavePlan():
    global bp
    if bp:
        f = filedialog.asksaveasfile(filetypes=[("Text Document", "*.txt")], initialfile="Betalingsplan.txt", mode="w")
        f.write(bplan.get("1.0", "end"))
        f.close()
    else:
        messagebox.showinfo(title="Kan ikke lagre", message="Du ikke har en betalingsplan!")

tkinter.Label(root, text="Boliglån kalkulator", font=('Segoe UI', '50')).place(x=10, y=10)

tkinter.Label(root, text="Hvor mye du ønsker å låne?", font=('Segoe UI', '15')).place(x=10, y=125)
loanamount = ttk.Entry(root, font=('Segoe UI', '9'))
loanamount.place(x=10, y=165, width=200)
tkinter.Label(root, text="kr", font=('Segoe UI', '9')).place(x=210, y=165)
tkinter.Label(root, text="Hvor mange terminer vil dette lånet ha?", font=('Segoe UI', '15')).place(x=10, y=195)
terminer = ttk.Entry(root, font=('Segoe UI', '9'))
terminer.place(x=10, y=235, width=30)
tkinter.Label(root, text="Hva er rente for lånet ditt?", font=('Segoe UI', '15')).place(x=10, y=265)
renter = ttk.Entry(root, font=('Segoe UI', '9'))
renter.place(x=10, y=305, width=200)
tkinter.Label(root, text="%", font=('Segoe UI', '9')).place(x=210, y=305)
tkinter.Label(root, text="Hvor mange biler har du?", font=('Segoe UI', '15')).place(x=10, y=335)
biler = ttk.Entry(root, font=('Segoe UI', '9'))
biler.place(x=10, y=375, width=30)
tkinter.Label(root, text="Hvor mye barner har du?", font=('Segoe UI', '15')).place(x=10, y=405)
barn = ttk.Entry(root, font=("Segoe UI", "9"))
barn.place(x=10, y=445, width=30)
tkinter.Label(root, text="Hvor mye har du i egenkapittel?", font=('Segoe UI', '15')).place(x=10, y=475)
egenkapittel = ttk.Entry(root, font=('Segoe UI', '9'))
egenkapittel.place(x=10, y=515, width=200)
tkinter.Label(root, text="kr", font=('Segoe UI', '9')).place(y=515, x=210)

ttk.Style().configure(style="submit.TButton", font=('Segoe UI', '15'))
ttk.Button(root, text="Regne ut betalingsplan", style="submit.TButton", command=Betalingsplan).place(x=10, y=600, width=605)

ttk.Separator(root, orient="vertical").place(x=625, y=0, height=720)

tkinter.Label(root, text="Betalingsplan", font=('Segoe UI', '50')).place(x=650, y=10)
bplan = tkinter.Text(root, font=('Segoe UI', '9'))
bplan.place(x=650, y=120, height=520, width=600)
bplan.insert("1.0", chars="""Når betalingsplan ditt var regnte ut,
du vil se det her.""")
bplan.config(state="disabled")
scroll = ttk.Scrollbar(root, command=bplan.yview)
bplan["yscrollcommand"] = scroll.set
scroll.place(y=120, x=1250, width=20, height=520)

ttk.Button(root, text="Lagre betalingsplan", style="submit.TButton", command=SavePlan).place(x=800, y=640, width=300)

root.mainloop()
import tkinter
from tkinter import ttk


root = tkinter.Tk()
root.title("Boliglån kalkulator")
root.geometry("1280x720")
root.wm_resizable(width=False, height=False)

tkinter.Label(root, text="Boliglån kalkulator", font=('Segoe UI', '50')).place(x=10, y=10)

tkinter.Label(root, text="Hvor mye du ønsker å låne?", font=('Segoe UI', '15')).place(x=10, y=125)
loanamount = ttk.Entry(root, font=('Segoe UI', '9'))
loanamount.place(x=10, y=165, width=200)
tkinter.Label(root, text="kr", font=('Segoe UI', '9')).place(x=210, y=165)
tkinter.Label(root, text="Hvor mange terminer vil dette lånet ha?", font=('Segoe UI', '15')).place(x=10, y=195)
terminer = ttk.Entry(root, font=('Segoe UI', '9'))
terminer.place(x=10, y=235, width=30)
tkinter.Label(root, text="Hva er rente for lånet ditt?", font=('Segoe UI', '15')).place(x=10, y=265)
rente = ttk.Entry(root, font=('Segoe UI', '9'))
rente.place(x=10, y=305, width=200)
tkinter.Label(root, text="%", font=('Segoe UI', '9')).place(x=210, y=305)
tkinter.Label(root, text="Hvor mange biler har du?", font=('Segoe UI', '15')).place(x=10, y=335)
biler = ttk.Entry(root, font=('Segoe UI', '9'))
biler.place(x=10, y=375, width=30)
tkinter.Label(root, text="Hvor mye barner har du?", font=('Segoe UI', '15')).place(x=10, y=405)
barn = ttk.Entry(root, font=("Segoe UI", "9"))
barn.place(x=10, y=445, width=30)
tkinter.Label(root, text="Hvor mye du har i egenkapittel?", font=('Segoe UI', '15')).place(x=10, y=475)
egenkapittel = ttk.Entry(root, font=('Segoe UI', '9'))
egenkapittel.place(x=10, y=515, width=200)
tkinter.Label(root, text="kr", font=('Segoe UI', '9')).place(y=515, x=210)

root.mainloop()
from tkinter import *



pencere = Tk()

pencere.title("Felix Sunucuları Çalışanları")
pencere.geometry("400x300")


uygulama = Frame(pencere)
uygulama.grid()

Lb1 = Listbox(uygulama)
Lb1.insert(1, "AryenN (Sahibi)")
Lb1.insert(2, "GlestG (Sahibi)")
Lb1.insert(3, "PunchOut (Yönetim)")
Lb1.insert(4, "Github")
Lb1.grid(padx=110, pady=10)


pencere.mainloop()


# https://hizliresim.com/7HQx0X

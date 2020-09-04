from tkinter import *
from tkinter import messagebox
from time import *

pencere = Tk()

pencere.title("MessageBox Tkinter AryenN")
pencere.geometry("500x250")

uygulama = Frame(pencere)  # Frame ( pencere içerisinde kullanabilecek olduğumuz pencereler )
uygulama.grid()


def dialog():
    var = messagebox.showinfo("Deneme", "Çalışıyor")
    print(var)
    sleep(2) # bekletme/uyutma süresi
    yok = messagebox.askyesnocancel("Tıkla","2 sn sonrasındaki hata")
    if yok == True:
        return dialog()
button1 = Button(uygulama, text="HATA", width=20,
                 command=dialog)
button1.grid(padx=110, pady=80)  # Grid ( Butonun olduğu piksel koordinatı )

# pencereyi ekranda tut
pencere.mainloop()

# 2 saniye bekleterek durmadan hata veren messagebox 
# https://hizliresim.com/rQBhVY
# https://hizliresim.com/18pbcX
# https://hizliresim.com/ip4zh1

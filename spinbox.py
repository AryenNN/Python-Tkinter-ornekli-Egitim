from tkinter import *
pencere = Tk()
pencere.geometry("400x300")
pencere.title("AryenN Spinbox Deneme")

def yaz():
	print(deger.get())

deger=IntVar()

secim=Spinbox(pencere,from_=0, to=10, width=5, textvariable=deger, command=yaz)
secim1=Spinbox(pencere,from_=2, to=20,increment=2, width=5 )

secim.pack()
secim1.pack()

secim_Gun=Spinbox(pencere,from_=1, to=31, width=5)
secim_Ay=Spinbox(pencere, values=("Ocak","Şubat","Mart","Nisan","Mayıs","Haziran","Temmuz","Ağustos","Eylül","Ekim","Kasım","Aralık"),  width=12)
secim_yil=Spinbox(pencere, bg="blue", fg="#C0C0C0", font=12, from_=1900, to=2015,  width=5)

secim_Gun.pack(side=LEFT)
secim_Ay.pack(side=LEFT)
secim_yil.pack(side=LEFT)

pencere.mainloop()

# https://hizliresim.com/NoGsCk

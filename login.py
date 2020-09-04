from tkinter import *
pencere = Tk()
pencere.title("AryenN Giriş")
pencere.geometry("700x500")
asilisim="aryen"
asilparola="aryenn"
def girisyapma():
    parola = parolagiris.get()  # Get ( Entry içerisindeki verileri alır ) bu veriler elde edilirken string tipinde veri olarak kullanılıyor !
    isim = isimgiris.get()
    if (parola == asilparola and isim == asilisim):
        girisdurumu.config(text="Doğru",bg="green")
    else:
        girisdurumu.config(text="Yanlış",bg="red")

isim = Label(pencere,text = "adınız")
isim.grid(row=0,column=0)
isimgiris = Entry(pencere,width="8")
isimgiris.grid(row=0,column=1)
parola = Label(pencere,text="şifreniz")
parolagiris = Entry(pencere,width="8",show="*") # Entry ( Girilen Alan ) Width ( Satır sayısı ) Show ( Gösterilen sembol )
parola.grid(row=1,column=0)
parolagiris.grid(row=1,column=1)
parolamihatirla =Checkbutton(pencere,text="şifremi hatırla")
parolamihatirla.grid(row=2,columnspan=2)
giris = Button(pencere,text="giriş",command=girisyapma)
giris.grid(row=3,column=0)
girisdurumu = Label(pencere,text="")
girisdurumu.grid(row=3,column=1)

pencere.mainloop()

# https://hizliresim.com/rPNWSi

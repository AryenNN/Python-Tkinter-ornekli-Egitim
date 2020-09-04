from tkinter import *
pencere = Tk()
pencere.title("AryenN")
pencere.geometry("800x600")

# Frame yazdım ancak şu anda kullanmadım altta bulunan kodlarda da zaten belli oluyor frame kullanılmamıştır istersen silebilirsin Orospu Ayten

frame1 = Frame(pencere)
frame1.pack()
frame2 = Frame(pencere)
frame2.pack()

rakam1 = Button(text = "C#",fg="red",bg="yellow")
rakam2 = Button(text = "AryenN",fg="blue",bg="yellow")
rakam3 = Button(text = "AryenN2",fg="green",bg="yellow")

# Pack() Butonları ekrana getirten kod ,yukarıdaki butonları tanımlamış olmak butonları ekrana getirtmez getirten şey alttaki gavattır kısacası pack burada yapıştır anlamında kullanılmaktadır

rakam1.pack()
rakam2.pack()
rakam3.pack(side = LEFT)

# side özelliği butonun nerede gözükmesini sağlar

yazi = Label(text = "AryenNNN")

yazi.pack()
pencere.mainloop()

# ekrana durmasını sağlayan ( mainloop() )

# https://hizliresim.com/I6xGpD

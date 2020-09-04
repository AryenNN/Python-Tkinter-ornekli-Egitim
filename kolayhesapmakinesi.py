import tkinter as tk


def hesapmakinesi(event):
    res.configure(text="Sonuç: " + str(eval(entry.get())))


w = tk.Tk()
baslik = w.title("Hesap Makinesi - AryenN")
w.geometry("325x125")

tk.Label(w, text="İşlemi Giriniz:").pack()
entry = tk.Entry(w)
entry.bind("<Return>", hesapmakinesi)
entry.pack()
res = tk.Label(w)
res.pack()
w.mainloop()

# https://hizliresim.com/X9rGyS

from tkinter import *
import random
from tkinter import messagebox

root = Tk()  # переменная рут есть окно тк

root.title("Random door")  # название окна

b = 0
dr1 = 0
dr2 = 1





def clicked():
    def bth3ran():
        bth1.configure(state=ACTIVE)
        bth2.configure(state=ACTIVE)
        bth1.configure(command=bth3ran)
        bth2.configure(command=bth3ran)
        def on_closing():
            if messagebox.askokcancel("ВНИМАНИЕ!", "Кто прочитал тот здохнет"):
                window.destroy()
                root.destroy()

        def clicked1():

            global b
            window.destroy()
            bth1.configure(state=ACTIVE)
            bth2.configure(state=ACTIVE)
            lbl2 = Label(root, text=b)
            lbl2.grid(row=0, column=3)
        c = random.randint(0, 10)  # управление рандомом дверь 3

        if dr1 or dr2 and c:
            global b
            b += 1
            lbl2 = Label(root, text=b)
            lbl2.grid(row=0, column=3)

        else:
            window = Tk()
            window.title("СМЭРТ")
            window.geometry('230x100')
            Label(window, text="Конец пути." + " Ты прошел " + str(b) + " дверь(ей).").grid(column=0, row=0)
            bth1.configure(state=DISABLED)
            bth2.configure(state=DISABLED)
            bth3.configure(state=DISABLED)
            Button(window, text="Начать сначала", command=clicked1).grid(row=1, column=0)
            b = 0
            window.protocol("WM_DELETE_WINDOW", on_closing)
            window.mainloop()




    def on_closing():
        if messagebox.askokcancel("ВНИМАНИЕ!", "Кто прочитал тот здохнет"):
            window.destroy()
            root.destroy()
    def clicked1():

        global b
        window.destroy()
        bth1.configure(state=ACTIVE)
        bth2.configure(state=ACTIVE)
        lbl2 = Label(root, text=b)
        lbl2.grid(row=0, column=3)


    c = random.randint(0, 13)  # управление рандомом дверь 1 и 2

    if dr1 or dr2 and c:
        global b

        b += 1
        lbl2 = Label(root, text=b)
        lbl2.grid(row=0, column=3)
        if b <= 5:  # третья дверь
            bth3.configure(state=DISABLED)
        else:
            bth1.configure(state=DISABLED)
            bth2.configure(state=DISABLED)
            bth3.configure(state=ACTIVE, command=bth3ran)






    else:
        window = Tk()
        window.title("СМЭРТ")
        window.geometry('230x100')
        Label(window, text="Конец пути."+" Ты прошел "+str(b)+" дверь(ей).").grid(column=0, row=0)
        bth1.configure(state=DISABLED)
        bth2.configure(state=DISABLED)
        bth3.configure(state=DISABLED)
        Button(window, text="Начать сначала", command=clicked1).grid(row=1, column=0)
        b = 0
        window.protocol("WM_DELETE_WINDOW", on_closing)
        window.mainloop()


bth1 = Button(root, text="Дверь 1", command=clicked)
bth1.grid(row=2, column=1)
bth1.config(height=17, width=10)
bth2 = Button(root, text="Дверь 2", command=clicked)
bth2.grid(row=2, column=2)
bth2.config(height=17, width=10)

bth3 = Button(root, text="Дверь 3", command=clicked)
bth3.grid(row=2, column=3)
bth3.config(height=17, width=10)
bth3.configure(state=DISABLED)


lbl1 = Label(root, text="Количество пройденных дверей:")
lbl1.grid(row=0, column=2)
lbl2 = Label(root, text=b)
lbl2.grid(row=0, column=3)

root.mainloop()
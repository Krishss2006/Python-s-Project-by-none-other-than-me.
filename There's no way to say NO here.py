from tkinter import*
from tkinter import messagebox
import pyautogui
import random

root = Tk()
root.geometry("450x600")
root.title("Survey")
def yes():
    messagebox.showinfo("Accepted","Yeah! Thankyou for accpeting.")
    root.overrideredirect(False)



def gotme():
    messagebox.showinfo("Got me","You got me.")
def movetoo(event):
    x_D,y_D=[],[]
    x_ = random.randint(0,300)
    
    y_ = random.randint(0,500)
    button_2.place(x=x_,y=y_-69)

label_1 = Label(root, text="Kya app pagal hain?")
label_1.pack(pady=5)

label_2 = Label(root, text="Click on yes button to get close window option 🙂. ")
label_2.pack(pady=4)
button_1 = Button(root, text="Offcorse Yes! I am.", command=yes)
button_1.pack(pady=10)


button_2 = Button(root,text="Offcourse No!\n Bet you! you can't get me",command=gotme)
button_2.pack(pady=10)
button_2.bind("<Enter>", movetoo)


root.overrideredirect(True)
root.mainloop()

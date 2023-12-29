



from tkinter import *
from tkinter import messagebox
import random

def no():
    messagebox.showinfo(' ', 'Thanks for true speak')
    quit()

def motionMouse(event):
    btnYes.place(x=random.randint(0, 300), y=random.randint(0, 300))

root = Tk()
root.geometry('400x400')
root.title('survey')
root.resizable(width=False, height=False)
root['bg'] = 'white'

label = Label(root, text="Are you 18+?", font="Arial 20 bold", bg="white").pack()
btnYes = Button(root, text="Yes", font="Arial 20 bold")
btnYes.place(x= 120, y=100)
btnYes.bind('<Enter>', motionMouse)
btnNo = Button(root, text="No", font="Arial 20 bold", command=no).place(x=210, y=100)

root.mainloop()



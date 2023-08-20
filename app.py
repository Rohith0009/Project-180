from googletrans import Translator
from tkinter import *

root = Tk()
root.title("idk")
root.geometry("1600x1600")
root.config(bg="pale green")

head = Label(root, text="Mr Translator", font=("Arial", 40), bg="pale green")
head.place(anchor=CENTER, relx=0.5, rely=0.06)

Et = Label(root, text="Enter Text", font=("Arial", 25), bg="pale green")
Et.place(anchor=CENTER, relx=0.5, rely=0.17)

TextArea = Text(root, font=("Arial", 20), wrap=WORD, height=10, bd=0, padx=10, pady=10)
TextArea.place(anchor=CENTER, relx=0.5, rely=0.4)

root.mainloop()

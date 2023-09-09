from googletrans import Translator
import googletrans
from tkinter import *
from tkinter import ttk

root = Tk()
root.title("idk")
root.geometry("1600x1600")
root.config(bg="pale green")

ll = list(googletrans.LANGUAGES.values())


head = Label(root, text="Mr Translator", font=("Arial", 40), bg="pale green")
head.place(anchor=CENTER, relx=0.5, rely=0.05)

Et = Label(root, text="Enter Text", font=("Arial", 25), bg="pale green")
Et.place(anchor=CENTER, relx=0.5, rely=0.14)

TextAreaIN = Text(root, font=("Arial", 20), wrap=WORD, height=7, bd=0, padx=10, pady=10)
TextAreaIN.place(anchor=CENTER, relx=0.5, rely=0.32)

OutLabel = Label(root, text="Output", font=("Arial", 25), bg="pale green")
OutLabel.place(anchor=CENTER, relx=0.45, rely=0.62)

LangOut = ttk.Combobox(root, state="readonly", values=ll, width=20)
LangOut.place(anchor=CENTER, relx=0.55, rely=0.62)

TextAreaOUT = Text(
    root, font=("Arial", 20), wrap=WORD, height=7, bd=0, padx=10, pady=10
)
TextAreaOUT.place(anchor=CENTER, relx=0.5, rely=0.8)


def TranslateF():
    src = "english"
    dest = LangOut.get()
    text = TextAreaIN.get(1.0, END)
    translator = Translator()

    try:
        translated = translator.translate(text=text, src=src, dest=dest)
        TextAreaOUT.delete(1.0, END)
        TextAreaOUT.insert(END, translated.text)
    except:
        print("Try Again.")


btn = Button(
    root, font=("Arial", 25), text="Translate", bg="pale turquoise", command=TranslateF
)
btn.place(anchor=CENTER, relx=0.5, rely=0.53)

root.mainloop()

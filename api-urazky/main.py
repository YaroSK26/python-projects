import requests
from tkinter import *

window = Tk()
window.title("Insult Generator")
window.geometry("300x300")
window.resizable(False, False)
window.configure(bg='lightgrey')

def insult():
    response = requests.get(f"https://evilinsult.com/generate_insult.php?lang={dropdown.get()}&type=json")
    data = response.json()
    insult_label.config(text=data["insult"])

dropdown = StringVar(window)
dropdown.set("cs")
dropdown_menu = OptionMenu(window, dropdown, "cs", "en", "es", "fr")
dropdown_menu.pack(pady=10)

insult_button = Button(window, text="Generate insult", command=insult)
insult_button.pack(pady=10)

insult_label = Label(window, text="", width=50, wraplength=250, justify="center", font=("Helvetica", 12), bg='lightgrey')
insult_label.pack(pady=10)

window.mainloop()
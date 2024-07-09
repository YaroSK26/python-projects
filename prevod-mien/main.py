from tkinter import * 
import os

window = Tk()
window.title("Prevod mien")
window.minsize(500, 500)
window.resizable(False, False)


script_dir = os.path.dirname(os.path.realpath(__file__))
icon_path = os.path.join(script_dir, "icon.ico")
window.iconbitmap(icon_path)


window.configure(bg="black")


def count_currency():
    amount = float(amount_input.get())
    result = amount / 25.15
    result_label["text"] = round(result, 2)


amount_input = Entry(window, width=10, font=("Arial", 20))
amount_input.grid(row=0, column=0, padx=10, pady=10)

czk_label = Label(window, text="CZK", font=("Arial", 20), bg="black", fg="white")
czk_label.grid(row=0, column=1)

result_label = Label(window, text="0", font=("Arial", 20), bg="black", fg="white")
result_label.grid(row=1, column=0)

eur_label = Label(window, text="EUR", font=("Arial", 20), bg="black", fg="white")
eur_label.grid(row=1, column=1)

count_button = Button(window, text="Prepocitat", font=("Arial", 20), bg="black", fg="white", command=count_currency)
count_button.grid(row=0, column=2 , padx=10, pady=10)


window.mainloop()
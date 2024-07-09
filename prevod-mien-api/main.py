from tkinter import *
import requests

main_color = "#14085f"
window = Tk()
window.title("Money App")
window.resizable(False, False)
window.geometry("400x150")
window.config(bg=main_color)

def count():
    try:
        user_input_number = float(user_input.get())
        url = f"https://api.exchangerate-api.com/v4/latest/{dropdown.get()}"
        data = requests.get(url).json()
        result = round(user_input_number * data["rates"][dropdown_to.get()], 2)
        result_label.config(text=result)
        notification_label.config(text="Success", fg="green")
    except ValueError:
        notification_label.config(text="Please enter a number", fg="red")
    except Exception as e:
        notification_label.config(text=f"Error: {str(e)}", fg="red")



user_input = Entry(window, font=("Arial", 12), bg="#e6e6e6", justify=CENTER)
user_input.insert(10,"0")
user_input.grid(row=0, column=0, padx=10, pady=(10,0))

dropdown = StringVar(window)
dropdown.set("CZK")
dropdown_menu = OptionMenu(window, dropdown, "CZK", "EUR", "USD")
dropdown_menu.grid(row=0, column=1)


dropdown_to = StringVar(window)
dropdown_to.set("CZK")
dropdown_menu_to = OptionMenu(window, dropdown_to, "CZK", "EUR", "USD")
dropdown_menu_to.grid(row=1, column=1, padx=5 , pady=(10,0))

count_button = Button(window, text="Count", font=("Arial", 12), bg="#e6e6e6", command=count)
count_button.grid(row=0, column=2, padx=10,pady=(10,0))

result_label = Label(window, text="0", font=("Arial", 12), bg=main_color, fg="white")
result_label.grid(row=1, column=0, padx=10, pady=(10,0))

notification_label = Label(window, font=("Arial", 12), bg=main_color, fg="white")
notification_label.grid(row=2, column=0, padx=10, pady=(10,0))

window.mainloop()
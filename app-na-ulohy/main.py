from tkinter import *
import customtkinter as ctk

window = ctk.CTk()
window.title("Úlohy")
window.geometry("600x430")
window.resizable(False, False)

main_font = ("Arial", 12)
main_color = "#dd7f00"
button_color = "#e2cff4"

def add_task():
    list_box.insert(END,input_label.get())
    input_label.delete(0, END)

def remove_task():
    list_box.delete(ANCHOR)

def clear_tasks():
    list_box.delete(0, END)

def save_tasks():
    tasks = list_box.get(0, END)
    with open("./tasks.txt", "w") as file:
        for task in tasks:
            if task.endswith("\n"):
                file.write(task)
            else:
                file.write(task + "\n")

def open_tasks():
    try:
        with open("./tasks.txt", "r") as file:
            for line in file:
                list_box.insert(END, line)
    except:
        print("No tasks")

input_frame = ctk.CTkFrame(window)
text_frame = ctk.CTkFrame(window)
button_frame = ctk.CTkFrame(window)
input_frame.pack(pady=5)
text_frame.pack(pady=5)
button_frame.pack()

input_label = ctk.CTkEntry(input_frame, width=400)
input_label.grid(row=0, column=0, padx=5, pady=5)

add_button = ctk.CTkButton(input_frame, text="Add",  command=add_task)
add_button.grid(row=0, column=1,padx=5, pady=5, ipadx=10)

list_box = Listbox(text_frame,  width=115, height=10, borderwidth=3, relief="sunken")
list_box.grid(row=0, column=0, sticky='nsew')

text_scrollbar = ctk.CTkScrollbar(text_frame)
text_scrollbar.grid(row=0, column=1, sticky='ns')

# text_scrollbar.config(command=list_box.yview)
list_box.config(yscrollcommand=text_scrollbar.set)

remove_button = ctk.CTkButton(button_frame, text="Remove",   command=remove_task)
clear_button = ctk.CTkButton(button_frame, text="Clear",   command=clear_tasks)
save_button = ctk.CTkButton(button_frame, text="Save",   command=save_tasks)
quit_button = ctk.CTkButton(button_frame, text="Quit",   command=window.destroy)

remove_button.grid(row=0, column=0,padx=2, pady=5)
clear_button.grid(row=0, column=1,padx=2, pady=5)
save_button.grid(row=0, column=2,padx=2, pady=5)
quit_button.grid(row=0, column=3,padx=2, pady=5)

open_tasks()

window.mainloop()
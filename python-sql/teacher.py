from tkinter import * 
import psycopg2

root = Tk()

root.title = "databáza sql"
root.geometry("300x280")
root.resizable(False, False)

def insert(name,age,address):
    entry_address.delete(0, END)
    entry_age.delete(0, END)
    entry_name.delete(0, END)

    connection = psycopg2.connect(
        dbname="student",
        user="postgres",
        password="admin",
        host="localhost",
        port="5432"
    )

    cur = connection.cursor()
    query =  "INSERT INTO teacher (name, age, address) VALUES (%s, %s, %s)"
    cur.execute(query, (name, age, address))
    connection.commit()
    connection.close()
    print("Insert successfully.")
    display_all()

def search(id):

    connection = psycopg2.connect(
        dbname="student",
        user="postgres",
        password="admin",
        host="localhost",
        port="5432"
    )
    cur = connection.cursor()
    query =  "SELECT * FROM teacher WHERE id = %s"
    cur.execute(query, (id,))
    print("Search successfully.")
    row = cur.fetchone()

    if row: 
        display_search(row)
    else:
        display_search("id not found")
        


    connection.commit()
    connection.close()

def display_search(data):
    listbox = Listbox(root, width=20, height=1)
    listbox.grid(row=7, column=1)
    listbox.insert(0, data)

def display_all():
    connection = psycopg2.connect(
        dbname="student",
        user="postgres",
        password="admin",
        host="localhost",
        port="5432"
    )
    cur = connection.cursor()
    query =  "SELECT * FROM  teacher "
    cur.execute(query)
    all_data = cur.fetchall()
    listbox = Listbox(root, width=20, height=5)
    listbox.grid(row=8, column=1)
    scrollbar = Scrollbar(root, orient=VERTICAL)
    scrollbar.grid(row=9,column=2, sticky="NSW")
    listbox.config(yscrollcommand=scrollbar.set)
    scrollbar.config(command=listbox.yview)
    for one_data in all_data:
        listbox.insert(0, one_data)
    connection.commit()
    connection.close()

display_all()

label_general = Label(root, text="Vitajte v databáze")
label_general.grid(row=0, column=1)

label_name = Label(root, text="Text:")
label_name.grid(row=1, column=0)

entry_name = Entry(root)
entry_name.grid(row=1, column=1)

label_age = Label(root, text="Age:")
label_age.grid(row=2, column=0)

entry_age = Entry(root)
entry_age.grid(row=2, column=1)

label_address = Label(root, text="Address:")
label_address.grid(row=3, column=0)

entry_address = Entry(root)
entry_address.grid(row=3, column=1)

button = Button(root, text="Add",command=lambda:insert(entry_name.get(),entry_age.get(),entry_address.get()))
button.grid(row=4, column=1)

label_search = Label(root, text="Search:")
label_search.grid(row=5, column=1)

label_id = Label(root, text="Search by id:")
label_id.grid(row=6, column=0)

entry_id = Entry(root)
entry_id.grid(row=6, column=1)

button_search = Button(root, text="Search", command=lambda:search(entry_id.get()) if entry_id.get().strip() else None)
button_search.grid(row=6, column=2)

root.mainloop()
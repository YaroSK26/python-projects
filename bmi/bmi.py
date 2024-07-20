from tkinter import * 
import psycopg2

root = Tk()

root.title("BMI")
root.geometry("250x250")
root.resizable(width=False, height=False)

def calculate_bmi():
    try:
        weight = float(entry_weight.get().replace(',', '.'))
        height = float(entry_height.get().replace(',', '.')) / 100
    except ValueError:
        label_result_value.config(text="Invalid input")
        label_result_user.config(text="Invalid input")
        return

    bmi = weight / (height ** 2)
    label_result_value.config(text=str(round(bmi, 2)))

    if bmi < 18.5:
        label_result_user.config(text="Underweight")
    elif bmi >= 18.5 and bmi < 25:
        label_result_user.config(text="Normal weight")
    elif bmi >= 25 and bmi < 30:
        label_result_user.config(text="Overweight")
    elif bmi >= 30:
        label_result_user.config(text="Obesity")

    conn = psycopg2.connect(
        host="localhost",
        database="bmi",
        user="postgres",
        password="admin"
    )

    cur = conn.cursor()

    cur.execute("INSERT INTO bmi(bmi_number,bmi_text) VALUES(%s , %s)", (bmi, label_result_user.cget("text")))

    conn.commit()

    update_user_count()

    cur.close()
    conn.close()
    weight = float(entry_weight.get())
    height = float(entry_height.get()) / 100
    bmi = weight / (height ** 2)
    label_result_value.config(text=str(round(bmi, 2)))

    if bmi < 18.5:
        label_result_user.config(text="Underweight")
    elif bmi >= 18.5 and bmi < 25:
        label_result_user.config(text="Normal weight")
    elif bmi >= 25 and bmi < 30:
        label_result_user.config(text="Overweight")
    elif bmi >= 30:
        label_result_user.config(text="Obesity")

    conn = psycopg2.connect(
        host="localhost",
        database="bmi",
        user="postgres",
        password="admin"
    )

    cur = conn.cursor()

    cur.execute("INSERT INTO bmi(bmi_number,bmi_text) VALUES(%s , %s)", (bmi, label_result_user.cget("text")))

    conn.commit()

    update_user_count()

    cur.close()
    conn.close()

def update_user_count():
    conn = psycopg2.connect(
        host="localhost",
        database="bmi",
        user="postgres",
        password="admin"
    )

    cur = conn.cursor()

    cur.execute("SELECT COUNT(*) FROM bmi")
    count = cur.fetchone()[0]

    label_count.config(text=str(count))

    cur.close()
    conn.close()

label_general = Label(root, text="BMI Calculator")
label_general.grid(row=0, column=0)

label_weight = Label(root, text="Weight (kg)")
label_weight.grid(row=1, column=0)

entry_weight = Entry(root)
entry_weight.grid(row=1, column=1)

label_height = Label(root, text="Height (cm)")
label_height.grid(row=2, column=0)

entry_height = Entry(root)
entry_height.grid(row=2, column=1)

button = Button(root, text="Calculate", command=calculate_bmi)
button.grid(row=3, column=1)

label_result = Label(root, text="Result")
label_result.grid(row=4, column=0)

label_result_value = Label(root, text="Add")
label_result_value.grid(row=4, column=1)

label_result_2 = Label(root, text="Result by text")
label_result_2.grid(row=5, column=0)

label_result_user = Label(root, text="Add")
label_result_user.grid(row=5, column=1)

label_count_text = Label(root, text="Users count")
label_count_text.grid(row=6, column=0)

label_count = Label(root, text="Add")
label_count.grid(row=6, column=1)

update_user_count()

root.mainloop()
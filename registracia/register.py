import bcrypt, psycopg2
from tkinter import * 

# password = b"admin"
# hashed = bcrypt.hashpw(password, bcrypt.gensalt())

# user_password = input("Enter password: ")
# user_password=bytes(user_password, 'utf-8')

# print(bcrypt.checkpw(user_password, hashed))

def password_to_hash(password):
    try:
        password_bytes = password.encode('utf-8')
        hashed = bcrypt.hashpw(password_bytes, bcrypt.gensalt())
        return hashed
    except Exception as e:
        print(e)
        return



def insert_bank_user(email,password):
    try:
        connection = psycopg2.connect(
            host="localhost",
            database="bank",
            user="postgres",
            password="admin",
            port=5432
        )
        cursor = connection.cursor()
        query = "INSERT INTO bank_user (email, password) VALUES (%s, %s)"

        hash = password_to_hash(password)

        cursor.execute(query, (email, hash))
        connection.commit()
        connection.close()
    except psycopg2.DatabaseError as e:
        print(f"Error databaze {e}")
    except Exception as e:
        print(f"Error {e}")
    else:
        print("Uspesne vlozeny")

def get_hash(email):
    try:
        connection = psycopg2.connect(
            host="localhost",
            database="bank",
            user="postgres",
            password="admin",
            port=5432
        )
        cursor = connection.cursor()
        query = "SELECT password FROM bank_user WHERE email = %s"
        cursor.execute(query, (email,))
        result = cursor.fetchone()
        connection.close()
        if result:
            return bytes.fromhex(result[0][2:])
        else:
            return b""
    except psycopg2.DatabaseError as e:
        print(f"Error databaze {e}")
        return b""
    except Exception as e:
        print(f"Error {e}")
        return b""
        
    
def login_auth(email, password):
    try:
        hash = get_hash(email)
        password_byte = bytes(password, 'utf-8')

        if hash == b"":
            result_label["text"] = "Zle meno alebo heslo"
        else:
            if bcrypt.checkpw(password_byte, hash):
                result_label["text"] = "Prihlaseny"
            else:
                result_label["text"] = "Zle meno alebo heslo"
    except Exception as e:
        print(f"Error pri vypisovani {e}")
        result_label["text"] = "Error"
       


root = Tk()
root.title("Registracia")
root.geometry("300x300")
root.resizable(False, False)

registration_label = Label(root, text="Registracia")
registration_label.grid(row=0, column=1)

email_label = Label(root, text="Email")
email_label.grid(row=1, column=0)

email_entry = Entry(root)
email_entry.grid(row=1, column=1)

password_label = Label(root, text="Heslo")
password_label.grid(row=2, column=0)

password_entry = Entry(root, show="*")
password_entry.grid(row=2, column=1)

registration_button = Button(root, text="Registrovat", command=lambda: insert_bank_user(email_entry.get(), password_entry.get()))
registration_button.grid(row=3, column=1)


login_label = Label(root, text="Prihlasenie")
login_label.grid(row=4, column=1)

login_email_label = Label(root, text="Email")
login_email_label.grid(row=5, column=0)

login_email_entry = Entry(root)
login_email_entry.grid(row=5, column=1)

login_password_label = Label(root, text="Heslo")
login_password_label.grid(row=6, column=0)

login_password_entry = Entry(root, show="*")
login_password_entry.grid(row=6, column=1)

login_button = Button(root, text="Prihlasit", command=lambda: login_auth(login_email_entry.get(), login_password_entry.get()))
login_button.grid(row=7, column=1)

result_label = Label(root)
result_label.grid(row=8, column=1)

root.mainloop()

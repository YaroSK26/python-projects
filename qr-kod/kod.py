import pyqrcode
from tkinter import *
from PIL import Image, ImageTk

root = Tk()
root.title("QR Kod")
root.geometry("400x400")
root.resizable(False, False)

def create_qr_code():
    global global_photo_image

    url = url_entry.get()
    qr_code = pyqrcode.create(url)
    qr_code.png("qr_code.png", scale=4)

    photo = Image.open("qr_code.png")
    global_photo_image = ImageTk.PhotoImage(photo)

    qr_code_label = Label(root, image=global_photo_image)
    qr_code_label.pack(pady=(0,20))

    qr_code_label.image = global_photo_image

    url_entry.delete(0, END)



global_photo_image = None

url_label = Label(root, text="URL:")
url_label.pack(pady=(10,20))

url_entry = Entry(root, width=30)
url_entry.pack(pady=(0,20))

button = Button(root, text="Vytvor QR kód", command=create_qr_code)
button.pack(pady=(0,20))

root.mainloop()
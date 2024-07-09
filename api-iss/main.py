from tkinter import *
import requests
from PIL import Image, ImageTk
from io import BytesIO

window = Tk()
window.title("ISS Tracker")
window.geometry("700x400")
window.resizable(False, False)

canvas = Canvas(window, width=500, height=280)
canvas.pack()

# URL obrázka
image_url = "https://www.esa.int/var/esa/storage/images/esa_multimedia/images/2003/05/artist_s_impression_of_the_completed_international_space_station/9874982-3-eng-GB/Artist_s_impression_of_the_completed_International_Space_Station_pillars.jpg"

# Stiahnutie obrázka z URL
response = requests.get(image_url)
img_data = response.content
img = Image.open(BytesIO(img_data))

# Zmena veľkosti obrázka, aby sa zmestil na plátno
img = img.resize((500, 280), Image.LANCZOS)

photo = ImageTk.PhotoImage(img)

canvas.create_image(0, 0, anchor=NW, image=photo)

def recount_iss_position():
    response = requests.get("http://api.open-notify.org/iss-now.json")
    data = response.json()

    latitude = data["iss_position"]["latitude"]
    longitude = data["iss_position"]["longitude"]

    latitude_label.config(text=f"Latitude: {latitude}")
    longitude_label.config(text=f"Longitude: {longitude}")
    

coordinates_frame = Frame(window)
coordinates_frame.pack(pady=20)

recount_button = Button(coordinates_frame, text="Recount ISS position", width=20, command=recount_iss_position)
recount_button.pack()

latitude_label = Label(coordinates_frame, text="Latitude: ")
latitude_label.pack()

longitude_label = Label(coordinates_frame, text="Longitude: ")
longitude_label.pack()

window.mainloop()
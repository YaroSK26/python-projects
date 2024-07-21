import base64
import zlib
from tkinter import * 
from tkinter import filedialog

window = Tk()
window.title("Compress and Decompress")
window.geometry('300x200')
window.resizable(False, False)

def upload_file():
    global file_path
    file_path= filedialog.askopenfilename()

    if file_path:
        file_name_label["text"] = file_path

def compress_file():
    global file_path
    if file_path:
        try:
            with open (file_path, "r") as myfile:
                data=myfile.read()
            
            data = bytes(data,"utf-8")
            compressed_data = zlib.compress(data)
            compressed_data_base64 = base64.b64encode(compressed_data)

            decoded_data =  compressed_data_base64.decode("utf-8")
            with open("compressed.txt", "w") as myfile:
                myfile.write(decoded_data)

            print("File compressed and saved as compressed.txt")
        except Exception as e:
            print(e)
    else:
        print("Please upload a file first")

def decompress_file():
    global file_path
    if file_path:
        try:
            with open (file_path, "r") as myfile:
                data=myfile.read()
            
            compressed_data = base64.b64decode(data)
            decompressed_data = zlib.decompress(compressed_data)

            with open("decompressed.txt", "w") as myfile:
                myfile.write(decompressed_data.decode("utf-8"))

            print("File decompressed and saved as decompressed.txt")
        except Exception as e:
            print(e)
    else:
        print("Please upload a file first")


upload_button = Button(window, text="Upload File", command=upload_file)
upload_button.grid(column=0, row=0)

file_name_label = Label(window, text="File Name")
file_name_label.grid(column=0, row=1)

compress_button = Button(window, text="Compress", command=compress_file)
compress_button.grid(column=0, row=2)

decopress_button = Button(window, text="Decompress", command=decompress_file)
decopress_button.grid(column=0, row=3)

window.mainloop()
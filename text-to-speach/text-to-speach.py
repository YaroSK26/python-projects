from gtts import gTTS
import os
from tkinter import *
from tkinter import ttk

# text_to_audio = open("demo.txt", "r", "utf-8").read().replace("\n", " ")

# output = gTTS(text_to_audio, lang='en', slow=False)
# output.save("output.mp3")

# os.system("start output.mp3")

root = Tk()
root.title("Text to Speech")
root.geometry("300x200")
root.resizable(0, 0)

def translate():
    try:
        text = text_entry.get()
        language = language_drop_down.get()
        audio_file = audio_entry.get()

        output = gTTS(text, lang=language, slow=False)
        output.save(audio_file + ".mp3")

        os.system("start " + audio_file + ".mp3")
    except Exception as e:
        print(e)

main_label = Label(root, text="Text to Speech")
main_label.grid(row=0, column=1)

language_label = Label(root, text="language")
language_label.grid(row=1, column=0)

language_drop_down = ttk.Combobox(root, state="readonly", values=["cs", "en"], width=27)
language_drop_down.grid(row=1, column=1)

text_label = Label(root, text="text")
text_label.grid(row=2, column=0)

text_entry = Entry(root, width=30)
text_entry.grid(row=2, column=1)

audio_label = Label(root, text="audio file name")
audio_label.grid(row=3, column=0)

audio_entry = Entry(root, width=30)
audio_entry.grid(row=3, column=1)

translate_button = Button(root, text="Translate",command=translate)
translate_button.grid(row=4, column=1)


root.mainloop()
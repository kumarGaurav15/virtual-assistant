from pathlib import Path
from tkinter import *
from PIL import Image, ImageTk
import speech_to_text
import action 

root = Tk()
root.title("Bood AI")
root.geometry("550x675")
root.resizable(False, False)
root.configure(bg="#6F8FAF")

#ask fun
def ask():
    user_value = speech_to_text.speech_to_text()
    if not user_value.strip():
        text.insert(END, "No speech input detected.\n")
        return
    bot_val = action.Action(user_value)
    text.insert(END, "User---->: " + user_value + "\n")
    text.insert(END, "BOT <----" + str(bot_val) + "\n")
    if bot_val == "Shutting down. Goodbye!":
        root.destroy()
   

def send():
    user_value = entry.get().strip()
    if not user_value:
        text.insert(END, "Please type a question before sending.\n")
        return
    bot_val = action.Action(user_value)
    text.insert(END, "User---->: " + user_value + "\n")
    text.insert(END, "BOT <----" + str(bot_val) + "\n")
    entry.delete(0, END)
    if bot_val == "Shutting down. Goodbye!":
        root.destroy()

def Delete():
    text.delete("1.0", END)


# top container
frame = Frame(root, bg="#6F8FAF", bd=3, relief="raised")
frame.place(x=75, y=20, width=400, height=330)

# title
text_label = Label(frame, text="Bood AI", font=("Comic Sans MS", 14, "bold"), fg="#356696", bg="#6F8FAF")
text_label.pack(pady=(15, 5))

# image
image = ImageTk.PhotoImage(Image.open("image/assitant.png"))
image_label = Label(frame, image=image, bg="#6F8FAF")
image_label.pack(pady=10)

#addinfg text to the root

text = Text(root, font=("courier 10 bold"), bg="#356696")
text.place(x=100, y=375, width=375, height=100)

#entry
entry = Entry(root, justify="center")
entry.place(x=100, y=500, width=355, height=30)

#button1
Button1 = Button(root , text = "Ask" , bg = "#356696" , pady = 16 , padx = 40, borderwidth=3, relief="solid", command= ask)
Button1.place(x=70, y=575)

Button2 = Button(root , text = "Send" , bg = "#356696" , pady = 16 , padx = 40, borderwidth=3, relief="solid", command= send)
Button2.place(x=400, y=575)

Button3 = Button(root , text = "Delete" , bg = "#356696" , pady = 16 , padx = 40, borderwidth=3, relief="solid", command= Delete)
Button3.place(x=225, y=575)



root.mainloop()
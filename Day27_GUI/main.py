from tkinter import *

window = Tk()
window.title("My First GUI Program.")
window.minsize(width=500, height=300)

# Label
my_label = Label(text="I am a Label.", font=("Arial",24,"bold"))
## my_label['text'] = "I am a Label2."
## my_label.config(text="I am a Label.")
my_label.pack()


# Button
def button_clicked():
    new_text = entry.get()
    my_label['text'] = new_text
button = Button(text="click me", command=button_clicked)
button.pack()


# Entry
entry = Entry(width=30)
entry.insert(END,string="default string")
entry.pack()


# Text
text = Text(height=5, width=30)
text.focus()
text.insert(END, "Example of multi-line text entry.")
print(text.get("1.0"),END)
text.pack()


# Spinbox
def spinbox_used():
    #gets the current value in spinbox.
    print(spinbox.get())
spinbox = Spinbox(from_=0, to=10, width=5, command=spinbox_used)
spinbox.pack()


# Scale
def scale_used(value):
    print(value)
scale = Scale(from_=0, to=100, command=scale_used)
scale.pack()


# Checkbutton
def checkbutton_used():
    print(checked_state.get()) # 0 is off, 1 is on
checked_state = IntVar()
checkbotton = Checkbutton(text = "Is On?", variable = checked_state, command = checkbutton_used)
checked_state.get()
checkbotton.pack()


# Radiobutton
def radio_used():
    print(radio_state.get())
radio_state = IntVar()
radiobutton1 = Radiobutton(text="Option1", value=1, variable=radio_state, command=radio_used)
radiobutton2 = Radiobutton(text="Option2", value=2, variable=radio_state, command=radio_used)
radiobutton1.pack()
radiobutton2.pack()


# Listbox
def listbox_used(event):
    print(listbox.get(listbox.curselection()))
listbox = Listbox(height=4)
fruits = ["Apple", "Pear", "Orange", "Banana"]
for item in fruits:
    listbox.insert(fruits.index(item), item)
listbox.bind("<<ListboxSelect>>",listbox_used)
listbox.pack()

window.mainloop()


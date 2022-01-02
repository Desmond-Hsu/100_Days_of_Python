from tkinter import *

window = Tk()
window.title('Test')
window.minsize(width=500, height=300)
window.config(padx=20, pady=20)

label = Label(font=("Arial",24,"bold"))
label.config(text="I am a label.")
# label.pack(side="left")
# label.place(x=0, y=0)
label.grid(column=0,row=0)

button = Button(text="Click Me")
# button.pack()
button.grid(column=1,row=1)

entry = Entry(width=10)
print(entry.get())
# entry.pack()
entry.grid(column=2,row=2)


window.mainloop()
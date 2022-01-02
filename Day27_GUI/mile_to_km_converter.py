from tkinter import *
window = Tk()
window.title("Mile to Km Converter")
window.minsize(width=500, height=300)
window.config(padx=20, pady=20)

# Entry
entry = Entry(width=10)
entry.grid(row=0, column=1)

# Label
label = Label(font=("Arial",20,"bold"))
label.grid(row=1, column=1)

# Button
def miles_to_km():
    input_miles = entry.get()
    new_km = round(float(input_miles)*1.609,2)
    label.config(text=new_km)
button = Button(text="Calculate", command=miles_to_km)
button.grid(row=2, column=1)

# Text Label
label1 = Label(text="Miles", font=("Arial",20))
label1.grid(row=0, column=2)
label2 = Label(text="is equal to", font=("Arial",20))
label2.grid(row=1, column=0)
label3 = Label(text="Km", font=("Arial",20))
label3.grid(row=1, column=2)

window.mainloop()

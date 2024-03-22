#entry - column 1, row 0
#label - column 0, row 1; column 1, row 1; column 2, row 1; column 2, row 0
#button - column 1, row 2

from tkinter import *

FONT = ("Arial", 12)

window = Tk()
window.title("Miles to KM converter")
window.config(padx=20,pady=20)

lala = Label()
lala.grid(column=0, row=0)

equal_to_label = Label(text="is equal to", font=FONT)
equal_to_label.grid(column=0,row=1)

miles_label = Label(text="Miles", font=FONT)
miles_label.config(padx=10)
miles_label.grid(column=2, row=0)

km_label = Label(text="Km", font=FONT)
km_label.grid(column=2,row=1)


def miles_to_km():
    miles = int(entry.get())
    km = miles * 1.60934
    rounded_km = str(round(km))
    calculated_number_label.config(text=rounded_km)


button = Button(text="Calculate", command=miles_to_km)
button.grid(column=1, row=2)

calculated_number_label = Label(text="0", font=FONT)
calculated_number_label.grid(column=1, row=1)

entry = Entry(width=15)
entry.grid(column=1, row=0)
print(type(entry.get()))


window.mainloop()
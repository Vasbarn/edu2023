from tkinter import *

root = Tk()
root.geometry("268x288")
root.title("Калькулятор")
root.resizable(0, 0)

frame_input = Frame(root)
frame_input.grid(row=0, column=0, columnspan=4, sticky="nsew")

input_field = Entry(frame_input, font='Arial 15 bold', width=24, state="readonly")
input_field.pack(fill=BOTH)

root.mainloop()
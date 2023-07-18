import tkinter as tk

window = tk.Tk()

window.title("Simple GUI")

label = tk.Label(window, text="Hello, GUI")
button = tk.Button(window, text="Click me",width="20")

def button_click():
    print("button clicked!")

label.pack()
button.pack()
button.bind("<Button-1>", button_click)

# Main loop
window.mainloop()
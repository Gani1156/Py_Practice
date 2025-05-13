import tkinter as tk
window = tk.Tk()
window.title("Ganesh")
window.geometry("400x400")


# creating a simple button
#button = tk.Button(window, text='Click Me', font=('Arial',20))
button = tk.Button(window, text="Click Me!", font=("", 20))
button.pack(expand=True)
window.mainloop()
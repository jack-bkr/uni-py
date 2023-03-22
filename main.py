import tkinter as tk

#init window
root = tk.Tk()
root.title("cunt")

#widgets
lblMain = tk.Label(root, text = "sup pricks")
lblMain.grid(row=0, column=0, columnspan=2)

lblName = tk.Label(root, text="Name:")
lblName.grid(row=1,column=0)
txtName = tk.Entry(root)
txtName.grid(row=1,column=1)


root.mainloop()

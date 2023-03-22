import tkinter as tk

#init window
root = tk.Tk()
root.title("canvas")

#canvas
c = tk.Canvas(root)
c.grid(row=0, column=0)

# for i in range(0, 100, 10):
#     c.create_line(0, i, i+10, 100, fill='blue')
    
# for i in range(100, 0, -10):
#     c.create_line(100, i, i+10, 0, fill='red')

for i in range(0, 100, 10):
    c.create_rectangle(100-i, i, i, i)

root.mainloop()

import tkinter as tk
window=tk.Tk()
window.title(' ')
window.geometry('400x400')
img = tk.PhotoImage(file='./阿甘正传.gif')
l_img = tk.Label(window, image=img)
l_img.pack()
window.mainloop()
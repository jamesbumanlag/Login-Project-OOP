from tkinter import *


root = Tk()
root.geometry('400x500+500+100')



class Button_Main:
    def __init__(self, canvas, text, _x, _y):
        
        self.button_login = Button(canvas, text=text, borderwidth=1)
        

        self.button1 = self.canvas1.create_window(_x, _y, anchor='nw', window=self.button_login)

canvas1 = Canvas(root, height=400, width=500, borderwidth=0)
canvas1.place(x=0, y=0)
button_login_main = Button_Main('Login', 150, 50)

button_create_main = Button_Main('Create Account', 120, 300)


root.mainloop()
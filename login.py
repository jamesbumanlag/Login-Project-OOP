from tkinter import *
from main_class import *

import os


root = Tk()
root.geometry('657x510+500+100')
root.title('Login')
root.resizable(False,False)

def show_hide():
    canvas_login.hide_show_pass(290,290, show_hide)

def open_create():
    root.destroy()
    os.system('python create_account.py')

def open_forgot():
    root.destroy()
    os.system('python forgot.py')

def button_login():
    return None
    

canvas_login = Canvas_Main(root,'Login')
canvas_login.input_user('Username',140,190,215,235)
canvas_login.input_pass('Password', 140, 270,295,315,290,290, show_hide)
canvas_login.button_main('login.png',190,340, button_login)
canvas_login.signin_signup_label_button('Not a member?', 'Sign up',210,440,270,430, open_create)
canvas_login.forgot_password(190,380, open_forgot)




root.mainloop()


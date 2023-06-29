from tkinter import *
from main_class import *
import os

root = Tk()
root.title('Create Account')
root.geometry('657x510+500+100')
root.resizable(0,0)

def show_hide():
    canvas_login.hide_show_pass(290,330, show_hide)

def open_login():
    root.destroy()
    os.system('python login.py')

def button_login():
    pass
    

canvas_login = Canvas_Main(root,'Create Account')
canvas_login.input_user('Email',140,190,215,235)
canvas_login.input_user('Username',140,250,275,295)
canvas_login.input_pass('Password', 140, 310,335,355,290,330, show_hide)
canvas_login.button_main('Continue.png',190,390, button_login)
canvas_login.signin_signup_label_button('Already a member?', 'Sign in',210,440,270,430,open_login )

root.mainloop()


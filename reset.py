from tkinter import *
from main_class import *
import os

root = Tk()
root.title('Reset Password')
root.geometry('657x510+500+100')
root.resizable(0,0)

def show_hide():
    canvas_login.hide_show_pass(290,290, show_hide)


def button_login():
    root.destroy()
    os.system('python login.py')

canvas_login = Canvas_Main(root,'Reset Password')
canvas_login.input_user('Password',140,190,215,235)
#hide_show = canvas_login.hide_show_pass(290,290)
canvas_login.input_pass('Confirm Password', 140, 270,295,315,290,290,show_hide )
canvas_login.button_main('Continue.png',190,340, button_login)
canvas_login.signin_signup_label_button('Already a member?', 'Sign in',210,440,270,430, button_login )


root.mainloop()

from tkinter import *
from main_class import *
import os

root = Tk()
root.title('Forgot Password')
root.geometry('657x510+500+100')
root.resizable(0,0)

def open_create():
    root.destroy()
    os.system('python create_account.py')
 
def open_reset():
    root.destroy()
    os.system('python reset.py')

def button_continue():
    root.destroy()
    os.system('python reset.py')
    

canvas_login = Canvas_Main(root,'Forgot Password')
canvas_login.input_user('Enter your Email/Username',140,210,245,265)
canvas_login.button_main('Continue.png', 190,340, button_continue)

canvas_login.signin_signup_label_button('Not a member?', 'Sign up',210,440,270,430, open_create )

root.mainloop()
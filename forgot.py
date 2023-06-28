from tkinter import *
from main_class import *

root = Tk()
root.title('Forgot Password')
root.geometry('657x510+500+100')
root.resizable(0,0)

canvas_login = Canvas_Main(root,'Forgot Password')
canvas_login.input_user('Enter your Email/Username',140,210,245,265)
canvas_login.button_main('Continue.png', 190,340)

canvas_login.signin_signup_label_button('Not a member?', 'Sign up',210,440,270,430 )

root.mainloop()
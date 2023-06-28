from tkinter import *
from main_class import *

root = Tk()
root.geometry('657x510+500+100')
root.title('Login')
root.resizable(False,False)

canvas_login = Canvas_Main(root,'Login')
canvas_login.input_user('Username',140,190,215,235)
canvas_login.input_pass('Password', 140, 270,295,315,290,290)
canvas_login.button_main('login.png',190,340)
canvas_login.signin_signup_label_button('Not a member?', 'Sign up',210,440,270,430)
canvas_login.forgot_password(190,380)



root.mainloop()


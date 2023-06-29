from tkinter import *

class root(Tk):
    def __init__(self, title, geometry, resizable, function,title_page ):
        super().__init__()
        self.title(title)
        self.geometry(f'{geometry[0]}x{geometry[1]}+{geometry[2]}+{geometry[3]}')
        self.resizable(resizable[0], resizable[1])

        # widgets starts here
        function = Canvas_Main(self,title)

        self.mainloop()
       
class Canvas_Main(Canvas):
    def __init__(self,parent,page):
        super().__init__(parent)
        self.pack(fill='both', expand=True)
        
        # main canvas properties
        self.configure(width=657, height=510, borderwidth=0, highlightthickness=0)

        # display main background
        self.imagebg = PhotoImage(file='imagebg.png')
        self.create_image(0,0, image=self.imagebg, anchor='nw')
               
        # create page banner and display user logo
        self.user_icon = PhotoImage(file='user_icon.png')
        self.create_image(215,75, image=self.user_icon, anchor='nw')
        self.create_text(240,145, text=page, font=('Inter', 20, 'bold'), fill='#7f7fcc')  

    def input_user(self, text_user, x, text_y, ent_y, line_y):
        self.create_text(x,text_y,text=text_user, font=['inter',11],fill='#7f7fcc', anchor='nw')
        self.entry_user = Entry(self, 
                                font=['inter',10],
                                width=19, fg='#336092', 
                                borderwidth=1,
                                border=0,
                                highlightthickness=0,
                                foreground='grey'
                                )
        self.create_window(x,ent_y, anchor='nw', window=self.entry_user)
        self.frame_entry_user = Frame(self)
        self.frame_entry_user.configure( width=180, bd=2)
        self.frame_entry_user.place(x=x, y=line_y)

    def input_pass(self, text_pass, x, text_y, entry_y,line_y, hide_x, hide_y, command):
        self.create_text(x,text_y,text=text_pass, font=['inter',11],fill='#7f7fcc', anchor='nw')
        self.entry_pass = Entry(self, 
                                font=['inter',10],
                                width=19, fg='#336092', 
                                borderwidth=1,
                                border=0,
                                bd=0,
                                highlightthickness=0,
                                foreground='grey',
                                show="●"
                                )
        self.create_window(x,entry_y, anchor='nw', window=self.entry_pass)
        self.frame_entry_pass = Frame(self)
        self.frame_entry_pass.configure( width=138, bd=2)
        self.frame_entry_pass.place(x=x, y=line_y)
        
        # Password button hide for display only
        self.image_hide = PhotoImage(file='pass_hide.png')
        self.image_show = PhotoImage(file='pass_show.png')
        self.button_hide = Button(self, image=self.image_hide, 
                                  activebackground='white',
                                  activeforeground='white',
                                  borderwidth=0,
                                  border=0,
                                  bd=0,
                                  background='white',
                                  command=command
                                  )       
        self.create_window(hide_x,hide_y, anchor='nw', window=self.button_hide)

    # Function hide and show password
    def hide_show_pass(self, hide_x, hide_y, command):
            if self.entry_pass['show'] == '●':
                    self.entry_pass.configure(show='') 
                    self.show_btn = Button(self,
                            image=self.image_hide,
                            bg="white",
                            borderwidth=0,
                            activebackground="white",
                            cursor='hand2',
                            command=command
                            )
                    
                    self.create_window(hide_x, hide_y, anchor='nw', window=self.show_btn)      
                    self.show_btn.config(image=self.image_show)

            else:
                    self.entry_pass.configure(show='●')
                    self.hide_btn = Button(self,
                            image=self.image_show,
                            borderwidth=0,
                            bg="white",
                            activebackground="white",
                            cursor='hand2',
                            command=command)
                    
                    self.create_window(hide_x, hide_y, anchor='nw', window=self.hide_btn)
                    self.hide_btn.config(image=self.image_hide) 
            
    def button_main(self, image_button, button_x, button_y, command):
        self.image_button = PhotoImage(file=image_button)
        self.main_bt = Button(self, 
                              image=self.image_button, 
                              borderwidth=0, 
                              activebackground='white', 
                              highlightbackground='white', 
                              bd=0,
                              background='white',
                              highlightcolor='white',
                              command = command
                              
                              )
        self.create_window(button_x,button_y, anchor='nw', window=self.main_bt)

    def signin_signup_label_button(self, text, button_text,label_x, label_y, sign_x, sign_y, command):
        self.create_text(label_x,label_y, 
                         text=f'{text} |',
                         font=['inter',9],
                         fill ='#7f7fcc')
        self.signup_bt = Button(self, 
                                text=button_text, 
                                font=['inter',9,'bold'],
                                fg='#7f7fcc',border=0, 
                                borderwidth=0, 
                                activebackground='white',
                                highlightbackground='white', 
                                background='white',
                                activeforeground='#7f7fcc', 
                                command=command
                               
                                )
        self.create_window(sign_x,sign_y, anchor='nw', window=self.signup_bt)

    def forgot_password(self, forgot_x, forgot_y, command):
        self.forgot_button = Button(self, 
                                text='Forgot Password', 
                                font=['inter',9],
                                fg='#7f7fcc',border=0, 
                                borderwidth=0, 
                                activebackground='white',
                                highlightbackground='white', 
                                activeforeground='#7f7fcc',
                                background='white',
                                command=command
                                
                                
                                    )
        
        self.create_window(forgot_x,forgot_y, anchor='nw', window=self.forgot_button)
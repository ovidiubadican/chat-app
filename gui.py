<<<<<<< HEAD
from Tkinter import *

top = Tk()
top.geometry('300x600+1550+50')
top.resizable(width = False, height = False)
top.title("Python Chat Application")

# info text
L0 = Label(top, text = "Please enter your credentials to proceed:")
L0.place(x = 15, y = 200)

# enter username
L1 = Label(top, text = "Username:")
L1.place(x = 15, y = 225)
E1 = Entry(top, bd = 2, width = 30)
E1.place(x = 100, y = 225)

# enter password
L1 = Label(top, text = "Password:")
L1.place(x = 15, y = 250)
E1 = Entry(top, width = 30, show = '*')
E1.place(x = 100, y = 250)

# login button
login_button = Button(top, text = "Login")
login_button.place(x = 250, y = 275)

top.mainloop()
=======
from tkinter import *

top = Tk()
screen_width = top.winfo_screenwidth()
screen_height = top.winfo_screenheight()
w = screen_width/6
h = screen_height/2
x_offset = screen_width/1.3
y_offset = screen_height/20

top.geometry('%dx%d+%d+%d' % (w, h, x_offset, y_offset))
top.resizable(width = False, height = False)
top.title("Python Chat Application")

# info text
L0 = Label(top, text = "Please enter your credentials to proceed:")
L0.place(x = w/20, y = h/0.6)

# enter username
L1 = Label(top, text = "Username:")
L1.place(x = w/20, y = h/2.4)
E1 = Entry(top, width = int(w/10))
E1.place(x = 100, y = 225)

# enter password
L1 = Label(top, text = "Password:")
L1.place(x = w/20, y = h/2.15)
E1 = Entry(top, width = int(w/10), show = '*')
E1.place(x = 100, y = 250)

# login button
login_button = Button(top, text = "Login")
login_button.place(x = w*0.8, y = h/1.95)

# sign up button
signup_button = Button(top, text = "Create Account")
signup_button.place(x = w*0.65, y = h/1.75)

top.mainloop()
"""
def draw_create_account():
    account_window = Tk()
    screen_width = top.winfo_screenwidth()
    screen_height = top.winfo_screenheight()
    x_offset = screen_width/1.2
    y_offset = screen_height/20
"""
>>>>>>> f5423af5ade57f1d7f811f1e515483d2e9e5b9fd

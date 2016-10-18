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

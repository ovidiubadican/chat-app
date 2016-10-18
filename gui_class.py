from tkinter import *

class Window:

    def __init__(self, name, height, width, x_offset, y_offset):
        self.name = Tk()
        screen_width = self.name.winfo_screenwidth()
        screen_height = self.name.winfo_screenheight()
        self.name.geometry('%dx%d+%d+%d' % (self.h, self.w, self.x_offset, self.y_offset))
        self.h = height
        self.w = width
        self.x_offset = x_offset
        self.y_offset = y_offset

    def draw(self, title, resize):

        self.name.title(title)
        if resize == 'N':
            self.name.resizable(width = False, height = False)

main_window = Window(main, 300, 600, screen_width/1.2, screen_height/20)
main_window.draw("Python Chat Application", 'N')

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

    # sign up button
    signup_button = Button(top, text = "Create Account")
    signup_button.place(x = 200, y = 310)

    top.mainloop()

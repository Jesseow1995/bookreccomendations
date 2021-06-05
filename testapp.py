from tkinter import *
app = Tk()
app.title("Open File")
app.geometry('200x200')
fileaddress = StringVar()
label1 = Label(app, text = 'Enter File Path: ').grid(row = 0)
fileName = Entry(app, textvariable = fileaddress.get()).grid(row = 0, column = 1)
Button(app, text = 'open', command = lambda: accessFile(name)).grid(row = 1, columnspan=2)
name = StringVar
def accessFile(name):
    name.set(fileaddress.get())
    open(name, 'r')



app.mainloop()
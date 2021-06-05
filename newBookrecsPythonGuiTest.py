from breezypythongui import *
import bookrecs


class BookRecsGui(EasyFrame):
    def __init__(self):
        EasyFrame.__init__(self, title='Book Recommendations')
        # Issue here is you directly called the init function which I think is automatically called when created
        # For the parent issue I just had the init have the parent as a parameter
        self.addButton(text='Friends', command=lambda: friends(my_parent=self), row=0, column=0)
        # Recommended should pretty much be the same as the friends one but with different output messageBox
        self.addButton(text='Recommended', command=None, row=0, column=1)
        # You could do this report one a few ways but I would just call your bookRecs main just how it is
        # then just read the file and print it in a messageBox
        # so the report button command would be command=self.messageBox( ... file contents ...)
        self.addButton(text='Report', command=None, row=0, column=2)


class friends(EasyDialog):
    # I was looking through the EasyDialog class and apparently it expects you to create a body and apply function
    def body(self, master):
        # This is were you want to display everything
        self.addLabel(master, text='Reader', row=0, column=0)
        self.reader_field = self.addTextField(master, text='', row=0, column=1)

    def apply(self):
        # This is where you show the results (once user hits ok this function is called)
        # do error checking before this box, idk how they want you to do that
        self.messageBox(title="Friends of "+self.reader_field.getText(), message="Probably print list of friends here", width=150, height=150)

    def __init__(self, my_parent):
        EasyDialog.__init__(self, parent=my_parent, title='Friends')


BookRecsGui().mainloop()

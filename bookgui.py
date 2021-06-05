from breezypythongui import *
import bookrecs


class BookRecsGui(EasyFrame):
    def __init__(self):
        EasyFrame.__init__(self, title='Book Recommendations')
        self.addButton(text='Friends', command=lambda: friends(myParent=self), row=0, column=0)
        self.addButton(text='Recommended', command=lambda: recommendedBooks(myParent=self), row=0, column=1)
        self.addButton(text='Report', command=lambda: report(myParent=self), row=0, column=2)


class friends(EasyDialog):

    def body(self, master):
        self.addLabel(master, text='Reader Name', row=0, column=0)
        self.readerField = self.addTextField(master, text='', row=0, column=1)
        self.addLabel(master, text='Number of friends', row=1, column=0)
        self.numField = self.addTextField(master, text='2', row=1, column=1)

    def apply(self):
        if self.readerField.get().lower() in bookrecs.sim_score.keys():
            if int(self.numField.get()) > 0:
                self.messageBox(title="Friends " + self.readerField.getText(),
                                message='\n'.join(
                                    bookrecs.friends(self.readerField.get().lower(), int(self.numField.get()))))
            else:
                self.messageBox(title='Error', message='number of friends must be greater than 0', width=25, height=5)
                friends(self)
        else:
            self.messageBox(title='Error', message='reader not found', width=25, height=5)
            friends(self)

    def __init__(self, myParent):
        EasyDialog.__init__(self, parent=myParent)


class recommendedBooks(EasyDialog):
    def body(self, master):
        self.addLabel(master, text='Reader Name', row=0, column=0)
        self.readerField = self.addTextField(master, text='', row=0, column=1)
        self.addLabel(master, text='Number of friends', row=1, column=0)
        self.numField = self.addTextField(master, text='2', row=1, column=1)

    def apply(self):
        if self.readerField.get().lower() in bookrecs.sim_score.keys():
            if int(self.numField.get()) > 0:
                i = 0
                a = 0
                books = bookrecs.recommend(self.readerField.get().lower(), self.numField.get())
                recbooks = {}
                for book in books:
                    recbooks[a] = book[i] + ', ' + book[i + 1] + '\n'
                    a += 1
                booklist = list(recbooks.values())
                self.messageBox(title="Recommended Books for " + self.readerField.getText(),
                                message=booklist, width=100,
                                height=100)
            else:
                self.messageBox(title='Error', message='number of friends must be greater than 0', width=25, height=5)
                recommendedBooks(self)
        else:
            self.messageBox(title='Error', message='reader not found', width=25, height=5)
            recommendedBooks(self)

    def __init__(self, myParent):
        EasyDialog.__init__(self, parent=myParent)


class report(MessageBox):
    def __init__(self, myParent):
        reportFile = open('recommendations.txt', 'r')
        MessageBox.__init__(self, parent=myParent, title='Report', message=reportFile.read(), width=100, height=100)


BookRecsGui().mainloop()

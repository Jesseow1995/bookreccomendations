from tkinter import *
import tkinter.scrolledtext as scrolledtext
from tkinter import messagebox
from tkinter import filedialog
import bookrecs


def getFriends():
    readerName = StringVar
    numFriends = IntVar

    reportWindow = Toplevel()
    reportWindow.propagate()
    reportWindow.title('Friends')
    reportWindow.config(bg='black')
    nameLabel = Label(reportWindow, text='Reader ', fg='light blue', bg='black')
    nameLabel.grid(row=0, column=0, padx=10, pady=10)
    readerName = Entry(reportWindow)
    readerName.grid(row=0, column=1, padx=10, pady=10)
    numLabel = Label(reportWindow, text='Enter number of friends', fg='light blue', bg='black')
    numLabel.grid(row=1, column=0, padx=10, pady=10)
    numFriends = Entry(reportWindow)
    numFriends.grid(row=1, column=1, padx=10, pady=10)
    numFriends.insert(END, '2')
    showFriends = Button(reportWindow, text='Okay', command=lambda: friendReport(), fg='light blue', bg='black')
    showFriends.grid(row=2, column=1, padx=10, pady=10)

    def friendReport():
        if readerName.get().lower() in bookrecs.sim_score.keys():
            if int(numFriends.get()) > 0:
                recommendedRep = Toplevel()
                recommendedRep.propagate()
                recommendedRep.title('Names of Friends')
                recommendedRep.config(bg='black')
                friendText = scrolledtext.ScrolledText(recommendedRep, fg='light blue', bg='black')
                friendText.insert(INSERT, '\n'.join(bookrecs.friends(readerName.get().lower(), numFriends.get())))
                friendText.pack()
            else:
                messagebox.showerror('Error', 'Number of friends must be greater than 0')
        else:
            messagebox.showerror('Error', 'No reader found')


def getRecommended():
    reportWindow = Toplevel()
    reportWindow.propagate()
    reportWindow.title('Recommended Books')
    reportWindow.config(bg='black')
    nameLabel = Label(reportWindow, text='Reader ', fg='light blue', bg='black')
    nameLabel.grid(row=0, column=0, padx=10, pady=10)
    readerName = Entry(reportWindow)
    readerName.grid(row=0, column=1)
    numLabel = Label(reportWindow, text='Enter number of friends', fg='light blue', bg='black')
    numLabel.grid(row=1, column=0, padx=10, pady=10)
    numFriends = Entry(reportWindow)
    numFriends.grid(row=1, column=1, pady=10)
    numFriends.insert(END, '2')
    showRecommendedBooks = Button(reportWindow, text='Okay', command=lambda: recommendedReport(), fg='light blue',
                                  bg='black')
    showRecommendedBooks.grid(row=2, column=0, padx=10, pady=10)

    def recommendedReport():
        if readerName.get().lower() in bookrecs.sim_score.keys():
            if int(numFriends.get()) > 0:
                recommendedRep = Toplevel()
                recommendedRep.propagate()
                recommendedRep.title('Names of Friends')
                recommendedRep.config(bg='black')
                recommendedBooks = scrolledtext.ScrolledText(recommendedRep, fg='light blue', bg='black')
                books = bookrecs.recommend(readerName.get().lower(), numFriends.get())
                i = 0
                for book in books:
                    recommendedBooks.insert(INSERT, book[i] + ', ' + book[i + 1] + '\n')
                recommendedBooks.pack()
            else:
                messagebox.showerror('Error', 'Number  ader found')


def getReport():
    reportWindow = Toplevel()
    reportWindow.grid_propagate()
    reportWindow.title('Report')
    reportWindow.config(bg='black')
    # reportFile = open('recommendations.txt', 'r')
    reportFile = filedialog.askopenfile()
    report = scrolledtext.ScrolledText(reportWindow, fg='light blue', bg='black')
    report.insert(INSERT, reportFile.read())
    report.pack()
    reportFile.close()


bookrecsGui = Tk()
bookrecsGui.config(bg='black')
bookrecsGui.title('Book Recommendations')
bookrecsGui.propagate()
friendButton = Button(bookrecsGui, text='Friends', command=lambda: getFriends(), fg='light blue', bg='black')
friendButton.pack(pady=10, padx=10, side=LEFT)
recommendButton = Button(bookrecsGui, text='Recommendations', command=lambda: getRecommended(), fg='light blue',
                         bg='black')
recommendButton.pack(pady=10, padx=10, side=LEFT)
reportButton = Button(bookrecsGui, text='Report', command=lambda: getReport(), fg='light blue', bg='black')
reportButton.pack(pady=10, padx=10, side=LEFT)

bookrecsGui.mainloop()

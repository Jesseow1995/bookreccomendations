from tkinter import *
taxUi = Tk()
taxUi.title('Tax Calculator')
taxUi.geometry('250x250')

def computeTax(income):
   tax.set((float(income.get()) * .10) - (float(numDependents.get()) * 1000.00))



tax = StringVar()

incomeLable = Label(taxUi, text = 'Gross Income', fg = 'blue')
incomeLable.grid(row = 0)
income = StringVar()
incomeEntry = Entry(taxUi, textvariable = income)
incomeEntry.grid(row = 0, column = 1)

numDependents = StringVar()
dependentsLable = Label(taxUi, text = 'Number of Dependents', fg = 'blue').grid(row = 1)
dependentsEntry = Entry(taxUi, textvariable = numDependents).grid(row = 1, column = 1)

taxButton = Button(taxUi, text = 'Compute Tax', command = lambda: computeTax(income))
taxButton.grid(row = 3, columnspan = 2)
totalTaxLable = Label(taxUi, text = 'Total Tax', fg = 'blue').grid(row = 4)
taxLabel = Label(taxUi, textvariable = tax)
taxLabel.grid(row = 4, column = 1)

stopButton = Button(taxUi, text = 'close', command = lambda: taxUi.forget(taxUi), fg = 'dark red')
stopButton.grid(row = 5, columnspan = 2)
taxUi.mainloop()
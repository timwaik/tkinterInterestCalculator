from tkinter import *

class Window(Frame):

    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.master = master
        self.init_window()

    def callbackAmountEntry(self, event):
        self.amountEntry.selection_range(0, END)
    def callbackInterestEntry(self, event):
        self.interestEntry.selection_range(0, END)
    def callbackDurationYearsEntry(self, event):
        self.durationYearsEntry.selection_range(0, END)
    def callbackDurationMonthsEntry(self, event):
        self.durationMonthsEntry.selection_range(0, END)

    def init_window(self):
        #Window Title
        self.master.title("Interest Calculation")
        #self.pack(fill = BOTH, expand = 1)

        #MenuBar
        menuMain = Menu(self.master)
        self.master.config(menu=menuMain)
        file = Menu(menuMain)
        file.add_command(label="Exit", command=self.client_exit)
        menuMain.add_cascade(label="File", menu=file)
        edit = Menu(menuMain)
        edit.add_command(label="Reset Values", command=self.reset_values)
        menuMain.add_cascade(label="Edit", menu=edit)

        #Labels
        title = Label(text = "Interest Calculator",justify=CENTER, font=(16))
        #myLabel.grid(column=1, row=5)
        title.grid(ipady= 10,sticky=W+E,columnspan = 2)
        initialAmount = Label(text = "Initial Amount: ")
        initialAmount.grid(row=2, column=0, sticky=W,ipady= 5)
        interestRate = Label(text = "Interest Rate %: ")
        interestRate.grid(row=3, column=0, sticky=W,ipady= 5)
        lengthYears = Label(text = "Duration (Years): ")
        lengthYears.grid(row=4, column=0, sticky=W,ipady= 5)
        lengthMonths = Label(text = "Duration (Months): ")
        lengthMonths.grid(row=5, column=0, sticky=W,ipady= 5)
        finalTotal = Label(text = "Final amount: ")
        finalTotal.grid(row=6, column=0, sticky=W,ipady= 5)

        #Entries
        self.amountEntry = Entry(self.master)
        self.amountEntry.grid(row=2,column=1)
        self.amountEntry.insert(0, "0")
        self.amountEntry.bind("<FocusIn>", self.callbackAmountEntry)

        self.interestEntry = Entry(self.master)
        self.interestEntry.grid(row=3,column=1)
        self.interestEntry.insert(0, "0")
        self.interestEntry.bind("<FocusIn>", self.callbackInterestEntry)

        self.durationYearsEntry = Entry(self.master)
        self.durationYearsEntry.grid(row=4,column=1)
        self.durationYearsEntry.insert(0, "0")
        self.durationYearsEntry.bind("<FocusIn>", self.callbackDurationYearsEntry)

        self.durationMonthsEntry = Entry(self.master)
        self.durationMonthsEntry.grid(row=5,column=1)
        self.durationMonthsEntry.insert(0, "0")
        self.durationMonthsEntry.bind("<FocusIn>", self.callbackDurationMonthsEntry)

        self.finalEntry = Entry(self.master)
        self.finalEntry.grid(row=6,column=1)
        self.finalEntry.insert(0, "0")

        self.calculateMonthlyButton = Button(text="Calculate monthly accruement: ", command=self.calculateMonthly)
        self.calculateMonthlyButton.grid(row=7,column=0,padx= 5,pady= 5)
        self.calculateYearlyButton = Button(text="Calculate yearly accruement: ", command=self.calculateYearly)
        self.calculateYearlyButton.grid(row=7,column=1,padx= 5,pady= 5)


        #Quit button
        quitButton = Button(text="Quit the app",command=self.client_exit)
        quitButton.grid(row = 8, sticky=W,padx= 5,pady= 10)

    #Test function
    def calculateMonthly(self):
        amountEntry_variable = int(self.amountEntry.get())
        interestEntry_variable = int(self.interestEntry.get())
        durationYearsEntry_variable = int(self.durationYearsEntry.get())
        durationMonthsEntry_variable = int(self.durationMonthsEntry.get())
        finalTally = amountEntry_variable

        totalMonthsDuration = durationYearsEntry_variable*12 + durationMonthsEntry_variable
        for x in range(totalMonthsDuration):
            finalTally = finalTally + finalTally*(interestEntry_variable/100)/12

        self.finalEntry.delete(0,"end")
        self.finalEntry.insert(0, finalTally)

    def calculateYearly(self):
        amountEntry_variable = int(self.amountEntry.get())
        interestEntry_variable = int(self.interestEntry.get())
        durationYearsEntry_variable = int(self.durationYearsEntry.get())
        durationMonthsEntry_variable = int(self.durationMonthsEntry.get())
        finalTally = amountEntry_variable

        for x in range(durationYearsEntry_variable):
            finalTally = finalTally + finalTally*(interestEntry_variable/100)

        finalTally = finalTally + amountEntry_variable*(interestEntry_variable/100)*durationMonthsEntry_variable/12

        self.finalEntry.delete(0,"end")
        self.finalEntry.insert(0, finalTally)

    #Reset Values
    def reset_values(self):
        self.amountEntry.delete(0,"end")
        self.interestEntry.delete(0,"end")
        self.durationYearsEntry.delete(0,"end")
        self.durationMonthsEntry.delete(0,"end")
        self.finalEntry.delete(0,"end")
        self.amountEntry.insert(0,"0")
        self.interestEntry.insert(0,"0")
        self.durationYearsEntry.insert(0,"0")
        self.durationMonthsEntry.insert(0,"0")
        self.finalEntry.insert(0,"0")

    #Exit
    def client_exit(self):
        exit()

root = Tk()
root.geometry("400x300")
root.resizable(width=False, height=False)
app = Window(root)
root.mainloop()

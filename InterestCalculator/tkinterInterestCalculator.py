from tkinter import *
from tkinter import messagebox
import tkinterInterestCalculator_Help as info_guide

class Window(Frame):

    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.master = master
        self.type = IntVar()
        self.init_window()

    def callbackAmountEntryIn(self, event):
        self.amountEntry.selection_range(0, END)
        self.amountEntry.config(bg = "#DCDCDC")
    def callbackAmountEntryOut(self, event):
        self.amountEntry.config({"background": "white"})

    def callbackInterestEntryIn(self, event):
        self.interestEntry.selection_range(0, END)
        self.interestEntry.config(bg = "#DCDCDC")
    def callbackInterestEntryOut(self, event):
        self.interestEntry.config({"background": "white"})

    def callbackDurationYearsEntryIn(self, event):
        self.durationYearsEntry.selection_range(0, END)
        self.durationYearsEntry.config(bg = "#DCDCDC")
    def callbackDurationYearsEntryOut(self, event):
        self.durationYearsEntry.config({"background": "white"})

    def callbackDurationMonthsEntryIn(self, event):
        self.durationMonthsEntry.selection_range(0, END)
        self.durationMonthsEntry.config(bg = "#DCDCDC")
    def callbackDurationMonthsEntryOut(self, event):
        self.durationMonthsEntry.config({"background": "white"})

    def init_window(self):
        #Window Title
        self.master.title("Interest Calculation")

        #MenuBar
        menuMain = Menu(self.master)
        self.master.config(menu=menuMain)
        file = Menu(menuMain)
        file.add_command(label="Exit", command=self.client_exit)
        menuMain.add_cascade(label="File", menu=file)
        edit = Menu(menuMain)
        edit.add_command(label="Reset Values", command=self.reset_values)
        menuMain.add_cascade(label="Edit", menu=edit)
        help = Menu(menuMain)
        help.add_command(label="Info", command = self.info_section)
        menuMain.add_cascade(label="Help", menu=help)

        #Labels
        title = Label(text = "Interest Calculator",justify=CENTER, font=16, bg = "#adcbe3",width = 16)
        title.grid(ipady= 10,sticky=W+E,columnspan = 2)
        initialAmount = Label(text = "Initial Amount: ",bg="#e7eff6")
        initialAmount.grid(row=2, column=0, sticky=E,ipady= 5, ipadx = 5)
        interestRate = Label(text = "Interest Rate %: ",bg="#e7eff6")
        interestRate.grid(row=3, column=0, sticky=E,ipady= 5, ipadx = 5)
        lengthYears = Label(text = "Duration (Years): ",bg="#e7eff6")
        lengthYears.grid(row=4, column=0, sticky=E,ipady= 5, ipadx = 5)
        lengthMonths = Label(text = "Duration (Months): ",bg="#e7eff6")
        lengthMonths.grid(row=5, column=0, sticky=E,ipady= 5, ipadx = 5)
        finalTotal = Label(text = "Final amount: ",bg="#e7eff6")
        finalTotal.grid(row=6, column=0, sticky=E,ipady= 5, ipadx = 5)

        #Entries
        self.amountEntry = Entry(self.master, width=19)
        self.amountEntry.grid(row=2,column=1, sticky=W)
        self.amountEntry.insert(0, "0")
        self.amountEntry.bind("<FocusIn>", self.callbackAmountEntryIn)
        self.amountEntry.bind("<FocusOut>", self.callbackAmountEntryOut)

        self.interestEntry = Entry(self.master, width=19)
        self.interestEntry.grid(row=3,column=1, sticky=W)
        self.interestEntry.insert(0, "0")
        self.interestEntry.bind("<FocusIn>", self.callbackInterestEntryIn)
        self.interestEntry.bind("<FocusOut>", self.callbackInterestEntryOut)

        self.durationYearsEntry = Entry(self.master, width=19)
        self.durationYearsEntry.grid(row=4,column=1, sticky=W)
        self.durationYearsEntry.insert(0, "0")
        self.durationYearsEntry.bind("<FocusIn>", self.callbackDurationYearsEntryIn)
        self.durationYearsEntry.bind("<FocusOut>", self.callbackDurationYearsEntryOut)

        self.durationMonthsEntry = Entry(self.master, width=19)
        self.durationMonthsEntry.grid(row=5,column=1, sticky=W)
        self.durationMonthsEntry.insert(0, "0")
        self.durationMonthsEntry.bind("<FocusIn>", self.callbackDurationMonthsEntryIn)
        self.durationMonthsEntry.bind("<FocusOut>", self.callbackDurationMonthsEntryOut)

        self.finalEntry = Entry(self.master, width=19)
        self.finalEntry.grid(row=6,column=1, sticky=W)
        self.finalEntry.insert(0, "0")
        self.finalEntry.config(state="readonly")

        #Toggle Buttons
        self.calculateMonthlyToggle = Radiobutton(text = "Monthly accruement", variable = self.type, value = 1, indicatoron = 0, bg = "#4b86b4")
        self.calculateMonthlyToggle.grid(row=7,column=0,padx= 10,pady= 5)
        self.calculateMonthlyToggle.config(activebackground="#adcbe3",selectcolor="#adcbe3")

        self.calculateYearlyToggle = Radiobutton(text = "Yearly accruement", variable = self.type, value = 2, indicatoron = 0, bg = "#4b86b4")
        self.calculateYearlyToggle.grid(row=7,column=1,padx= 10,pady= 5, sticky = E)
        self.calculateYearlyToggle.config(activebackground="#adcbe3",selectcolor="#adcbe3")
        #self.calculateYearlyToggle.bind("<Button-1>", self.callbackCalculateYearlyToggleIn)

        #Calculate Button
        self.calculateButton = Button(text = "Calculate", command = self.calculateInterest, bg="#8be28b")
        self.calculateButton.grid(padx = 10, row=8, column =0, sticky = W)
        self.calculateButton.config(activebackground = "#4ed34e")


        #Quit button
        self.quitButton = Button(text="Quit the app",command=self.client_exit, bg="#ff6666")
        self.quitButton.grid(row = 8, column = 1, sticky = E, padx= 10,pady= 10)
        self.quitButton.config(activebackground = "#ff1919")

    #Test function
    def calculateInterest(self):
        try:
            amountEntry_variable = int(self.amountEntry.get())
            interestEntry_variable = int(self.interestEntry.get())
            durationYearsEntry_variable = int(self.durationYearsEntry.get())
            durationMonthsEntry_variable = int(self.durationMonthsEntry.get())
        except ValueError:
            messagebox.showerror("Error", "There is an invalid variable in your input!")
            return

        finalTally = amountEntry_variable

        if self.type.get() == 1:
            totalMonthsDuration = durationYearsEntry_variable*12 + durationMonthsEntry_variable
            for x in range(totalMonthsDuration):
                finalTally = finalTally + finalTally*(interestEntry_variable/100)/12
        elif self.type.get() == 2:
            for x in range(durationYearsEntry_variable):
                finalTally = finalTally + finalTally*(interestEntry_variable/100)
            finalTally = finalTally + amountEntry_variable*(interestEntry_variable/100)*durationMonthsEntry_variable/12
        else:
            messagebox.showerror("Error", "You didn't select an monthly or yearly interest accruement!")

        self.finalEntry.config(state="normal")
        self.finalEntry.delete(0,"end")
        self.finalEntry.insert(0, finalTally)
        self.finalEntry.config(state="readonly")

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

    def info_section(self):
        info_guide.Help_Guide()


root = Tk()
root.geometry("270x300")
root.resizable(width=False, height=False)
root.config(background="#e7eff6")
app = Window(root)
root.mainloop()

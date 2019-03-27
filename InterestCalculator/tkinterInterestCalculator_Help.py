from tkinter import *
from tkinter import messagebox

inputDescription = """1. Enter the amount of the principle you would like to calculate interest from.\n
2. Enter the interest rate you would like to have.\n
3. Enter the number of years you would like to calculate interest for.\n
4. Enter the number of months you would like to calculate interest for.\n
5. Choose whether you want to return the interest monthly or yearly."""


menubarDescription = """1. Exit - To exit the application\n
2. Reset Values - Changes the values of all inputs back to zero\n
3. Info - Provides useful information and serves as a guide for the application\n"""

def Help_Guide():
    info_Window = Toplevel()
    info_Window.geometry("460x500")
    info_Window.title("Help Guide")
    info_Window.config(background="#e7eff6")
    info_Window.resizable(width=False, height=False)

    #scrbr=Scrollbar(info_Window)
    #scrbr.grid(row=0, column=1, sticky=N+S+E)
    #info_Window_Canvas = Canvas(info_Window, yscrollcommand = scrbr.set)


    title = Label(info_Window, text="Interest Calculator help guide", bg = "#879eb0")
    title.grid(row=0,column=0,ipadx=150,ipady=10,sticky=W+E)
    subtitle = Label(info_Window, text="... for the clueless ones", bg = "#879eb0")
    subtitle.grid(row=1,pady=(0,10),column=0,sticky=W+E)

    summary = Label(info_Window, text="Short guide to explaining the details of this app", bg = "#adcbe3",anchor=W)
    summary.grid(row=3,column=0,ipadx=10,ipady=5,sticky=W+E)

    title_inputs = Label(info_Window, text="Inputs", bg = "#b0d2cf",anchor=W)
    title_inputs.grid(row=4,column=0,ipadx=10,ipady=10,sticky=W+E)
    descriptions_inputs = Label(info_Window, text=inputDescription, bg="#cee9ea")
    descriptions_inputs.grid(row=5,column=0,ipadx=10,ipady=3,sticky=W+E)

    title_menubar = Label(info_Window, text="Menubar", bg = "#b0d2cf",anchor=W)
    title_menubar.grid(row=6,column=0,ipadx=10,ipady=10,sticky=W+E)
    descriptions_menubar = Label(info_Window, text=menubarDescription, bg="#cee9ea")
    descriptions_menubar.grid(row=7,column=0,ipadx=10,ipady=3,sticky=W+E)

    go_back = Button(info_Window, text="Close", command=info_Window.destroy)
    go_back.grid(row=8,column=0, pady = 5)

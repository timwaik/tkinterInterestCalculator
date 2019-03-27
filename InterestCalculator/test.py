from tkinter import *

root = Tk()
scrollbar = Scrollbar(root)
scrollbar.grid(row=0,column=1,sticky=N+S)

mylist = Canvas(root, yscrollcommand = scrollbar.set )
for line in range(100):
   a = (mylist, "This is line number " + str(line))

mylist.grid(row=0,column=0)
scrollbar.config( command = mylist.yview )

mainloop()

from tkinter import * 
from tkinter.ttk import *
  
master = Tk()
  
master.geometry("1000x1000")

def openNewWindow():

    newWindow = Toplevel(master)

    newWindow.title("Compliment 1")

    newWindow.geometry("355x225")

    Label(newWindow, 
          text ="Hey I think you are very awesome").pack()
    
    newWindow = Toplevel(master)

    newWindow.title("Compliment 2")

    newWindow.geometry("325x325")

    Label(newWindow, 
          text ="I appriciate you so much").pack()              #I made this for you so you better enjoy it ay <3
    
    newWindow = Toplevel(master)

    newWindow.title("Compliment 3")

    newWindow.geometry("525x325")

    Label(newWindow, 
          text ="I love you").pack()
    
    newWindow = Toplevel(master)

    newWindow.title("Compliment 4")
    newWindow.geometry("725x525")

    Label(newWindow, 
          text ="You are amazing").pack()
    
    newWindow = Toplevel(master)

    newWindow.title("Compliment 5")
    newWindow.geometry("525x225")

    Label(newWindow, 
          text ="Im here for you").pack()
    
    newWindow = Toplevel(master)

    newWindow.title("Compliment 6")
    newWindow.geometry("625x625")

    Label(newWindow, 
          text ="You are very talented").pack()
    
    newWindow = Toplevel(master)

    newWindow.title("Compliment 7")
    newWindow.geometry("425x325")

    Label(newWindow, 
          text ="Youre *drip* is amazing").pack()
    
  
label = Label(master, 
              text ="Welcome to the compliment machine!")
  
label.pack(pady = 10)

btn = Button(master, 
             text ="Do you want a compliment?", 
             command = openNewWindow)
btn.pack(pady = 10)
  
mainloop()
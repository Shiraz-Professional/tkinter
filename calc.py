import tkinter as tk
from tkinter import font as tkFont
import random


class App(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self.geometry("900x900+100+100")
        self.titlefont = tkFont.Font(family="Arial", size=20, slant="italic")
        self.buttonFont = tkFont.Font(family="Arial", size=18)
        
        self.label = tk.Label(self, text="Welcome to my app", font=self.titlefont)
        #column span makes a label spread throughout 2 columns
        self.label.grid(row=0, column=0, columnspan=2)
        
        self.Button1 = tk.Button(self, text="Press Me", bg="green", fg="white", command = self.buttonPressed)
        self.Button1.grid(row=2, column=1)
        
        self.textbox = tk.Entry(self, text="enter here",show="*")
        self.textbox.grid(row=2, column=0)
        self.textbox.bind("<Return>", self.buttonPressed)
        
        self.c_label = tk.Label(self, text="HB is on the spectrum", font=self.titlefont, bg="blue", fg="white")
        self.c_label.grid(row=3, column=0, sticky = "EW")
        



        self.mainloop()        


    def buttonPressed(self, e=None):
        if self.textbox.get() == "banana":
            self.c_label.config(text="Good HB",bg = "green")
        else:
            self.c_label.config(text="Naughty HB",bg = "red")
            
class CalculatorApp(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self.titleFont = tkFont.Font(family="Arial", size=30)
        self.titleFont2 = tkFont.Font(family="Arial", size=15)
        self.output = tk.Label(text="Output",fg="#111111", bg="#a3f7f1", font=self.titleFont)
        self.output.grid(column=0, row=0, columnspan=4, sticky="NSEW")
        
        self.geometry("900x900+100+100")
        self.button0 = tk.Button(self, text = "0", font=self.titleFont)
        self.button1 = tk.Button(self, text = "1", font=self.titleFont)
        self.button2 = tk.Button(self, text = "2", font=self.titleFont)
        self.button3 = tk.Button(self, text = "3", font=self.titleFont)
        self.button4 = tk.Button(self, text = "4", font=self.titleFont)
        self.button5 = tk.Button(self, text = "5", font=self.titleFont)
        self.button6 = tk.Button(self, text = "6", font=self.titleFont)
        self.button7 = tk.Button(self, text = "7", font=self.titleFont)
        self.button8 = tk.Button(self, text = "8", font=self.titleFont)
        self.button9 = tk.Button(self, text = "9", font=self.titleFont)
        self.addButton = tk.Button(self, text = "+", font=self.titleFont)
        self.minusButton = tk.Button(self, text = "-", font=self.titleFont)
        self.equalButton = tk.Button(self, text = "=", font=self.titleFont)
        
        self.button0.grid(row = 4, column = 2, sticky = "nesw")
        self.button1.grid(row = 1, column = 0, sticky = "nesw")
        self.button2.grid(row = 1, column = 1, sticky = "nesw")
        self.button3.grid(row = 1, column = 2, sticky = "nesw")
        self.button4.grid(row = 2, column = 0, sticky = "nesw")
        self.button5.grid(row = 2, column = 1, sticky = "nesw")
        self.button6.grid(row = 2, column = 2, sticky = "nesw")
        self.button7.grid(row = 3, column = 0, sticky = "nesw")
        self.button8.grid(row = 3, column = 1, sticky = "nesw")
        self.button9.grid(row = 3, column = 2, sticky = "nesw")
        self.addButton.grid(row = 3, column = 3, sticky = "nesw")
        self.minusButton.grid(row = 2, column = 3, sticky = "nesw")
        self.equalButton.grid(row = 4, column = 3, sticky = "nesw")
        
        
        self.columnconfigure(0,weight=100)
        self.columnconfigure(1,weight=100)
        self.columnconfigure(2,weight=100)
        self.columnconfigure(3,weight=100)
        self.rowconfigure(0,weight=100)
        self.rowconfigure(1,weight=100)
        self.rowconfigure(2,weight=100)
        self.rowconfigure(3,weight=100)
        self.rowconfigure(4,weight=100)
        self.currentNumber = ""
        self.total = 0
        self.operation = "add"
        self.mainloop()
        
    def digitPressed(self,num):
        self.currentNumber += str(num)
        if self.total == 0:
            self.output.config(text=self.currentNumber)
        else:
            self.output.config(text = str(self.total) + self.operation + self.currentNumber)
        
    def addPressed(self):
        self.equalsPressed()
        self.operation = "add"
        self.currentNumbers = ""
        pass

    def minuspressed(self):
        # set current operation to subtract
        # put current number into the total
        # start a new current number
        pass

    def equalsPressed(self):
        # if the current operation is "add"
        #    Add the current number to the total
        #    output the result
        # if the current operation is "subtract"
        #    subtract the current number from the total
        #    output the result
        pass


    
app = CalculatorApp()


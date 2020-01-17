import datetime
from tkinter import *
import os.path
import random

class Trace:
    
    def __init__(self):
        
        global const_Filename

        self.filename = datetime.date.today().__str__()
        const_Filename = self.filename

        while os.path.exists(const_Filename):
            const_Filename = self.filename + str(chr(random.randint(67, 122))) + ".txt"

        file = open(const_Filename, "a")
        file.write("*** STACK TRACE STARTED ***\n")
        file.close()
        
    def Trace(self, event: E) -> E:
        
        self.Event = event

        if self.Event == "":
            file = open(const_Filename, "a")
            file.write(f"[{datetime.datetime.now()}]:::[Raised ValueError, Tracer Must Have Valid Event]\n")
            file.close()
        else:
            file = open(const_Filename, "a")
            file.write(f"[{datetime.datetime.now()}]:::[{self.Event}]\n")
            file.close()
        
    def EndTrace(self):
        
        self.EndEvent = "Stack Trace End\n"
        file = open(const_Filename, "a")
        file.write(self.EndEvent)
        file.write(f"Stack trace ended at: {datetime.datetime.now()}\n")
        file.write("*** STACK TRACE ENDED ***\n")

class _EndTrace:

    def __init__(self):
        print(f"New Contrauctor: {self} created")

    def _EndTrace(self, master: object, row: object, column: object, _width: object, _height: object, _bg: object, _fg: object) -> object:

        self.Master = master
        self.Y = row
        self.X = column
        self.Width = _width
        self.Height = _height

        EndTraceButton = Button(self.Master, text= "End", width= self.Width, height= self.Height, bg= _bg, fg=_fg, command=_EndTrace.__EndTrace)
        EndTraceButton.grid(row=self.Y, column=self.X)

    @staticmethod
    def __EndTrace():

        file = open(const_Filename, "a")
        file.write(f"Stack Trace Ended at: {datetime.datetime.now()}\n")
        file.write("*** STACK TRACE ENDED ***\n")

        exit()
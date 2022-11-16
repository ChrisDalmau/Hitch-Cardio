#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 12 08:20:55 2022

@author: christopherdalmau
"""

from fileinput import close
from tkinter import RAISED
from math import *


import tkinter as tk                # python 3
from tkinter import font as tkfont  # python 3


def calc():
    mx = maxhr.get()
    rest = resthr.get()
    math = tk.Label(right_frame, text = int (maxhr / minhr)**15.3).grid(row = 0, column = 0, padx = 5, pady = 5)
         
        

def close():
    app.destroy()
    
class Vo2Max(tk.Tk):

    def __init__(self, *args, **kwargs):

        
        tk.Tk.__init__(self, *args, **kwargs)

        self.title_font = tkfont.Font(family='Helvetica', size=18, weight="bold", slant="italic")

        # the container is where we'll stack a bunch of frames
        # on top of each other, then the one we want visible
        # will be raised above the others
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}
        for F in (StartPage, PageOne, weeklyavg, monthavg1, yearavg1, adddata, datapage,VO2Calc):
            page_name = F.__name__
            frame = F(parent=container, controller=self)
            self.frames[page_name] = frame

            # put all of the pages in the same location;
            # the one on the top of the stacking order
            # will be the one that is visible.
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame("StartPage")

    def show_frame(self, page_name):
        '''Show a frame for the given page name'''
        frame = self.frames[page_name]
        frame.tkraise()

class adddata(tk.Frame):
    
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

                # Create left and right frames
        left_frame = tk.Frame(self, width=200, height=400, bg='grey')
        left_frame.grid(row=0, column=0, padx=10, pady=5)

        right_frame = tk.Frame(self, width=650, height=400, bg='grey')
        right_frame.grid(row=0, column=1, padx=10, pady=5)


        # Create frames and labels in left_frame
        tk.Label(left_frame, text="Are you in a good shape?").grid(row=0, column=0, padx=5, pady=5)
        

        tk.Label(left_frame).grid(row=1, column=0, padx=50, pady=50)


        # Create tool bar frame
        tool_bar = tk.Frame(left_frame, width=180, height=185)
        tool_bar.grid(row=2, column=0, padx=5, pady=5)

        # Example labels that serve as placeholders for other widgets
        tk.Label(tool_bar, text="Tools", font=('Arial', 9, 'bold', 'underline'),relief=RAISED).grid(row=0, column=0, padx=5, pady=3, ipadx=10)  # ipadx is padding inside the Label widget
        weekavg =tk.Button(tool_bar, text="Weekly Average", command=lambda: controller.show_frame("weeklyavg")).grid(row=1, column=0, padx=5, pady=5)
        monthavg = tk.Button(tool_bar, text="Monthly Average", command=lambda: controller.show_frame("monthavg1")).grid(row=2, column=0, padx=5, pady=5)
        yearavg = tk.Button(tool_bar, text="Yearly Average", command=lambda: controller.show_frame("yearavg1")).grid(row=3, column=0, padx=5, pady=5)
       
        addmore=tk.Button(tool_bar, text="Add More Data", 
                          command=lambda: controller.show_frame("datapage")).grid(row=4, column=0, padx=5, pady=5)
        exitapp =tk.Button(tool_bar, text="Exit", command=close).grid(row=5, column=0, padx=5, pady=5)

class VO2Calc(tk.Frame):
    
    
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        left_frame = tk.Frame(self, width=200, height=400, bg='grey')
        left_frame.grid(row=0, column=0, padx=10, pady=5)
        
        right_frame = tk.Frame(self, width=650, height=400, bg='grey')
        right_frame.grid(row=0, column=1, padx=10, pady=5)
        
        tk.Label(left_frame, text="Are you in a good shape?").grid(row=0, column=0, padx=5, pady=5)
        tk.Label(right_frame,text = "Enter your max heart rate: ").grid(row=0, column = 1, padx = 5, pady = 5)
        maxhr = tk.Entry(right_frame).grid(row = 1, column = 1)
        tk.Label(right_frame,text = "Enter your resting heart rate: ").grid(row=2, column = 1, padx = 5, pady = 5)
        resthr = tk.Entry(right_frame).grid(row = 3, column = 1)
        calculate = tk.Button(right_frame, text = "Calculate",
                              command = lambda: controller.show_frame("VO2Calc")).grid(row = 4,column = 1,padx = 5,pady = 5)
        
        
        
        
        tool_bar = tk.Frame(left_frame, width=180, height=185)
        tool_bar.grid(row=2, column=0, padx=5, pady=5)
        
        tk.Label(tool_bar, text="Tools", font=('Arial', 9, 'bold', 'underline'),relief=RAISED).grid(row=0, column=0, padx=5, pady=3, ipadx=10)
        backbutton = tk.Button(tool_bar, text = "Back",command=lambda: controller.show_frame("PageOne")).grid(row = 2,column = 0,padx = 5,pady = 5)
        
        tk.Label(right_frame, text = "Your VO2Max is: ", command = calc).grid(row = 0, column = 0, padx = 5, pady = 5)
        

    

    
        
class datapage(tk.Frame):
    
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        left_frame = tk.Frame(self, width=200, height=400, bg='grey')
        left_frame.grid(row=0, column=0, padx=10, pady=5)
       
        
        right_frame = tk.Frame(self, width=650, height=400, bg='grey')
        right_frame.grid(row=0, column=1, padx=10, pady=5)

        
        # Create frames and labels in left_frame
        tk.Label(left_frame, text="Are you in a good shape?").grid(row=0, column=0, padx=5, pady=5)
        
        
        tk.Label(right_frame,text = "Enter your max heart rate: ").grid(row=0, column = 1, padx = 5, pady = 5)
        maxhr = tk.Entry(right_frame).grid(row = 1, column = 1)
        tk.Label(right_frame,text = "Enter your resting heart rate: ").grid(row=2, column = 1, padx = 5, pady = 5)
        resthr = tk.Entry(right_frame).grid(row = 3, column = 1)
        calculate = tk.Button(right_frame, text = "Calculate",
                              command = lambda: controller.show_frame("VO2Calc")).grid(row = 4,column = 1,padx = 5,pady = 5)

        tk.Label(left_frame).grid(row=1, column=0, padx=50, pady=50)
        # Create tool bar frame
        tool_bar = tk.Frame(left_frame, width=180, height=185)
        tool_bar.grid(row=2, column=0, padx=5, pady=5)

        # Example labels that serve as placeholders for other widgets
        tk.Label(tool_bar, text="Tools", font=('Arial', 9, 'bold', 'underline'),relief=RAISED).grid(row=0, column=0, padx=5, pady=3, ipadx=10)
        backbutton = tk.Button(tool_bar, text = "Back",command=lambda: controller.show_frame("PageOne")).grid(row = 2,column = 0,padx = 5,pady = 5)

        

class StartPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="Hitch Cardio", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)

        button1 = tk.Button(self, text="Click to see your Vo2 max",
                            command=lambda: controller.show_frame("PageOne"))

        button1.pack()

  
class PageOne(tk.Frame):
    
        
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        # Create left and right frames
        left_frame = tk.Frame(self, width=200, height=400, bg='grey')
        left_frame.grid(row=0, column=0, padx=10, pady=5)

        right_frame = tk.Frame(self, width=650, height=400, bg='grey')
        right_frame.grid(row=0, column=1, padx=10, pady=5)


        # Create frames and labels in left_frame
        tk.Label(left_frame, text="Are you in a good shape?").grid(row=0, column=0, padx=5, pady=5)
        

        tk.Label(left_frame).grid(row=1, column=0, padx=50, pady=50)


        # Create tool bar frame
        tool_bar = tk.Frame(left_frame, width=180, height=185)
        tool_bar.grid(row=2, column=0, padx=5, pady=5)

        # Example labels that serve as placeholders for other widgets
        tk.Label(tool_bar, text="Tools", font=('Arial', 9, 'bold', 'underline'),relief=RAISED).grid(row=0, column=0, padx=5, pady=3, ipadx=10)  # ipadx is padding inside the Label widget
        weekavg =tk.Button(tool_bar, text="Weekly Average", command=lambda: controller.show_frame("weeklyavg")).grid(row=1, column=0, padx=5, pady=5)
        monthavg = tk.Button(tool_bar, text="Monthly Average", command=lambda: controller.show_frame("monthavg1")).grid(row=2, column=0, padx=5, pady=5)
        yearavg = tk.Button(tool_bar, text="Yearly Average", command=lambda: controller.show_frame("yearavg1")).grid(row=3, column=0, padx=5, pady=5)
        addmore=tk.Button(tool_bar, text="Add More Data", command=lambda: controller.show_frame("adddata")).grid(row=4, column=0, padx=5, pady=5)
        exitapp =tk. Button(tool_bar, text="Exit", command = close).grid(row=5, column=0, padx=5, pady=5)


class weeklyavg(tk.Frame):
    
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

                # Create left and right frames
        left_frame = tk.Frame(self, width=200, height=400, bg='grey')
        left_frame.grid(row=0, column=0, padx=10, pady=5)

        right_frame = tk.Frame(self, width=650, height=400, bg='grey')
        right_frame.grid(row=0, column=1, padx=10, pady=5)


        # Create frames and labels in left_frame
        tk.Label(left_frame, text="Are you in a good shape?").grid(row=0, column=0, padx=5, pady=5)
        

        tk.Label(left_frame).grid(row=1, column=0, padx=50, pady=50)


        # Create tool bar frame
        tool_bar = tk.Frame(left_frame, width=180, height=185)
        tool_bar.grid(row=2, column=0, padx=5, pady=5)

        # Example labels that serve as placeholders for other widgets
        tk.Label(tool_bar, text="Tools", font=('Arial', 9, 'bold', 'underline'),relief=RAISED).grid(row=0, column=0, padx=5, pady=3, ipadx=10)  # ipadx is padding inside the Label widget
        monthavg = tk.Button(tool_bar, text="Monthly Average", command=lambda: controller.show_frame("monthavg1")).grid(row=2, column=0, padx=5, pady=5)
        yearavg = tk.Button(tool_bar, text="Yearly Average", command=lambda: controller.show_frame("yearavg1")).grid(row=3, column=0, padx=5, pady=5)
        addmore=tk.Button(tool_bar, text="Add More Data", command=lambda: controller.show_frame("adddata")).grid(row=4, column=0, padx=5, pady=5)
        exitapp =tk. Button(tool_bar, text="Exit", command=close).grid(row=5, column=0, padx=5, pady=5)

class monthavg1(tk.Frame):
    
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

                # Create left and right frames
        left_frame = tk.Frame(self, width=200, height=400, bg='grey')
        left_frame.grid(row=0, column=0, padx=10, pady=5)

        right_frame = tk.Frame(self, width=650, height=400, bg='grey')
        right_frame.grid(row=0, column=1, padx=10, pady=5)


        # Create frames and labels in left_frame
        tk.Label(left_frame, text="Are you in a good shape?").grid(row=0, column=0, padx=5, pady=5)
        

        tk.Label(left_frame).grid(row=1, column=0, padx=50, pady=50)


        # Create tool bar frame
        tool_bar = tk.Frame(left_frame, width=180, height=185)
        tool_bar.grid(row=2, column=0, padx=5, pady=5)

        # Example labels that serve as placeholders for other widgets
        tk.Label(tool_bar, text="Tools", font=('Arial', 9, 'bold', 'underline'),relief=RAISED).grid(row=0, column=0, padx=5, pady=3, ipadx=10)  # ipadx is padding inside the Label widget
        weekavg =tk.Button(tool_bar, text="Weekly Average", command=lambda: controller.show_frame("weeklyavg")).grid(row=1, column=0, padx=5, pady=5)
        yearavg = tk.Button(tool_bar, text="Yearly Average", command=lambda: controller.show_frame("yearavg1")).grid(row=3, column=0, padx=5, pady=5)
        addmore=tk.Button(tool_bar, text="Add More Data", command=lambda: controller.show_frame("adddata")).grid(row=4, column=0, padx=5, pady=5)
        exitapp =tk. Button(tool_bar, text="Exit", command=close).grid(row=5, column=0, padx=5, pady=5)

class yearavg1(tk.Frame):
    
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

                # Create left and right frames
        left_frame = tk.Frame(self, width=200, height=400, bg='grey')
        left_frame.grid(row=0, column=0, padx=10, pady=5)

        right_frame = tk.Frame(self, width=650, height=400, bg='grey')
        right_frame.grid(row=0, column=1, padx=10, pady=5)


        # Create frames and labels in left_frame
        tk.Label(left_frame, text="Are you in a good shape?").grid(row=0, column=0, padx=5, pady=5)
        

        tk.Label(left_frame).grid(row=1, column=0, padx=50, pady=50)


        # Create tool bar frame
        tool_bar = tk.Frame(left_frame, width=180, height=185)
        tool_bar.grid(row=2, column=0, padx=5, pady=5)

        # Example labels that serve as placeholders for other widgets
        tk.Label(tool_bar, text="Tools", font=('Arial', 9, 'bold', 'underline'),relief=RAISED).grid(row=0, column=0, padx=5, pady=3, ipadx=10)  # ipadx is padding inside the Label widget
        weekavg =tk.Button(tool_bar, text="Weekly Average", command=lambda: controller.show_frame("weeklyavg")).grid(row=1, column=0, padx=5, pady=5)
        monthavg = tk.Button(tool_bar, text="Monthly Average", command=lambda: controller.show_frame("monthavg1")).grid(row=2, column=0, padx=5, pady=5)
        addmore=tk.Button(tool_bar, text="Add More Data", command=lambda: controller.show_frame("adddata")).grid(row=4, column=0, padx=5, pady=5)
        exitapp =tk. Button(tool_bar, text="Exit", command=close).grid(row=5, column=0, padx=5, pady=5)





if __name__ == "__main__":
    app = Vo2Max()
    app.mainloop()
    





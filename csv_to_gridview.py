import tkinter
from tkinter import * 
from tkinter.ttk import *
from tkinter import messagebox
from tkinter import filedialog
import os
import pathlib
import pandas as pd
import csv

root = tkinter.Tk()

file = filedialog.askopenfile(mode ='r', filetypes =[('csv', '*.csv')]) 

with open(file.name, newline = "") as file:
   reader = csv.reader(file)

   # Construction du tableau
   r = 0
   for col in reader:
      c = 0
      for row in col:
         # Mise en forme
         label = tkinter.Label(root, width = 10, height = 2, \
                               text = row, relief = tkinter.RIDGE)
         label.grid(row = r, column = c)
         c += 1
      r += 1

root.mainloop()

import tkinter 
from tkinter import *
from tkinter.messagebox import *
from tkinter.font import Font
from tkinter.scrolledtext import *
from tkinter.filedialog import *
"""import help_menu
import file_menu
import edit_menu
import format_menu"""

r = Tk()
r.title("Building bridges")
Label(r, text="Registration Form").pack()
button = Button(r, text="Sleep", width=30)

"""help_menu.main(r, text, menubar)"""
button.pack()
r.mainloop()
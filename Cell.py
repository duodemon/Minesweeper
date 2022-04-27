from tkinter import *


class Cell(Button):
    state = 0
    value = -1

    def __init__(self, master=None, cnf={}, **kw):
        super().__init__(master, cnf, **kw)

import random
from tkinter import *
from tkinter import ttk
from Cell import Cell
from random import randint
from functools import partial
from constants import Constants
from threading import Timer


def initialize_reset():
    Button(frm1, command=lambda: initialize_grid(), text="Reset", height=2, width=10).pack(side=LEFT, expand=True)


def initialize_custom():
    Label(frm2, text="Height").grid(column=0, row=0)
    height_text = Text(frm2, height=1, width=5)
    height_text.insert('end', Constants.height)
    height_text.grid(column=1, row=0)
    Label(frm2, text="Width").grid(column=0, row=1)
    width_text = Text(frm2, height=1, width=5)
    width_text.insert('end', Constants.width)
    width_text.grid(column=1, row=1)
    Label(frm2, text="Number of Mines").grid(column=0, row=2)
    num_mines_text = Text(frm2, height=1, width=5)
    num_mines_text.insert('end', Constants.num_mines)
    num_mines_text.grid(column=1, row=2)
    Button(frm2, command=lambda: confirm_custom(height_text.get('1.0', 'end'), width_text.get('1.0', 'end'), num_mines_text.get('1.0', 'end')), text="Confirm").grid(column=1, row=3)


def confirm_custom(new_height, new_width, new_mines):
    if not new_height.strip().isdigit() or not new_width.strip().isdigit() or not new_mines.strip().isdigit() or new_height == 0 or new_width == 0:
        return
    Constants.height = int(new_height)
    Constants.width = int(new_width)
    Constants.num_mines = int(new_mines)
    if Constants.num_mines > Constants.height * Constants.width:
        Constants.num_mines = Constants.height * Constants.width
    initialize_grid()


def initialize_clock():
    seconds = 0
    clock = Label(root, font=("Courier", 30))
    clock.place(relx=1, rely=0, x=0, y=25, anchor=E)
    t = Timer(1, lambda: update_clock(seconds + 1, clock))
    t.daemon = True
    t.start()


def update_clock(seconds, clock):
    clock["text"] = seconds
    t = Timer(1, lambda: update_clock(seconds + 1, clock))
    t.daemon = True
    t.start()


def initialize_grid():
    mines.clear()
    width = Constants.width
    height = Constants.height
    num_mines = Constants.num_mines
    for child in frm3.winfo_children():
        child.destroy()
    cells.clear()
    for x in range(width):
        for y in range(height):
            cells[x, y] = Cell(frm3, command=partial(on_click, x, y), height=1, width=2)
            cells[x, y].grid(column=x, row=y)
            cells[x, y].bind("<Button-2>", right_click)
            cells[x, y].bind("<Button-3>", right_click)

    for mine in range(num_mines):
        x = random.randint(0, width - 1)
        y = random.randint(0, height - 1)
        while (x, y) in mines:
            x = random.randint(0, width - 1)
            y = random.randint(0, height - 1)
        mines.add((x, y))

    for x in range(width):
        for y in range(height):
            if (x, y) in mines:
                continue
            count = 0
            if (x-1, y) in cells and (x-1, y) in mines:
                count += 1
            if (x-1, y-1) in cells and (x-1, y-1) in mines:
                count += 1
            if (x-1, y+1) in cells and (x-1, y+1) in mines:
                count += 1
            if (x, y+1) in cells and (x, y+1) in mines:
                count += 1
            if (x, y-1) in cells and (x, y-1) in mines:
                count += 1
            if (x+1, y-1) in cells and (x+1, y-1) in mines:
                count += 1
            if (x+1, y) in cells and (x+1, y) in mines:
                count += 1
            if (x+1, y+1) in cells and (x+1, y+1) in mines:
                count += 1
            cells[x, y].value = count

    for y in range(height):
        for x in range(width):
            print(cells[x, y].value, end=" ")
        print("")


def right_click(*args):
    print(args)


def on_click(x, y):
    if (x, y) in mines:
        for mine_coords in mines:
            cells[mine_coords]["text"] = "x"
            cells[mine_coords]["relief"] = SUNKEN
    elif cells[x, y].value > 0:
        cells[x, y]["text"] = str(cells[x, y].value)
        cells[x, y]["relief"] = SUNKEN
    elif cells[x, y].value == 0:
        cells[x, y]["relief"] = SUNKEN
        traverse_empty_cells(x, y)
    return


def traverse_empty_cells(starting_x, starting_y):
    queue = [(starting_x, starting_y)]
    visited = set()
    while queue:
        x, y = queue.pop()
        visited.add((x, y))
        if (x - 1, y) in cells and (x - 1, y) not in visited:
            if cells[x - 1, y].value == 0:
                queue.append((x - 1, y))
            else:
                cells[x - 1, y]["text"] = str(cells[x - 1, y].value)
            cells[x - 1, y]["relief"] = SUNKEN
        if (x - 1, y - 1) in cells and (x - 1, y - 1) not in visited:
            if cells[x - 1, y - 1].value == 0:
                queue.append((x - 1, y - 1))
            else:
                cells[x - 1, y - 1]["text"] = str(cells[x - 1, y - 1].value)
            cells[x - 1, y - 1]["relief"] = SUNKEN
        if (x - 1, y + 1) in cells and (x - 1, y + 1) not in visited:
            if cells[x - 1, y + 1].value == 0:
                queue.append((x - 1, y + 1))
            else:
                cells[x - 1, y + 1]["text"] = str(cells[x - 1, y + 1].value)
            cells[x - 1, y + 1]["relief"] = SUNKEN
        if (x, y + 1) in cells and (x, y + 1) not in visited:
            if cells[x, y + 1].value == 0:
                queue.append((x, y + 1))
            else:
                cells[x, y + 1]["text"] = str(cells[x, y + 1].value)
            cells[x, y + 1]["relief"] = SUNKEN
        if (x, y - 1) in cells and (x, y - 1) not in visited:
            if cells[x, y - 1].value == 0:
                queue.append((x, y - 1))
            else:
                cells[x, y - 1]["text"] = str(cells[x, y - 1].value)
            cells[x, y - 1]["relief"] = SUNKEN
        if (x + 1, y - 1) in cells and (x + 1, y - 1) not in visited:
            if cells[x + 1, y - 1].value == 0:
                queue.append((x + 1, y - 1))
            else:
                cells[x + 1, y - 1]["text"] = str(cells[x + 1, y - 1].value)
            cells[x + 1, y - 1]["relief"] = SUNKEN
        if (x + 1, y) in cells and (x + 1, y) not in visited:
            if cells[x + 1, y].value == 0:
                queue.append((x + 1, y))
            else:
                cells[x + 1, y]["text"] = str(cells[x + 1, y].value)
            cells[x + 1, y]["relief"] = SUNKEN
        if (x + 1, y + 1) in cells and (x + 1, y + 1) not in visited:
            if cells[x + 1, y + 1].value == 0:
                queue.append((x + 1, y + 1))
            else:
                cells[x + 1, y + 1]["text"] = str(cells[x + 1, y + 1].value)
            cells[x + 1, y + 1]["relief"] = SUNKEN


cells = {}
mines = set()
root = Tk()
frm1 = ttk.Frame(root, padding=50, width=100, height=50)
frm1.pack(side=TOP)
frm2 = ttk.Frame(root, padding=50, width=100, height=100)
frm2.pack(side=LEFT)
frm3 = ttk.Frame(root, padding=50, width=100, height=100)
frm3.pack(side=BOTTOM)
root.title("Minesweeper")
initialize_reset()
initialize_clock()
initialize_custom()
initialize_grid()
root.mainloop()
import random
from tkinter import *
from tkinter import ttk
from Cell import Cell
from random import randint
from functools import partial


def initialize_grid(width, height, num_flags):
    for x in range(width):
        for y in range(height):
            cells[x, y] = Cell(frm, command=partial(on_click, x, y), height=1, width=2)
            cells[x, y].grid(column=x, row=y)

    for flag in range(num_flags):
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
frm = ttk.Frame(root, padding=50, width=100, height=100)
frm.grid()
root.title("Minesweeper")
initialize_grid(15, 15, 15)
root.mainloop()
import random
import curses

curses.initscr()
win = curses.newwin(20,60,0,0)
win.keypad(1)
curses.noecho()
curses.curs_set(0)
win.border(0)
win.nodelay(1)
score = 0

while True:
    event = win.getch()





curses.endwin()
print(f"final score = {score}")


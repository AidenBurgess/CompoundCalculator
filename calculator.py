'''
Visual calculator in python for interest rates
Author: Aiden Burgess
'''
from tkinter import *
import settings
import compound_calculator
import year_by


def new_screen(fnc):
    main_screen.destroy()
    fnc()


def initialise_main_screen(screen):
    screen.title("Aiden's Calculator")
    screen.geometry('400x400')
    screen.configure(background=settings.BLACK)


def main_screen_format(screen):
    Label(screen, text='Aiden\'s Calculator\nMain Screen', fg=settings.WHITE, bg=settings.BLACK, font=settings.title_font) \
        .grid(row=0, column=0, sticky=NSEW)
    Button(screen, text='Calculate ending capital', width=18, command=lambda: new_screen(compound_calculator.start_calc)) \
        .grid(row=1, column=0, sticky=NSEW)
    Button(screen, text='Year by year', width=18, command=lambda: new_screen(year_by.start_calc)) \
        .grid(row=2, column=0, sticky=NSEW)


# Open main window
main_screen = Tk()
initialise_main_screen(main_screen)
# Add widgets to main window
main_screen_format(main_screen)

print('hi')
# Center everything
main_screen.grid_rowconfigure(0, weight=2)
main_screen.grid_rowconfigure(1, weight=1)
main_screen.grid_rowconfigure(2, weight=1)
main_screen.grid_columnconfigure(0, weight=1)

# Run the window
main_screen.mainloop()

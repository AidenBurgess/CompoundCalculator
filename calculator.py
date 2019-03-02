'''
Visual calculator in python for interest rates
Author: Aiden Burgess
'''
import tkinter as tk
import settings
import simple_calc
import compound_calculator
import year_by


class MainScreen:

    def __init__(self):
        # Open main window
        self.screen = tk.Tk()
        self.init_main_screen()
        # Add widgets to main window
        self.format_main_screen()
        # Run the window
        self.screen.mainloop()

    def new_screen(self, fnc):
        self.screen.destroy()
        fnc()

    def init_main_screen(self):
        self.screen.title("Aiden's Calculator")
        self.screen.geometry('600x400')
        self.screen.configure(background=settings.BLACK)

    def format_main_screen(self):
        # Display title logo
        photo = tk.PhotoImage(file='title_logo.gif')
        logo = tk.Label(self.screen, image=photo, bg=settings.BLACK)
        logo.grid(row=0, column=0, sticky=tk.NSEW)
        logo.image = photo
        # Display buttons to the calculators
        tk.Button(self.screen, text='Simple Compound Calculator', width=18, command=lambda: self.new_screen(simple_calc.SimpleCalc)) \
            .grid(row=1, column=0, sticky=tk.NSEW)
        tk.Button(self.screen, text='Calculate Ending Capital', width=18, command=lambda: self.new_screen(compound_calculator.CompoundCalc)) \
            .grid(row=2, column=0, sticky=tk.NSEW)
        tk.Button(self.screen, text='Year by Year', width=18, command=lambda: self.new_screen(year_by.YearBy)) \
            .grid(row=3, column=0, sticky=tk.NSEW)
        # Center everything
        self.screen.grid_rowconfigure(0, weight=2)
        self.screen.grid_rowconfigure(1, weight=1)
        self.screen.grid_rowconfigure(2, weight=1)
        self.screen.grid_rowconfigure(3, weight=1)
        self.screen.grid_columnconfigure(0, weight=1)


if __name__ == '__main__':
    MainScreen()

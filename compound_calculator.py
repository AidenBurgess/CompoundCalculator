'''
This module is the capital calculator. It calculates ending capital from
interest rate, starting capital, number of years, and yearly contribution.

Author: Aiden Burgess
'''
from tkinter import *
import settings


def start_calc():
    new = CompoundCalculator()


class CompoundCalculator:

    def __init__(self):
        # Open new window for
        self.screen = Tk()
        self.screen.title('Compound Interest Calculator')
        self.screen.configure(background=settings.BLACK)
        # Build widgets onto window
        self.display_title()
        self.display_entry_boxes()
        self.display_radio_buttons()
        self.display_submit_button()
        self.output_ending_capital()
        # Build graph
        # Back button
        # Quit button
        # Start the window
        print('Initialised Capital Calculator')
        self.screen.mainloop()

    def display_title(self):
        Label(self.screen, text='Compound Interest', fg=settings.WHITE, bg=settings.BLACK,
              font=settings.title_font).grid(row=0, column=0, sticky=NSEW)

    def display_text(self, text, textbox):
        textbox.delete(0.0, END)
        textbox.insert(END, text)

    def display_entry_boxes(self):
        # Display all entry boxes and add them to a list, so they are callable
        self.entries = []
        entry_list = [('Starting Capital ($)', 1), ('Interest Rate (%)', 2),
                      ('Number of Years', 3), ('Yearly Contribution', 4)]
        for name, row in entry_list:
            Label(self.screen, text=name + ':', fg=settings.WHITE, bg=settings.BLACK,
                  font=settings.menu_font).grid(row=row, column=0, sticky=W)
            self.entries.append(Entry(self.screen, width=20, bg=settings.WHITE,
                                      font=settings.entry_font))
            self.entries[-1].grid(row=row, column=1, sticky=W)

    def display_radio_buttons(self):
        # Determines whether the yearly contribution is added to start or end
        # of the year
        Label(self.screen, text='Contribution Timing' + ':', fg=settings.WHITE, bg=settings.BLACK, font=settings.menu_font) \
            .grid(row=5, column=0, sticky=W)
        # Add the buttons into the same cell
        framing = Frame(self.screen, bg=settings.BLACK)
        framing.grid(row=5, column=1, sticky=NSEW)
        self.start_year_contribution = IntVar()
        radio1 = Radiobutton(framing, text='End of year', width=12,
                             indicatoron=0, variable=self.start_year_contribution, value=0)
        radio2 = Radiobutton(framing, text='Start of year',
                             width=12, indicatoron=0, variable=self.start_year_contribution, value=1)
        radio1.pack(side='left')
        radio2.pack(side='right')
        print('Radios constructed')

    def output_ending_capital(self):
        # Display the ending capital in textbox
        Label(self.screen, text='\nEnding Capital:', fg=settings.WHITE,
              bg=settings.BLACK, font=settings.menu_font).grid(row=7, column=0, sticky=W)
        self.ending_capital_disp = Text(
            self.screen, width=16, height=2, wrap=WORD, background=settings.WHITE, font=settings.entry_font)
        self.ending_capital_disp.grid(row=7, column=1, sticky=S)

    def display_submit_button(self):
        Button(self.screen, text='SUBMIT', width=10, command=self.calculate_ending_capital,
               font=settings.entry_font).grid(row=6, column=1, sticky=N, pady=10)

    def get_entries(self):
        # Grab all the entries from entry boxes
        self.capital = self.entries[0].get()
        self.rate = self.entries[1].get()
        self.num_periods = self.entries[2].get()
        self.contribution = self.entries[3].get()
        self.convert_entries_int()

    def convert_entries_int(self):
        # Convert parameters to int
        try:
            self.capital, self.rate, self.num_periods, self.contribution = list(
                map(int, [self.capital, self.rate, self.num_periods, self.contribution]))
        except:
            self.capital = 'Please enter numbers only'

    def calculate_ending_capital(self):
        self.get_entries()
        # Display error message
        if isinstance(self.capital, str):
            self.display_text(self.capital, self.ending_capital_disp)
        # Calculate ending capital then display final amount
        else:
            for self.year in range(self.num_periods):
                if self.start_year_contribution.get():
                    self.capital = (
                        self.capital + self.contribution) * (1 + self.rate / 100)
                else:
                    self.capital = self.capital * \
                        (1 + self.rate / 100) + self.contribution
            # Record each capital
            self.capital = '$' + str("{:,}".format(round(self.capital)))
            self.display_text(self.capital, self.ending_capital_disp)


if __name__ == '__main__':
    start_calc()

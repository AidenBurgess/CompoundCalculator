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
        print('Initialised Capital Calculator')
        Label(self.screen, text='Compound Interest', fg=settings.WHITE, bg=settings.BLACK, font=settings.title_font)\
            .grid(row=0, column=0, sticky=NSEW)
        # Display entry boxes
        self.display_entry_boxes()
        # Display radio buttons
        self.display_radio_buttons()
        # Submit button calculates end_capital
        Button(self.screen, text='SUBMIT', width=10, command=self.calculate_ending_capital,
               font=settings.entry_font).grid(row=6, column=1, sticky=N, pady=10)
        # Output ending capital
        self.output_ending_capital()
        # Build graph
        # Back button
        # Quit button
        # Start the window
        self.screen.mainloop()

    def display_text(self, text, textbox):
        textbox.delete(0.0, END)
        textbox.insert(END, text)

    def display_entry_boxes(self):
        # Display all entry boxes and add them to a list, so they are callable
        self.entries = []
        entry_list = [('Starting Capital ($)', 1), ('Interest Rate (%)', 2),
                      ('Number of Years', 3), ('Yearly Contribution', 4)]
        for name, row in entry_list:
            Label(self.screen, text=name + ':', fg=settings.WHITE, bg=settings.BLACK, font=settings.menu_font) \
                .grid(row=row, column=0, sticky=W)
            self.entries.append(
                Entry(self.screen, width=20, bg=settings.WHITE, font=settings.entry_font))
            self.entries[-1].grid(row=row, column=1, sticky=W)

    def display_radio_buttons(self):
        # Determines whether the yearly contribution is added to start or end
        # of the year
        Label(self.screen, text='Contribution Timing' + ':', fg=settings.WHITE, bg=settings.BLACK, font=settings.menu_font) \
            .grid(row=5, column=0, sticky=W)
        # Add the buttons into the same cell
        framing = Frame(self.screen, bg=settings.BLACK)
        framing.grid(row=5, column=1, sticky=NSEW)
        self.radvar = IntVar()
        radio1 = Radiobutton(framing, text='End of year', width=12,
                             indicatoron=0, variable=self.radvar, value=0)
        radio2 = Radiobutton(framing, text='Start of year',
                             width=12, indicatoron=0, variable=self.radvar, value=1)
        radio1.pack(side='left')
        radio2.pack(side='right')
        print('Radios constructed')

    def output_ending_capital(self):
        #Display the ending capital in textbox
        Label(self.screen, text='\nEnding Capital:', fg=settings.WHITE,
              bg=settings.BLACK, font=settings.menu_font).grid(row=7, column=0, sticky=W)
        self.ending_capital_disp = Text(
            self.screen, width=16, height=2, wrap=WORD, background=settings.WHITE, font=settings.entry_font)
        self.ending_capital_disp.grid(row=7, column=1, sticky=S)

    def calculate_ending_capital(self):
        print('Calculate ending capital called')
        #
        capital = self.entries[0].get()
        rate = self.entries[1].get()
        num_periods = self.entries[2].get()
        contribution = self.entries[3].get()
        capital, rate, num_periods, contribution = list(
            map(int, [capital, rate, num_periods, contribution]))
        #
        try:
            for year in range(num_periods):
                if self.radvar.get():
                    capital = (capital + contribution) * (1 + rate / 100)
                else:
                    capital = capital * (1 + rate / 100) + contribution
                # Record each capital
            capital = '$' + str("{:,}".format(round(capital)))
        except:
            capital = 'Please enter numbers only'
            raise Exception('Non-number entered in entry box')
        self.display_text(capital, self.ending_capital_disp)


if __name__ == '__main__':
    start_calc()

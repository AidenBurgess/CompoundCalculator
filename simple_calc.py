'''
Simple compound interest calculator.

Author: Aiden Burgess
'''
import tkinter as tk
import settings
import calculator


class SimpleCalc:

    def __init__(self):
        # Open new window for
        self.screen = tk.Tk()
        self.screen.title('Simple Compound Interest')
        self.screen.configure(background=settings.BLACK)
        # Build widgets onto window
        self.disp_title()
        self.disp_entry_boxes()
        self.disp_submit_buttons()
        self.out_ending_cap()
        # Back button
        self.disp_back_button()
        print('Simple Calculator')
        self.screen.mainloop()

    def disp_title(self):
        tk.Label(self.screen, text='Simple Calculator', fg=settings.WHITE,
                 bg=settings.BLACK, font=settings.title_font)\
                 .grid(row=0, column=0, sticky=tk.NSEW)

    def display_text(self, text, textbox):
        textbox.delete(0.0, tk.END)
        textbox.insert(tk.END, text)

    def disp_entry_boxes(self):
        # Display all entry boxes and add them to a list, so they are callable
        self.entries = []
        entry_list = [('Starting Capital ($)', 1), ('Interest Rate (%)', 2),
                      ('Number of Years', 3)]
        for name, row in entry_list:
            tk.Label(self.screen, text=name + ':', fg=settings.WHITE, bg=settings.BLACK,
                     font=settings.menu_font).grid(row=row, column=0, sticky=tk.W)
            self.entries.append(tk.Entry(self.screen, width=20, bg=settings.WHITE,
                                         font=settings.entry_font))
            self.entries[-1].grid(row=row, column=1, sticky=tk.W)

    def disp_submit_buttons(self):
        # Calculate the ending capital
        tk.Button(self.screen, text='Submit', width=10,
                  command=self.calc_ending_cap, font=settings.entry_font)\
            .grid(row=4, column=1, sticky=tk.N, pady=10)

    def out_ending_cap(self):
        # Display the ending capital in textbox
        tk.Label(self.screen, text='\nEnding Capital:', fg=settings.WHITE,
                 bg=settings.BLACK, font=settings.menu_font)\
                 .grid(row=5, column=0, sticky=tk.W)
        self.ending_capital_disp = tk.Text(
            self.screen, width=16, height=2, wrap=tk.WORD,
            background=settings.WHITE, font=settings.entry_font)
        self.ending_capital_disp.grid(row=5, column=1, sticky=tk.S)

    def disp_back_button(self):
        tk.Button(self.screen, text='<-- back', width=10,
                  command=self.back_to_main, font=settings.entry_font)\
            .grid(row=6, column=0, sticky=tk.W, pady=10)

    def get_entries(self):
        # Grab all the entries from entry boxes
        self.capital = self.entries[0].get()
        self.rate = self.entries[1].get()
        self.num_periods = self.entries[2].get()
        try:
            self.capital, self.rate, self.num_periods = list(
                map(int, [self.capital, self.rate, self.num_periods]))
        except:
            self.capital = 'Please enter numbers only'

    def calc_ending_cap(self):
        self.get_entries()
        # Display error message
        if isinstance(self.capital, str):
            self.display_text(self.capital, self.ending_capital_disp)
        # Calculate ending capital then display final amount
        else:
            for self.year in range(self.num_periods):
                self.capital = self.capital * (1 + self.rate / 100)
            # Record each capital
            self.capital = '$' + str("{:,}".format(round(self.capital)))
            self.display_text(self.capital, self.ending_capital_disp)

    def back_to_main(self):
        self.screen.destroy()
        calculator.MainScreen()


if __name__ == '__main__':
    SimpleCalc()

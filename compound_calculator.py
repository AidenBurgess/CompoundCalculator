'''
This module is the capital calculator. It calculates ending capital from
interest rate, starting capital, number of years, and yearly contribution.

Author: Aiden Burgess
'''
import tkinter as tk
import multi_line_annot as mla
import settings


def start_calc():
    CompoundCalculator()


class CompoundCalculator:

    def __init__(self):
        # Open new window for
        self.screen = tk.Tk()
        self.screen.title('Compound Interest Calculator')
        self.screen.configure(background=settings.BLACK)
        # Build widgets onto window
        self.disp_title()
        self.disp_entry_boxes()
        self.disp_rad_buttons()
        self.disp_submit_buttons()
        self.out_ending_cap()
        # Back button
        # Quit button
        # Start the window
        print('Initialised Capital Calculator')
        self.screen.mainloop()

    def disp_title(self):
        tk.Label(self.screen, text='Compound Interest', fg=settings.WHITE, bg=settings.BLACK,
              font=settings.title_font).grid(row=0, column=0, sticky=tk.NSEW)

    def display_text(self, text, textbox):
        textbox.delete(0.0, tk.END)
        textbox.insert(tk.END, text)

    def disp_entry_boxes(self):
        # Display all entry boxes and add them to a list, so they are callable
        self.entries = []
        entry_list = [('Starting Capital ($)', 1), ('Interest Rate (%)', 2),
                      ('Number of Years', 3), ('Yearly Contribution', 4)]
        for name, row in entry_list:
            tk.Label(self.screen, text=name + ':', fg=settings.WHITE, bg=settings.BLACK,
                  font=settings.menu_font).grid(row=row, column=0, sticky=tk.W)
            self.entries.append(tk.Entry(self.screen, width=20, bg=settings.WHITE,
                                      font=settings.entry_font))
            self.entries[-1].grid(row=row, column=1, sticky=tk.W)

    def disp_rad_buttons(self):
        # Determines whether the yearly contribution is added to start or end
        # of the year
        tk.Label(self.screen, text='Contribution Timing' + ':', fg=settings.WHITE, bg=settings.BLACK, font=settings.menu_font) \
            .grid(row=5, column=0, sticky=tk.W)
        # Add the buttons into the same cell
        framing = tk.Frame(self.screen, bg=settings.BLACK)
        framing.grid(row=5, column=1, sticky=tk.NSEW)
        self.toggle_contr = tk.IntVar()
        radio1 = tk.Radiobutton(framing, text='End of year', width=12,
                             indicatoron=0, variable=self.toggle_contr, value=0)
        radio2 = tk.Radiobutton(framing, text='Start of year', width=12,
                             indicatoron=0, variable=self.toggle_contr, value=1)
        radio1.pack(side='left')
        radio2.pack(side='right')
        print('Radios constructed')

    def out_ending_cap(self):
        # Display the ending capital in textbox
        tk.Label(self.screen, text='\nEnding Capital:', fg=settings.WHITE,
              bg=settings.BLACK, font=settings.menu_font).grid(row=7, column=0, sticky=tk.W)
        self.ending_capital_disp = tk.Text(
            self.screen, width=16, height=2, wrap=tk.WORD, background=settings.WHITE, font=settings.entry_font)
        self.ending_capital_disp.grid(row=7, column=1, sticky=tk.S)

    def disp_submit_buttons(self):
        # Build the graph button
        tk.Button(self.screen, text='Build Graph', width=10, command=self.build_graph,
               font=settings.entry_font).grid(row=6, column=0, sticky=tk.N, pady=10)
        # Calculate the ending capital
        tk.Button(self.screen, text='Submit', width=10, command=self.calc_ending_cap,
               font=settings.entry_font).grid(row=6, column=1, sticky=tk.N, pady=10)

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

    def calc_ending_cap(self):
        self.get_entries()
        # Display error message
        if isinstance(self.capital, str):
            self.display_text(self.capital, self.ending_capital_disp)
        # Calculate ending capital then display final amount
        else:
            self.cap_list = [self.capital]
            for self.year in range(self.num_periods):
                if self.toggle_contr.get():
                    self.capital = (
                        self.capital + self.contribution) * (1 + self.rate / 100)
                else:
                    self.capital = self.capital * \
                        (1 + self.rate / 100) + self.contribution
                self.cap_list.append(self.capital)
            # Record each capital
            self.capital = '$' + str("{:,}".format(round(self.capital)))
            self.display_text(self.capital, self.ending_capital_disp)

    def build_graph(self):
        self.get_entries()
        # Total contribution line
        total_contributions = range(self.capital, self.capital+self.contribution*self.num_periods + 1, self.contribution)
        time_period = range(self.num_periods+1)
        # Add legends to lines
        new = mla.LineGraph()
        new.plot_line(time_period, total_contributions)
        new.plot_line(time_period, self.cap_list)
        new.show_graph()


if __name__ == '__main__':
    start_calc()

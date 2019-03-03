'''
This module can calculate a sequence of capital values for different values of
interest rate, yearly contribution, num_periods.

Author: Aiden Burgess
'''
from itertools import accumulate
import tkinter as tk
import multi_line_annot as mla
import settings
import calculator


class YearBy:

    def __init__(self):
        # Open new window for
        self.screen = tk.Tk()
        self.screen.title('Compound Sequence Calculator')
        self.screen.configure(background=settings.BLACK)
        # Build widgets onto window
        self.disp_title()
        self.disp_entry_boxes()
        self.disp_rad_buttons()
        self.disp_submit_buttons()
        self.out_ending_cap()
        # Back button
        self.disp_back_button()
        # Quit button
        # Start the window
        print('Initialised YearBy')
        self.screen.mainloop()

    def disp_title(self):
        tk.Label(self.screen, text='Year by Year', fg=settings.WHITE,
                 bg=settings.BLACK, font=settings.title_font)\
            .grid(row=0, column=0, sticky=tk.NSEW)

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
        tk.Label(self.screen, text='Contribution Timing' + ':',
                 fg=settings.WHITE, bg=settings.BLACK, font=settings.menu_font)\
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
                 bg=settings.BLACK, font=settings.menu_font)\
            .grid(row=7, column=0, sticky=tk.W)
        self.ending_capital_disp = tk.Text(
            self.screen, width=16, height=2, wrap=tk.WORD,
            background=settings.WHITE, font=settings.entry_font)
        self.ending_capital_disp.grid(row=7, column=1, sticky=tk.S)

    def disp_submit_buttons(self):
        # Build the graph button
        tk.Button(self.screen, text='Build Graph', width=10,
                  command=self.build_graph, font=settings.entry_font)\
            .grid(row=6, column=0, sticky=tk.N, pady=10)
        # Calculate the ending capital
        framing = tk.Frame(self.screen, bg=settings.BLACK)
        framing.grid(row=6, column=1, sticky=tk.NSEW)
        # Next Year, New Sequence
        new_seq = tk.Button(framing, text='New Sequence', width=12,
                            command=self.calc_ending_cap)
        add_seq = tk.Button(framing, text='Add Sequence', width=12,
                            command=lambda: self.calc_ending_cap(1))
        new_seq.pack(side='left')
        add_seq.pack(side='right')

    def get_entries(self):
        # Grab all the entries from entry boxes
        self.capital = self.entries[0].get()
        self.rate = self.entries[1].get()
        self.num_periods = self.entries[2].get()
        self.contr = self.entries[3].get()
        self.convert_entries_int()

    def convert_entries_int(self):
        # Convert parameters to int
        try:
            self.capital, self.rate, self.num_periods, self.contr = list(
                map(int, [self.capital, self.rate, self.num_periods, self.contr]))
        except:
            self.capital = 'Please enter numbers only'

    def calculation_loop(self):
        # Loop over each year and record capital
        for self.year in range(self.num_periods):
            if self.toggle_contr.get():
                self.capital = (self.cap_list[-1] + self.contr)\
                    * (1 + self.rate / 100)
            else:
                self.capital = self.cap_list[-1] * \
                    (1 + self.rate / 100) + self.contr
            self.cap_list.append(self.capital)

    def calc_ending_cap(self, add=0):
        self.get_entries()
        # Display error message
        if isinstance(self.capital, str):
            self.display_text(self.capital, self.ending_capital_disp)
        else:
            # If not adding a new sequence, reset capital and year vals.
            if not add:
                self.cap_list = [self.capital]
                self.total_num_periods = 0
                self.total_contr = [self.capital]
            # Perform appropriate calculations on capital
            self.calculation_loop()
            self.total_num_periods += self.num_periods
            self.total_contr += [self.contr] * self.num_periods
            # Display ending capital
            self.capital = '$' + str("{:,}".format(round(self.capital)))
            self.display_text(self.capital, self.ending_capital_disp)

    def graph_exception(self):
        return False

    def build_graph(self):
        self.get_entries()
        # Total contribution line
        if self.graph_exception():
            # Output error to textbox
            return
        total_contr = list(accumulate(self.total_contr))
        time_period = range(self.total_num_periods + 1)
        # Create graph and display
        new = mla.LineGraph()
        new.plot_line(time_period, self.cap_list, 'Total Capital')
        new.plot_line(time_period, total_contr, 'Total Contribution')
        new.show_graph()

    def disp_back_button(self):
        tk.Button(self.screen, text='<-- back', width=10,
                  command=self.back_to_main, font=settings.entry_font)\
            .grid(row=8, column=0, sticky=tk.W, pady=10)

    def back_to_main(self):
        self.screen.destroy()
        calculator.MainScreen()


if __name__ == '__main__':
    YearBy()

import tkinter as tk


class ContentView(tk.LabelFrame):
    def __init__(self, parent):
        super().__init__(parent)

        self.config(text="")

        self.sub_label = tk.Label(self, text='Subnests', width="10", )
        name_label = tk.Label(self, text='Name')
        size_label = tk.Label(self, text='Size')

        name_label.grid(column=1, row=0)
        size_label.grid(column=2, row=0)

        self.entries_names = []
        self.input_names = []
        self.entries_size = []
        self.input_size = []
        self.nb_row = 6

    def add_sub_label(self):
        self.sub_label.grid(column=0, row=0, rowspan=self.nb_row)

    def set_nb_row(self, nb):
        self.nb_row = nb

    def create_lines(self, old_input_name=[], old_input_size=[]):
        for i in range(self.nb_row):
            input_text = old_input_name[i] if 0 <= i < len(old_input_name) else tk.StringVar(self)
            my_entry = tk.Entry(self, textvariable=input_text)
            self.entries_names.append(my_entry)
            self.input_names.append(input_text)

        for i in range(self.nb_row):
            input_text = old_input_size[i] if 0 <= i < len(old_input_size) else tk.StringVar(self)
            size_entry = tk.Entry(self, textvariable=input_text)
            self.entries_size.append(size_entry)
            self.input_size.append(input_text)

    def add_name_in_view(self, column, row):
        for i, en_name in enumerate(self.entries_names):
            en_name.grid(column=column, row=row + i)

    def add_size_in_view(self, column, row):
        for i, en_size in enumerate(self.entries_size):
            en_size.grid(column=column, row=row + i)

    def get_sub_division(self):
        size = len(self.input_names) if len(self.input_names) < len(self.input_size) else len(self.input_size)

        names = [n.get() for n in self.input_names if len(n.get()) != 0]
        sizes = [int(n.get()) for n in self.input_size if len(n.get()) != 0]

        return dict(zip(names, sizes))

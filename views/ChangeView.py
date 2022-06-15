import tkinter as tk
from functools import partial


class ChangeView(tk.LabelFrame):
    def __init__(self, parent):
        super().__init__(parent)

        self.label = tk.Label(self, text="        Numbers of subnests:                 ")

        self.entry_text = tk.StringVar(self)
        self.entry = tk.Entry(self, textvariable=self.entry_text, highlightthickness=2, width="15")

        self.button = tk.Button(self, text="   Change    ",
                                       command=partial(self.change_number))

        self.label.grid(column=0, row=0)
        self.entry.grid(column=1, row=0)
        self.button.grid(column=2, row=0)

    def change_number(self):
        return self.entry_text.get()

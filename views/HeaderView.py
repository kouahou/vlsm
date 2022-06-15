import tkinter as tk


class HeaderView(tk.LabelFrame):
    def __init__(self, parent):
        super().__init__(parent)

        self.config(text="", width="10")

        self.label = tk.Label(self, text='   Major Network                                                    ')

        self.major_text = tk.StringVar(self)
        self.ip_entry = tk.Entry(self, textvariable=self.major_text, highlightthickness=2)

        self.label.grid(column=0, row=0)
        self.ip_entry.grid(column=1, row=0, rowspan=3)

    def get_ip(self):
        return self.major_text.get().split("/")

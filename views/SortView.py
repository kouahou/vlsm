import tkinter as tk
from tkinter import ttk


class SortView(tk.LabelFrame):
    def __init__(self, parent):
        super().__init__(parent)

        self.label = tk.Label(self, text="               Sort results by:                      ")
        self.list_tri = ["Name", "Size"]
        self.list_combo = ttk.Combobox(self, values=self.list_tri, width="25")
        self.list_combo.current(0)

        self.label.grid(column=0, row=0)
        self.list_combo.grid(column=1, row=0)

        # print(list_combo.current(), list_combo.get())

    def get_sort(self):
        return self.list_combo.get()

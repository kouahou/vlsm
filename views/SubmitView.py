import tkinter as tk
from functools import partial


class SubmitView(tk.LabelFrame):
    def __init__(self, parent):
        super().__init__(parent)

        self.button = tk.Button(self, text="   Submit   ", command=partial(self.calcul_vlsm))

        self.input1 = tk.StringVar(self)
        self.input1_name = tk.Entry(self, textvariable=self.input1, highlightthickness=2, width="20")

        self.input2 = tk.StringVar(self)
        self.input2_name = tk.Entry(self, textvariable=self.input2, highlightthickness=2, width="20")

        self.button.grid(column=0, row=0)
        self.input1_name.grid(column=1, row=0)
        self.input2_name.grid(column=2, row=0)

        self.controller = None

    def set_controller(self, controller):
        self.controller = controller

    def calcul_vlsm(self):
        return self.controller.get_data()




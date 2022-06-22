import tkinter as tk
import matplotlib
import matplotlib.pyplot as plt

matplotlib.use('TkAgg')

from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg


class GraphView(tk.LabelFrame):
    def __init__(self, parent):
        super().__init__(parent)

        self.controller = None

        self.canvas = None

    def set_controller(self, controller):
        self.controller = controller

    def render_fig(self):
        figure = plt.figure(figsize=(6, 6), dpi=100)
        figure.set_size_inches(6, 4)

        data = self.controller.service.get_data()

        labels = [f'{k} /{v}' for k, v in data.items()]
        sizes = self.controller.service.size

        plt.pie(sizes, labels=labels, shadow=True, startangle=148)

        plt.axis("equal")

        canvasbar = FigureCanvasTkAgg(figure, master=self)

        canvasbar.draw()

        canvasbar.get_tk_widget().grid(column=0, row=0)

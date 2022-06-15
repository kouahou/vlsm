import tkinter as tk
import matplotlib
import pandas as pd

matplotlib.use('TkAgg')

from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk


class GraphView(tk.LabelFrame):
    def __init__(self, parent):
        super().__init__(parent)

        self.controller = None

        self.canvas = None

    def set_controller(self, controller):
        self.controller = controller

    def render_fig(self):
        figure = Figure(figsize=(6, 4), dpi=100)

        data = self.controller.service.get_data()

        sub_name = data.keys()
        masks = data.values()

        df = pd.DataFrame({"Name": sub_name, "Size": masks})

        figure = df.groupby(['Name']).sum().plot(kind='pie', y='Size')

        figure_canvas = FigureCanvasTkAgg(figure, self)

        NavigationToolbar2Tk(figure_canvas, self)

        axes = figure.add_subplot()

        axes.bar(sub_name, masks)

        axes.set_title('Mask')
        axes.set_ylabel('/')

        figure_canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)

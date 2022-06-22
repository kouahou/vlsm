import tkinter as tk
import graphviz


class TreeView(tk.LabelFrame):
    def __init__(self, parent):
        super().__init__(parent)

        self.controller = None

    def set_controller(self, controller):
        self.controller = controller

    def render_fig(self):
        data = self.controller.service.get_data()

        dot = graphviz.Digraph('Subnet', comment='Sub network', format='png')

        for key, val in data.items():
            dot.node(key, label=str(val))

        links = []
        for i, key in enumerate(data.keys()):
            if i + 1 < len(data.keys()):
                links.append(f'{key}{list(data.keys())[i+1]}')

        dot.edges(links)

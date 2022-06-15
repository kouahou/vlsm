import tkinter as tk


class ResultView(tk.LabelFrame):
    def __init__(self, parent):
        super().__init__(parent)

        self.controller = None

        self.config(text="")

        self.list_label = []

        self.columns = [
            "Subnet Name", "Needed Size",
            "Allocated Size", "Address", " Mask",
            "Dec Mask",	"Assignable Range",
            "Broadcast"]

        for i, column in enumerate(self.columns):
            label = tk.Label(self, text=f"{column} ")
            label.grid(column=i, row=0)

    def set_controller(self, controller):
        self.controller = controller

    def update_data(self):
        result = self.controller.service.result()
        if len(self.list_label) != 0:
            for la in self.list_label:
                la.destroy()

        for j, r in enumerate(result):
            for i, column in enumerate(r):
                label = tk.Label(self, text=f"{column} ")
                label.grid(column=i, row=j+1)
                self.list_label.append(label)

    def update_graph_view(self):
        self.controller
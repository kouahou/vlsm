import tkinter as tk
from tkinter import ttk

from controllers.AppController import AppController
from controllers.GraphController import GraphController
from controllers.ResultController import ResultController
from controllers.TreeController import TreeController
from models.AppModel import AppModel
from services.IPService import IPService
from views.AppView import AppView
from views.GraphView import GraphView
from views.ResultView import ResultView
from views.TreeView import TreeView


class App(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("VLSM")

        self.config(background="#4c283c", highlightthickness=6)

        w = self.winfo_reqwidth()
        h = self.winfo_reqheight()
        ws = self.winfo_screenwidth()
        hs = self.winfo_screenheight()
        x = (ws / 2) - (w / 2)
        y = (hs / 2) - (h / 2)

        # create a model
        model = AppModel()

        # create a view and place it on the root window
        view = AppView(self)

        note_book = ttk.Notebook(self)

        result_view = ResultView(note_book)
        graph_view = GraphView(note_book)
        tree_view = TreeView(note_book)

        view.grid(row=0, column=0)
        result_view.grid()
        graph_view.grid()
        tree_view.grid()

        result_controller = ResultController(result_view)
        graph_controller = GraphController(result_view)
        tree_controller = TreeController(result_view)

        # create a controller
        controller = AppController(model, view)

        view.set_controller(controller)
        result_view.set_controller(result_controller)
        graph_view.set_controller(graph_controller)
        tree_view.set_controller(tree_controller)
        view.submit_view.controller.set_result_view(result_view)
        view.submit_view.controller.set_graph_view(graph_view)
        view.submit_view.controller.set_tree_view(tree_view)

        note_book.add(result_view, text="vlsm")
        note_book.add(graph_view, text="Graph")
        note_book.add(tree_view, text="Tree")
        note_book.grid()


if __name__ == "__main__":
    app = App()
    app.mainloop()

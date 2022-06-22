import tkinter as tk

from controllers.SubmitController import SubmitController
from views.ChangeView import ChangeView
from views.ContentView import ContentView
from views.HeaderView import HeaderView
from views.SortView import SortView
from views.SubmitView import SubmitView


class AppView(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)

        self.controller = None

        self.config(background="#4c283c", highlightthickness=4)

        self.header = HeaderView(self)
        self.header.grid(padx=20, ipadx=5, pady=20)

        self.content_view = ContentView(self)
        self.content_view.create_lines()
        self.content_view.add_name_in_view(1, 2)
        self.content_view.add_size_in_view(2, 2)
        self.content_view.add_sub_label()
        self.content_view.grid(padx=10, ipadx=5, ipady=5)

        self.change = ChangeView(self)
        self.change.grid(padx=20, ipadx=5)
        self.change.button.bind('<Button-1>', self.change_nb)

        self.sort = SortView(self)
        self.sort.grid(padx=20, ipadx=5)

        self.submit_view = SubmitView(self)
        self.submit_view.grid(padx=20, ipadx=5, pady=20)
        self.submit_view.button.bind('<Button-1>', self.get_data)
        submit_controller = SubmitController(self.content_view, self.header, self.sort)
        self.submit_view.set_controller(submit_controller)

    def change_number(self, var):
        self.controller.change_number(var)
        self.render_content(int(var.get()))

    def set_controller(self, controller):
        self.controller = controller

    def render_content(self, nb=7):
        list_names = self.content_view.input_names
        list_size = self.content_view.input_size
        self.content_view.destroy()
        self.content_view = ContentView(self)
        self.content_view.set_nb_row(nb)
        self.content_view.create_lines(list_names, list_size)
        self.content_view.add_name_in_view(1, 2)
        self.content_view.add_size_in_view(2, 2)
        self.content_view.add_sub_label()
        self.content_view.grid(padx=10, ipadx=5, ipady=5)
        self.render_change()
        self.render_sort()
        self.render_submit()

    def render_change(self):
        self.change.destroy()
        self.change = ChangeView(self)
        self.change.grid(padx=20, ipadx=5)
        self.change.button.bind('<Button-1>', self.change_nb)

    def render_sort(self):
        self.sort.destroy()
        self.sort = SortView(self)
        self.sort.grid(padx=20, ipadx=5)

    def render_submit(self):
        result_view = self.submit_view.controller.result
        graph_view = self.submit_view.controller.graph
        tree_view = self.submit_view.controller.tree
        self.submit_view.destroy()
        self.submit_view = SubmitView(self)
        self.submit_view.grid(padx=20, ipadx=5, pady=20)
        submit_controller = SubmitController(self.content_view, self.header, self.sort)
        self.submit_view.set_controller(submit_controller)
        self.submit_view.controller.set_result_view(result_view)
        self.submit_view.controller.set_graph_view(graph_view)
        self.submit_view.controller.set_tree_view(tree_view)

    def change_nb(self, event):
        self.render_content(int(self.change.entry_text.get()))

    def get_data(self, event):
        ip = self.header.get_ip()

from services.GraphService import GraphService
from services.IPService import IPService
from services.TreeService import TreeService


class SubmitController:
    def __init__(self, content_view, header_view, sort_view, result_view=None, graph_view=None, tree_view=None):
        self.content = content_view
        self.header = header_view
        self.result = result_view
        self.graph = graph_view
        self.sort = sort_view
        self.tree = tree_view

    def set_result_view(self, result_view):
        self.result = result_view

    def set_graph_view(self, graph_view):
        self.graph = graph_view

    def set_tree_view(self, tree_view):
        self.tree = tree_view

    def get_data(self):
        content_data = self.content.get_sub_division()
        header_data = self.header.get_ip()
        sort_data = self.sort.get_sort()

        service = IPService(*header_data)
        service.set_sub_network(content_data)

        self.result.controller.set_service(service)

        graph_service = GraphService(service.sub_networks.values(), service.sub_networks.keys(), sort_data)
        self.graph.controller.set_service(graph_service)

        tree_service = TreeService(service.sub_networks)
        self.tree.controller.set_service(tree_service)

        self.result.update_data()
        self.graph.render_fig()
        self.tree.render_fig()


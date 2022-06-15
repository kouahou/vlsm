from services.GraphService import GraphService
from services.IPService import IPService


class SubmitController:
    def __init__(self, content_view, header_view, sort_view, result_view=None, graph_view=None):
        self.content = content_view
        self.header = header_view
        self.result = result_view
        self.graph = graph_view
        self.sort = sort_view

    def set_result_view(self, result_view):
        self.result = result_view

    def set_graph_view(self, graph_view):
        self.graph = graph_view

    def get_data(self):
        content_data = self.content.get_sub_division()
        header_data = self.header.get_ip()
        sort_data = self.sort.get_sort()

        service = IPService(*header_data)
        service.set_sub_network(content_data)

        self.result.controller.set_service(service)

        graph_service = GraphService(content_data.values(), content_data.keys(), sort_data)
        self.graph.controller.set_service(graph_service)

        self.result.update_data()
        self.graph.render_fig()


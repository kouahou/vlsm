class ResultController:
    def __init__(self, view):
        self.view = view

        self.service = None

    def set_service(self, service):
        self.service = service

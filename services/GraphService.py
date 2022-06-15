import math


class GraphService:
    def __init__(self, sizes, names, group):
        self.group = group
        self.size = sizes
        self.names = names

    def set_size(self, sizes):
        self.size = sizes

    def set_names(self, names):
        self.names = names

    def set_group(self, group):
        self.group = group

    def get_data(self):
        return dict(zip(self.names,
                        list(map(lambda x: 32 - math.ceil(math.log2(int(x))), self.size))))

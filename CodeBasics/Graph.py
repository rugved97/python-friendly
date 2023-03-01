class Graph:
    def __init__(self, paths):
        self.graph = paths
        self.graph_dict = {}
        for start, end in paths:
            if start in self.graph_dict:
                self.graph_dict[start].append(end)
            else:
                self.graph_dict[start] = [end]

        print('Graph', self.graph_dict)

    def find_all_paths(self, start, end, path=[]):
        path = path + [start]
        if start == end:
            return [path]

        if start not in self.graph_dict:
            return []

        complete_path = []
        for node in self.graph_dict[start]:
            new_paths = self.find_all_paths(node, end, path)
            for element in new_paths:
                complete_path.append(element)
        return complete_path

    def find_shortest_path(self, start, end, path=[]):
        path = path + [start]

        if start == end:
            return [path]

        if start not in self.graph_dict:
            return None

        shortest_path = None

        for node in self.graph_dict[start]:
            new_paths = self.find_shortest_path(node, end, path)
            for element in new_paths:
                if shortest_path:
                    if len(element) < len(shortest_path):
                        shortest_path = element
                else:
                    shortest_path = [element]
        return shortest_path

    # def get_shortest_path(self, start, end, path=[]):
    #     path = path + [start]
    #
    #     if start == end:
    #         return path
    #
    #     if start not in self.graph_dict:
    #         return None
    #
    #     shortest_path = None
    #     for node in self.graph_dict[start]:
    #         if node not in path:
    #             sp = self.get_shortest_path(node, end, path)
    #             if sp:
    #                 if shortest_path is None or len(sp) < len(shortest_path):
    #                     shortest_path = sp
    #
    #     return shortest_path


if __name__ == '__main__':
    routes = (
        ('Mumbai', 'Paris'),
        ('Mumbai', 'Dubai'),
        ('Paris', 'New York'),
        ('Paris', 'Dubai'),
        ('Dubai', 'New York'),
        ('New York', 'Toronto'),

    )
    flight_graph = Graph(routes)
    start_loc = 'Paris'
    end_loc = 'New York'
    paths = flight_graph.find_all_paths(start_loc, end_loc)
    sp = flight_graph.find_shortest_path(start_loc, end_loc)

    print(f'All paths between {start_loc} and {end_loc} ', paths)
    print(f'Shortest path between {start_loc} and {end_loc} ', sp)

    # test = ['a']
    # test = test + ['b']
    # print([test] + ['c'])

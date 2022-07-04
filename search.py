import collections
import math


class BinarySearch:
    @staticmethod
    def search(list_for_sort, item_for_search):
        _index_low_element = 0
        _index_high_element = len(list_for_sort) - 1

        while _index_low_element <= _index_high_element:
            _index_middle_element = int((_index_low_element + _index_high_element) / 2)
            _found_element = list_for_sort[_index_middle_element]
            if _found_element == item_for_search:
                return _index_middle_element
            if _found_element > item_for_search:
                _index_high_element = _index_middle_element - 1
            else:
                _index_low_element = _index_middle_element + 1

        return None


class BFS:
    @staticmethod
    def search(start_item_name, graph):
        _search_queue = collections.deque()
        _search_queue += graph[start_item_name]
        _searched_list = []
        while _search_queue:
            _person = _search_queue.popleft()
            if BFS.__person_is_seller(_person):
                print(_person + " is a mango seller!")
                break
            else:
                _search_queue += graph[_person]
                _searched_list.append(_person)

    @staticmethod
    def __person_is_seller(name):
        return len(name) == 6


class Dijkstra:
    @staticmethod
    def search(graph, costs, parent):
        _processed = []
        _lowest_cost_node = Dijkstra.__find_lowest_cost_node(costs, _processed)
        while _lowest_cost_node is not None:
            _cost_node = costs[_lowest_cost_node]
            _neighbors_node = graph[_lowest_cost_node]
            for node in _neighbors_node.keys():
                _new_cost_node = _cost_node + _neighbors_node[node]
                if costs[node] > _new_cost_node:
                    costs[node] = _new_cost_node
                    parent[node] = _lowest_cost_node
            _processed.append(_lowest_cost_node)
            _lowest_cost_node = Dijkstra.__find_lowest_cost_node(costs, _processed)

    @staticmethod
    def __find_lowest_cost_node(costs, processed):
        _lowest_cost = math.inf
        _lowest_cost_node = None
        for node in costs:
            _cost_node = costs[node]
            if _cost_node < _lowest_cost and node not in processed:
                _lowest_cost = _cost_node
                _lowest_cost_node = node
        return _lowest_cost_node
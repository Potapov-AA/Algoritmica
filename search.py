class BinarySearch:
    def __init__(self, list_for_sort):
        self.list_for_sort = list_for_sort

    def binary_search(self, item_for_search):
        _index_low_element = 0
        _index_high_element = len(self.list_for_sort) - 1

        while _index_low_element <= _index_high_element:
            _index_middle_element = int((_index_low_element + _index_high_element) / 2)
            _found_element = self.list_for_sort[_index_middle_element]
            if _found_element == item_for_search:
                return _index_middle_element
            if _found_element > item_for_search:
                _index_high_element = _index_middle_element - 1
            else:
                _index_low_element = _index_middle_element + 1

        return None
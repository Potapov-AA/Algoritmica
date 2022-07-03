class SelectionSort:
    def __init__(self, array_for_sort: list):
        self.array_for_sort = array_for_sort

    def __findSmallestElementIndex(self):
        _smallest_element = self.array_for_sort[0]
        _smallest_element_index = 0
        for i in range(1, len(self.array_for_sort)):
            if self.array_for_sort[i] < _smallest_element:
                _smallest_element = self.array_for_sort[i]
                _smallest_element_index = i
        return _smallest_element_index

    def selectionSort(self):
        _sorted_array = []
        for i in range(len(self.array_for_sort)):
            _smallest_element_index = SelectionSort.__findSmallestElementIndex(self)
            _sorted_array.append(self.array_for_sort.pop(_smallest_element_index))
        return _sorted_array

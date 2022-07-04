import random


class SelectionSort:
    @staticmethod
    def __findSmallestElementIndex(array_for_sort: list):
        _smallest_element = array_for_sort[0]
        _smallest_element_index = 0
        for i in range(1, len(array_for_sort)):
            if array_for_sort[i] < _smallest_element:
                _smallest_element = array_for_sort[i]
                _smallest_element_index = i
        return _smallest_element_index

    @staticmethod
    def sort(array_for_sort: list):
        _sorted_array = []
        for i in range(len(array_for_sort)):
            _smallest_element_index = SelectionSort.__findSmallestElementIndex(array_for_sort)
            _sorted_array.append(array_for_sort.pop(_smallest_element_index))
        return _sorted_array


class QuickSort:
    @staticmethod
    def sort(array_for_sort: list):
        if len(array_for_sort) < 2:
            return array_for_sort
        else:
            _support_element = array_for_sort[0]
            _less_support_array = [i for i in array_for_sort[1:] if i <= _support_element]
            _more_support_array = [i for i in array_for_sort[1:] if i > _support_element]
            return QuickSort.sort(_less_support_array) + [_support_element] + QuickSort.sort(_more_support_array)

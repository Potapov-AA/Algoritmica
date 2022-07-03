from search import BinarySearch
from sort import SelectionSort
from factorial import Factorial


if __name__ == '__main__':
    _list_for_sort = [2, 5, 7, 1, 3, 4, 6, 11]
    _list_for_find = SelectionSort(_list_for_sort).selectionSort()
    print(_list_for_find)
    print(BinarySearch(_list_for_find).binary_search(5))
    print(Factorial().factorial(5))


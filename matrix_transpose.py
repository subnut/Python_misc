from typing import List


def transpose(matrix: List[List]) -> List[List]:
    _len_array: List[int] = []
    for row in matrix:
        _len_array.append(len(row))
    if _len_array.count(_len_array[0]) != len(_len_array):
        raise RuntimeError("Invalid Matrix")
    matrix_new: List[List] = []
    for column in range(len(matrix[0])):
        _new_row: List = []
        for row in matrix:
            _new_row.append(row[column])
        matrix_new.append(_new_row)
    return matrix_new

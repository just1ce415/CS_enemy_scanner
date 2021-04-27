"""
Data structures for CS Rival Scanner:
Array and Array2D
Provided by anrom7.
"""

import ctypes


# Implements the Array ADT using array capabilities of the ctypes module.


class Array:
    """
    Creates an array with size elements.
    """

    def __init__(self, size):
        assert size > 0, "Array size must be > 0"
        self._size = size
        # Create the array structure using the ctypes module.
        PyArrayType = ctypes.py_object * size
        self._elements = PyArrayType()
        # Initialize each element.
        self.clear(None)

    def __len__(self):
        """
        Returns the size of the array.
        """
        return self._size

    def __getitem__(self, index):
        """
        Gets the contents of the index element.
        """
        assert 0 <= index < len(self), "Array subscript out of range"
        return self._elements[index]

    def __setitem__(self, index, value):
        """
        Puts the value in the array element at index position.
        """
        assert 0 <= index < len(self), "Array subscript out of range"
        self._elements[index] = value

    def clear(self, value):
        """
        Clears the array by setting each element to the given value.
        """
        for i in range(len(self)):
            self._elements[i] = value

    def __iter__(self):
        """
        Returns the array's iterator for traversing the elements.
        """
        return _ArrayIterator(self._elements)


class _ArrayIterator:
    """
    An iterator for the Array ADT.
    """

    def __init__(self, the_array):
        self._array_ref = the_array
        self._cur_index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self._cur_index < len(self._array_ref):
            entry = self._array_ref[self._cur_index]
            self._cur_index += 1
            return entry
        raise StopIteration


# Implementation of the Array2D ADT using an array of arrays.


class Array2D:
    """
    Creates a 2 -D array of size numRows x numCols.
    """

    def __init__(self, num_rows, num_cols):
        # Create a 1 -D array to store an array reference for each row.
        self.rows = Array(num_rows)

        # Create the 1 -D arrays for each row of the 2 -D array.
        for i in range(num_rows):
            self.rows[i] = Array(num_cols)

    def num_rows(self):
        """
        Returns the number of rows in the 2 -D array.
        """
        return len(self.rows)

    def num_cols(self):
        """
        Returns the number of columns in the 2 -D array.
        """
        return len(self.rows[0])

    def clear(self, value):
        """
        Clears the array by setting every element to the given value.
        """
        for row in self.rows:
            row.clear(value)

    def __getitem__(self, index_tuple):
        """
        Gets the contents of the element at position [i, j]
        """
        assert len(index_tuple) == 2, "Invalid number of array subscripts."
        row = index_tuple[0]
        col = index_tuple[1]
        assert (
            0 <= row < self.num_rows() and 0 <= col < self.num_cols()
        ), "Array subscript out of range."
        array_1d = self.rows[row]
        return array_1d[col]

    def __setitem__(self, index_tuple, value):
        """
        Sets the contents of the element at position [i,j] to value.
        """
        assert len(index_tuple) == 2, "Invalid number of array subscripts."
        row = index_tuple[0]
        col = index_tuple[1]
        assert (
            0 <= row < self.num_rows() and 0 <= col < self.num_cols()
        ), "Array subscript out of range."
        array_1d = self.rows[row]
        array_1d[col] = value

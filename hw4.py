'''
Created on 10/21/2024
@author:   Yahia Abdelsalam
Pledge:    "I pledge my honor that I have abided by the Stevens Honor System"
CS115 - Hw 4
'''

# Task 1
def pascal_row(n):
    """Computes the nth row of Pascal's Triangle using recursion."""
    if n == 0:
        return [1]
    def add_pairs(lst):
        """Helper function to add adjacent elements in a list."""
        if len(lst) < 2:
            return []
        return [lst[0] + lst[1]] + add_pairs(lst[1:])
    previous_row = pascal_row(n - 1)
    return [1] + add_pairs(previous_row) + [1]

# Task 2
def pascal_triangle(n):
    """Computes Pascal's Triangle up to the nth row using recursion."""
    if n < 0:
        return []
    if n == 0:
        return [[1]]
    triangle = pascal_triangle(n - 1)
    return triangle + [pascal_row(n)]

# Task 3
def test_pascal_row():
    """
    Tests the pascal_row function.
    """
    assert pascal_row(0) == [1], "Test case 1 failed"
    assert pascal_row(1) == [1, 1], "Test case 2 failed"
    assert pascal_row(5) == [1, 5, 10, 10, 5, 1], "Test case 3 failed"
    assert pascal_row(2) == [1, 2, 1], "Test case 4 failed"
    print("All tests for pascal_row passed!")

def test_pascal_triangle():
    """
    Tests the pascal_triangle function.
    """
    assert pascal_triangle(0) == [[1]], "Test case 1 failed"
    assert pascal_triangle(1) == [[1], [1, 1]], "Test case 2 failed"
    assert pascal_triangle(5) == [
        [1], [1, 1], [1, 2, 1], [1, 3, 3, 1], 
        [1, 4, 6, 4, 1], [1, 5, 10, 10, 5, 1]
    ], "Test case 3 failed"
    assert pascal_triangle(2) == [[1], [1, 1], [1, 2, 1]], "Test case 4 failed"
    print("All tests for pascal_triangle passed!")

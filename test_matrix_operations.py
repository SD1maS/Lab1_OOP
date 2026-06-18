import unittest
from lab1 import MatrixOperations

class TestMatrixOperations(unittest.TestCase):

    def test_multiply_matrices_valid(self):
        matrix_a = [[1, 2],
                    [3, 4]]
        
        matrix_b = [[2, 0],
                    [1, 2]]
        expected_result = [[4, 4],
                           [10, 8]]
        self.assertEqual(MatrixOperations.multiply_matrices(matrix_a, matrix_b), expected_result)

    def test_multiply_matrices_invalid_dimensions(self):
        matrix_a = [[1, 2]]
        matrix_b = [[1, 2, 3]]
        with self.assertRaises(ValueError):
            MatrixOperations.multiply_matrices(matrix_a, matrix_b)

    def test_calculate_minmax_sum(self):
        matrix = [
            [1, 5, 10],
            [4, 5, 6],
            [7, 8, 9]]
        self.assertEqual(MatrixOperations.calculate_minmax_sum(matrix), 14)

if __name__ == '__main__':
    unittest.main()
#Ragib Ahsan ragib@bu.edu and Aanya Kutty akutty@bu.edu
import unittest

class TestMatrixInput(unittest.TestCase):
    def test_matrix_input(self):
        # Test case 1: Test matrix1 input with 2x3 dimensions
        input_values = ["2", "3", "1", "2", "3", "4", "5", "6"]
        expected_output = [[1, 2, 3], [4, 5, 6]]
        with unittest.mock.patch('builtins.input', side_effect=input_values):
            matrix1 = []
            R = int(input("Enter the number of rows:"))
            C = int(input("Enter the number of columns:"))
            for i in range(R):
                a = []
                for j in range(C):
                    a.append(int(input()))
                matrix1.append(a)
            self.assertEqual(matrix1, expected_output)

        # Test case 2: Test matrix2 input with 3x2 dimensions
        input_values = ["3", "2", "1", "2", "3", "4", "5", "6"]
        expected_output = [[1, 2], [3, 4], [5, 6]]
        with unittest.mock.patch('builtins.input', side_effect=input_values):
            matrix2 = []
            R1 = int(input("Enter the number of rows:"))
            C1 = int(input("Enter the number of columns:"))
            for i in range(R1):
                a = []
                for j in range(C1):
                    a.append(int(input()))
                matrix2.append(a)
            self.assertEqual(matrix2, expected_output)

if __name__ == '__main__':
    unittest.main()

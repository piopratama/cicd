# test_triangle_area.py
import unittest
from unittest.mock import patch
from main import calculate_triangle_area

class TestCalculateTriangleArea(unittest.TestCase):
    @patch('os.getenv')
    def test_calculate_triangle_area(self, mock_getenv):
        # Set up the mock environment variables
        mock_getenv.side_effect = lambda var_name: {
            "ENV_WIDTH": "10",
            "ENV_HEIGHT": "20"
        }.get(var_name)
        
        # Get the values from the mocked environment variables
        width = float(mock_getenv("ENV_WIDTH"))
        height = float(mock_getenv("ENV_HEIGHT"))
        
        # Call the function to test
        result = calculate_triangle_area(width, height)
        
        # Verify the expected result
        expected_result = 0.5 * 10 * 20
        self.assertEqual(result, expected_result)
    
    def test_calculate_triangle_area_invalid(self):
        # Test with invalid values that should return -1
        self.assertEqual(calculate_triangle_area(None, 20), -1)
        self.assertEqual(calculate_triangle_area(10, None), -1)
        self.assertEqual(calculate_triangle_area("invalid", 20), -1)

if __name__ == '__main__':
    unittest.main()

import unittest
from themes import List_of_Duty

class TestThemes(unittest.TestCase):
    def test_duties_count(self):
        self.assertEqual(len(List_of_Duty), 13)
    




if __name__ == "__main__":
    unittest.main()
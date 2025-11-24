import unittest
from themes import List_of_Duty

class TestThemes(unittest.TestCase):

    
    def test_duties_count(self):
        self.assertEqual(len(List_of_Duty), 13)

    def test_duty_contents(self):
        for i, duty in enumerate(List_of_Duty, start=1):
            self.assertTrue(duty.startswith(f"Duty {i}"))
    

if __name__ == "__main__":
    unittest.main()
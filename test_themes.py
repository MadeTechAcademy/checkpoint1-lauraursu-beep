import unittest
from themes import List_of_Duty

class TestThemes(unittest.TestCase):
    
    def test_duty_has_no_dublicates(self):
        self.assertEqual(len(List_of_Duty), len(set(List_of_Duty)))
    #Checking if there are no duplicates in the list

    def test_duties_count(self):
        self.assertEqual(len(List_of_Duty), 13)
    #Checking if there are 13 duties in the list

    def test_duty_contents(self):
        for i, duty in enumerate(List_of_Duty, start=1):
            self.assertTrue(duty.startswith(f"Duty {i}"))
    #Checking if each duty starts with the correct "Duty X" prefix

if __name__ == "__main__":
    unittest.main()
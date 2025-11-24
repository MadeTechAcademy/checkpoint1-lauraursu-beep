import unittest
from themes import List_of_Duty

class TestThemes(unittest.TestCase):
    def test_duties_count(self):
        self.assertEqual(len(List_of_Duty), 13)

    def test_duty_1(self):
        Duty_1 = "Duty 1 Script and code in at least one general purpose language and at least one domain-specific language to orchestrate infrastructure, follow test driven development and ensure appropriate test coverage."
        self.assertEqual(List_of_Duty[0], Duty_1)
    
    def test_duty_2(self):
        Duty_2 = "Duty 2 Initiate and facilitate knowledge sharing and technical collaboration with teams and individuals, with a focus on supporting development of team members."
        self.assertEqual(List_of_Duty[1], Duty_2)
    
    
    




if __name__ == "__main__":
    unittest.main()
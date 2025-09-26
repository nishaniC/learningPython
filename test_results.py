import unittest
from results_module import Results, Result, Exam  # assuming you save the above code in results_module.py

class TestResults(unittest.TestCase):
    def setUp(self):
        self.r = Results()
        self.r.results = [
            Result("Maths", "C1", 85, "Pass"),
            Result("Maths", "C1", 70, "Fail"),
            Result("Physics", "C2", 90, "Pass"),
            Result("Biology", "C3", 60, "Fail"),
            Result("Biology", "C3", 65, "Pass"),
        ]
        self.r.candidates = {"C1", "C2", "C3"}

    def test_count_results(self):
        self.r.count_results()
        self.assertEqual(self.r.exams["Maths"].number_of_candidates, 1)
        self.assertEqual(self.r.exams["Maths"].number_of_passed_exams, 1)
        self.assertEqual(self.r.exams["Maths"].number_of_failed_exams, 1)
        self.assertEqual(self.r.exams["Maths"].best_score, 85)
        self.assertEqual(self.r.exams["Maths"].worst_score, 70)

    def test_export_to_csv(self):
        self.r.count_results()
        self.r.export_to_csv("test_output.csv")
        with open("test_output.csv", newline='') as f:
            lines = f.readlines()
        self.assertTrue("Maths" in lines[1])

if __name__ == '__main__':
    unittest.main()
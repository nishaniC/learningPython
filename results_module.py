import csv

class Result:
    def __init__(self, exam_name, candidate_id, score, grade):
        self.exam_name = exam_name
        self.candidate_id = candidate_id
        self.score = int(score)
        self.grade = grade

class Exam:
    def __init__(self, name):
        self.exam_name = name
        self.number_of_candidates = 0
        self.number_of_passed_exams = 0
        self.number_of_failed_exams = 0
        self.best_score = 0
        self.worst_score = 1000

class Results:
    def __init__(self):
        self.results = []
        self.candidates = set()
        self.exams = {
            "Maths": Exam("Maths"),
            "Physics": Exam("Physics"),
            "Biology": Exam("Biology")
        }

    def read_results(self, filename):
        with open(filename, newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                self.candidates.add(row['Candidate ID'])
                self.results.append(Result(row['Exam Name'], row['Candidate ID'], row['Score'], row['Grade']))

    def count_results(self):
        duplicate_tracker = {exam: {} for exam in self.exams}

        for result in self.results:
            exam = self.exams[result.exam_name]
            if result.grade == "Pass":
                exam.number_of_passed_exams += 1
            elif result.grade == "Fail":
                exam.number_of_failed_exams += 1

            exam.best_score = max(exam.best_score, result.score)
            exam.worst_score = min(exam.worst_score, result.score)

            # Track duplicates
            if result.candidate_id in duplicate_tracker[result.exam_name]:
                duplicate_tracker[result.exam_name][result.candidate_id] += 1
            else:
                duplicate_tracker[result.exam_name][result.candidate_id] = 1

        for exam_name, exam in self.exams.items():
            duplicates = sum(count - 1 for count in duplicate_tracker[exam_name].values() if count > 1)
            exam.number_of_candidates = exam.number_of_passed_exams + exam.number_of_failed_exams - duplicates

    def print_results(self):
        print("Results:")
        print("Exam Name,Number of Candidates,Number of Passed Exams,Number of Failed Exams,Best Score,Worst Score")
        for exam in self.exams.values():
            print(f"{exam.exam_name},{exam.number_of_candidates},{exam.number_of_passed_exams},{exam.number_of_failed_exams},{exam.best_score},{exam.worst_score}")

    def export_to_csv(self, output_filename):
        with open(output_filename, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(["Exam Name", "Number of Candidates", "Number of Passed Exams", "Number of Failed Exams", "Best Score", "Worst Score"])
            for exam in self.exams.values():
                writer.writerow([
                    exam.exam_name,
                    exam.number_of_candidates,
                    exam.number_of_passed_exams,
                    exam.number_of_failed_exams,
                    exam.best_score,
                    exam.worst_score
                ])
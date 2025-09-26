import csv

class Result:
    def __init__(self, name, candidate_id,score, grade):
        # Exam Name,Number of Candidates,Number of Passed Exams,Number of Failed Exams,Best Score,Worst Score
        self.exam_name = name
        self.candidate_id = candidate_id
        self.score = score
        self.grade = grade

class Exam:

    def __init__(self,name,number_of_candidates,number_of_passed_exams,number_of_failed_exams,best_score,worst_score):
        self.exam_name = name
        self.number_of_candidates = number_of_candidates
        self.number_of_passed_exams = number_of_passed_exams
        self.number_of_failed_exams = number_of_failed_exams
        self.best_score = best_score
        self.worst_score = worst_score



class Results:
    results=[]
    candidates=[]
    math_exam=Exam("Maths",0,0,0,0,1000)
    physics_exam=Exam("Physics",0,0,0,0,1000)
    biology_exam=Exam("Biology",0,0,0,0,1000)

    def readresults(self,filename):
        with (open(filename, newline='') as csvfile):
            reader = csv.DictReader(csvfile)
            for row in reader:
                if row['Candidate ID'] not in Results.candidates:
                    Results.candidates.append(row['Candidate ID'])
                Results.results.append(Result(row['Exam Name'], row['Candidate ID'],row["Score"], row["Grade"]))

    def countresults(self):
        for result in Results.results:
            if result.exam_name == "Maths":
                if result.grade == "Fail":
                    Results.math_exam.number_of_failed_exams +=1
                if result.grade == "Pass":
                    Results.math_exam.number_of_passed_exams +=1
                if int(result.score) > Results.math_exam.best_score:
                    Results.math_exam.best_score = int(result.score)
                if int(result.score) < Results.math_exam.worst_score:
                    Results.math_exam.worst_score = int(result.score)
            elif result.exam_name == "Physics":
                if result.grade == "Fail":
                    Results.physics_exam.number_of_failed_exams +=1
                if result.grade == "Pass":
                    Results.physics_exam.number_of_passed_exams +=1
                if int(result.score) > Results.physics_exam.best_score:
                    Results.physics_exam.best_score = int(result.score)
                if int(result.score) < Results.physics_exam.worst_score:
                    Results.physics_exam.worst_score = int(result.score)
            elif result.exam_name == "Biology":
                if result.grade == "Fail":
                    Results.biology_exam.number_of_failed_exams +=1
                if result.grade == "Pass":
                    Results.biology_exam.number_of_passed_exams +=1
                if int(result.score) > Results.biology_exam.best_score:
                    Results.biology_exam.best_score = int(result.score)
                if int(result.score) < Results.biology_exam.worst_score:
                    Results.biology_exam.worst_score = int(result.score)

        math_duplicate_IDs =0
        physics_duplicate_IDs = 0
        biology_duplicate_IDs = 0
        for cid in Results.candidates:
            math_duplicate_IDs = self.countofduplicate(cid,"Maths")

        Results.math_exam.number_of_candidates = Results.math_exam.number_of_passed_exams + Results.math_exam.number_of_failed_exams-math_duplicate_IDs
        Results.physics_exam.number_of_candidates = Results.physics_exam.number_of_passed_exams + Results.physics_exam.number_of_failed_exams - physics_duplicate_IDs
        Results.biology_exam.number_of_candidates = Results.biology_exam.number_of_passed_exams + Results.biology_exam.number_of_failed_exams-biology_duplicate_IDs

    def countofduplicate(self,candidate_id,exam_name):
        countduplicate=0
        for result in Results.results:
            if result.candidate_id == candidate_id and result.exam_name == exam_name:
                countduplicate+=1
        return countduplicate


    def printresults(self):
        print("Results:")
        print("Exam Name,Number of Candidates,Number of Passed Exams,Number of Failed Exams,Best Score,Worst Score")
        print(Results.math_exam.exam_name,",",Results.math_exam.number_of_candidates,",",Results.math_exam.number_of_passed_exams,",",Results.math_exam.number_of_failed_exams,",",Results.math_exam.best_score,",",Results.math_exam.worst_score)
        print(Results.physics_exam.exam_name, ",", Results.physics_exam.number_of_candidates, ",",
              Results.physics_exam.number_of_passed_exams, ",", Results.physics_exam.number_of_failed_exams, ",",
              Results.physics_exam.best_score, ",", Results.physics_exam.worst_score)
        print(Results.biology_exam.exam_name, ",", Results.biology_exam.number_of_candidates, ",",
              Results.biology_exam.number_of_passed_exams, ",", Results.biology_exam.number_of_failed_exams, ",",
              Results.biology_exam.best_score, ",", Results.biology_exam.worst_score)


myresults=Results()
myresults.readresults("exam_results.csv")
myresults.countresults()
myresults.printresults()



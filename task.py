student_scores = {
    'Harry': 88,
    'Ron': 78,
    'Hermione': 95,
    'Draco': 75,
    'Neville': 60
}
student_grades={}

def score_to_grade(score):
   if(score>90 and score<=100):
      grade='Outstanding'
   elif(score>80 and score<=90):
      grade='Exceeds Expectations'
   elif(score>70 and score<=80):
      grade='Acceptable'
   else:
      grade='Fail'
   return grade
      

for name in student_scores:
   score=student_scores[name]
   student_grades[name]=score_to_grade(score)

print(student_grades)

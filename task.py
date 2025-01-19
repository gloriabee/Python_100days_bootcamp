student_scores=[10,30,22,34,300,210,33]
print(max(student_scores))

max=student_scores[0]
for score in student_scores:
   if score>max:
        max=score
print(max)
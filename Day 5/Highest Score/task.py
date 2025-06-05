student_scores = [150, 142, 185, 120, 171, 184, 149, 24, 59, 68, 199, 78, 65, 89, 86, 55, 91, 64, 89]
# print(range(1, 10))
max1 = student_scores[0]
for i in student_scores:
    if i > max1:
        max1 = i
print(max1)

sum1 = 0
for i in range(1,101):
    sum1 += i
print(sum1)
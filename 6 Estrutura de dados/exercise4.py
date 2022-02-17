# Alunos e suas respectivas notas
students = [
    ("Alice", 8),
    ("Bob", 7),
    ("Carlos", 9),
]

sum = 0

for student in students:
    name, grade = student
    sum += grade

average = sum / len(students)

print('A média dos alunos é:', average)

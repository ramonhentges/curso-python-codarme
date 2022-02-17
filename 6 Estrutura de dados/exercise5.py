# Alunos e suas respectivas notas através de dicionários
students = [
    {
        "name": "Alice",
        "grade": 8,
    },
    {
        "name": "Bob",
        "grade": 7,
    },
    {
        "name": "Carlos",
        "grade": 9,
    }
]

sum = 0

for student in students:
    sum += student['grade']

average = sum / len(students)

print('A média dos alunos é:', average)

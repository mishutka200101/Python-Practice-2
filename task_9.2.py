lessons = int(input())
students = []
now_students = []
for i in range(0, lessons):
    students_count = int(input())
    for f in range(0, students_count):
        now_students.append(input())
    if len(students) != 0:
        for c in range(0, len(students)):
            if students[c] not in now_students:
                students.pop(c)
    else:
        students.append(now_students)
    now_students = []
print(students)

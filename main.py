A_plus: tuple[int, ...] = tuple(range(91, 100))
A_minus: tuple[int, ...] = tuple(range(81, 90))
A: tuple[int, ...] = tuple(range(71, 80))
B: tuple[int, ...] = tuple(range(61, 70))
C: tuple[int, ...] = tuple(range(51, 60))
D: tuple[int, ...] = tuple(range(41, 50))
F: tuple[int, ...] = tuple(range(40))
marks: tuple[int, ...] = (100, 90, 80, 70, 60, 50, 40, 0)
grades: list[str] = []

for mark in marks:
    if mark in A_plus:
        grades.append("A+")
    elif mark in A_minus:
        grades.append("A-")
    elif mark in A:
        grades.append("A")
    elif mark in B:
        grades.append("B")
    elif mark in C:
        grades.append("C")
    elif mark in D:
        grades.append("D")
    else:
        grades.append("F")

zipped = zip(marks, grades)
print(zipped)

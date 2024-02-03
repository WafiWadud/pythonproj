A_plus = tuple(range(91, 100))
A_minus = tuple(range(81, 90))
A = tuple(range(71, 80))
B = tuple(range(61, 70))
C = tuple(range(51, 60))
D = tuple(range(41, 50))
F = tuple(range(40))
marks = (100, 90, 80, 70, 60, 50, 40, 0)

grades = [
    "A+"
    if mark in A_plus
    else "A-"
    if mark in A_minus
    else "A"
    if mark in A
    else "B"
    if mark in B
    else "C"
    if mark in C
    else "D"
    if mark in D
    else "F"
    for mark in marks
]

zipped = zip(marks, grades)
print(list(zipped))

def average(grades):
    return sum(grades.values()) / len(grades)
class_B ={
    "g": 1,
    "e": 5,
    "n": 8,
    "o": 9,
}
class_C ={
    "p": 20,
    "u": 15,
    "m": 10,
    "x": 12
}
print(f"Average for class B: {average(class_B)}.")
print(f"Average for class c: {average(class_C)}.")
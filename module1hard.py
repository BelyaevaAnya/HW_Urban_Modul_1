grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
def find_average_grade(lst):
    return sum(lst)/len(lst)

def get_dict_average_grade(students: set, grades: list)->dict:
    avr_grade_dict = {}
    students = sorted(students)
    for index in range(len(students)):
        avr_grade_dict[students[index]] = find_average_grade(grades[index])
    return avr_grade_dict

avr_grade_dict = get_dict_average_grade(students, grades)
print(avr_grade_dict, type(avr_grade_dict))
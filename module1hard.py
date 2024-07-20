grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}


def find_average_grade(lst):
    return sum(lst) / len(lst)


average_lst = []
for grades_one_st in grades:
    average_lst.append(find_average_grade(grades_one_st))

avr_grade_dict = dict(zip(students, average_lst))
print(avr_grade_dict, type(avr_grade_dict))
# => {'Johnny': 4.0, 'Steve': 2.25, 'Khendrik': 4.0, 'Bilbo': 3.6666666666666665, 'Aaron': 4.8} <class 'dict'>

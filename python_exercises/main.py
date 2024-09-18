# Python Exercises
from sort_by_data_type import sort_by_data_type
from factorial import factorial
from is_even import is_even
import student_dict
import ode_plot

dash_count = 40 # For print() formatting

# sort_by_data_type()
print('-' * dash_count)
data = [1, 0, 'python', 4.2, 'robot', 7, 0.123, 12.345, 'pi']
int_list, float_list, str_list = sort_by_data_type(data)

print("Mixed Data:", data)
print("Integers:", int_list)
print("Floats:", float_list)
print("Strings:", str_list)

# factorial()
print('-' * dash_count)
n = 10
f = factorial(n)
if f >= 1:
  print(str(n), "! = ", str(f), sep='')
else:
  print("Input must be a positive integer")

# is_even()
print('-' * dash_count)
n = 7
if is_even(n) == True:
  print(n, "is even")
elif is_even(n) == False:
  print(n, "is odd")
else: print("Input must be an integer")

# student_dict
print('-' * dash_count)
grades = {
  'Math': 'A',
  'English': 'C',
  'Art': 'D'
}
student = student_dict.create_student('Monty', 55, grades)
student_dict.add_grade(student, 'Chemistry', 'B')
student_dict.add_grade(student, 'Theatre', 'A')
print("Student Name:", student['name'])
print("Student Age:", student['age'])
print("Grades by Subject:", student['grades'])
print("Student Average Grade:", student_dict.calculate_average(student))

print('-' * dash_count)
print("Generating Grade Chart...")
student_dict.generate_grade_chart(student)

# ode_plot
print('-' * dash_count)
print("Generating Solution Plot...")
def func(x, y): # First order differential equation in form: dy/dx = q(x) + p(x) * y
  dydx = -2 * x + 4 * y
  return dydx
initial_y = 1
initial_x = 0
ode_plot.plot(func, 1, 0, 10, x_label = 't')

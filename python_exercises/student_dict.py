from matplotlib import pyplot

def create_student(name, age, grades):
  student = {
    'name': name,
    'age': age,
    'grades': grades
  }
  return student

def add_grade(student, subject, mark):
  student['grades'][subject] = mark

def letter_to_points(grades):
  points = []
  key = {
  'A': 4.0,
  'B': 3.0,
  'C': 2.0,
  'D': 1.0,
  'F': 0
  }

  for letter in grades:
    if letter in key:
      points.append(key[letter])
  
  return points

def calculate_average(student):
  points = letter_to_points(student['grades'].values())
  gpa = sum(points) / len(points)
  
  return gpa

def generate_grade_chart(student_dict):
  grades = student_dict['grades']
  name = student_dict['name']

  figure = pyplot.figure()
  pyplot.bar(grades.keys(), letter_to_points(grades.values()))
  pyplot.title(f"{name}'s Grade Chart")
  pyplot.xlabel('Subject')
  pyplot.ylabel('Grade')

  figure.savefig(f'./grade_chart_{name.lower()}.png', dpi=figure.dpi)
  pyplot.show()

class Student:
  def __init__(self,name,  roll_number,cgpa): 
     self.name=name                      self.roll_number=roll_number 
     self.cgpa = cgpa 

def sort_students(student_list):
    # Sort the list of students in descending order of CGPA 
      sorted_students=sorted(student_list,key=lambda student:student.cgpa, reverse=True)   return sorted_students 



# Example usuage:
students=[
  Student("Hari","A 123",7.8),
  Student("Srikanth","A 124",8.9),
  Student("Sowmiya","A 125",9.1),
  Student("Mohana","A 126",9.9), 
] 
sorted_students = sort_students(students) 

# Print the sorted List of students 
for student in sorted_students:
  print("Name:{}, Roll Number:{}, CGPA:{}".format(student.name, student.roll_number,
                                                  student.cgpa))
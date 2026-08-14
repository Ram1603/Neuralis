# Parent Class
class Student:
    def __init__(self, name, age, grade):
        self.name = name
        self.__age = age  # Private attribute from Encapsulation exercise
        self.grade = grade

    def get_age(self):
        return self.__age

    def display_info(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.get_age()}")
        print(f"Grade: {self.grade}")


# Subclass inheriting from Student
class HighSchoolStudent(Student):
    def __init__(self, name, age, grade, grade_level):
        super().__init__(name, age, grade)
        self.grade_level = grade_level

    # Overridden method
    def display_info(self):
        super().display_info()
        print(f"Grade Level: {self.grade_level}")

# POLYMORPHISM FUNCTION
# ==============================================================================
def print_student_info(student_object):
    """
    Accepts ANY object that has a display_info() method
    (whether it's a Student or HighSchoolStudent) and calls it.
    """
    print("--- Student Information ---")
    student_object.display_info()  # Calls the correct display_info() automatically!
    print("---------------------------\n")


# --- Sample Test Run ---

# 1. Create a Student object
student1 = Student("Ram", 23, "C")

# 2. Create a HighSchoolStudent object
student2 = HighSchoolStudent("Suraj", 16, "B+", "10th Grade")

# 3. Pass both objects into the SAME function
print_student_info(student1)
print_student_info(student2)
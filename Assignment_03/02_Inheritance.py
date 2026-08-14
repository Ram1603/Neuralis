# Parent Class
class Student:
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade

    def display_info(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Grade: {self.grade}")


# Subclass (Child Class) inheriting from Student
class HighSchoolStudent(Student):
    def __init__(self, name, age, grade, grade_level):
        # super().__init__() calls the parent class constructor to set name, age, and grade
        super().__init__(name, age, grade)
        self.grade_level = grade_level

    # Overriding the parent's display_info method
    def display_info(self):
        # Call the parent class display_info() to print name, age, and grade
        super().display_info()
        # Print the extra attribute
        print(f"Grade Level: {self.grade_level}")


# --- Sample Test Run ---

# Create a HighSchoolStudent object
student1 = HighSchoolStudent("Ram", 23, "C+", "12th Grade")

# Call the overridden display_info method
student1.display_info()
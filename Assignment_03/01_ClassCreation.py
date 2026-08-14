class Student:
    # Constructor method to initialize attributes when a new student is created
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade

    # Method to display the student's information
    def display_info(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Grade: {self.grade}")


# --- Sample Test Run ---

# Create a Student object
student1 = Student("Ram", 23, "C")

# Call the display_info method
student1.display_info()
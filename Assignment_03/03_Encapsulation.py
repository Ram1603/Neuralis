class Student:

    def __init__(self, name, age, grade):
        self.name = name
        self.__age = age  # Private attribute (starts with two underscores __)
        self.grade = grade

    # Getter method: Used to RETRIEVE the private age
    def get_age(self):
        return self.__age

    # Setter method: Used to UPDATE the private age safely
    def set_age(self, new_age):
        # We can add validation to ensure the age is valid!
        if new_age > 0:
            self.__age = new_age
        else:
            print("Invalid age! Age must be a positive number.")

    def display_info(self):
        print(f"Name: {self.name}")
        # Use get_age() internally to access the private attribute
        print(f"Age: {self.get_age()}")
        print(f"Grade: {self.grade}")


# --- Sample Test Run ---

student1 = Student("Ram", 22, "C")

# 1. Retrieve the age using getter
print("Original Age:", student1.get_age())

# 2. Update the age using setter
student1.set_age(23)
print("Updated Age:", student1.get_age())

print("\n--- Displaying Full Info ---")
student1.display_info()
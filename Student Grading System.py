from abc import ABC , abstractmethod
class Student(ABC):

    def __init__(self,name,age,marks):
        self.name = name
        self.age  = age
        self.marks = marks

    @abstractmethod
    def calculate_grade(self):
        pass

    @abstractmethod
    def display_info(self):
        pass

class HighSchoolStudent(Student):

    def __init__(self,name,age,marks,school_name):
        super().__init__(name,age,marks)
        self.school_name = school_name

    def calculate_grade(self):
        if self.marks >= 90:
            return "A"
        elif self.marks >= 75:
            return "B"
        elif self.marks >= 60:
            return "C"
        else:
            return "D"
    def display_info(self):
        return f"Name is {self.name} Age is {self.age} Marks  is {self.marks} and Grad is {self.calculate_grade()}"

class Collage_Student(Student):

    def __init__(self,name,age,marks ,collage_name):
        super().__init__(name,age,marks)
        self.collage_name = collage_name

    def calculate_grade(self):
        if self.marks >= 90:
            return "A"
        elif self.marks >= 75:
            return "B"
        elif self.marks >= 60:
            return "C"
        else:
            return "D"

    def display_info(self):
        return f"Name is {self.name} Age is {self.age} Marks is {self.marks} and Grad is {self.calculate_grade()}"

if __name__ =="__main__":

    ll = Collage_Student()


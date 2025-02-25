
class Animal:

    def make_sound(self):
        print("some generic animal sound")


class Dog(Animal):

    def make_sound(self):
        print("Bark")


class Cat(Animal):
    def make_sound(self):
        print("Meow")

if __name__ =="__main__":
    dog = Dog()
    dog.make_sound()

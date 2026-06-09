class Person:
	name="Snehal";
class Student(Person):
	name="sakshi";
	def display(self):
		print("Name is:",super().name);
s1=Student();
s1.display();
class Person:
	name="snehal";
class Student(Person):
	name="sakshi";
	def display(self):
		print("Name is:",self.name);
s1=Student();
s1.display();
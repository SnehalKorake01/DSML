class Person:
	name="shubham";
	def display(self):
		print("Name is:",self.name);
class Student(Person):
	pass
s=Student();
s.display();
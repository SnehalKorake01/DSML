class Person:
	name="";
	age=0;
	def __init__(self,name,age):
		self.name=name;
		self.age=age;
class Student(Person):
	marks=0;
	add="";
	def __init__(self,marks,add,name,age):
		super().__init__(name,age);
		self.marks=marks;
		self.add=add;
	def display(self):
		print("Name is:",self.name,"Age is:",self.age);
s1=Student(90,"satara","snehal",23);
s1.display();
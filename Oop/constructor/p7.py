class Student:
	age=10;
	name=" ";
	def __init__(self,b,c):
		self.age=b;
		self.name=c;
	def display(self):
		print("Name:",self.name);
		print("Age:",self.age);
s1=Student(24,"snehal");
s2=Student(20,"sakshi");
s1.display();
s2.display();
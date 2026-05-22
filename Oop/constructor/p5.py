class Student:
	age=10;
	name=" ";
	def __init__(self,b,c):
		print("in init");
		self.age=b;
		self.name=c
s1=Student(20,"snehal");
print(s1.name);

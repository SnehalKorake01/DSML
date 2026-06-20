class Person:
	def fun(self):
		print("in parent constr");
		return 100;
class Student(Person):
	def fun(self):
		print("in child constr");
		print(super().fun());
		
s1=Student();
s1.fun();
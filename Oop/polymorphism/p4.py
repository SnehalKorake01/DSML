class Person:
	def fun(self):
		print("in person constr");
class Employee(Person):
	def fun(self):
		print("in Employee constr");
		super().fun();
e1=Employee();
e1.fun();

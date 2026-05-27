class Parent:
	def __init__(self):
		print("in parent constr");
class Child(Parent):
	def __init__(self):
		print("in child constr");
c1=Child();

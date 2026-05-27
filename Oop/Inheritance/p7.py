class Person:
	def __init__(self):
		print("in parent constr");
class Child(Person):
	def __init__(self):
		super().__init__();
		print("in child constr");
class GrandChild(Child):
	def __init__(self):
		super().__init__();
		print("in GrandChild constr");
G1=GrandChild();

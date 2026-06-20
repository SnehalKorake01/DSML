from abc import ABC ,abstractmethod
class Parent(ABC):
	def education(self):
		pass;
	def __init__(self):
		print("in parent constr");
class Child(Parent):
	def __init__(self):
		
		print("in child constr");
		super().__init__();
 		


c1=Child();

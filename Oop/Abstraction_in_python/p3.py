from abc import ABC,abstractmethod
class Parent(ABC):
	@abstractmethod
	def education(self):
		pass;
	def property(self):
		print("parent property");
class Child(Parent):
	pass;
c1=Child();
c1.education();
		
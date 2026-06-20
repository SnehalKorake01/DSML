from abc import ABC,abstractmethod
class Parent(ABC):
	@abstractmethod
	def education(self):
		pass;
	def property(self):
		print("parent property");
class Child(Parent):
	def education(self):
		print("Btech");
	pass;
c1=Child();
c1.education();
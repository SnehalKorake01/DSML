from abc import ABC,abstractmethod
class Parent(ABC):
	@abstractmethod
	def education(self):
		pass;
class Child(Parent):
	def education(self):
		print("btech");
p1=Parent();
p1.education();
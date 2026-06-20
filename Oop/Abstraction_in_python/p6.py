import dis
from abc import ABC,abstractmethod
class Parent(ABC):
	@abstractmethod
	def education(self):
		pass;
	a=0;
	name="";
	def __init__(self,a,name):
		self.a=a;
		self.name=name;
class Child(Parent):
	add="";
	def education(self):
		print("Btech");
		
	def __init__(self,a,name,add):
		super().__init__(a,name);
		self.add=add;
	def display(self):
		print(self.add);
		print(self.name);
		print(self.a);
c1=Child(10,"snehal","satara");
c1.display();
		
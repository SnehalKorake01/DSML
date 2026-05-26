class Demo:
	name="";
	age=0;
	def __init__(self,name,age):
		self.name=name;
		self.age=age;
	def display(self):
		print("Name is",self.name);
		print("Age is",self.age);
d1=Demo("snehal",23);
d1.display();
d2=Demo("Nilkanth",16);
d2.display();

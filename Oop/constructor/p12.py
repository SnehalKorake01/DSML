class Demo:
	name="";
	age=0;
	marks=0;
	add="";
	def __init__(self,name,age,marks,add):
		self.name=name;
		self.age=age;
		self.marks=marks;
		self.add=add;
	def display(self):
		print("Name is",self.name,"   Age is",self.age,"  Marks is",self.marks,"  Add is",self.add);
d1=Demo("snehal",23,96,"pandharpur");
d1.display();
d2=Demo("sakshi",20,98,"satara");
d2.display();
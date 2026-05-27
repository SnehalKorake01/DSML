class Parent:
	name="";
	age=0;
	add="";
	def __init__(self,name,age,add):
		self.name=name;
		self.age=age;
		self.add=add;
class Child(Parent):
	marks=0;
	roll_number=0;
	def __init__(self,marks,roll_number,name,age,add):
		super().__init__(name,age,add);
		self.marks=marks;
		self.roll_number=roll_number;
c1=Child(40,1,"snehal",23,"satara");
print(c1.name);
print(c1.marks);
class Person:
	name="";
	age=0;
	add="";
	ph_No=0;
	def __init__(self,name,age,add,ph_No):
		self.name=name;
		self.age=age;
		self.add=add;
		self.ph_No=ph_No;
class Manager(Person):
		sal=0;
		company="";
		def __init__(self,sal,company,name,age,add,ph_No):
			super().__init__(name,age,add,ph_No);
			self.sal=sal;
			self.company=company;
class Employee(Manager):
		lang="";
		def __init__(self,lang,sal,company,name,age,add,ph_No):
			super().__init__(sal,company,name,age,add,ph_No);
			self.lang=lang;
		def display(self):
			print("Name is:",self.name,"Lang is:",self.lang);
E1=Employee("java",50000,"tcs","snehal",23,"satara",1234);
E1.display();
E2=Employee("python ",600000,"amazon","nilkanth",16,"pune",98988);
E2.display();

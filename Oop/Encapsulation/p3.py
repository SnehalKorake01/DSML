class Student:
	def __init__(self,name,roll_no,age):
		self.name=name;
		self.__roll_no=roll_no;
		self.age=age;
	def display(self):
		print(self.__roll_no);
s1=Student("snehal",93,23);
s1.display();
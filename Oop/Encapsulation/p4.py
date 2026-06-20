class Student:
	def __init__(self,name,roll_no,age):
		self.name=name;
		self.__roll_no=roll_no;
		self.age=age;
	def get_roll_no(self):
		return self.__roll_no;
s1=Student("snehal",93,23);
print(s1.get_roll_no());
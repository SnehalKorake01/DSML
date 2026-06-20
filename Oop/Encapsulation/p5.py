class Student:
	def __init__(self,name,roll_no,age):
		self.name=name;
		self.__roll_no=roll_no;
		self.age=age;
	def set_roll_no(self,roll_no):
		self.__roll_no=roll_no;
	def get_roll_no(self):
		return self.__roll_no;

s1=Student("snehal",93,23);
s1.set_roll_no(115);
print(s1.get_roll_no());
class Student:
	def __init__(self,name,age,id,compname):
		self.name=name;
		self.age=age;
		self.__id=id;
		self.__compname=compname;
	def set_id(self,id):
		self.__id=id;
	def set_compname(self,compname):
		self.__compname=compname;
	def get_id(self):
		return self.__id;
	def get_compname(self):
		return self.__compname;
s1=Student("snehal",23,1,"tcs");
print(s1.get_id());
print(s1.get_compname());
s1.set_id(115);
s1.set_compname("amazon");
print(s1.get_id());
print(s1.get_compname());

class Parent:
	def education(self):
		print("Btech");
class Child(Parent):
	def education(self):
		print("MTech");
c1=Child();
c1.education();
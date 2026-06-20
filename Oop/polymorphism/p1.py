class A:
	def fun(self):
		print("in parent constr A");
class B(A):
	def gun(self):
		print("in child constr B");
b1=B();
b1.gun();
b1.fun();
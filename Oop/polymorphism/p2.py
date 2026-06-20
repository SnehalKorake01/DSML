class A:
	def fun(self):
		print("in parent constr A");
class B(A):
	def fun(self):
		print("in child constr B");
		super().fun();
b1=B();
b1.fun();
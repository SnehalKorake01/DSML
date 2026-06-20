class A:
	def __init__(self):
		print("constr in A");
class B:
	def __init__(self):
		print("constr in B");
class C(A,B):
	def __init__(self):
		super().__init__();
c1=C();
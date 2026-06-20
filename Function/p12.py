def fun(a,b):
	print(a,b)
fun(b=20,a=10);

def fun(**data):
	print(data);
	print(data['c']);
fun(b=20,a=40,c=50);
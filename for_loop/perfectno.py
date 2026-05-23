num=6;
sum=0
for i in range(1,num):
	if(num%i==0):
		sum=sum+i;
if(num==sum):
	print("perfect no");
else:
	print("not perfect");
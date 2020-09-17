# Function to add two numbers 
def add(num1, num2): 
	addition = num1 + num2
	return addition

# Function to subtract two numbers 
def subtract(num1, num2): 
	subtraction = num1 - num2
	return subtraction

# Function to multiply two numbers 
def multiply(num1, num2): 
	multiplication = num1*num2
	return multiplication

# Function to divide two numbers 
def divide(num1, num2): 
	division = num1/num2
	return division
	
# Function to add power function
#You cant use the inbuilt python function x ** y . Write your own function
def power(num1, num2):
	if(type(num2)==float or type(num2)==int) and (type(num1)==int or type(num2)==float):
		if (abs(num1)>((1<<31)-1)) or (abs(num2)>((1<<31)-1)):
			return 0
		power = num1
		num2 = int(num2)
		if num2==0:
			return 1
		if num2>0:
			while num2>1:
				power*= num1
				num2 -=1
		if num2<0:
			while num2<=0:
				power/= num1
				num2 += 1
		return round(power,3)
	else:
		return 0
	
# Python 3 program to print GP.  geometric Progression
#You cant use the inbuilt python function. Write your own function
def printGP(a, r, n):
	if(type(a)==int or type(a)==float) and (type(r)==int or type(r)==float)and (type(n)==int or type(n)==float) and n>=0:
		if (abs(a)>((1<<31)-1)) or (abs(r)>((1<<31)-1)) or (abs(n)>((1<<31)-1)):
			return 0
		gp = []
		n = int(n)
		if n==0:
			return gp
		if n>0:
			gp.append(a)
			for i in range(1,n):
				gp.append(round(gp[-1]*r,3))
			return gp
	else:
		return 0

# Python 3 program to print AP.  arithmetic Progression
#You cant use the inbuilt python function. Write your own function
def printAP(a, d, n):
	if(type(a)==int or type(a)==float) and (type(d)==int or type(d)==float)and (type(n)==int or type(n)==float) and n>=0:
		if (abs(a)>((1<<31)-1)) or (abs(d)>((1<<31)-1)) or (abs(n)>((1<<31)-1)):
			return 0	
		ap=[]
		n = int(n)
		if n==0:
			return ap
		if n>0:
			ap.append(a)
			for i in range(1,n):
				ap.append(round(ap[-1]+d,3))
			return ap
	else:
		return 0


# Python 3 program to print HP.   Harmonic Progression
#You cant use the inbuilt python function. Write your own function
def printHP(a, d, n):
	# if(type(a)==int or type(a)==float) and (type(d)==int or type(d)==float)and (type(n)==int or type(n)==float) and n>=0:
	# 	if (abs(a)>((1<<31)-1)) or (abs(d)>((1<<31)-1)) or (abs(n)>((1<<31)-1)):
	# 		return 0 
	hp=[]
	n = int(n)
	if n==0:
	return hp


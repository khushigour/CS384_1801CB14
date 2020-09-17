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
	gp=[]
	return gp 

# Python 3 program to print AP.  arithmetic Progression
#You cant use the inbuilt python function. Write your own function
def printAP(a, d, n): 
	ap=[]
	return ap

# Python 3 program to print HP.   Harmonic Progression
#You cant use the inbuilt python function. Write your own function
def printHP(a, d, n): 
	hp=[]
	return hp


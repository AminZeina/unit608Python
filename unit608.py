# Created By: Amin Zeina 	
# Created On: Apr 2018

# Multiplication


answer = 0
number_a = int(input('Enter your first number: '))
number_b = int(input('Enter your second number: '))

for timesAdded in range(0,number_b):
	answer = answer + number_a

print('Your answer is {}' .format(answer))
input('Program End.')

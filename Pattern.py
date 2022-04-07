# Python 3.x code to demonstrate star pattern

# Function to demonstrate printing pattern triangle
from multiprocessing.connection import wait
import time


def triangle(n):
	
	# number of spaces
	k = n - 1

	# outer loop to handle number of rows
	for i in range(0, n):
	
		# inner loop to handle number spaces
		# values changing acc. to requirement
		for j in range(0, k):
			print(end=" ")
	
		# decrementing k after each loop
		k = k - 1
	
		# inner loop to handle number of columns
		# values changing acc. to outer loop
		for j in range(0, i+1):
		
			# printing stars
			print("* ", end="")
	
		# ending line after each row
		print("\r")

# Driver Code
for i in range(20):
    n = 5
    print(i)
    triangle(n)
    time.sleep(1000)


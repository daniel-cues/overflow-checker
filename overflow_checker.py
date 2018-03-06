#!/usr/bin/python3
"""This program finds the minimun number of bytes needed to overflow the stack of a simple binary."""

import struct, subprocess, sys
from subprocess import PIPE, TimeoutExpired 

__author__= "Daniel Cuesta Suárez. @danielcues"


insane = 99999
program = ""


def overflow(n): 
	"""Tries to overflow the given program with n bytes.

	Returns True if the program overflows, false if it doesn't. 
	It also returns false if the program excedes the timeout. 
	This is to prevent never-ending binaries to stall this program
	"""
	command = "./"+program
	payload = "A"*n
	try:
		process = subprocess.run(command.split(" "), 
					 stdout=PIPE, 
					 stderr=PIPE, 
					 input= payload, 
					 encoding='ascii', 
					 timeout=0.1)

		if(process.returncode == -11):
			return True
		return False

	except TimeoutExpired:
   		return False



def insaneOverflow():
	"""Calls the overflow function with the stablished maximun value"""
	return overflow(insane)



def findMinPaddingInInterval(start, end):
	"""Recursively looks for the minimun value needed to overflow the program. 
	Complexity O(log n)
	"""
	if (start == end):
		return start
	mid = (int)((start+end)/2)
	if (overflow(mid)):
		return findMinPaddingInInterval(start, mid)
	return findMinPaddingInInterval(mid+1, end)



def findMinPadding():
	"""Starts the search for minimun padding"""
	return findMinPaddingInInterval(1,insane)


def main():
	global program 
	program= sys.argv[1]

	if (insaneOverflow()):
		minimunPadding = findMinPadding()
		print("Program needs at least %d bytes to break." % minimunPadding)
		print("That means your padding should be %d bytes long" %  (minimunPadding-4))
		
	else:
		print("%s is not vulnerable to buffer oveflow. Better luck next time" % program)
	return



main()

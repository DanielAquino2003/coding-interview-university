from queue import Queue
import math

def hash():
	thisdict = {
		'bob': 7387,
		'alice': 3719,
		'jack': 7052,
	}

	x = thisdict['bob']

	thisdict['alice'] = 2456

	for x in thisdict:
		print(x)

	for x in thisdict:
		print(thisdict[x])

def queue_usage():
	q = Queue(maxsize=3)
	print(q.queue)
	print(q.qsize())

	q.put('a')
	print(q.full())
	print(q.queue)
	print(q.get())
	print(q.empty())
class Stack:
	def __init__(self):
		self.stack = []

	def isEmpty(self):
		return len(self.stack) == 0
	def push(self, p):
		self.stack.append(p)
	def pop(self):
		return self.stack.pop()

def stack_usage():
	stack = Stack()
	stack.push(6)
	stack.push(2)
	stack.push(3)
	stack.push(8)
	print(stack.stack)
	stack.pop()
	print(stack.stack)

def exception():
	try:
		fh = open("testfile", "r")
		fh.write("This is my test file for exception handling!!")
	except IOError:
		print("Error: cant find file or read data")
	else:
		print("Written content in the successfully")
	finally:
		print("Error: cant find fule or read data")

	x = 10
	if x < 5:
		raise Exception('x should not exceed 5. The value of x was: {}'.format(x))

	import sys
	assert('linux' in sys.platform), "This code runs on linux only"

def string_usage():
	s = 'hi'
	print(s[1])
	print(len(s))
	print(s + ' there')

def casting():
	s = 12
	print(11 + int("12"))
	print(str(s))

def arithmetic():
	print(5%2)
	print(5/2)
	print(5//2)
	print(round(51.6))
	print(round(2.665,2))
	print(math.floor(300.16))
	print(math.floor(300.76))
	print(math.ceil(300.76))
	print(math.ceil(300.76))

print("QUEUE")
queue_usage()
print("\nSTACK")
stack_usage()
print("\nHASH")
hash()
print("\EXCEPTION")
exception()
print("\nSTRING")
string_usage()
print("\nCASTING")
casting()
print("\nARITHMETIC")
arithmetic()

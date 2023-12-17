# 3-valued truth functions
# 3-valued * 2-arguments
# 19683 functions can be defined
# meaning of value  1:true  -1:false  0:unknown
# input: function number you want to test (0<=fn<19683)
# output: truth table of input function
# example: (input)9841  (output)0 0 0 0 0 0 0 0 0 :f9841

from itertools import product

def threeVL(fn,a,b):
	if fn == 0:
		return -1
	elif fn == 1:
		if a == -1 and b == -1: return 0
		else: return -1
	elif fn == 2:
		if a == -1 and b == -1: return 1
		else: return -1
	elif 3 <= fn < 6:
		if a == -1 and b == 0: return 0
		else: return threeVL(fn-3,a,b)
	elif 6 <= fn < 9:
		if a == -1 and b == 0: return 1
		else: return threeVL(fn-6,a,b)
	elif 9 <= fn < 18:
		if a == -1 and b == 1: return 0
		else: return threeVL(fn-9,a,b)
	elif 18 <= fn < 27:
		if a == -1 and b == 1: return 1
		else: return threeVL(fn-18,a,b)
	elif 27 <= fn < 54:
		if a == 0 and b == -1: return 0
		else: return threeVL(fn-27,a,b)
	elif 54 <= fn < 81:
		if a == 0 and b == -1: return 1
		else: return threeVL(fn-54,a,b)
	elif 81 <= fn < 162:
		if a == 0 and b == 0: return 0
		else: return threeVL(fn-81,a,b)
	elif 162 <= fn < 243:
		if a == 0 and b == 0: return 1
		else: return threeVL(fn-162,a,b)
	elif 243 <= fn < 486:
		if a == 0 and b == 1: return 0
		else: return threeVL(fn-243,a,b)
	elif 486 <= fn < 729:
		if a == 0 and b == 1: return 1
		else: return threeVL(fn-486,a,b)
	elif 729 <= fn < 1458:
		if a == 1 and b == -1: return 0
		else: return threeVL(fn-729,a,b)
	elif 1458 <= fn < 2187:
		if a == 1 and b == -1: return 1
		else: return threeVL(fn-1458,a,b)
	elif 2187 <= fn < 4374:
		if a == 1 and b == 0: return 0
		else: return threeVL(fn-2187,a,b)
	elif 4374 <= fn < 6561:
		if a == 1 and b == 0: return 1
		else: return threeVL(fn-4374,a,b)
	elif 6561 <= fn < 9842:
		if a == 1 and b == 1: return 0
		else: return threeVL(fn-6561,a,b)
	elif 9842 <= fn < 19683:
		return -threeVL(19682-fn,a,b)

f_num = int(input())

for a,b in product([1,0,-1],[1,0,-1]):
	print("%2s" % a,end=" ")
print(": a")
for a,b in product([1,0,-1],[1,0,-1]):
	print("%2s" % b,end=" ")
print(": b")
print("-"*35)

for i in range(max(0,f_num-10),min(f_num+11,19683)):
	for x,y in product([1,0,-1],[1,0,-1]):
		print("%2s" % threeVL(i,x,y),end=" ")
	print(": f{}".format(i))
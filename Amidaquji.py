# input example: ABCDEFG (7 member's symbol), VWXYZ (5 member's) etc.

import random as rd

member = list(input())
assignment = [str(n) for n in range(len(member))]
rd.shuffle(member)
rd.shuffle(assignment)

def makeLadder(lst0,lst1):
	lst00 = lst0.copy()
	lst11 = lst1.copy()
	for i in range(1,len(lst0)*2-1,2):
		lst00.insert(i," ")
		lst11.insert(i," ")
	ladder_t = [["%2s" % m for m in lst00]]
	def makeRow(lst0):
		ladder = ["" for r in range(len(lst0)*2-1)]
		parts = [[" | "," |_","_| "],[" ","_"]]
		for i in range(len(lst0)*2-1):
			if i == 0:
				ladder[i] = rd.choice(parts[0][:2])
			elif i % 2 == 1:
				if ladder[i-1] == parts[0][1]:
					ladder[i] = parts[1][1]
				else:
					ladder[i] = parts[1][0]
			elif i % 2 == 0:
				if ladder[i-1] == parts[1][1]:
					ladder[i] = parts[0][2]
				elif i == len(lst0)*2-2:
					ladder[i] = parts[0][0]
				else:
					ladder[i] = rd.choice(parts[0][:2])
		return ladder
	for j in range(len(lst0)*3):
		ladder_t.append(makeRow(lst0))
	ladder_t.append([" | "," "]*(len(lst0)-1)+[" | "])
	ladder_t.append(["%2s" % a for a in lst11])
	return ladder_t

def searchAssign(st,lst):
	move = {" | ":0," |_":2,"_| ":-2}
	idx = lst[0].index(st)
	axis = idx
	for i in range(1,len(lst)-1):
		axis += move.get(lst[i][axis])
	return lst[-1][axis]

lad = makeLadder(member,assignment)

for row in lad:
	print("".join("%s" % x for x in row))

print("\nResults;")
for m in member:
	print(f"{m}:{searchAssign(' '+m,lad)}")
# Tower of Hanoi

num = int(input())

rod1,rod2,rod3 = [i for i in range(num,0,-1)],[],[]

def move(n,start,temp,end):
	if n >= 1:
		move(n-1,start,end,temp)
		end.append(start.pop())
		printR()
		move(n-1,temp,start,end)

def printR():
	print(rod1,rod2,rod3,"",sep="\n")

printR()
move(num,rod1,rod2,rod3)
# binary numbers

n = int(input())
pw = 0
pwr = {}

while 2**pw <= n:
  pwr[2**pw] = format(2**pw,'b')
  pw += 1

for k in pwr:
  print(f"{pwr[k]:>{pw}}",end=" ")
  print(f"{k:>{len(str(n))}}",end=" ")
  print(f"{pwr[k].count('0'):>{len(str(pw-1))}}")
print()

r = n
bt = 0
for t in sorted(pwr.items(),key=lambda x:-x[0]):
  r -= t[0]
  if r >= 0:
    bt |= t[0]
    print(f"{t[1]:>{pw}}")
  else:
    r += t[0]
print()

print(format(bt,'b'),end=" ")
print(int(format(bt,'b'),2))
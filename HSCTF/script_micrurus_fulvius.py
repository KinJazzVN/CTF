from hashlib import sha256 as k 
from string import ascii_letters, digits

def a(n):
	b = 0
	while n != 1:
		if n & 1:
			n *= 3
			n += 1
		else:
			n//=2
		b +=1
	return b

def d(u, p):
	return (u << p % 5) - 158 

def dd(u, p):	# Reverse d 
	return u + 158 >> p % 5 

def j(q,w):
	return ord(q) * 115 + ord(w) * 21

l = [-153, 462, 438, 1230, 1062, -24, -210, 54, 2694, 1254, 69, -162, 210, 150]
v = "b4f9d505"

l_d = [dd(l[i] // 3, i) for i in range(len(l))]

alp = ascii_letters + digits + '{_}@!?'

# find the first, second character
# for i in alp:
# 	for z in alp:
# 		if a(j(i, z) - 10) == l_d[0]:
# 			print(i, z)

def solve(pre, idx):
	if idx == 14:
		return [""]
	p = [] 
	for i in alp:
		if a(j(pre, i) - 10) == l_d[idx]:
			p.append(i)
	return [c + cc for c in p for cc in solve(c, idx+1)]

flag = 'fl'

for i in solve('l', 1):
	flag += i 
	if k(''.join(flag).encode()).hexdigest()[:8] == v:
		print(flag)

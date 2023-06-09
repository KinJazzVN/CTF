from z3 import *

ins = [Int('i' + str(i)) for i in range(20)]
solver = Solver()

s = 0
a = 0
x = 0
y = 0

for i in range(20):
    c = ins[i]

    solver.add(Or(c == ord('r'), c == ord('L'), c == ord('R')))

    s = If(c == ord('r'), s + 1, s)

    a = If(c == ord('L'), (a + 1) % 4, If(c == ord('R'), (a + 3) % 4, a))

    x = If(a == 0, x + s, If(a == 2, x - s, x))

    y = If(a == 1, y + s, If(a == 3, y - s, y))

solver.add(x == 168, y == 32)

flag = []
i = 0 
for j in range(10):
    solver.check()
    model = solver.model()
    tmp = "".join([chr(model[ins[i]].as_long()) for i in range(20)])
    if i == 0 or (tmp not in flag):
        flag.append(tmp)
        print("flag{" + flag[i] + "}")
        i += 1
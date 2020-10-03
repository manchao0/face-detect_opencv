#测试列表分片的用法
a = [1, 2, 3, 4, 5]
print(a)
b = a[:-1]
print(b)
c = a[2:-1]
print(c)
d = a[-1:0:-1]
print(d)
e = a[:-2]
print(e)
f = [[1,2],[3,4],[5,6]]
print(f[2][1])
g = [[1,2],[3,4],[5,[7,8,9]]]
print(g[2][1][2])


print(a[1])

#测试argsort
import numpy as np
x=np.array([1,4,3,-1,6,9])
print(x.argsort())


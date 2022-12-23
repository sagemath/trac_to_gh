# Issue 292: Problems with stacked polynomial rings and vector

Issue created by migration from https://trac.sagemath.org/ticket/292

Original creator: ncalexan

Original creation time: 2007-02-24 05:33:12

Assignee: somebody

Keywords: polynomial rings vector


```
R1, (r0, r1, s1, s2) = QQ['r0', 'r1', 's1', 's2'].objgens()
R2, z = R1['z'].objgen()
R3, zb = R2.quo(z**3 + r1*z + r0, names='zb').objgen()

s = s1*z + s2*z**2

f1 = R3(s*1)
f2 = R3(s*z)
f3 = R3(s*z**2)
print vector(f1)
```


Spins off into 100% CPU land.


---

Comment by was created at 2007-08-19 01:30:03

Resolution: fixed


---

Comment by was created at 2007-08-19 01:30:03

fixed for sage-2.8.2 by William

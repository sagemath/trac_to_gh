# Issue 344: pari compare fails for some finite field elements

Issue created by migration from https://trac.sagemath.org/ticket/344

Original creator: malb

Original creation time: 2007-04-03 11:33:12

Assignee: somebody


```
# setup
f = conway_polynomial(2,63)
K.<a> = GF(2**63, name='a', modulus=f)
n = f.degree()
m = 3;
e = (2^n - 1) / (2^m - 1)
c = a^e
conway = conway_polynomial(2,m)
```



```
# element 1
print conway(c)   # says 0
print type(c)
print parent(c)
print c in K          # says True
```



```
# element 2
print K(0)      # says 0
print type(K(0))
print parent(K(0))
```



```
print conway(c) == K(0)    # says False???
```



---

Comment by malb created at 2007-04-03 11:35:22

More details:

```
e1 = conway(c)
e2 = K(0)
e1p = e1._FiniteField_ext_pariElement__value
e2p = e2._FiniteField_ext_pariElement__value
e1p._cmp(e2p)
<class 'gen.PariError'>                   Traceback (most recent call last)
/home/malb/<ipython console> in <module>()
/home/malb/gen.pyx in gen._pari_trap()
<class 'gen.PariError'>: incorrect type (20)
```



---

Comment by malb created at 2007-08-14 07:48:25

Resolution: fixed


---

Comment by malb created at 2007-08-14 07:48:25

Fixed for 2.8.1.

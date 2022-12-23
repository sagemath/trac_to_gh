# Issue 771: GF(p^n) vector() NotImplemented for p^n > 2^16

Issue created by migration from https://trac.sagemath.org/ticket/771

Original creator: malb

Original creation time: 2007-10-01 13:26:30

Assignee: was


```
K.<a> = GF(2^15, 'a')
V = K.vector_space()
z = (a+1)^13
V(z)

(1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 0)
```


2^16: Error!

```
K.<a> = GF(2^16, 'a')
V = K.vector_space()
z = (a+1)^13
V(z)



Exception (click to the left for traceback):
...
TypeError: can't initialize vector from nonzero non-list
```



---

Attachment


---

Comment by was created at 2007-10-20 22:08:48

Resolution: fixed

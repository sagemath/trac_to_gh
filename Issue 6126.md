# Issue 6126: Symmetric group algebra jucys_murphy elements incorrect

Issue created by migration from Trac.

Original creator: arattan

Original creation time: 2009-05-24 21:14:01

Assignee: mhansen

Keywords: jucys_murphy

The error is observed on my linux box as well as sage.math.washington.edu (my version is 3.4.1, sage.math version is 3.4.2, the error is the same).  The error is in the function "jucys_murphy".


```
sage: G=SymmetricGroupAlgebra(QQ,5)
sage: PermutationOptions(mult='l2r', display='cycle')
sage: for i in range(2,6):
....: G.jucys_murphy(i)
....:
(1,2)
(2,3) + (1,2)
(3,4) + (2,3) + (1,2)
(4,5) + (3,4) + (2,3) + (1,2)
```

I believe the returned elements should be

```
(1,2)
(2,3) + (1,3)
(3,4) + (2,4) + (1,4)
(4,5) + (3,5) + (2,5) + (1,5)
```

I found the relevant code.  On both machines the offending code is in

/usr/local/sage/devel/sage-main/build/sage/combinat/symmetric_group_algebra.py,

and

/usr/local/sage/devel/sage-main/sage/combinat).  I have fixed on my machine by changing in those files the lines 180-185 from


```
------------
for i in range(1, k):
p = range(1, self.n+1)
p[i-1] = i+1
p[i] = i
res += self(p)
return res
----------------
```


to


```
------------
for i in range(1, k):
p = range(1, self.n+1)
+ p[i-1] = k
+ p[k-1] = i
res += self(p)
return res
----------------
```


Thanks,
Amps


---

Comment by mhansen created at 2009-05-27 20:40:27

Changing status from new to assigned.


---

Attachment

I've attached a patch with these changes, and they look good to me.


---

Comment by mhansen created at 2009-05-27 20:40:42

Resolution: fixed


---

Comment by mhansen created at 2009-05-27 20:40:42

Merged in 4.0.rc1.


---

Comment by nthiery created at 2009-06-04 21:31:30

Please synchronize with sage-combinat-devel next time!
We got a conflict in the patch server.


---

Comment by nthiery created at 2009-06-04 23:44:17

See followup on #6215 which includes the doctests that had been written for the same bug in Sage-Combinat

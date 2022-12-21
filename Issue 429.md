# Issue 429: cannot create empty sparse matrix over reals

Issue created by migration from Trac.

Original creator: malb

Original creation time: 2007-08-15 16:53:44

Assignee: was

Try:

```
sage: A = Matrix(RR,2,2,sparse=True) 
<type 'exceptions.TypeError'>: Unable to convert x (='None')
to real number.
```

while

```
sage: A = Matrix(GF(127),2,2,sparse=True)
```

works.


---

Comment by malb created at 2007-08-15 16:54:20

Oh, Complex numbers don't work, too.


---

Comment by was created at 2007-08-19 01:17:36

fixed for sage-2.8.2.


---

Comment by was created at 2007-08-19 01:17:36

Resolution: fixed

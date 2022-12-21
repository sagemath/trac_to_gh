# Issue 738: probably easy-to-fix bug in matrix2.pyx

Issue created by migration from Trac.

Original creator: was

Original creation time: 2007-09-22 21:58:39

Assignee: robertwb


```
There's a bug in matrix2.pyx which is making my new
Polynomial_integer_dense class fail some doctests.

When you run this command:

       matrix(ZZ,3,range(9))._charpoly_hessenberg('Z')

then on line 992 of matrix2.pyx, the list v contains Rationals even
though the polynomial constructor (for base ring Z) is called with
check=False.

And to answer your next question:

sage: R.<x> = PolynomialRing(ZZ)
sage: R([1/2, 3/4, 5/6, 7/8], check=False)
7*x^3 + 5*x^2 + 3*x + 1

!!!

I'm sure one of you can fix this much faster than I can....
```



---

Comment by dmharvey created at 2007-09-23 18:10:29

Changing assignee from robertwb to dmharvey.


---

Comment by dmharvey created at 2007-09-23 18:10:29

Changing status from new to assigned.


---

Attachment

fixes this bug


---

Comment by dmharvey created at 2007-09-23 23:02:43

note: I uploaded a patch for #528 which includes the above patch


---

Comment by was created at 2007-09-23 23:12:29

Resolution: fixed

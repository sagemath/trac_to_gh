# Issue 1478: M2 interface -- make it so large input gets read in from a file

Issue created by migration from Trac.

Original creator: was

Original creation time: 2007-12-12 16:56:19

Assignee: was

From Joel Mohler:


```
> In any case, mpolynomial factorization, gcd, and division algorithms in singular
> pretty much entirely stop me cold computing in a fraction field of mpolynomials.
> My solution for the moment is to hack in calls to mathematica or magma from the
> libsingular code in sage.  I had a version of that hackage with M2, but the
> pexpect sage wrapper for M2 choked up on my polynomials (about 1/4 mb in string
> form.)  This "choked up" might merit more precise diagnosis investigation
> itself.

There are ways to get around that by writing large input to a file and telling
M2 to read in that file.   This is something this interface should do automatically,
but doesn't yet (for M2 -- it does it for most of the interfaces).    

```



---

Comment by jdemeyer created at 2015-06-23 13:46:00

Changing assignee from was to tbd.


---

Comment by jdemeyer created at 2015-06-23 13:46:00

Changing component from interfaces to packages: experimental.


---

Comment by jdemeyer created at 2015-06-23 13:49:26

Changing component from packages: experimental to interfaces: optional.


---

Comment by chapoton created at 2018-04-28 06:40:16

Changing keywords from "" to "Macaulay2".

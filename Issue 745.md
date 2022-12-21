# Issue 745: update the version of FLINT that is in Sage

Issue created by migration from Trac.

Original creator: was

Original creation time: 2007-09-24 20:48:19

Assignee: somebody


```
Guys,

I've removed all known bugs from fmpz_poly, including the memory
management ones I referred to previously. This includes some bugs
which should affect the FLINT polynomial multiplication in SAGE (but
apparently don't). They were in all the set_coeff type functions. To
be honest I'm not sure how you got the FLINT wrapper to work. You must
have just been lucky in the way you implemented it.

I've also now removed all the bugs I know of in the division
functions. There's also some memory leaks removed from the polynomial
division test code.

If you find any further bugs please report them. In the mean time
revision 1010 is what you want to use in SAGE with the respective
wrappers that you guys wrote.

Time to start working on Z_poly.
```



---

Comment by was created at 2007-10-04 03:15:28

Resolution: fixed

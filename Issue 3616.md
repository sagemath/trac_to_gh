# Issue 3616: flint hangs on itanium

Issue created by migration from Trac.

Original creator: was

Original creation time: 2008-07-08 19:13:57

Assignee: somebody

Using sage-3.0.4.rc0 on ia64 SUSE we have:

```
            sage: P.<x> = PolynomialRing(ZZ)
            sage: F = (x^2 + 2)*x^3; G = (x^2+2)*(x-3)
            sage: g, u, v = F.xgcd(G)
HANG
```



---

Comment by was created at 2008-07-08 19:27:36

Recompiling with -O0 does *not* fix the problem.  The flint test suite *fails* on
itanium even with -O0:


```
Testing fmpz_CRT_ui()... FAIL!
Testing fmpz_sqrtrem()... ok

At least one test FAILED!
```


That's the first failure.

This is flint-1.010.

william


---

Comment by was created at 2008-07-08 19:51:45

More test failures on iras (itanium box):


```
Testing fmpz_poly_CRT_unsigned()... FAIL!
Testing fmpz_poly_CRT()... FAIL!
```



---

Comment by mabshoff created at 2008-07-09 16:04:11

Due to the hard work by Bill Hard we now have a 1.0.11 spkg at

http://sage.math.washington.edu/home/mabshoff/flint-1.011.spkg

I turned on spkg-check per default. Builds and tests fine on x86-64 and Itanium.

Cheers,

Michael


---

Comment by was created at 2008-07-09 16:22:52

Resolution: fixed


---

Comment by mabshoff created at 2008-07-09 16:24:01

Merged in Sage 3.0.4.rc2

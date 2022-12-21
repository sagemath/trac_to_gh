# Issue 1436: FLINT 1.01 doesn't pass test suite on OSX 10.5.1

Issue created by migration from Trac.

Original creator: mabshoff

Original creation time: 2007-12-09 16:12:45

Assignee: mabshoff

I got the following on bsd:

```
Testing _fmpz_poly_scalar_mul_si()... ok
Testing fmpz_poly_scalar_mul_si()... ok
Testing _fmpz_poly_scalar_mul_fmpz()... ok
Testing fmpz_poly_scalar_mul_fmpz()... ./spkg-check: line 16: 94786
Floating point exception./fmpz_poly-test

real    4m39.394s
user    4m44.254s
sys     0m6.256s
sage: An error occurred while installing flint-1.01
```


FLINT 1.0 build and tested fine.

Cheers,

Michael


---

Comment by mabshoff created at 2007-12-10 04:02:51

Fixed by updating to FLINT 1.02. Merged in 2.9.alpha3.


---

Comment by mabshoff created at 2007-12-10 04:02:51

Resolution: fixed

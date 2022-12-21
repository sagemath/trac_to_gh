# Issue 1744: FLINT 1.05 "make check" failure on Linux/Itanium

Issue created by migration from Trac.

Original creator: mabshoff

Original creation time: 2008-01-10 06:51:38

Assignee: mabshoff

The following issue has been reported by two independent parties with vastly different setups, but both using gcc 4.2.2:

The `make check` in FLINT fails with

```
Testing _fmpz_poly_mul_KS()... GNU MP: Cannot reallocate memory
(old_size=8 new_size=4294959128)
./spkg-check: line 51: 13014 Aborted                 ./fmpz_poly-test 
```

This indicates a potential bug in gmp, but so far nobody has figured out what causes it. Bill Hart is investigating.

Cheers,

Michael


---

Comment by wbhart created at 2008-01-19 05:02:49

This bug appears to have been caused by the builtin functions in gcc for counting the number of bits in an unsigned long x. FLINT 1.0.6 hopefully fixes this issue by dealing with the special case of x == 0 at which point the bug occurred. The fix has been tested on one of the systems which failed.

SAGE should upgrade to FLINT 1.0.6 to rectify this.

Bill.


---

Comment by mabshoff created at 2008-01-24 09:16:21

The problem has been solved via #1821.


---

Comment by mabshoff created at 2008-01-24 09:16:21

Resolution: fixed

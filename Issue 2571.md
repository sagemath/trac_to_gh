# Issue 2571: problem with copy() on sage.rings.integer_mod.IntegerMod_gmp

Issue created by migration from https://trac.sagemath.org/ticket/2571

Original creator: dfdeshom

Original creation time: 2008-03-17 12:55:24

Assignee: somebody

John Cremona:

```
sage: a=[Mod(2,next_prime(2^n)) for n in range(28,35)]
sage: [type(x) for x in a]

[<type 'sage.rings.integer_mod.IntegerMod_int64'>,
 <type 'sage.rings.integer_mod.IntegerMod_int64'>,
 <type 'sage.rings.integer_mod.IntegerMod_int64'>,
 <type 'sage.rings.integer_mod.IntegerMod_gmp'>,
 <type 'sage.rings.integer_mod.IntegerMod_gmp'>,
 <type 'sage.rings.integer_mod.IntegerMod_gmp'>,
 <type 'sage.rings.integer_mod.IntegerMod_gmp'>]

sage: [copy(x) for x in a]
[2, 2, 2, None, None, None, None]

sage: [deepcopy(x) for x in a]
[2, 2, 2, 2, 2, 2, 2]
```



---

Attachment


---

Comment by cremona created at 2008-03-17 14:27:41

To fix this I added a return statement to the `__copy__()` function of IntegerMod_gmp.  Patch attached (based on 2.10.4.rc0)


---

Comment by cremona created at 2008-03-17 14:27:41

Changing status from new to assigned.


---

Comment by cremona created at 2008-03-17 14:27:41

Changing assignee from somebody to cremona.


---

Comment by dfdeshom created at 2008-03-17 14:34:52

While you're editing that function, would you mind adding a doctest or 2 to it? That would help with the overall 3.0 goal of >50% function doctest coverage


---

Comment by cremona created at 2008-03-17 16:56:03

apply after 8950.patch


---

Attachment

As suggested, a few doctests have been added, in the second patch.


---

Comment by jbmohler created at 2008-03-18 15:39:27

These patches fix the bug and add and improve documentation bits.  I've tested everything I could see that could go wrong (including the copy and sqrt/square_root change) and all looks good to me.

This is a positive review to both patches!


---

Comment by mabshoff created at 2008-03-19 00:36:59

Resolution: fixed


---

Comment by mabshoff created at 2008-03-19 00:36:59

Merged both patches in Sage 2.11.alpha0

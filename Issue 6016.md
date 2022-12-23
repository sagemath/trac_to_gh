# Issue 6016: factoring rational functions

Issue created by migration from https://trac.sagemath.org/ticket/6016

Original creator: syazdani

Original creation time: 2009-05-11 02:15:12

Assignee: tbd

It would be nice to be able to factor rational functions. The implementation is trivial, and the enclosed patch tries to do that.




---

Comment by mabshoff created at 2009-05-11 02:19:41

Soroosh,

please post a proper patch.

Cheers,

Michael


---

Attachment

Is this the right format?


---

Comment by mabshoff created at 2009-05-11 04:33:06

Yep, looks like a nice patch to me :)

Cheers,

Michael


---

Comment by mvngu created at 2009-05-11 05:45:25

based on sage-3.4.2


---

Attachment

REFEREE REPORT



The patch `12063.patch` looks good. The new method `factor()` works over `ZZ`, `QQ`, `RR`, `CC`, and `GF`. There's only a trivial Sphinx formatting issue, which is fixed in the reviewer patch `trac_6016-reviewer.patch`.


---

Comment by mabshoff created at 2009-05-14 05:44:58

I am not sure this should go in as is since the return result is a little strange. Is this consistent with other interfaces in Sage? What does Magma do?

Cheers,

Michael


---

Comment by cremona created at 2009-05-30 17:14:06

Replying to [comment:6 mabshoff]:
> I am not sure this should go in as is since the return result is a little strange. Is this consistent with other interfaces in Sage? What does Magma do?
> 
> Cheers,
> 
> Michael

This is entirely consistent with (for example) factorization of rational numbers in Sage:

```
sage: QQ(123/456).factor()
2^-3 * 19^-1 * 41
```

Magma does not allow factorization in QQ or in function fields, which is very annoying (e.g. you cannot factor the discriminant of an elliptic curve (with integral model) over QQ without coercing it into ZZ first).  But Magma does allow for some non-integral factorizations, e.g. of fractional ideals.

So Michael's worry is a reasonable one but this should definitely be included.  I have therefore removed the "needs discussion" tag!


---

Comment by mhansen created at 2009-06-01 04:59:57

Resolution: fixed


---

Comment by mhansen created at 2009-06-01 04:59:57

Merged in 4.0.1.alpha0.

# Issue 6458: Inverse modulo an ideal in a relative number field

Issue created by migration from Trac.

Original creator: davidloeffler

Original creation time: 2009-07-02 13:27:16

Assignee: was

This adds a few lines to get `inverse_mod` working in the ring of integers of a relative field.


---

Comment by davidloeffler created at 2009-07-02 13:28:30

patch against 4.1.alpha2


---

Attachment


---

Comment by ncalexan created at 2009-07-14 21:15:50

These doctests don't actually assert that the results are correct.  Could you add the few lines verifying that you're really getting a basis and really getting an inverse?


---

Comment by ncalexan created at 2009-07-14 21:20:02

Also, I get a doctest failure on sage.math.  This could be transient -- this is with a slightly out of date sage build.  But there's no way this will work on all architectures, so testing the property will be much better.


```
sage -t -long devel/sage/sage/rings/number_field/number_field_element.pyx
**********************************************************************
File "/scratch/ncalexan/sage-4.0.2.alpha1/devel/sage-main/sage/rings/number_field/number_field_element.pyx", line 3436:
    sage: OE(b - a).inverse_mod(17*b)
Expected:
    (-25*b + 26)*a + 51*b - 1
Got:
    (26*b - 25)*a - 51*b - 1
```



---

Attachment

apply after previous patch


---

Comment by davidloeffler created at 2009-07-14 22:05:36

Good point; I have uploaded a second patch that adjusts the doctests as you suggest.


---

Comment by ncalexan created at 2009-07-15 02:34:01

Beautiful.


---

Comment by mvngu created at 2009-07-16 19:54:38

David, the patch `trac_6458-relative_ideal_inverse_mod.patch` doesn't have your username. So I'm committing it in your name. Merged both patches in sage-4.1.1-alpha0. I can't close this ticket because I don't have the privilege to do so. Sorry, folks :-(


---

Comment by mvngu created at 2009-07-16 21:10:37

Resolution: fixed

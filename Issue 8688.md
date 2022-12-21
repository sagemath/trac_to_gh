# Issue 8688: extra parenthesis when typesetting fractions

Issue created by migration from Trac.

Original creator: burcin

Original creation time: 2010-04-14 22:31:13

Assignee: burcin


```
sage: latex((x+2)/(x^3+1))
\frac{{\left(x + 2\right)}}{{\left(x^{3} + 1\right)}}
```


Note the extra parenthesis in the numerator and denominator.


---

Comment by burcin created at 2010-05-06 04:24:37

Changing keywords from "" to "pynac".


---

Attachment

This is fixed by the pynac package in #8903. attachment:trac_8688-typeset_fraction.patch contains doctests.

Note that #8542, #8651 and #8775 is also fixed by the new pynac version. Patches from these tickets should be applied before doctesting.


---

Comment by burcin created at 2010-05-06 04:24:37

Changing status from new to needs_review.


---

Comment by was created at 2010-05-26 03:03:43

Resolution: fixed

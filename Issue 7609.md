# Issue 7609: numerical noise in doctests after pynac update

Issue created by migration from https://trac.sagemath.org/ticket/7609

Original creator: burcin

Original creation time: 2009-12-06 00:38:29

Assignee: burcin

The new pynac package and patch from #7490 introduced numerical noise in some doctests. Attached patch should fix this.


---

Attachment

fix numerical noise


---

Comment by burcin created at 2009-12-06 00:41:28

Changing status from new to needs_review.


---

Comment by kcrisman created at 2009-12-06 02:32:10

Changing status from needs_review to needs_work.


---

Comment by kcrisman created at 2009-12-06 02:32:10

This is fine, but there was another one in functions/trig.py (this on a 32-bit Macintel 10.5):

```
sage: float(cot(1))
0.64209261593433065
```

but gave

```
0.64209261593433076
```



---

Comment by burcin created at 2009-12-06 16:10:41

apply only this patch


---

Attachment

Hi Karl-Dieter,

attachment:trac_7609-pynac_numerical_noise.take2.patch adds a fix for the error you get as well. It is a good coincidence that you're testing on that box. :)

Thanks.


---

Comment by burcin created at 2009-12-06 16:15:51

Changing status from needs_work to needs_review.


---

Comment by kcrisman created at 2009-12-07 14:36:21

Okay, this seems good.  I do still get the segfault in symbolic/expression.pyx but that is addressed elsewhere.


---

Comment by kcrisman created at 2009-12-07 14:36:21

Changing status from needs_review to positive_review.


---

Comment by mhansen created at 2009-12-07 23:22:25

Resolution: fixed

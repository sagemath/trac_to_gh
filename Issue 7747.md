# Issue 7747: miscellaneous documentation fixes

Issue created by migration from Trac.

Original creator: jhpalmieri

Original creation time: 2009-12-21 22:40:57

Assignee: mvngu

With Sage 4.3.rc0, I get a few doctest failures from sage/doc, at least one of which is related to #7406.  The attached patch fixes them.  It also reinstates some doctests which were disabled until #5338 was fixed.

I'm marking this as a blocker since without it, there are doctest failures.


---

Attachment


---

Comment by jhpalmieri created at 2009-12-21 22:42:23

Changing status from new to needs_review.


---

Comment by mvngu created at 2009-12-22 08:15:08

Changing status from needs_review to positive_review.


---

Comment by mvngu created at 2009-12-22 08:15:08

Doctesting Sage 4.3.rc0 on `sage.math` results in the following failures:

```
sage -t -long devel/sage/doc/en/constructions/calculus.rst
**********************************************************************
File "/scratch/mvngu/sandbox/sage-4.3.rc0-7747-doc/devel/sage-main/doc/en/constructions/calculus.rst", line 29:
    sage: latex(f.diff(x))
Expected:
    k x^{3} e^{k x} \sin\left(w x\right) + w x^{3} e^{k x} \cos\left(w x\right) + 3 \, x^{2} e^{k x} \sin\left(w x\right)
Got:
    k x^{3} e^{\left(k x\right)} \sin\left(w x\right) + w x^{3} e^{\left(k x\right)} \cos\left(w x\right) + 3 \, x^{2} e^{\left(k x\right)} \sin\left(w x\right)
**********************************************************************
1 items had failures:
   1 of   6 in __main__.example_0
***Test Failed*** 1 failures.
For whitespace errors, see the file /tmp/mvngu/tmp/.doctest_calculus.py
         [5.6 s]

sage -t -long devel/sage/doc/en/bordeaux_2008/nf_introduction.rst
**********************************************************************
File "/scratch/mvngu/sandbox/sage-4.3.rc0-7747-doc/devel/sage-main/doc/en/bordeaux_2008/nf_introduction.rst", line 300:
    sage: latex(a)
Expected:
    -\frac{1}{2} \, {(I \, \sqrt{3} + 1)} ...
Got:
    -\frac{1}{2} \, {\left(I \, \sqrt{3} + 1\right)} {\left(\frac{1}{18} \, \sqrt{8 \, \sqrt{2} + 675} \sqrt{3} - \frac{5}{2}\right)}^{\left(\frac{1}{3}\right)} + \frac{1}{6} \, \frac{{\left(-I \, \sqrt{3} + 1\right)} \sqrt{2}\
}{{\left(\frac{1}{18} \, \sqrt{8 \, \sqrt{2} + 675} \sqrt{3} - \frac{5}{2}\right)}^{\left(\frac{1}{3}\right)}}
**********************************************************************
1 items had failures:
   1 of   7 in __main__.example_10
***Test Failed*** 1 failures.
For whitespace errors, see the file /tmp/mvngu/tmp/.doctest_nf_introduction.py
         [3.6 s]
```

The patch `trac_7747-doc.patch` fixes both of these failures. All doctests now pass on sage.math.


---

Comment by jhpalmieri created at 2009-12-22 19:02:44

This is a duplicate of #7659, but the patch here does a little more.  Can we use this patch instead of that one?


---

Comment by mhansen created at 2009-12-23 13:28:27

I've merged the patch here instead of the one at #7659.


---

Comment by mhansen created at 2009-12-23 13:28:27

Resolution: fixed


---

Comment by jhpalmieri created at 2009-12-23 15:54:35

Could you please make sure that burcin also gets author credit for this (for his work on #7659)?  Thanks.


---

Comment by mhansen created at 2009-12-23 17:40:05

Done.

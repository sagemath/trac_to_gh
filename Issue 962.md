# Issue 962: automatic precision extension for long decimal literals does very strange things

Issue created by migration from https://trac.sagemath.org/ticket/962

Original creator: cwitty

Original creation time: 2007-10-21 15:09:21

Assignee: somebody

Long decimal literals become floating-point numbers whose precision depends on the length of the input literal _in characters_.  See this script for some of the confusing (and, in my opinion, wrong) behavior that results.

```
sage: (1.10000000000000000000).prec()
73
sage: (1.10000000000000000000e0).prec()
79
sage: (1e-25).prec()
53
sage: (0.0000000000000000000000001).prec()
89
sage: (00000000.0000000000000000000000001).prec()
112
```




---

Comment by malb created at 2007-10-23 22:23:29

Changing assignee from somebody to cwitty.


---

Comment by mhansen created at 2007-10-24 20:18:20

Changing assignee from cwitty to mhansen.


---

Comment by mhansen created at 2007-10-24 20:18:20

Changing status from new to assigned.


---

Attachment

Initial version


---

Comment by mhansen created at 2007-11-13 03:21:55

I posted an initial patch which fixes some of the major issues.  I would like others to comment on it to make sure the final version of this patch does the "right thing" since it will break lots of doctests.


---

Comment by mhansen created at 2007-11-13 03:54:35

Here is the behavior of the above examples after the patch:

```
sage: sage: (1.10000000000000000000).prec()
74
sage: sage: (1.10000000000000000000e0).prec()
74
sage: sage: (1e-25).prec()
87
sage: sage: (0.0000000000000000000000001).prec()
87
sage: sage: (00000000.0000000000000000000000001).prec()
87
```



---

Comment by cwitty created at 2007-11-13 05:51:33

Actually, I think that all of the last three examples should give 53 (that is, leading zeroes shouldn't affect the precision).  I think that matches the rules for significant figures I learned in grade school...


---

Comment by was created at 2007-11-18 04:11:10

NOT YET -- note that I think many doctests will (and should) break after applying this patch, so this isn't being posted to actually include in the next release.  It's being posted for feedback.   After people like it, then Mike will post an additional patch that fixes all failing doctests. 

I also think I agree with Carl witty's remark above about significant figures.


---

Comment by mhansen created at 2007-12-01 18:01:40

Patch updated that now gives the following results:

```
sage: sage: sage: (1.10000000000000000000).prec()
74
sage: sage: sage: (1.10000000000000000000e0).prec()
74
sage: sage: sage: (1e-25).prec()
53
sage: sage: sage: (0.0000000000000000000000001).prec()
53
sage: sage: sage: (00000000.0000000000000000000000001).prec()
53
```



---

Attachment

Looks good to me!  Thank you for making so many changes at my request.


---

Comment by mhansen created at 2007-12-02 01:15:19

This causes the following doctest failures:


```
        sage -t  devel/sage-main/sage/modular/dirichlet.py
        sage -t  devel/sage-main/sage/gsl/dft.py
        sage -t  devel/sage-main/sage/functions/constants.py
        sage -t  devel/sage-main/sage/calculus/calculus.py
        sage -t  devel/sage-main/sage/calculus/wester.py
        sage -t  devel/sage-main/sage/interfaces/gp.py
        sage -t  devel/sage-main/sage/misc/functional.py
        sage -t  devel/sage-main/sage/rings/real_mpfr.pyx
        sage -t  devel/sage-main/sage/rings/fraction_field_element.py
        sage -t  devel/sage-main/sage/rings/rational.pyx
        sage -t  devel/sage-main/sage/rings/arith.py
        sage -t  devel/sage-main/sage/rings/integer.pyx
        sage -t  devel/sage-main/sage/rings/contfrac.py
        sage -t  devel/sage-main/sage/rings/qqbar.py
        sage -t  devel/sage-main/sage/rings/number_field/number_field.py
        sage -t  devel/sage-main/sage/rings/complex_number.pyx
        sage -t  devel/sage-main/sage/rings/complex_interval.pyx
        sage -t  devel/sage-main/sage/rings/polynomial/real_roots.pyx
        sage -t  devel/sage-main/sage/rings/polynomial/polynomial_element.pyx
        sage -t  devel/sage-main/sage/rings/polynomial/complex_roots.py
        sage -t  devel/sage-main/sage/rings/real_mpfi.pyx
```


I will post a patch in a bit fixing this.


---

Comment by cwitty created at 2007-12-02 02:43:26

Excellent!  I read through 962-doctests.patch (yes, I really did), and I only saw one issue: on real_mpfr.pyx line 21, we will need to change:

```
    2147483647.00000         # 32-bit
```

to

```
    2.14748364700000e9       # 32-bit
```



---

Comment by mhansen created at 2007-12-02 02:45:59

The patches should be applied in this order:
1) 962-2.patch
2) 962-doctests.patch


---

Attachment


---

Comment by mabshoff created at 2007-12-02 03:06:22

Merged in 2.8.15.alpha2.


---

Comment by mabshoff created at 2007-12-02 03:06:22

Resolution: fixed

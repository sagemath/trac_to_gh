# Issue 4765: Sage 3.2.2.alpha1: numerical noise in sage/rings/number_field/number_field_morphisms.pyx on OSX 10.4/G5

Issue created by migration from https://trac.sagemath.org/ticket/4765

Original creator: mabshoff

Original creation time: 2008-12-12 03:42:00

Assignee: mabshoff


```
sage -t -long "devel/sage/sage/rings/number_field/number_field_morphisms.pyx"
**********************************************************************
File "/Users/mabshoff/sage-3.2.2.alpha1/devel/sage/sage/rings/number_field/number_field_morphisms.pyx", line 214, in __main__.example_10
Failed example:
    matching_root(x**Integer(3)-Integer(1), CDF.gen(0))###line 227:_sage_    >>> matching_root(x^3-1, CDF.0)
Expected:
    -0.500000000000000 + 0.86602540378443...*I
Got:
    -0.500000000000001 + 0.866025403784439*I
**********************************************************************
```



---

Comment by mabshoff created at 2008-12-12 03:42:11

Changing status from new to assigned.


---

Attachment


---

Comment by mhansen created at 2008-12-12 13:55:11

Looks good to me.


---

Comment by mabshoff created at 2008-12-12 14:44:24

Merged in Sage 3.2.2.alpha2


---

Comment by mabshoff created at 2008-12-12 14:44:24

Resolution: fixed

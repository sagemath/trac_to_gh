# Issue 5521: fix serious bug in pickling the rational numbers and the magma interface

Issue created by migration from Trac.

Original creator: was

Original creation time: 2009-03-14 22:39:00

Assignee: malb

After converting QQ to Magma it suddenly stops pickling!


```
wstein`@`sage:~$ sage
----------------------------------------------------------------------
----------------------------------------------------------------------
sage: loads(dumps(QQ))
Rational Field
sage: magma(QQ)
Rational Field
sage: loads(dumps(QQ))
---------------------------------------------------------------------------
RuntimeError                              Traceback (most recent call last)
| Sage Version 3.4, Release Date: 2009-03-11                         |
| Type notebook() for the GUI, and license() for information.        |
/scratch/wstein/sage/temp/sage.math.washington.edu/13063/_scratch_wstein_sage_init_sage_0.py in <module>()

/home/wstein/sage/local/lib/python2.5/site-packages/sage/structure/sage_object.so in sage.structure.sage_object.loads (sage/structure/sage_object.c:6159)()

RuntimeError: (TypeError(RuntimeError('Error evaluating Magma code.\nIN:_sage_[3]:=Rational Field;\nOUT:\n>> _sage_[3]:=Rational Field;\n                       ^\nUser error: bad syntax',),), <function reduce_load at 0x11318c0>, (Magma, 'Rational Field'))
invalid data stream
invalid load key, 'x'.
Unable to load pickled data.
```



---

Attachment

This patch causes 20 doctests to fail in extended_rational_field.py starting with:

```
sage -t -long "devel/sage/sage/rings/extended_rational_field.py"
**********************************************************************
File "/scratch/mabshoff/sage-3.4.1.alpha0/devel/sage/sage/rings/extended_rational_field.py", line 51:
    sage: loads(dumps(f))
Expected:
    Natural morphism:
      From: Rational Field
      To:   Extended Rational Field
Got:
    Natural endomorphism of Rational Field
**********************************************************************
File "/scratch/mabshoff/sage-3.4.1.alpha0/devel/sage/sage/rings/extended_rational_field.py", line 110:
    sage: E == loads(dumps(E))
Expected:
    True
Got:
    False
**********************************************************************
<SNIP>
```



---

Comment by mabshoff created at 2009-03-31 08:45:10

This has been fixed via the patch at #5520.

Cheers,

Michael


---

Comment by mabshoff created at 2009-03-31 08:45:10

Resolution: fixed

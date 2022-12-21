# Issue 5630: improve doctest coverage for schemes/generic/spec.py

Issue created by migration from Trac.

Original creator: AlexGhitza

Original creation time: 2009-03-29 04:55:42

Assignee: was

Keywords: spec doctest latex

The attached patch adds a `_latex_()` method for Spec's of rings and improves the doctest coverage of `spec.py` from 42% (3 of 7) to 75% (6 of 8).

The two remaining methods are currently involved in other tickets that will also take care of adding doctests: see #5629 for `dimension()` and #5479 for `__call__()`



---

Comment by AlexGhitza created at 2009-03-29 08:16:56

Changing assignee from was to AlexGhitza.


---

Comment by AlexGhitza created at 2009-03-29 08:17:04

Changing status from new to assigned.


---

Comment by was created at 2009-03-29 17:12:07

This doctest fails for me on 32-bit OS X:

```
teragon:sage-3.4 wstein$ sage -t devel/sage/sage/schemes/generic/spec.py 
sage -t  "devel/sage/sage/schemes/generic/spec.py"          
**********************************************************************
File "/Users/wstein/build/sage-3.4/devel/sage/sage/schemes/generic/spec.py", line 116:
    sage: Spec(QQ) < 5
Expected:
    True
Got:
    False
```


Since the result is meaningless, you could flag it 

```
sage:  spec(QQ) < 5   # random -- platform dependent
```


or instead have a test

```
sage: spec(QQ) == 5
False
```


If you fix this one issue, then this will get "positive review" from me.


---

Attachment

Ah, I had misinterpreted the existing docstring for `_cmp_`.  I removed the offending doctest (the one with `Spec(QQ) == 5` is already there) and clarified the docstring a little bit.

New patch is up replacing the old one.


---

Comment by mabshoff created at 2009-03-31 06:41:31

Merged in Sage 3.4.1.rc0.

Cheers,

Michael


---

Comment by mabshoff created at 2009-03-31 06:41:31

Resolution: fixed

# Issue 3654: [with patch, needs review] Deprecation warning function

Issue created by migration from Trac.

Original creator: jason

Original creation time: 2008-07-14 15:27:47

Assignee: cwitty

This function introduces a "deprecation" function that sounds a warning when a user calls a function that has been deprecated.  It uses the standard Python mechanism for this sort of thing.


---

Comment by mabshoff created at 2008-07-15 01:53:23

IIRC warn prints to stderr, so we are not catching the output. This seems similar to Burcin's code:

```
def MPolynomialRing(*args, **kwds):
    import warnings
    warnings.warn("MPolynomialRing is deprecated, use PolynomialRing instead!", DeprecationWarning, stacklevel=2)
    return PolynomialRing(*args, **kwds)
```

The above should certainly use some more generic infrastructure like the one provided by Jason's patch.

Cheers,

Michael


---

Attachment


---

Comment by jason created at 2008-08-25 20:36:17

patch updated to fix all doctest errors and make this functionality used.


---

Comment by mabshoff created at 2008-08-25 21:49:35


```
[2:44pm] mabshoff: mhansen: how do you like #3654?
[2:44pm] mabshoff: I think I will merge it 
[2:45pm] mhansen: Yep -- looks good.
[2:45pm] mabshoff: I agree. Nice work jason-
[2:45pm] jason-: yeah!
```


Positive review from me and the gang.

Cheers,

Michael


---

Comment by mabshoff created at 2008-08-25 22:07:51

Merged in Sage 3.1.2.alpha1


---

Comment by mabshoff created at 2008-08-25 22:07:51

Resolution: fixed

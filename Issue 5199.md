# Issue 5199: [with patch, needs review] new symbolics can treat floats as integers inappropriately

Issue created by migration from Trac.

Original creator: cwitty

Original creation time: 2009-02-07 05:15:40

Assignee: burcin

CC:  burcin

Consider the following, in 3.3.alpha5:

```
sage: from sage.symbolic.ring import NSR
sage: NSR(10.0).gamma()
362880
```

We have produced an exact integral result of .gamma() on a floating-point number.

After #2898, this behavior makes doctests fail; but the above happens even before #2898.

I don't know if this is the "right" patch, but it does make all doctests pass after #2898.


---

Attachment

The patch looks good. 

We might think about optimizing this function for speed later. Specialcasing Integer and Rational, and using the _parent attribute should help here.


---

Comment by mabshoff created at 2009-02-09 07:53:59

Merged in Sage 3.3.rc0.

Cheers,

Michael


---

Comment by mabshoff created at 2009-02-09 07:53:59

Resolution: fixed

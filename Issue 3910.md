# Issue 3910: [with patch,  needs review] adjust interval printing: precise integers print as integers

Issue created by migration from https://trac.sagemath.org/ticket/3910

Original creator: cwitty

Original creation time: 2008-08-20 14:22:59

Assignee: somebody

This patch adjusts interval printing so that sufficiently small precise integers print as integers.  (It also fixes a loss-of-precision bug when one endpoint is tiny and the other endpoint is zero.)

Before:

```
sage: RIF(0)
0.?e-17
sage: RIF(1)
1.0000000000000000?
sage: RIF(0, 2^-256)
1.?e-17
```


After:

```
sage: RIF(0)
0
sage: RIF(1)
1
sage: RIF(0, 2^-256)
1.?e-77
```




---

Attachment


---

Comment by cremona created at 2008-08-23 20:47:21

The design decision behind this was well aired on sage-devel and I seem to remember the consensus was for this change.

The patch (a lot of which consists in changing the doctest outputs) looks fine, applies cleanly to 3.1.1 and passes all doctests in sage/rings and sage/calculus.  I did not check the docs.

I recommend that this passes.


---

Comment by mabshoff created at 2008-08-25 01:43:02

Merged in Sage 3.1.2.alpha1. All doctests pass with the patch applied.

Cheers,

Michael


---

Comment by mabshoff created at 2008-08-25 01:43:02

Resolution: fixed

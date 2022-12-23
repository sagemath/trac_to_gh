# Issue 6751: implement ternary quadratic forms associated to orders in rational quaternion algebras

Issue created by migration from https://trac.sagemath.org/ticket/6751

Original creator: was

Original creation time: 2009-08-15 01:18:30

Assignee: tbd

This patch could possibly depend on #6745.

The goal of this patch is to implement computation of the ternary quadratic form associated to an order in a rational quaternion algebra.  These are useful, e.g, in computing with Heegner points, in decided whether quaternion orders have embeddings from orders in quadratic imaginary fields, and in computing elements of the Kohnen + subspace of modular forms of weight 3/2. 


---

Attachment


---

Comment by cremona created at 2009-08-23 16:07:51

Apply after previous


---

Attachment

Looks good to me:  applies fine to 4.1.1, tests pass, some examples I tried looked correct (as does the code).

There's one small typo ("had" for "has" in the docstring) which I put into a second patch (overkill perhaps!)


---

Comment by mvngu created at 2009-08-30 09:29:13

Merged both patches. The patch `trac_6751.patch` applies OK, but with fuzz:

```
[mvngu@sage sage-main]$ hg qimport http://trac.sagemath.org/sage_trac/raw-attachment/ticket/6751/trac_6751.patch && hg qpush
adding trac_6751.patch to series file
applying trac_6751.patch
patching file sage/algebras/quatalg/quaternion_algebra_element.pyx
Hunk #1 succeeded at 537 with fuzz 2 (offset -76 lines).
Now at: trac_6751.patch
```



---

Comment by mvngu created at 2009-08-30 09:29:13

Resolution: fixed


---

Comment by mvngu created at 2009-08-30 09:55:33

See #6846 for a follow up to this ticket.

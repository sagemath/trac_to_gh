# Issue 6200: Use mpmath to compute constants

Issue created by migration from Trac.

Original creator: fredrik.johansson

Original creation time: 2009-06-03 20:29:36

Assignee: jkantor

Assumes that mpmath has been added to Sage (#6196)

Patch summary:

Use mpmath to compute numerical values of constants.

Previously khinchin, mertens and twinprime were LimitedPrecisionConstant,
but with this patch they can be computed to any precision.

The patch also adds the Glaisher constant (which is available in mpmath)
and corrects the name of the Mertens constant.


---

Attachment


---

Attachment


---

Comment by mhansen created at 2009-06-19 23:07:33

For backward compatibility, I added merten as an alias to mertens.  Other than that, the patch looks good.


---

Comment by ncalexan created at 2009-06-19 23:18:29

Looks good to me.  Apply both patches.


---

Comment by rlm created at 2009-07-03 16:55:53

Resolution: fixed

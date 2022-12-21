# Issue 2002: creating a fresh new notebook in sage-2.10.1.rc3 is broken

Issue created by migration from Trac.

Original creator: was

Original creation time: 2008-01-31 07:25:06

Assignee: boothby


```
[02:20am] william_stein: the notebook doesn't even work in rc3!!
[02:21am] william_stein: sage: notebook(address="sage.math.washington.edu", port=8389, directory="notebook")
[02:21am] william_stein: ...
[02:21am] william_stein: <type 'exceptions.AttributeError'>: 'Notebook' object has no attribute 'set_prettyprint'
[02:21am] william_stein: This is what happens when making a NEW NOTEBOOK not loading an existing one.
[02:21am] william_stein: I'm glad I caught this!!
[02:21am] william_stein: trac ticket coming up
```





---

Comment by jason created at 2008-01-31 21:00:16

I think the attached fixes the issue, but I'm not sure how to create a new notebook, so I'm not sure how to test it.


---

Comment by jason created at 2008-01-31 21:00:58

(which probably explains why this was never tested when submitting the original patch.  sorry!)


---

Attachment


---

Comment by jason created at 2008-01-31 21:10:29

The attached patch also standardizes on "pretty_print" instead of "prettyprint".  The previous code had a mixture of the two spellings.


---

Comment by mabshoff created at 2008-02-01 05:56:05

The issue has been solved, but I do believe that somebody else ought to double check this.

Cheers,

Michael


---

Comment by jkantor created at 2008-02-01 06:00:53

The issue appears to have been solved to me as well.


---

Comment by mabshoff created at 2008-02-01 06:02:19

Merged in Sage 2.10.1.rc4


---

Comment by mabshoff created at 2008-02-01 06:02:19

Resolution: fixed

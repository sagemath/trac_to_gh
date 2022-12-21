# Issue 1162: [with patch] fix issues in RealField <-> RQDF conversions

Issue created by migration from Trac.

Original creator: zimmerma

Original creation time: 2007-11-13 00:04:53

Assignee: jkantor




---

Attachment


---

Comment by cwitty created at 2007-11-15 03:10:25

The first chunk of the patch (patching polynomial_element.pyx) makes doctesting polynomial_element.pyx fail for me (on 32-bit x86 Linux).  (Plus, the first chunk seems unrelated to the other chunks, and to the bug report.  Maybe it was included by accident?)

The other two chunks look good to me.


---

Comment by zimmerma created at 2007-11-22 08:01:06

Yes the first chunk was included by accident and is unrelated. About this first chunk, I do not understand why
roots() gives different results on different architectures. It shouldn't if mpfr is used inside.


---

Attachment


---

Comment by cwitty created at 2007-12-02 00:03:46

I've added my own patch for these issues.  It's based on Paul Zimmerman's patch (and includes the two chunks that I said "look good", above); but it also fixes issues with converting to complex, and adds some more doctests.


---

Comment by was created at 2007-12-15 11:32:13


```
was-1162: #1162 is ready.
[03:27am] was-1162: But it is hard to apply.
[03:27am] mabshoff: ok
[03:27am] was-1162: Basically apply each patch, ignore all the failed hunks.
[03:28am] mabshoff: arrg.
[03:28am] mabshoff: will do.
[03:28am] was-1162: then go into real_mpfr.pyx and manually delete
[03:28am] was-1162: 658        elif hasattr(x, '_mpfr_'):
[03:28am] was-1162: 659            return x._mpfr_(self)
[03:28am] was-1162: It's scary--
[03:28am] mabshoff: +1
[03:28am] was-1162: but *all* that is being done is that the rounding mode is being changed from Z to N in one place.
[03:28am] was-1162: and some doctests are being changed to reflect this.
[03:28am] mabshoff: ok
```



---

Comment by mabshoff created at 2007-12-15 11:45:28

Merged in 2.9.rc0.


---

Comment by mabshoff created at 2007-12-15 11:45:28

Resolution: fixed

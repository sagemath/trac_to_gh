# Issue 6668: Allow doctesting of .tex, .rst. .sage files outside the devel tree

Issue created by migration from https://trac.sagemath.org/ticket/6668

Original creator: fwclarke

Original creation time: 2009-08-03 19:06:43

Assignee: tbd

Keywords: sage-doctest

Since 3.4.1 it has not been possible to doctest .tex, .rst or .sage files which were not in the SAGE_ROOT/devel tree.  The patch (for the scripts repository) fixes this, and a few other things are tidied up.



---

Comment by fwclarke created at 2009-08-03 19:08:07

apply to scripts repository in sage-4.1.1.rc0


---

Attachment


---

Comment by fwclarke created at 2009-09-05 22:50:36

A new patch to has been attached to #6861 which includes the changes proposed here as well as others addressing related issues.  If that is postively reviewed, then this ticket can be closed.


---

Comment by fwclarke created at 2009-09-24 19:59:47

This ticket could now be closed, since the proposed changes have been incorporated in #6861.


---

Comment by mhansen created at 2009-10-23 16:05:59

Resolution: fixed

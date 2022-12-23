# Issue 6957: $SAGE_DATA/extcode/javascript/jsmath appears to be the same as $SAGE_LOCAL/notebook/javascript/jsmath

Issue created by migration from https://trac.sagemath.org/ticket/6957

Original creator: pcpa

Original creation time: 2009-09-18 23:10:48

Assignee: mabshoff

This appears to be a duplicate directory tree.

The other places where there are javascript files appear to not share any files.

I just tried moving $SAGE_DATA/extcode/javascript/jsmath from a sage 4.1.1 binary downloaded from a mirror, and the notebook appears to runs just fine.

If this is really a duplicate, it can reduce a sage install by around 18Mb.



---

Comment by jdemeyer created at 2013-05-16 07:55:30

Resolution: worksforme


---

Comment by jdemeyer created at 2013-05-16 07:55:30

Fixed already.

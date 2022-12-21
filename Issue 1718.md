# Issue 1718: bug in parametric_plot

Issue created by migration from Trac.

Original creator: wdj

Original creation time: 2008-01-07 22:34:39

Assignee: was

sage: parametric_plot([t, t + RR(pi)], -2, 2, rgbcolor=(1,0,0))

works but not this:

sage: parametric_plot([t, t + pi], -2, 2, rgbcolor=(1,0,0))
---------------------------------------------------------------------------
<type 'exceptions.AttributeError'>        Traceback (most recent call last)

....

<type 'exceptions.AttributeError'>: 'Pi' object has no attribute
'number_of_arguments'


---

Attachment


---

Comment by mabshoff created at 2008-01-21 02:38:22

Looks good to me.

Cheers,

Michael


---

Comment by mabshoff created at 2008-01-21 02:39:49

Merged in Sage 2.10.1.alpha1


---

Comment by mabshoff created at 2008-01-21 05:26:27

Merged in Sage 2.10.1.alpha1 - and this time I closed the ticket, too.


---

Comment by mabshoff created at 2008-01-21 05:26:27

Resolution: fixed

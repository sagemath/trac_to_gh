# Issue 5071: [with patch, needs review] unit of least precision for RR and RDF

Issue created by migration from https://trac.sagemath.org/ticket/5071

Original creator: robertwb

Original creation time: 2009-01-23 12:23:50

Assignee: somebody

I wrote this while attacking #4746. Didn't turn out to be relevant to that, but it's useful to have on its own anyways. 


---

Comment by roed created at 2009-01-24 09:49:48

Looks good.  The only change I would suggest is that the docstring should include the behavior on inf and NaN.


---

Attachment


---

Comment by robertwb created at 2009-01-28 00:07:11

OK, doctests updated.


---

Comment by cwitty created at 2009-02-05 06:55:51

Code looks good, doctests pass.

Excellent idea!

Positive review.


---

Comment by mabshoff created at 2009-02-07 01:38:34

Resolution: fixed


---

Comment by mabshoff created at 2009-02-07 01:38:34

Merged in Sage 3.3.alpha6.

Cheers,

Michael

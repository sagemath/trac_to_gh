# Issue 5593: [with patch; needs review or throwing away] CremonaDB.conductor_range does not give a Python style range

Issue created by migration from https://trac.sagemath.org/ticket/5593

Original creator: nbruin

Original creation time: 2009-03-23 19:02:14

Assignee: nbruin

CremonaDB().conductor_range() gives an inclusive upper bound, so that
srange(*CremonaDB().conductor_range()) may miss a conductor.

Fix attached


---

Comment by nbruin created at 2009-03-23 19:03:11

Patch


---

Attachment

Yes, this looks like the right thing to do.


---

Comment by cremona created at 2009-03-23 20:07:46

Looks good to me too.


---

Comment by mabshoff created at 2009-03-23 21:17:10

Merged in Sage 3.4.1.alpha0.

Cheers,

Michael


---

Comment by mabshoff created at 2009-03-23 21:17:10

Resolution: fixed

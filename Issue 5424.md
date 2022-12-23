# Issue 5424: Move infinity to new coercion model

Issue created by migration from https://trac.sagemath.org/ticket/5424

Original creator: robertwb

Original creation time: 2009-03-03 09:23:25

Assignee: robertwb




---

Comment by robertwb created at 2009-03-03 13:15:46

Plus got coverage from 9% to 100%


---

Attachment


---

Attachment

I've attached trac_5424.patch which is the original patch rebased against 3.4.rc1 (and converted  use Sphinx syntax).


---

Comment by roed created at 2009-03-18 08:39:56

Looks good.  Thanks for cleaning up my old code.  :-/

The only problem I saw was that the doctest on line 449 was a bit strange (though not technically wrong).


---

Comment by robertwb created at 2009-03-18 19:25:25

Thanks for the review. The docstring on line 449 is to test uniqueness, and seemed like the only logical thing to test for that function anyways.


---

Comment by mabshoff created at 2009-03-20 21:05:09

Resolution: fixed


---

Comment by mabshoff created at 2009-03-20 21:05:09

Merged in Sage 3.4.1.alpha0.

Cheers,

Michael

# Issue 3657: [with patch against 3.0.5, needs review] Documentation for latin squares, DLXCPP; minor fixes

Issue created by migration from Trac.

Original creator: carlohamalainen

Original creation time: 2008-07-15 11:59:28

Assignee: mhansen

CC:  sage-combinat

Fixed some LaTeX problems so that the docs from latin.py would compile properly, also fixed some minor things.


---

Attachment


---

Attachment

Carlo,

I have nuked the bundles. Not knowing the subject at hand I will not comment on chlatin.patch, but chlatindocs.patch looks good. The first hunk in the last patch will be removed when applying it, so don't worry about that for now.

Mike: Can you be the editor for this?

Cheers,

Michael


---

Comment by mhansen created at 2008-07-15 23:35:17

Changing keywords from "" to "editor_mhansen".


---

Comment by mhansen created at 2008-07-16 02:39:56

With the exception of patchlevel.tex as Michael noted, everything else looks good to me.  The sage-main tests applies and passes tests, and the documentation builds with both patches applied.


---

Comment by mabshoff created at 2008-07-16 03:26:52

Merged in Sage 3.0.6.alpha0


---

Comment by mabshoff created at 2008-07-16 03:26:52

Resolution: fixed

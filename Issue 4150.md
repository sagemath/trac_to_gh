# Issue 4150: [with patch, needs review and testing] migrate graphs to new refinement code

Issue created by migration from Trac.

Original creator: rlm

Original creation time: 2008-09-19 07:42:32

Assignee: rlm

CC:  jason

This moves the automorphism group and isomorphism functions for graphs over to the new framework. It should be tested on a few different architectures before getting merged.


---

Attachment


---

Comment by rlm created at 2008-09-19 07:47:19

Dependends on #4115, if you're applying to 3.1.2.final


---

Comment by mhansen created at 2008-09-19 08:11:25

Positive review for Robert's part.  He just needs to sign off on my small second patch.


---

Comment by rlm created at 2008-09-19 08:12:34

+1


---

Comment by mhansen created at 2008-09-19 08:16:18

Note that the second patch depends on #4139 being applied.


---

Comment by mabshoff created at 2008-09-19 14:50:40

The first hunk from trac_4150-fixes.patch ought to be deleted since I ended up fixing that doctest failure at #4139.

Cheers,

Michael


---

Attachment

Patch fixed.


---

Comment by mabshoff created at 2008-09-19 23:52:54

Thanks, valgrinds clean and also works on Itanium with Python build with `-fwrapv`, which caused trouble with the old codebase, so what could go wrong :)

Cheers,

Michael


---

Comment by mabshoff created at 2008-09-19 23:55:39

Resolution: fixed


---

Comment by mabshoff created at 2008-09-19 23:55:39

Merged both patches in Sage 3.1.3.alpha0

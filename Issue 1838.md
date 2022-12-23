# Issue 1838: [with patch] comma in latex lists need a trailing space

Issue created by migration from https://trac.sagemath.org/ticket/1838

Original creator: schilly

Original creation time: 2008-01-18 21:45:02

Assignee: cwitty

normally, after writing a "," follows a space. latex needs this explicitly as "\,"


---

Attachment


---

Comment by ncalexan created at 2008-01-22 18:10:32

This seems strange -- I never use explicit spaces ("\,") in latex, preferring the system to do the layout as it sees best.  Is this really necessary?

Also, I can't believe this doesn't touch lots of doctests throughout the system.  It also has no doctests.


---

Comment by schilly created at 2008-01-22 20:57:09

well, i just thought this could be an easy fix without dependencies. i don't know where the doctests for latex expressions are, i have to look at them.

latex doesn't do it the right way. it just does what it is told to do but has no intelligence and white space is ignored inside formulas. that's why packages like amsmath redefine a lot, or introduce new commands for rather normal things (dots, triple integrals, ...). they all do a lot of "intelligent" white space management. an also well known example are matrices, where it defines the pmatrix environment. there all the spacings are corrected with negative spaces. or you need a "\;" after the inner part before the "dx" when you type an integral. 

so, you have to do something but it's not crucial. trusting latex doesn't do the job.


---

Comment by robertwb created at 2008-01-23 04:00:09

I don't think the "right way" is well defined--without the explicit space there is a bit more space after a comma than before, but just barely, and I think it looks fine. 

Unless things look really bad, I think we should error on the side of producing the cleanest, simplest latex--as something to avoid just look at the state of auto-generated HTML that tries to be faithful to a given WYSIWYG editor.


---

Comment by cwitty created at 2008-01-29 00:02:22

I don't think we want this patch at all.  While LaTeX does sometimes need some help with spacing, I've never heard of this being one of the problem cases.  Since Nick, Robert, and I agree (I think), I'm closing this bug as invalid for now.

Feel free to reopen it if you get some more support for your position (like an example that looks a lot better with the spacing than without, or a style guide that requires the spacing).


---

Comment by cwitty created at 2008-01-29 00:02:22

Resolution: invalid

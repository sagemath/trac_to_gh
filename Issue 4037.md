# Issue 4037: [with trivial patch, needs review] list_of_first_n() broken in interact.py

Issue created by migration from https://trac.sagemath.org/ticket/4037

Original creator: AlexGhitza

Original creation time: 2008-09-02 04:37:21

Assignee: AlexGhitza

In server/notebook/interact.py, the function list_of_first_n() claims to return n elements, but it returns n+1 of them.  The attached trivial patch fixes the function and the doctests.



---

Attachment

Ok, a simple out-by-one bug.  Patch applies cleanly to 3.1.2.alpha3 and doctests in sage.server.notebook all pass.

OK by me, though I usually steer clear of notebook patches as I rarely use the notebook!


---

Comment by mabshoff created at 2008-09-02 09:36:30

Resolution: fixed


---

Comment by mabshoff created at 2008-09-02 09:36:30

Merged in Sage 3.1.2.alpha4

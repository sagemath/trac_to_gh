# Issue 5207: remove unnecessary use of symbolics in doctests in weierstrass_morphism.py

Issue created by migration from https://trac.sagemath.org/ticket/5207

Original creator: AlexGhitza

Original creation time: 2009-02-08 13:11:37

Assignee: was

CC:  cremona

As discussed at

http://groups.google.com/group/sage-devel/browse_thread/thread/48b893e904634273

there are two doctests in weierstrass_morphism.py that use symbolic variables.  This is slow, completely unnecessary, and causes trouble given that Maxima has a tendency to hang.



---

Attachment

As suggested by John Cremona, the attached patch replaces the use of symbolic variables by variables in a polynomial ring over QQ.


---

Comment by cremona created at 2009-02-08 14:52:16

Thanks, Alex.  Patch applies fine to 3.3.alpha5 and tests pass, so positive review (unsurprisingly!).

Note that this only affects docstrings/tests so cannot affect anything else.


---

Comment by mabshoff created at 2009-02-09 07:54:15

Resolution: fixed


---

Comment by mabshoff created at 2009-02-09 07:54:15

Merged in Sage 3.3.rc0.

Cheers,

Michael

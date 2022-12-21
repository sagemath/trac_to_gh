# Issue 5282: In %python mode in the notebook, tracebacks are not properly reported

Issue created by migration from Trac.

Original creator: wasI

Original creation time: 2009-02-16 06:29:42

Assignee: was




---

Comment by was created at 2009-02-16 07:00:07

OK, I'm posting a patch that fixes this problem.  I improved syseval by getting rid of the weird hack of it just raising an exception when the system doesn't provide the interface it should.  This meant fixing many of the interfaces, which had evals that didn't work if a locals var was passed in.  I think this improved the quality of those interfaces as well, since many had customized eval methods that didn't properly pass extra options up to the base class, but now do.


---

Attachment


---

Comment by mabshoff created at 2009-02-16 08:15:54

Positive review and nice cleanup.

Cheers,

Michael


---

Comment by mabshoff created at 2009-02-16 08:22:30

Merged in Sage 3.3.rc1.

Cheers,

Michael


---

Comment by mabshoff created at 2009-02-16 08:22:30

Resolution: fixed


---

Comment by certik created at 2009-02-16 13:57:02

Nice patch, thanks!

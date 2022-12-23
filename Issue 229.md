# Issue 229: make it so all objects pickled now can be loaded in all future versions of SAGE

Issue created by migration from https://trac.sagemath.org/ticket/229

Original creator: was

Original creation time: 2007-01-29 19:03:53

Assignee: was

PLAN


Make it so pickled objects can always be reloaded. To do this, ever single class *must* have a couple example pickled objects, and the doctest has to simply load them and make sure it works.   Make this a requirement for all SAGE classes (!).


---

Comment by mabshoff created at 2008-08-02 03:04:38

Resolution: fixed


---

Comment by mabshoff created at 2008-08-02 03:04:38

This ticket has been resolved by the "pickle jar".

Cheers,

Michael

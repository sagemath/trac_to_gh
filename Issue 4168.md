# Issue 4168: native mpfr polynomials

Issue created by migration from Trac.

Original creator: robertwb

Original creation time: 2008-09-22 17:59:42

Assignee: tbd

#4151 implements these, should be used by default for RR['x']


---

Comment by mabshoff created at 2008-10-26 03:35:47

Hi Robert,

what is the plan here?

Cheers,

Michael


---

Comment by robertwb created at 2008-10-27 16:32:24

Well, this is pretty low-hanging fruit, but I've just got too many things higher on my priority list (sage and otherwise). 

If no one else gets around to this, eventually I will. The code is there, it's just a matter of hooking it up and making sure it still works everywhere (and there might be some numerical noise as it handles polynomial multiplication in a more numerically stable way).


---

Attachment

OK, I did this yesterday during bug days. Ran all tests and fixed a bit of numerical noise this morning.


---

Comment by mhansen created at 2008-11-21 15:27:14

Looks good and passes tests.


---

Comment by mabshoff created at 2008-11-21 20:19:41

Resolution: fixed


---

Comment by mabshoff created at 2008-11-21 20:19:41

Merged in Sage 3.2.1.alpha0

# Issue 1795: [with-patch] Adds support for cdef'd and cpdef'd functions to sage-coverage

Issue created by migration from Trac.

Original creator: roed

Original creation time: 2008-01-16 18:06:01

Assignee: roed

CC:  jason

The previous version of sage-coverage did not check cdef'd functions, and it incorrectly claimed that cpdef'd functions did not have doctests.  This patch fixes that problem.


---

Attachment

Adds cdef, cpdef support to sage-coverage


---

Comment by was created at 2008-01-16 18:10:04

At a quick glance it looks good.  Also I agree with the design decisions.  Does it work when run on all our codebase?


---

Comment by roed created at 2008-01-16 19:27:57

A minor fix to how Python classes are printed


---

Attachment

It gives reasonable output on sage -coverageall and gives reasonable output on a few selected files (integer.pyx, padic_capped_relative_element.pyx, graph.py).


---

Comment by mhansen created at 2008-09-19 07:15:35

Changing status from new to assigned.


---

Comment by mhansen created at 2008-09-19 07:15:35

Changing assignee from roed to mhansen.


---

Comment by robertwb created at 2008-10-19 05:41:51

This no longer applies cleanly (against, e.g. 3.1.3)


---

Comment by mabshoff created at 2009-04-18 04:15:54

Ok, we should get this rebased. I think that since we do not test cdef-ed functions those should not be accounted for.

Thoughts?

Cheers,

Michael


---

Comment by mabshoff created at 2009-04-18 04:17:58

Fix the summary so it is picked up by the right reports.

Cheers,

Michael


---

Comment by jdemeyer created at 2013-03-07 08:16:45

The question I would like to see answered is: _should_ we check `cdef` functions? We already check `cpdef` functions.

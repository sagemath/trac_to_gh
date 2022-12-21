# Issue 2102: add pull/incoming/outgoing wrappers to HG objects (like hg_sage)

Issue created by migration from Trac.

Original creator: mhansen

Original creation time: 2008-02-08 07:14:11

Assignee: mabshoff

CC:  jdemeyer




---

Comment by jason created at 2008-02-08 13:51:48

Also add the queue functions, like qinit, qnew, qrefresh, etc.


---

Comment by ncalexan created at 2008-02-09 03:45:34

The `push` command is implemented in a patch attached to a different ticket, http://trac.sagemath.org/sage_trac/ticket/1371.  William and I would like that ticket applied.

The other items are valid.


---

Comment by ncalexan created at 2008-02-09 03:45:34

Changing type from defect to enhancement.


---

Comment by mhansen created at 2012-03-28 23:22:05

This ticket can be closed not since all of these things are already implemented as of Sage 4.8.  See #11142 and changsets cbf23a4344e8dbd2321502b98974860c2947ef42 and 16ce7802b5aa2bcd43548973abb04614d62c2396 for these.


---

Comment by jdemeyer created at 2012-03-29 06:24:23

Changing status from new to needs_review.


---

Comment by jdemeyer created at 2012-03-29 06:24:33

Changing status from needs_review to positive_review.


---

Comment by jdemeyer created at 2012-04-04 13:26:04

Resolution: duplicate

# Issue 2140: [with bundle, needs review] enhance search_src and add search_def for easier source navigating.

Issue created by migration from https://trac.sagemath.org/ticket/2140

Original creator: ncalexan

Original creation time: 2008-02-11 07:30:03

Assignee: ncalexan

CC:  ncalexander@gmail.com

Keywords: sage search_src search_def source search grep

The attached bundle does two things.
 * makes `search_src` accept more extra arguments
 * adds `search_def` to find the definition of a name in the Sage library.

The ugly patch is the result of a Python 2.6 bug.

This was all motivated by Craig Citro's post to `sage-devel` at http://groups.google.com/group/sage-devel/msg/82829f101a6e209b.


---

Attachment


---

Comment by craigcitro created at 2008-02-11 07:57:01

Changing component from algebraic geometry to user interface.


---

Comment by craigcitro created at 2008-02-11 07:57:01

I definitely like the patch. Apparently Nick was channeling Tony the Tiger, though, because the "library" became "librrary" twice. The extra patch fixes that typo in two places.


---

Attachment


---

Comment by mabshoff created at 2008-02-13 08:05:54

Merged in Sage 2.10.2.alpha0


---

Comment by mabshoff created at 2008-02-13 08:05:54

Resolution: fixed

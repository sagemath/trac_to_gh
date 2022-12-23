# Issue 2042: [with patch, needs review] change is_simplified to has_been_simplified in calculus.py

Issue created by migration from https://trac.sagemath.org/ticket/2042

Original creator: AlexGhitza

Original creation time: 2008-02-04 00:39:37

Assignee: AlexGhitza

See
http://groups.google.com/group/sage-devel/browse_thread/thread/e342c0b1020de8bc

The point of is_simplified() is to keep track of whether the expression has already been simplified, rather than to check whether the expression is simplified.  The attached patch changes the name to has_been_simplified and adds a doctest.




---

Attachment


---

Comment by AlexGhitza created at 2008-02-07 04:42:21

William's patches in #2073 already fix this and much much more.  So close this ticket (as duplicate, I guess) as soon as #2073 gets closed.


---

Comment by AlexGhitza created at 2008-02-07 17:44:39

Resolution: duplicate

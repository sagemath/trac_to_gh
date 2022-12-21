# Issue 5449: Implement @cache_method with cache stored in the parent

Issue created by migration from Trac.

Original creator: nthiery

Original creation time: 2009-03-06 15:57:38

Assignee: nthiery

CC:  sage-combinat

When the elements of a parent do not have unique representation, it can be desirable to store the cache of (some of) the methods in the parent rather than in the element.

Comments, suggestions?

`@`cached_in_parent_method ?

I'll write a quick patch in sage-combinat


---

Comment by nthiery created at 2009-05-02 00:41:31

Changing keywords from "" to "cached_method, cache".


---

Attachment


---

Comment by roed created at 2009-05-12 13:38:08

Passes doctests, good documentation.


---

Comment by nthiery created at 2009-05-19 06:24:04

Changing status from new to assigned.


---

Comment by mabshoff created at 2009-05-22 13:57:14

Merged in Sage 4.0.rc1.

Cheers,

Michael


---

Comment by mabshoff created at 2009-05-22 13:57:14

Resolution: fixed

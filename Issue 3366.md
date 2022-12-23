# Issue 3366: improve subs/subsitute inheritance

Issue created by migration from https://trac.sagemath.org/ticket/3366

Original creator: malb

Original creation time: 2008-06-04 20:39:40

Assignee: somebody

CC:  jbmohler

jbmohler wrote at #1440:
"""
subs has been overridden in a few different classes and the overridden implementation is not quite as robust as (or duplicates code from) the implementation in the element base class. I think that the base implementation/architecture should be strengthened in ways that make these overrides unneeded. Of course, then the subs/substitute synonym should entirely be handled by the base class making it impossible for the inconsistency of the noted bug. 
"""


---

Comment by gfurnish created at 2008-06-09 06:36:03

I don't understand the complaint; the entire point of subs is that you can subs override for different for things in different parents (such as calculus).  This is vague, can you give some concrete examples of things we can fix?


---

Comment by AlexGhitza created at 2009-01-22 18:17:36

Changing type from defect to enhancement.


---

Comment by malb created at 2014-06-25 00:47:36

Let's just close this ticket.


---

Comment by rws created at 2015-02-01 16:08:02

Agreed.


---

Comment by rws created at 2015-02-01 16:08:02

Changing status from new to needs_review.


---

Comment by rws created at 2015-02-01 16:08:16

Changing status from needs_review to positive_review.


---

Comment by vbraun created at 2015-02-08 15:30:07

Resolution: invalid

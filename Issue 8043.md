# Issue 8043: #7544 breaks #7355: "sage -i foo" does not automatically find the version number

Issue created by migration from Trac.

Original creator: ddrake

Original creation time: 2010-01-23 05:54:41

Assignee: tbd

As detailed at comment:4:ticket:7544, the functionality introduced in #7355 was broken by #7544.


---

Comment by jhpalmieri created at 2010-04-10 18:58:17

Changing status from new to needs_review.


---

Comment by jhpalmieri created at 2010-04-10 18:58:17

Here's a patch.  See #8669 for a somewhat related ticket.


---

Attachment

scripts repo


---

Comment by ddrake created at 2010-04-12 06:28:47

Changing status from needs_review to positive_review.


---

Comment by ddrake created at 2010-04-12 06:28:47

This fixes the problem, and does so in a simple, POSIX-compliant way. Positive review.


---

Comment by jhpalmieri created at 2010-04-23 19:10:20

Resolution: fixed


---

Comment by jhpalmieri created at 2010-04-23 19:10:20

Merged in 4.4.alpha2.

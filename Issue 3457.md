# Issue 3457: Install sqlalchemy_migrate

Issue created by migration from https://trac.sagemath.org/ticket/3457

Original creator: boothby

Original creation time: 2008-06-18 01:30:18

Assignee: cwitty

Keywords: database

We need this for #3456 and #2318

http://code.google.com/p/sqlalchemy-migrate/

it provides tools to migrate databases / tables between versions.


---

Comment by AlexGhitza created at 2009-01-23 02:46:48

Changing type from defect to enhancement.


---

Comment by boothby created at 2009-01-23 09:04:05

What idiot marked this as a blocker?


---

Comment by boothby created at 2009-01-23 09:04:05

Changing priority from blocker to trivial.


---

Comment by kcrisman created at 2015-01-06 15:19:10

Nice idea, but since #15593 suggests we will remove sqlalchemy and since we have never actually used sqlalchemy _anywhere_ in Sage _and_ since it's available with `pip`, this is (currently) invalid and should have a new ticket opened if and when it is _necessary_.


---

Comment by kcrisman created at 2015-01-06 15:19:10

Changing status from new to needs_review.


---

Comment by kcrisman created at 2015-01-06 15:19:15

Changing status from needs_review to positive_review.


---

Comment by vbraun created at 2015-01-13 01:19:50

Resolution: wontfix

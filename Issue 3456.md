# Issue 3456: SQLize the notebook

Issue created by migration from https://trac.sagemath.org/ticket/3456

Original creator: boothby

Original creation time: 2008-06-18 01:25:47

Assignee: boothby

CC:  was

Keywords: notebook database sql

The public notebook is useless as is.  Life will be better with SQL.  This is probably a duplicate, but I couldn't find the original ticket.


---

Attachment

very very pre-pre-alpha!


---

Comment by boothby created at 2008-07-04 07:37:29

The attachment 3456-prelim.patch is a start.  Currently, it makes the notebook unrunnable.  The schema contained in base.py should be taken as a suggestion, and has not been tested.  One big issue that's currently slowing my progress is unfamiliarity with certain unpickling issues.  I'll be able to experimentally verify what will work, but it's taking much more time than expected.  The problem is, every object that's databased through the SQLAlchemy ORM must inherit from Object.  Further, it would be nice to use the [declarative base model](http://www.sqlalchemy.org/docs/05/ormtutorial.html#datamapping_declarative).  I'm not sure what happens when one unpickles an instance of a class which has changed to inherit from something else, etc, so I'm unsure how I should proceed here.


---

Comment by boothby created at 2008-07-14 20:39:54

Changing priority from blocker to minor.


---

Comment by boothby created at 2008-07-14 20:39:54

I'm officially back-burnering this because 1) wstein has resolved the biggest problem that this addresses, 2) I'm busier than I expected to be, and I can't devote myself to such a large-scale project.  If somebody else wants to take the torch, I support it.


---

Comment by kcrisman created at 2014-09-17 02:58:18

Nice idea!  But at this point probably needs to be "wontfix" because real database stuff is in the cloud and the notebook will probably be dedicated to smaller-scale solutions.


---

Comment by kcrisman created at 2014-09-17 02:58:18

Changing status from new to needs_review.


---

Comment by kcrisman created at 2014-09-17 02:58:25

Changing status from needs_review to positive_review.


---

Comment by vbraun created at 2014-09-18 18:00:06

Resolution: wontfix

# Issue 4268: SQLDatabase, et al. should use SQLAlchemy

Issue created by migration from Trac.

Original creator: ekirkman

Original creation time: 2008-10-12 13:53:52

Assignee: ekirkman

SQLAlchemy is far more robust and intuitive than the current relational database and query classes in Sage.  The classes should instead be based on SQLAlchemy with extensions written to cover the current capabilities.  This will be my main focus during Sage Days 10 and if anyone is interested in helping they should contact me.


---

Comment by ekirkman created at 2008-10-13 14:33:38

Another project (graph plotting) came up at Sage Days 10 so I will get to this at some other point in time if it's still open.  I do have some notes started, so please let me know if anyone starts working on this.


---

Comment by kcrisman created at 2015-01-06 14:57:18

See also #8757.  Currently the discussion is whether to just remove sqlalchemy from Sage, e.g. #15593.


---

Comment by vdelecroix created at 2015-01-15 07:09:42

Because of #15593 this is invalid. Moreover, it was discussed on sage-devel several times that sqlalchemy is too high level for simple database interaction.

Vincent


---

Comment by vdelecroix created at 2015-01-15 07:09:42

Changing status from new to needs_review.


---

Comment by vdelecroix created at 2015-01-15 07:09:50

Changing status from needs_review to positive_review.


---

Comment by vbraun created at 2015-01-25 12:55:01

Resolution: invalid

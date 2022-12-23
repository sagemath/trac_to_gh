# Issue 7059: [with patch, needs review] Stop Sage tests from saving things to hard drive -- really!

Issue created by migration from https://trac.sagemath.org/ticket/7059

Original creator: jhpalmieri

Original creation time: 2009-09-29 02:59:58

Assignee: jhpalmieri

CC:  kcrisman

This is a followup to #6864. A few doctests are still writing some files to non-temporary directories.  I think the attached patch fixes this, and it also adds a paragraph to the developer's guide warning about this sort of thing.



---

Attachment

Positive review.  You beat me to it!  Good idea to add it to the devel guide.


---

Comment by was created at 2009-10-02 17:26:28

I'm making this a 4.1.2 blocker.


---

Comment by was created at 2009-10-02 17:26:28

Changing priority from major to blocker.


---

Comment by was created at 2009-10-02 17:36:45

Resolution: fixed

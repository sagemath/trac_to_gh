# Issue 4833: sage -upgrade should complain when queues are used and patches are applied

Issue created by migration from Trac.

Original creator: jason

Original creation time: 2008-12-19 19:32:57

Assignee: mabshoff

CC:  jthurber

I've messed up at least one upgrade by accidentally having mercurial queue patches applied when trying to upgrade.  sage -upgrade should at least warn the user, and maybe give an option of popping off all of the patches before upgrading or just quitting.



---

Comment by robertwb created at 2009-02-21 15:42:41

See also #4759


---

Comment by jdemeyer created at 2014-01-09 09:36:59

Changing status from new to needs_review.


---

Comment by jdemeyer created at 2014-01-09 09:36:59

Obsolete because of `git`


---

Comment by jdemeyer created at 2014-01-09 09:37:05

Changing status from needs_review to positive_review.


---

Comment by vbraun created at 2014-01-10 08:47:31

Resolution: wontfix

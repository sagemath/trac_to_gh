# Issue 9234: Bring doc coverage of plot/plot3d/texture.py to 100%

Issue created by migration from Trac.

Original creator: slabbe

Original creation time: 2010-06-14 09:50:06

Assignee: slabbe

CC:  sage-combinat

from 30% (3/10)


---

Attachment


---

Comment by slabbe created at 2010-06-14 09:54:03

Changing status from new to needs_review.


---

Attachment

Apply after initial patch


---

Comment by kcrisman created at 2010-06-18 19:32:50

Looks nice!  This corrects a few minor typos, adds some examples at the top of the module, adds the document to the reference manual, and one or two other things.  The reviewer patch is all that needs to be checked now; try the command (from within the Sage directory)

```
./sage -docbuild reference html
```

to create the changed manual, after building the reviewer patch.


---

Comment by jhpalmieri created at 2010-06-21 19:20:28

Reviewer patch looks good.


---

Comment by jhpalmieri created at 2010-06-21 19:20:28

Changing status from needs_review to positive_review.


---

Comment by mpatel created at 2010-07-21 10:03:40

Resolution: fixed

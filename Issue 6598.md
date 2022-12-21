# Issue 6598: Change the sage build system to use "set -e" so that if any error occurs in spkg-install then the build immediately terminates with an error

Issue created by migration from Trac.

Original creator: was

Original creation time: 2009-07-23 09:46:34

Assignee: tbd

CC:  dimpase jhpalmieri


```
> Nonetheless, we should be checking the error code after every line
> executes, one way or another.  Is there a way to automatically do this
> in bash?

"set -e" should do it.

Google brings up this page, besides lots of others:

http://www.davidpashley.com/articles/writing-robust-shell-scripts.html


Cheers,
Burcin
```



---

Comment by mkoeppe created at 2020-08-30 19:06:37

Changing status from new to needs_review.


---

Comment by mkoeppe created at 2020-08-30 19:06:37

outdated, can be closed


---

Comment by jhpalmieri created at 2020-08-31 02:15:35

Changing status from needs_review to positive_review.


---

Comment by jhpalmieri created at 2020-08-31 02:15:35

Okay


---

Comment by chapoton created at 2020-10-04 07:53:46

Resolution: invalid

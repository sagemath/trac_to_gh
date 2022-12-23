# Issue 1082: "sage -upgrade" behaves poorly when sage-main has not-checked-in changes

Issue created by migration from https://trac.sagemath.org/ticket/1082

Original creator: cwitty

Original creation time: 2007-11-03 18:08:01

Assignee: was

Currently, "sage -upgrade" automatically checks in code in sage-main (asking you for a commit message, etc.) without explaining what's happening, and what exactly is being checked in.

Instead, "sage -upgrade" should either explain what's going on before it checks in the code, or explain what's going on and then exit without doing anything, so the user can use hg_sage.ci().


---

Comment by mmezzarobba created at 2014-02-02 10:54:28

Changing status from new to needs_review.


---

Comment by mmezzarobba created at 2014-02-02 10:54:28

No more relevant?


---

Comment by aapitzsch created at 2014-02-09 21:36:09

Changing status from needs_review to positive_review.


---

Comment by aapitzsch created at 2014-02-09 21:36:09

No longer relevant.


---

Comment by vbraun created at 2014-02-11 21:21:19

Resolution: wontfix

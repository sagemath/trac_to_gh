# Issue 9454: Add support for account tokens

Issue created by migration from https://trac.sagemath.org/ticket/9454

Original creator: wjp

Original creation time: 2010-07-08 14:57:46

Assignee: jason, was

CC:  chapoton

The attached patch adds support for a new token-based challenge mechanism for account creation in the sage notebook.

Workflow:

The admin enables challenges, and sets challenge_type to token.

The admin generates 50 tokens (through the user management interface) and distributes these to 50 people. (Students taking some class, for example.)

Each person that receives a token can use that token (once) to create an account.



---

Attachment


---

Comment by wjp created at 2010-07-08 14:58:26

Changing status from new to needs_review.


---

Comment by jdemeyer created at 2012-07-27 20:42:38

Please fill in your real name as Author.


---

Comment by kcrisman created at 2013-06-18 20:13:35

This looks really cool, and some stuff could still be used directly [upstream](https://github.com/sagemath/sagenb/blob/master/sagenb/notebook/challenge.py), but it does need some rebasing or an upstream request or something.


---

Comment by kcrisman created at 2013-06-18 20:13:35

Changing status from needs_review to needs_work.


---

Comment by mkoeppe created at 2020-08-18 00:36:52

Changing status from needs_work to needs_review.


---

Comment by mkoeppe created at 2020-08-18 00:36:52

Proposing to close all sagenb tickets as outdated, so that all remaining open tickets in the notebook component are about the Jupyter notebook.


---

Comment by chapoton created at 2020-09-09 09:39:30

Resolution: invalid

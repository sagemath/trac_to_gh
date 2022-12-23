# Issue 5668: notebook optimization -- when saving state sometimes the sage public notebook server (after running for a long time) takes a *huge* amount of RAM

Issue created by migration from https://trac.sagemath.org/ticket/5668

Original creator: was

Original creation time: 2009-04-02 20:06:46

Assignee: boothby

CC:  kcrisman jhpalmieri

The attached screenshot shows the public Sage notebook server (which has about 7000 user accounts) saving state after I pressed control-C.  It uses a huge amount of RAM, but does finish after several minutes.




---

Comment by was created at 2009-04-02 20:07:11

picture of top and fact that we're saving state.


---

Attachment

picture of too many open files.


---

Comment by chapoton created at 2020-03-28 20:36:23

ancient ticket about deprecated sagenb, can we close ?


---

Comment by chapoton created at 2020-03-28 20:36:23

Changing status from new to needs_review.


---

Comment by kcrisman created at 2020-03-28 20:41:09

Changing status from needs_review to positive_review.


---

Comment by kcrisman created at 2020-03-28 20:41:09

This was only really ever applicable to absolutely immense notebook instantiations anyway :)


---

Comment by chapoton created at 2020-03-28 20:41:42

Resolution: invalid


---

Comment by chapoton created at 2020-03-28 20:41:42

thx

# Issue 7975: remove dsage from sage

Issue created by migration from Trac.

Original creator: was

Original creation time: 2010-01-18 12:42:39

Assignee: tbd

I just noticed that dsage is completely broken in sage-4.3 and sage-4.3.1.rc0, etc.:

```
sage: dsage.setup()
sage: D = dsage.start_all()
sage: a = D('2+3')
BOOM?
sage: a
BOOM!
```



---

Comment by jhpalmieri created at 2010-01-18 15:28:03

Reminder to anyone who wants to deal with this: in addition to removing any actual dsage code, also remove the sections on dsage from the tutorial (English and French) and reference manual.


---

Attachment


---

Comment by was created at 2010-01-19 06:39:39

This is the new deps file, which is fine assuming you didn't change the deps file in making the 4.3.1.rc1 release (I just took 4.3.1.rc0's deps and fixed it).


---

Attachment

This is the new spkg/install file, which is fine assuming you didn't change the install file in making the 4.3.1.rc1 release (I just took 4.3.1.rc0's install and fixed it).


---

Attachment


---

Attachment

See http://boxen.math.washington.edu/home/wstein/patches/sagenb/sagenb-0.6.spkg for the new sagenb spkg.


---

Comment by was created at 2010-01-19 07:22:12

Changing status from new to needs_review.


---

Attachment


---

Comment by rlm created at 2010-01-19 07:32:45

Changing status from needs_review to positive_review.


---

Comment by rlm created at 2010-01-19 07:33:15

Resolution: fixed

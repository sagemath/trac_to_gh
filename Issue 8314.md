# Issue 8314: numerical noise in sage/misc/functional.py

Issue created by migration from Trac.

Original creator: mvngu

Original creation time: 2010-02-20 16:26:06

Assignee: tbd

From [sage-devel](http://groups.google.com/group/sage-devel/msg/ba90601a2c25291d):

```
On 32-bit Suse I get this fuzz:

File "/local/jec/sage-4.3.3.alpha1/devel/sage/sage/misc/functional.py",
line 705:
    sage: h.n()
Expected:
    0.33944794097891573
Got:
    0.33944794097891567 
```



---

Comment by mvngu created at 2010-02-20 16:28:08

based on Sage 4.3.3.alpha1


---

Comment by mvngu created at 2010-02-20 16:28:28

Changing status from new to needs_review.


---

Attachment


---

Comment by cremona created at 2010-02-20 17:15:27

positive review -- the patch replaces two digits by ... so the tests pass.  It would have been nice to know why those digits are platform-dependent though...


---

Comment by cremona created at 2010-02-20 17:15:27

Changing status from needs_review to positive_review.


---

Comment by was created at 2010-02-21 19:46:58

Changing priority from major to blocker.


---

Comment by mvngu created at 2010-02-22 03:57:49

Resolution: fixed

# Issue 7875: sage -preparse fails

Issue created by migration from https://trac.sagemath.org/ticket/7875

Original creator: iandrus

Original creation time: 2010-01-09 13:41:58

Assignee: tbd

Running `sage -preparse somefile.sage` fails with

```
Traceback (most recent call last):
  File "/Users/gvol/vcs/cur-sage/local/bin/sage-preparse", line 230, in <module>
    do_preparse(f)
  File "/Users/gvol/vcs/cur-sage/local/bin/sage-preparse", line 119, in do_preparse
    G = preparse_file(F, magic=False, do_time=True, ignore_prompts=False)
TypeError: preparse_file() got an unexpected keyword argument 'magic'
```


It looks like local/bin/sage-preparse wasn't updated to remove magic and ignore_prompts when sage/misc/preparser.py was.



---

Attachment


---

Comment by was created at 2010-01-10 22:26:50

Changing priority from critical to blocker.


---

Comment by was created at 2010-01-10 22:26:50

This was caused by a change to the preparse_file function.


---

Comment by was created at 2010-01-10 22:26:50

Changing status from new to needs_review.


---

Comment by mpatel created at 2010-01-12 15:46:06

Changing status from needs_review to positive_review.


---

Comment by rlm created at 2010-01-13 04:41:41

Resolution: fixed

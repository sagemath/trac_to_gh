# Issue 3708: something screwy in the reference manual -- coding theory

Issue created by migration from Trac.

Original creator: was

Original creation time: 2008-07-22 14:17:04

Assignee: wdjoyner


```
39. Coding Theory

    * 39.1 Linear Codes
    * 39.2 AUTHOR: 
```



---

Attachment

patch based on 3.0.6.rc0


---

Comment by wdj created at 2008-07-22 15:26:52

Patch attached. One liner added to a docstring, so did not run sage -testall. (I'll run this right now and post in a few hours if there is a failure.)


---

Comment by cremona created at 2008-07-29 01:39:48

I applied the patch ok and did "sage -br", then opened a notebook and clicked through to the ref manual, but the AUTHOR entry was still there.  If you can tell me how to get the manual to rebuild then I'll happily give this a positive review.


---

Comment by mabshoff created at 2008-07-31 03:53:06

With rebuild in doc the issue is fixed in the documentation. Positive review.

Cheers,

Michael


---

Comment by mabshoff created at 2008-07-31 03:54:22

Resolution: fixed


---

Comment by mabshoff created at 2008-07-31 03:54:22

Merged in Sage 3.1.alpha0

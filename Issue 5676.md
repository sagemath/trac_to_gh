# Issue 5676: Preparser identifies hex literals as floating point.

Issue created by migration from https://trac.sagemath.org/ticket/5676

Original creator: boothby

Original creation time: 2009-04-03 16:26:19

Assignee: was

CC:  robertwb


```
    sage: 0xe
    Traceback (most recent call last)
    ...
    TypeError: Unable to convert x (='0xe') to real number.
```



---

Comment by mabshoff created at 2009-04-15 04:15:36

Unless someone is working on this I will bump it tomorrow. 

Cheers,

Michael


---

Comment by boothby created at 2009-04-15 17:30:51

I have a fix for this, I'll post a patch in 1 hour.


---

Attachment


---

Comment by robertwb created at 2009-04-15 21:35:38

Yep, that works great.


---

Comment by mabshoff created at 2009-04-15 23:37:06

Merged in Sage 3.4.1.rc3.

Cheers,

Michael


---

Comment by mabshoff created at 2009-04-15 23:37:06

Resolution: fixed

# Issue 1238: update the cremona spkg

Issue created by migration from https://trac.sagemath.org/ticket/1238

Original creator: was

Original creation time: 2007-11-21 17:30:10

Assignee: was


```


Attached bundle fixes the point below: now cerr is only used for
prompts, hence not at all in the library functions.  Instead, the
fatal error conditions which send output now to cout are followed by a
call to abort().  Clearly this should never happen except if there's a
bug.

Ralf -- a lot of those error outputs were in the linalg code which you
are going to refactor.

Secondly, I fixed the unintended output of "transposing..." reported by William.
```



---

Attachment


---

Comment by mabshoff created at 2007-11-24 10:51:06

This issue will also be closed by the spkg at #1247.

Cheers,

Michael


---

Comment by mabshoff created at 2007-11-24 15:37:37

Resolution: fixed

# Issue 4145: [with patch, needs review] linear codes list function is slow

Issue created by migration from https://trac.sagemath.org/ticket/4145

Original creator: rlm

Original creation time: 2008-09-18 15:05:53

Assignee: tbd

Before:

```
sage: G = ExtendedBinaryGolayCode()
sage: time L = G.list()
CPU times: user 16.24 s, sys: 0.32 s, total: 16.57 s
Wall time: 17.14 s
```


After:

```
sage: G = ExtendedBinaryGolayCode()
sage: time L = G.list()
CPU times: user 3.65 s, sys: 0.04 s, total: 3.68 s
Wall time: 3.71 s
```



---

Attachment

This may actually be a bugfix, see:
http://trac.sagemath.org/sage_trac/ticket/4115#comment:13


---

Comment by wdj created at 2008-09-18 17:07:22

This is obviously correct (the code is 1 line). I didn't know about the list method for vector spaces but I'd not surprised that that list method is a great deal faster and more efficient that the current LinearCodes one.

I have tested this does fix the comment 13 in #4115. Thanks Robert!


---

Comment by mabshoff created at 2008-09-19 00:48:07

Resolution: fixed


---

Comment by mabshoff created at 2008-09-19 00:48:07

Merged in Sage 3.1.3.alpha0

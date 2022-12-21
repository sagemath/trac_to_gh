# Issue 3270: [with patch, easy review] trivial 100x speedup in coding theory

Issue created by migration from Trac.

Original creator: rlm

Original creation time: 2008-05-22 00:26:04

Assignee: rlm

CC:  wdj

Was:

```
sage: C = ExtendedBinaryGolayCode()
sage: time G = C.permutation_automorphism_group()
CPU times: user 2.39 s, sys: 0.58 s, total: 2.97 s
Wall time: 24.32
```

Now:

```
sage: C = ExtendedBinaryGolayCode()
sage: time G = C.permutation_automorphism_group()
CPU times: user 0.19 s, sys: 0.04 s, total: 0.23 s
Wall time: 0.24
```



---

Attachment

Looks good to me.


---

Comment by mabshoff created at 2008-05-22 10:36:46

Resolution: fixed


---

Comment by mabshoff created at 2008-05-22 10:36:46

Merged in Sage 3.0.2.rc0

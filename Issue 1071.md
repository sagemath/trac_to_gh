# Issue 1071: [with patch] IntegerVectors_nk

Issue created by migration from https://trac.sagemath.org/ticket/1071

Original creator: malb

Original creation time: 2007-11-02 22:48:35

Assignee: mhansen

CC:  sage-combinat

calling IntegerVectors.list after applying the attached patch is much faster now.

old:

```
sage: time l1 = map(tuple, IntegerVectors(2, 60).list())
CPU time: 5.01 s,  Wall time: 5.11 s
```


new:

```
sage: time l1 = map(tuple, IntegerVectors(2, 60).list())
CPU time: 0.20 s,  Wall time: 0.20 s
```




---

Attachment


---

Attachment


---

Comment by mhansen created at 2007-11-03 18:30:04

Updated patch attached.


---

Comment by malb created at 2007-11-05 11:04:44

Please note that the cleaner version by mhansen is by a factor of three than the original submission:

```
the untouched implementation
sage: time l1 = map(tuple, IntegerVectors(2, 60).list())
CPU times: user 5.06 s, sys: 0.11 s, total: 5.18 s
Wall time: 5.18
```


mhansen's implementation

```
sage: time l1 = map(tuple, IntegerVectors(2, 60, min_part=0).list())
CPU time: 0.56 s,  Wall time: 0.57 s
```


malb's original submission

```
sage: time l1 = map(tuple, IntegerVectors(2, 60).list())
CPU time: 0.20 s,  Wall time: 0.20 s
```


I don't mean to push my original patch (which's problems were fixed by mhansen) but propose to optimise mhansen's patch eventually.


---

Comment by mabshoff created at 2007-11-06 22:19:50

applied mhansen's patch to 2.8.12.rc0


---

Comment by mabshoff created at 2007-11-06 22:19:50

Resolution: fixed


---

Attachment


---

Attachment

# Issue 2839: bug in conversion from symmetrica's longint

Issue created by migration from https://trac.sagemath.org/ticket/2839

Original creator: mhansen

Original creation time: 2008-04-07 07:15:33

Assignee: mabshoff

CC:  sage-combinat

This was reported here: http://groups.google.com/group/sage-devel/tree/browse_frm/thread/718d1d2853988d13/beece4dabd2d84c8?rnum=1&_done=%2Fgroup%2Fsage-devel%2Fbrowse_frm%2Fthread%2F718d1d2853988d13%3F#doc_909abc517bb7eeb6


---

Comment by mhansen created at 2008-04-07 07:15:57

Changing status from new to assigned.


---

Comment by mhansen created at 2008-04-07 07:15:57

Changing assignee from mabshoff to mhansen.


---

Comment by mhansen created at 2008-04-07 07:15:57

Changing component from Cygwin to combinatorics.


---

Attachment


---

Comment by mhansen created at 2008-04-07 07:21:02

The patch also includes a speed up for change of bases over QQ.

Before:

```
sage: time s(p(s([17,11])))
CPU times: user 1252.31 s, sys: 8.24 s, total: 1260.55 s
Wall time: 1259.90
s[17, 11]
sage: time a = s([10,10]).itensor(s([10,10]))
CPU times: user 30.87 s, sys: 0.21 s, total: 31.09 s
Wall time: 31.09
```


After:

```
sage: time s(p(s([17,11])))
CPU times: user 257.11 s, sys: 0.03 s, total: 257.14 s
Wall time: 257.15
s[17, 11]
sage: time a = s([10,10]).itensor(s([10,10]))
CPU times: user 3.60 s, sys: 0.00 s, total: 3.60 s
Wall time: 3.60
```



---

Comment by ddrake created at 2008-04-07 08:33:31

The patch works for me (32-bit Ubuntu Hardy) and fixes the issues mentioned in the sage-devel thread. All tests pass on /libs/symmetrica/symmetrica.pxi.


---

Comment by mabshoff created at 2008-04-07 14:22:58

Merged in Sage 3.0.alpha3


---

Comment by mabshoff created at 2008-04-07 14:22:58

Resolution: fixed

# Issue 1747: [with patch, needs review] speed improvement for mq.SR.polynomial_system

Issue created by migration from Trac.

Original creator: malb

Original creation time: 2008-01-10 15:14:18

Assignee: malb

See attached patch.


---

Attachment


---

Comment by mabshoff created at 2008-01-16 15:55:15

Looks good to me. I would be curious how much a difference it does make.

Cheers,

Michael


---

Comment by mabshoff created at 2008-01-16 15:59:45

malb commented on the performance issue in IRC:

```
[16:46] <mabshoff> Did you run benchmarks? I.e. does it make a difference?
[16:46] <malb> a LOT
[16:46] <malb> from unfeasible to < 1s
[16:46] <malb> the preparser is slow slow slow
```



---

Comment by mabshoff created at 2008-01-16 15:59:53

Resolution: fixed

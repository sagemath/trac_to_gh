# Issue 4144: [with patch, needs review] allow finite field elements in SBox constructor

Issue created by migration from Trac.

Original creator: malb

Original creation time: 2008-09-18 10:26:59

Assignee: malb

Keywords: crypto, aes, sbox, mq

make it so that this works:


```
sage: sr = mq.SR(1,1,1,4, allow_zero_inversions=True)
sage: S = mq.SBox([sr.sub_byte(e) for e in list(sr.k)])
sage: S
(6, 5, 2, 9, 4, 7, 3, 12, 14, 15, 10, 0, 8, 1, 13, 11)
```




---

Attachment


---

Comment by malb created at 2008-09-20 15:47:11

Changing status from new to assigned.


---

Comment by cwitty created at 2008-11-23 02:01:41

The code does something that looks reasonable, and doctests pass.  (I don't know enough crypto to be sure that this is a useful thing to do, so I'm relying on malb for that part.)

Positive review.


---

Comment by mabshoff created at 2008-11-23 07:56:15

Merged in Sage 3.2.1.alpha0


---

Comment by mabshoff created at 2008-11-23 07:56:15

Resolution: fixed

# Issue 579: pass additional *args and **kwds for GF to finite field implementations

Issue created by migration from https://trac.sagemath.org/ticket/579

Original creator: malb

Original creation time: 2007-09-03 15:17:47

Assignee: somebody

For example, you may print finite field elements as integers via the Givaro implementation. But the constructor parameter to allow this is not passed to the actual implementation so far.

After the attached patch is applied, this works:

```
sage: k.<a> = GF(2^8,repr='int')
sage: a
2
```



---

Attachment


---

Comment by was created at 2007-09-05 05:00:50

Resolution: fixed

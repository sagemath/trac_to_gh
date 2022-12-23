# Issue 5077: bug in fibonacci function

Issue created by migration from https://trac.sagemath.org/ticket/5077

Original creator: was

Original creation time: 2009-01-23 22:22:02

Assignee: somebody

Delete this line from the docstring.  It is just inconsistent.


```
  For negative n, define F_{n} = -F_{|n|}.
```



---

Attachment

Trivial patch attached.  While I was at it I fixed a couple of typos.


---

Comment by mhansen created at 2009-01-24 08:40:44

Looks good to me.


---

Comment by mabshoff created at 2009-01-24 14:48:29

Resolution: fixed


---

Comment by mabshoff created at 2009-01-24 14:48:29

Merged in Sage 3.3.alpha2

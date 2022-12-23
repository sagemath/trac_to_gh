# Issue 3066: empty matrices: gram_schmidt() throws a NameError

Issue created by migration from https://trac.sagemath.org/ticket/3066

Original creator: dfdeshom

Original creation time: 2008-04-30 15:20:39

Assignee: was

Looks like an explicit import is the only thing missing on this one:


```
sage: a = matrix([])
sage: m.gram_schmidt()
<type 'exceptions.NameError'>: global name 'ZZ' is not defined
```



---

Attachment


---

Comment by dfdeshom created at 2008-04-30 17:35:44

Patch attached.


---

Comment by mabshoff created at 2008-05-01 05:47:16

Resolution: fixed


---

Comment by mabshoff created at 2008-05-01 05:47:16

Merged in Sage 3.0.1.alpha1

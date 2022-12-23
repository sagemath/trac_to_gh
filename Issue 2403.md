# Issue 2403: Cannot copy Sequence

Issue created by migration from https://trac.sagemath.org/ticket/2403

Original creator: novoselt

Original creation time: 2008-03-06 06:18:45

Assignee: cwitty

I get an error when I am trying to copy a sequence:



```
sage: copy([1,2])
[1, 2]
sage: copy(Sequence([1,2]))
Traceback (most recent call last):
...
TypeError: sage.structure.sage_object.SageObject.__new__(Sequence) is not safe, use list.__new__()
```




---

Attachment


---

Comment by cwitty created at 2008-03-14 01:28:22

Looks good; testall passes.


---

Comment by mabshoff created at 2008-03-14 02:31:41

Merged in Sage 2.10.4.alpha0


---

Comment by mabshoff created at 2008-03-14 02:31:41

Resolution: fixed

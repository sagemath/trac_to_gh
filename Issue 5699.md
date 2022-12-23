# Issue 5699: notebook -- %r mode is completely broken (trivial to fix)

Issue created by migration from https://trac.sagemath.org/ticket/5699

Original creator: was

Original creation time: 2009-04-06 19:28:16

Assignee: boothby

In the notebook


```
%r
2+5
///
Traceback (most recent call last):
...
TypeError: eval() got multiple values for keyword argument 'synchronize'
```



---

Attachment


---

Comment by mhansen created at 2009-04-10 22:14:12

Looks good to me.


---

Comment by mabshoff created at 2009-04-11 00:00:10

Resolution: fixed


---

Comment by mabshoff created at 2009-04-11 00:00:10

Merged in Sage 3.4.1.rc2.

Cheers,

Michael

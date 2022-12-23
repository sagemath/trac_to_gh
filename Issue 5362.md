# Issue 5362: [with patch, needs review] bug in transpose for matrix_double_dense

Issue created by migration from https://trac.sagemath.org/ticket/5362

Original creator: ylchapuy

Original creation time: 2009-02-24 22:27:41

Assignee: was

Keywords: transpose

A copy is missing:

```
sage: m=matrix(RDF,2,2,range(4))
sage: m2=m.transpose()
sage: m2

[0.0 2.0]
[1.0 3.0]
sage: m[0,0]=1
sage: m2

[1.0 2.0]
[1.0 3.0]
```



---

Comment by mhansen created at 2009-02-24 23:03:11

I updated the formatting of the docstring to be compatible with the new documentation system.  Other than that, looks good.  Good catch!


---

Attachment


---

Comment by mabshoff created at 2009-02-28 17:09:14

Resolution: fixed


---

Comment by mabshoff created at 2009-02-28 17:09:14

Merged in Sage 3.4.rc0.

Cheers,

Michael

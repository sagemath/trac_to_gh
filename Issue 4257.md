# Issue 4257: [with patch, needs review] support for Singular's  'intmat' and 'intvec'

Issue created by migration from https://trac.sagemath.org/ticket/4257

Original creator: malb

Original creation time: 2008-10-09 21:54:29

Assignee: malb

CC:  singular

This now works:


```
sage: A = random_matrix(ZZ,3,3); A
[ -8   2   0]
[  0   1  -1]
[  2   1 -95]
sage: As = singular(A); As
-8     2     0
 0     1    -1
 2     1   -95
sage: As._sage_()
[ -8   2   0]
[  0   1  -1]
[  2   1 -95]
```



---

Attachment


---

Comment by mhansen created at 2008-10-10 16:18:51

Looks good to me.


---

Comment by mabshoff created at 2008-10-11 06:40:58

Resolution: fixed


---

Comment by mabshoff created at 2008-10-11 06:40:58

Merged in Sage 3.1.3.rc0

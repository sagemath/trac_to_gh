# Issue 37: preparser doesn't parse hex input:

Issue created by migration from https://trac.sagemath.org/ticket/37

Original creator: was

Original creation time: 2006-09-12 23:30:00

Assignee: somebody


```
sage: 0x5
------------------------------------------------------------
   File "<ipython console>", line 1
     ZZ(0)x5
           ^
SyntaxError: invalid syntax
```




---

Comment by was created at 2006-09-12 23:30:11

Changing priority from major to minor.


---

Comment by was created at 2006-09-12 23:30:11

Changing type from defect to enhancement.


---

Comment by mabshoff created at 2007-08-22 19:43:45

This is still a problem with Sage 2.8.2.

Cheers,

Michael


---

Comment by malb created at 2008-02-27 00:09:49

The behaviour has changes (this is 2.10.2):

```
sage: 0x10
16

sage: 0xA
------------------------------------------------------------
   File "<ipython console>", line 1
     Integer(0x)A
                ^
<type 'exceptions.SyntaxError'>: invalid syntax

sage: 0xa
------------------------------------------------------------
   File "<ipython console>", line 1
     Integer(0x)a
                ^
<type 'exceptions.SyntaxError'>: invalid syntax
```



---

Comment by was created at 2008-02-28 04:58:08

Note: #2144 is (a) a dupe of this, and (b) actually doesn't fix the problem.


---

Attachment


---

Comment by was created at 2008-02-28 05:07:11

Changing type from enhancement to defect.


---

Comment by ncalexan created at 2008-02-28 06:38:40

Doctests look good, commit.


---

Comment by mabshoff created at 2008-02-28 06:41:24

Merged in Sage 2.10.3.rc0


---

Comment by mabshoff created at 2008-02-28 06:41:24

Resolution: fixed


---

Comment by robertwb created at 2008-02-28 08:23:38

Nick beat me too it, but I think it looks good too.

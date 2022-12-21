# Issue 1084: invalid use of ring notation gives bizarre post-preparser syntax error

Issue created by migration from Trac.

Original creator: cwitty

Original creation time: 2007-11-03 20:09:14

Assignee: ncalexan

Consider this example:

```
sage: QQX = QQ['x']
sage: K.<x> = QQX
------------------------------------------------------------
   File "<ipython console>", line 1
     K = QQ,names=(u'x',)); (x,) = K._first_ngens(Integer(1))
                         ^
<type 'exceptions.SyntaxError'>: invalid syntax
```


I don't care if this actually works; but if it doesn't, it should fail with a friendlier error message.  And where did the 'X' from QQX go?


---

Attachment


---

Comment by ncalexan created at 2007-11-04 01:43:10

Patch may require 1040-ncalexan-2.hg be attached first; check ticket 1040.


---

Comment by mabshoff created at 2007-11-06 22:03:39

applied to 2.8.12.rc0


---

Comment by mabshoff created at 2007-11-06 22:03:39

Resolution: fixed

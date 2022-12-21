# Issue 2638: complex QQbar expressions exceed maximum recursion depth when exact computation is triggered

Issue created by migration from Trac.

Original creator: cwitty

Original creation time: 2008-03-21 22:01:45

Assignee: somebody

For example, 

```
sage: s = SFASchur(QQ)
sage: a=s([3,2]).expand(8)(flatten([[QQbar.zeta(3)^d for d in range(3)], [QQbar.zeta(5)^d for d in range(5)]]))
sage: a.exactify() 
```

(as reported in http://groups.google.com/group/sage-devel/browse_thread/thread/8cf79f359cceef3d/e931afceebf3fe35#e931afceebf3fe35)


---

Attachment


---

Comment by boothby created at 2009-01-24 11:04:29

Works for me, all tests in QQbar pass.


---

Comment by mabshoff created at 2009-01-24 19:31:05

Resolution: fixed


---

Comment by mabshoff created at 2009-01-24 19:31:05

Merged in Sage 3.3.alpha2

Cheers,

Michael

# Issue 2046: [with patch] save(srange(3), './foo') fails

Issue created by migration from Trac.

Original creator: cwitty

Original creation time: 2008-02-05 01:51:21

Assignee: was

This bug was reported by Georg here: http://groups.google.com/group/sage-support/browse_thread/thread/a1c5910c053abc90/28f1b635fba382a4#28f1b635fba382a4

```
sage: save(srange(3), './foo')
---------------------------------------------------------------------------
<type 'exceptions.AttributeError'>        Traceback (most recent call last)

/home/cwitty/<ipython console> in <module>()

/home/cwitty/sage_object.pyx in sage.structure.sage_object.save()

<type 'exceptions.AttributeError'>: 'list' object has no attribute 'save'
```



---

Attachment


---

Comment by was created at 2008-02-05 05:07:28

it looks right, applies cleanly, and works.


---

Comment by mabshoff created at 2008-02-07 05:27:00

Merged in Sage 2.10.2.alpha0


---

Comment by mabshoff created at 2008-02-07 05:27:00

Resolution: fixed

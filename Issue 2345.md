# Issue 2345: negative indicies in vectors

Issue created by migration from Trac.

Original creator: mhansen

Original creation time: 2008-02-28 08:47:58

Assignee: was


```
sage: vector(RR,range(3))[2]
 2.00000000000000

sage: vector(RR,range(3))[-1]
----------------------------------------------------

/home/dfdeshom/custom/sage/devel/sage-gcd2/<ipython
console> in <module>()

/home/dfdeshom/custom/sage/devel/sage-gcd2/free_modu
le_element.pyx in sage.modules.free_module_element.F
reeModuleElement_generic_dense.__getitem__()

<type 'exceptions.IndexError'>: index (i=-1) must be
 between 0 and 2
```



---

Comment by mhansen created at 2008-02-28 09:36:58

Changing assignee from was to mhansen.


---

Attachment


---

Comment by mhansen created at 2008-02-28 09:36:58

Changing status from new to assigned.


---

Comment by dfdeshom created at 2008-02-28 14:33:10

The patch looks great, thanks!


---

Comment by mabshoff created at 2008-03-03 02:55:16

There was a long discussion about it and in the end the patch was voted in in the thread:

https://groups.google.com/group/sage-devel/browse_thread/thread/0aadcca5557ea45a/80148bb28bec02d1#80148bb28bec02d1

Cheers,

Michael


---

Comment by mabshoff created at 2008-03-03 02:55:16

Resolution: fixed


---

Comment by mhansen created at 2008-03-03 03:42:22

Merged in 2.10.3.rc1.

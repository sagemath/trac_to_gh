# Issue 2668: loads/dumps do not work with QQbar and AA

Issue created by migration from Trac.

Original creator: ncalexan

Original creation time: 2008-03-25 21:42:47

Assignee: was

CC:  ncalexan

Keywords: QQbar AA loads dumps save


```
sage: loads(dumps(QQbar.zeta(5))) == QQbar.zeta(5)
---------------------------------------------------------------------------
<type 'exceptions.RuntimeError'>          Traceback (most recent call last)

/Users/ncalexan/Documents/School/MATH235/genus2cm/<ipython console> in <module>()

/Users/ncalexan/Documents/School/MATH235/genus2cm/sage_object.pyx in sage.structure.sage_object.loads()

<type 'exceptions.RuntimeError'>: __new__() takes exactly 3 arguments (1 given)
invalid data stream
invalid load key, 'x'.
Unable to load pickled data.
```



---

Attachment


---

Comment by mabshoff created at 2008-03-28 13:33:48

Mmmh, I think it is customary to use `loads(dumps(t)) == t` - you should check if `coverage` picks up on those doctests. It does usually complain if the `loads(dumps())` test isn't define since it pickling is required for DSage to work. Otherwise the patch looks nice, but cwitty should be the one to referee this.

Cheers,

Michael


---

Attachment


---

Comment by cwitty created at 2008-03-28 14:48:19

Looks good.  "sage -coverage" does want doctests for `__reduce__` methods, so I copied Nick's doctests from the module header into the `__reduce__` methods in my attached patch.

Apply both patches.


---

Comment by mabshoff created at 2008-03-28 18:46:07

Merged in Sage 2.11.alpah2


---

Comment by mabshoff created at 2008-03-28 18:46:07

Resolution: fixed

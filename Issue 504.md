# Issue 504: make lie interface more robust

Issue created by migration from https://trac.sagemath.org/ticket/504

Original creator: was

Original creation time: 2007-08-28 23:38:44

Assignee: was

The Lie interface doesn't gracefully handle errors, which totally corrupt the io stream. 


```
sage: A4 = lie('A4')
sage: A4.i_Cartan()

     [[4,3,2,1]
     ,[3,6,4,2]
     ,[2,4,6,3]
     ,[1,2,3,4]
     ]

sage: A4.multiplicative_order()
---------------------------------------------------------------------------
<type 'exceptions.NotImplementedError'>   Traceback (most recent call last)

/home/was/<ipython console> in <module>()

/home/was/element.pyx in element.RingElement.multiplicative_order()

/home/was/element.pyx in element.RingElement.is_unit()

<type 'exceptions.NotImplementedError'>:
sage: A4.i_Cartan()

sage: A4.i_Cartan()
sage0
sage: A4.i_Cartan()

Argument types do not match in call. Types are: ==(grp, bin).
Valid argument types are for instance: ==(bin, bin).
sage: A4.i_Cartan()

     [[4,3,2,1]
     ,[3,6,4,2]
     ,[2,4,6,3]
     ,[1,2,3,4]
     ]
```



---

Comment by mhansen created at 2007-08-28 23:53:06

Changing assignee from was to mhansen.


---

Attachment


---

Comment by mhansen created at 2007-08-29 00:02:48

Resolution: fixed

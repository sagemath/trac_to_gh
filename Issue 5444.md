# Issue 5444: elipses + float = boom

Issue created by migration from https://trac.sagemath.org/ticket/5444

Original creator: boothby

Original creation time: 2009-03-05 19:58:26

Assignee: robertwb


```
   sage: [(1.0)..(2.0)]
   [1.00000000000000, 2.00000000000000]
   sage: [1.0..2.0]
    line 4
    (ellipsis_range(_sage_const_1p0 ,Ellipsis,_sage_const_2 RealNumber('.0')))
                                                                     ^
SyntaxError: invalid syntax
```



---

Comment by robertwb created at 2009-05-18 21:54:16

This has been resolved, probably while cleaning up the preparser code. 


```
----------------------------------------------------------------------
----------------------------------------------------------------------
| Sage Version 3.4.2, Release Date: 2009-05-05                       |
| Type notebook() for the GUI, and license() for information.        |
sage: [1.0..2.0]
 [1.00000000000000, 2.00000000000000]

```



---

Comment by robertwb created at 2009-05-18 21:54:16

Resolution: worksforme


---

Comment by mabshoff created at 2009-05-18 22:02:58

Has a doctest been added? Otherwise this ticket should be reopened.

Cheers,

Michael


---

Comment by mabshoff created at 2009-05-19 04:57:15

Resolution changed from worksforme to 


---

Comment by mabshoff created at 2009-05-19 04:57:15

Changing status from closed to reopened.


---

Comment by mabshoff created at 2009-05-19 04:57:15

Reopening until someone either points to a doctests or post a doctest patch.

Cheers,

Michael


---

Attachment


---

Comment by robertwb created at 2009-06-05 03:42:21

Doctest looks fine to me.


---

Comment by ncalexan created at 2009-06-13 21:50:49

Resolution: fixed

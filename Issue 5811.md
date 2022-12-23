# Issue 5811: Sage 3.4.1.rc3: Fedora 10/64 - type_reducible.py doctest failure due to '__cmp__"

Issue created by migration from https://trac.sagemath.org/ticket/5811

Original creator: mabshoff

Original creation time: 2009-04-17 11:29:02

Assignee: mabshoff

CC:  bump sage-combinat

This is also observable with FC9/64 bit with gcc 4.3.3 on SkyNet

```
sage -t -long "devel/sage/sage/combinat/root_system/type_reducible.py"
**********************************************************************
File "/space/wstein/farm/sage-3.4.1.rc3/devel/sage/sage/combinat/root_system/type_reducible.py", line 53:
    sage: [[x.__cmp__(y) for x in ct] for y in ct]
Expected:
    [[0, 1, -1], [-1, 0, -1], [1, 1, 0]]
Got:
    [[0, 1, 1], [-1, 0, 1], [1, 1, 0]]
**********************************************************************
File "/space/wstein/farm/sage-3.4.1.rc3/devel/sage/sage/combinat/root_system/type_reducible.py", line 55:
    sage: sorted(ct)
Expected:
    [['A', 4], A1xB2, B2xA1]
Got:
    [A1xB2, B2xA1, ['A', 4]]
**********************************************************************
```


Maybe '__cmp__' is broken?

Cheers,

Michael


---

Comment by mhansen created at 2009-04-18 06:22:10

Changing assignee from mabshoff to mhansen.


---

Attachment


```
<mhansen> mabs: Yep
<mabs> Have you seen #5811 ?  [17:12]
<mabs> It can be reproduced on the farm, i.e. the FC10 test box.
<mabs> wstein can create you an account. 
<mhansen> Actually, it don't think we need that.  [17:14]
<mhansen> It most likely comes from this line in cartan_type.py
<mhansen>         if other.__class__ != self.__class__:
<mhansen>             return cmp(self.__class__, other.__class__)
<mhansen> 
<mabs> So you think it is a bug?  [17:15]
<mhansen> Well, I think there are no guarantees on the results of class
          comparisons.
<mhansen> I would be fine with just changing that doctest since the order of
          the types doesn't really matter.  [17:17]
<mhansen> What matters most is deciding if they are equal or not.
```



---

Comment by mhansen created at 2009-04-18 06:22:10

Changing status from new to assigned.


---

Comment by mabshoff created at 2009-04-18 06:59:40

Dan, 

since this is in your back yard I figure it is worth CCing you.

Cheers,

Michael


---

Comment by mabshoff created at 2009-04-19 00:12:11

Ok, having read up on `__cmp___` I agree with Mike's patch. It also fixes the problem observed, so I am giving it a positive review.

Cheers,

Michael


---

Comment by mabshoff created at 2009-04-19 00:12:50

Resolution: fixed


---

Comment by mabshoff created at 2009-04-19 00:12:50

Merged in Sage 3.4.1.rc4.

Cheers,

Michael

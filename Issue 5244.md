# Issue 5244: is_unit is mostly not implemented for symbolic ring.

Issue created by migration from https://trac.sagemath.org/ticket/5244

Original creator: hivert

Original creation time: 2009-02-12 14:06:17

Assignee: hivert

CC:  sage-combinat

Keywords: is_unit, symbolic ring

Here is the code of is_unit for symbolic rings (it is actually iherited from Ring):

```
    def is_unit(self):
        if self == 1 or self == -1:
            return True
        raise NotImplementedError
```

On can do better !!!

As a result

```
sage: m=matrix(SR, 2,2)
sage: m.is_invertible()
---------------------------------------------------------------------------
NotImplementedError                       Traceback (most recent call last)
```




---

Attachment

Patch proposal for is_unit is SR


---

Comment by hivert created at 2009-02-13 16:02:23

The attached patch propose a solution.


---

Comment by mabshoff created at 2009-02-13 17:34:16

Sage 3.4 is for ReST patches only at the moment, so I am bumping it to 3.4.1.

Cheers,

Michael


---

Comment by hivert created at 2009-02-13 18:53:11

Changing status from new to assigned.


---

Comment by mabshoff created at 2009-02-14 16:33:46

I have doctested this patch on top of #5242 in my current Sage 3.3.rc1 merge tree and:

```
All tests passed!
```


Cheers,

Michael


---

Comment by malb created at 2009-02-14 17:10:39

Patch reads good, since in SR really everything != 0 is a unit.


---

Comment by mabshoff created at 2009-02-15 07:17:35

Merged in Sage 3.3.rc1.

Cheers,

Michael


---

Comment by mabshoff created at 2009-02-15 07:17:35

Resolution: fixed

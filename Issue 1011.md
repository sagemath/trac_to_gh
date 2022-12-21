# Issue 1011: [with patch] MagmaElement.__nonzero__

Issue created by migration from Trac.

Original creator: malb

Original creation time: 2007-10-27 13:59:24

Assignee: malb

This used to not work: `bool(magma('true'))` with the attached tiny patch it does.


---

Comment by mabshoff created at 2007-10-27 16:39:54

Mmmh, any chance this is related to/also  fixes #845?

Cheers,

Michael


---

Comment by cwitty created at 2007-10-27 19:58:07

Wouldn't that break `magma(25).is_zero()`?

```
sage: magma(25).is_zero()
False
sage: magma(25).bool()
---------------------------------------------------------------------------
<type 'exceptions.RuntimeError'>          Traceback (most recent call last)
[... elided ...]
<type 'exceptions.RuntimeError'>: Error evaluation Magma code.
IN:_sage_[18] eq true;
OUT:
>> _sage_[18] eq true;
              ^
Runtime error in 'eq': Bad argument types
Argument types given: RngIntElt, BoolElt
```



---

Attachment

Replying to [comment:2 cwitty]:
> Wouldn't that break `magma(25).is_zero()`?

You are right and thus I updated the patch:


```
sage: magma(9).is_zero()
False
sage: magma(0).is_zero()
True
sage: magma('false').bool()
False
sage: bool(magma(9).IsPrime())
False
sage: bool(magma(7).IsPrime())
True
```



---

Comment by mabshoff created at 2007-11-01 09:41:09

applied to 2.8.11.alpha0


---

Comment by mabshoff created at 2007-11-01 09:41:09

Resolution: fixed

# Issue 2264: Sage 2.10.2.rc0: numerical noise doctest failure in rings/real_rqdf.pyx

Issue created by migration from Trac.

Original creator: mabshoff

Original creation time: 2008-02-22 19:19:06

Assignee: failure

Craig Citro reported:

```
**********************************************************************
File "real_rqdf.pyx", line 32:
    sage: RQDF(a)
Expected:
    0.868588963806503655302257837833210164588794011607333132228907565
Got:
    0.868588963806503655302257837833210164588794011607333132228907566
********************************************************************** 
```

The above failure corresponds to:

```
Mixing of symbolic an quad double elements:
    sage: a = RQDF(2) / log(10); a
    2.00000000000000/log(10)
    sage: parent(a)
    Symbolic Ring
    sage: RQDF(a)
    0.868588963806503655302257837833210164588794011607333132228907565
```

So in this case it isn't so much a failure of an RQDF element (which should always print the same), but a numerical inconsistency from coercion the result into the quad double ring, i.e. coercion to the ring with lower precision. If the fix is to add "..." here we should comment on the fact that coercion causes the numerical noise and that RQDF is not at fault for that.

Cheers,

Michael


---

Comment by mabshoff created at 2008-02-22 19:40:47

Changing assignee from failure to mabshoff.


---

Comment by mabshoff created at 2008-02-22 19:40:47

Changing status from new to assigned.


---

Comment by was created at 2008-02-22 21:07:13

>  precision. If the fix is to add "..." here we should comment on the fact
> that coercion causes the numerical noise and that RQDF is not at fault for
> that.

I agree.


---

Attachment


---

Comment by mabshoff created at 2008-02-22 22:12:30

Resolution: fixed


---

Comment by mabshoff created at 2008-02-22 22:12:30

Merged in Sage 2.10.2.final

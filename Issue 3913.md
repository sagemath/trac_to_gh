# Issue 3913: order function not defined for ideal classes

Issue created by migration from https://trac.sagemath.org/ticket/3913

Original creator: cremona

Original creation time: 2008-08-20 16:36:43

Assignee: was

CC:  alexghitza

In 3.1 you can't ask for the order of an ideal class.  Example:

```
sage: K.<w>=QuadraticField(-23)
sage: OK=K.ring_of_integers()
sage: C=OK.class_group()
sage: h=C.order()
sage: P2a,P2b=[P for P,e in (2*OK).factor()]
sage: c=C(P2a); c
Fractional ideal class (2, 1/2*w - 1/2)
sage: c.order()
#boom
```


This is easily provided:

```
sage: sage.groups.generic.order_from_multiple(c,c.parent().order(),operation='*')
3
```


Patch coming up.



---

Attachment

The patch implements this, and adds doctests to some other functions.  Based on 3.1.1, and all doctests in sage/rings/number_fields pass.


---

Comment by AlexGhitza created at 2008-08-27 07:12:43

Looks good and passes doctests.  Also, when this gets merged, #1400 should be closed as a duplicate (note btw that John's patch addresses precisely Nick's objection on #1400).


---

Comment by mabshoff created at 2008-08-27 07:54:18

Resolution: fixed


---

Comment by mabshoff created at 2008-08-27 07:54:18

Merged in Sage 3.1.2.alpha1


---

Comment by cremona created at 2008-08-27 08:10:02

Replying to [comment:3 AlexGhitza]:
> Looks good and passes doctests.  Also, when this gets merged, #1400 should be closed as a duplicate (note btw that John's patch addresses precisely Nick's objection on #1400).

Thanks -- sorry to have opened a new ticket unnecessarily (I did look, honest).  In any case this patch is more efficient, and shows how useful the generic algorithms I implemented are!

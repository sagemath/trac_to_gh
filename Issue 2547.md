# Issue 2547: Implement gradient(), hessian() for callable function rings

Issue created by migration from Trac.

Original creator: edrex

Original creation time: 2008-03-16 16:46:18

Assignee: joyner

This is the extent of my understanding of what #2143 does, perhaps there are other new methods that should be implemented for function rings, or other rings which should have this.

This relates to making vectors over function rings see #2546


---

Comment by gfurnish created at 2008-03-16 20:09:24

Changing assignee from joyner to gfurnish.


---

Comment by gfurnish created at 2008-03-16 20:09:24

Changing status from new to assigned.


---

Comment by was created at 2008-03-16 20:51:24

Resolution: invalid


---

Comment by was created at 2008-03-16 20:51:24

This is not a clear precise task.  This could be discussed on sage-devel.


---

Comment by was created at 2008-03-16 20:57:23

Resolution changed from invalid to 


---

Comment by was created at 2008-03-16 20:57:23

Changing status from closed to reopened.


---

Comment by was created at 2008-03-16 20:58:03


```
13:57 < jkantor> The fact that gradient doesn't work with functions defined as f(x,y) is 
                 something I was aware of and was going to fix
```



---

Comment by was created at 2008-03-16 20:58:22

Changing assignee from gfurnish to jkantor.


---

Comment by was created at 2008-03-16 20:58:22

Changing status from reopened to new.


---

Comment by gfurnish created at 2008-03-16 21:34:15

Changing component from group_theory to calculus.


---

Comment by jwmerrill created at 2008-08-31 15:06:25

See also #3941 regarding the symbolic jacobian.


---

Comment by jwmerrill created at 2008-09-01 02:50:42

I did a little spelunking on this one, and so far, what it appears to come down to is that is_field is not implemented on CallableSymbolicExpressionRing_class, but it is implemented (and is True) on SymbolicExpressionRing_class.


---

Attachment


---

Comment by jwmerrill created at 2008-09-01 04:33:55

Changing assignee from jkantor to jwmerrill.


---

Comment by jwmerrill created at 2008-09-01 04:33:55

This patch implements the gradient and hessian (along with doctests) on callable symbolic expressions.  In order to make this work, I added an is_field method on CallablesSymbolicExpressionRing_class, which just returns true.  This is the same behavior as SymbolicExpressionRing_class, which seems appropriate.  I checked that addition and multiplication work okay with callable symbolic expressions, so they seem like an okay ring to me.

This should take care of #3941 as well, I think, though I wonder if Sage should be more careful about making a distinction between the gradient (which really only makes sense in inner product spaces), and the jacobian, which is a more generally sensible object.


---

Comment by mhansen created at 2008-09-01 22:48:28

Looks good to me.


---

Comment by mabshoff created at 2008-09-02 10:08:49

Merged in Sage 3.1.2.alpha4


---

Comment by mabshoff created at 2008-09-02 10:08:49

Resolution: fixed

# Issue 4281: [with patch, needs review] elliptic curve doctest coverage (part 4)

Issue created by migration from https://trac.sagemath.org/ticket/4281

Original creator: zimmerma

Original creation time: 2008-10-14 13:47:05

Assignee: was

This is for the file ell_tate_curve.py. I was unable to doctest the _height function, which is used
as a closure. Also, the missing loads(dumps(..)) test fails:

```
sage: e = EllipticCurve('130a1')
sage: eq = e.tate_curve(5)
sage: eq == loads(dumps(eq))
False
```



---

Attachment


---

Attachment


---

Comment by zimmerma created at 2008-10-14 14:01:52

The second patch fixed a few typos (to be applied after the 1st one).


---

Comment by robertwb created at 2008-10-14 21:51:40

The attached patch fixes the loads/dumps issue.


---

Comment by wuthrich created at 2008-10-15 10:00:00

The last patch does not for fix it for me. Do I do something wrong ?
(This is the same patch as for #4289.)


---

Comment by zimmerma created at 2008-10-18 11:30:46

I agree with Chris. Probably Robert attached the wrong patch. This one (4281-tate-pickle.patch)
is already in 3.1.4 but the loads/dumps problem is still there:

```
----------------------------------------------------------------------
----------------------------------------------------------------------
| SAGE Version 3.1.4, Release Date: 2008-10-16                       |
| Type notebook() for the GUI, and license() for information.        |
sage: e = EllipticCurve('130a1')
sage: eq = e.tate_curve(5)
sage: eq == loads(dumps(eq))
False
```



---

Attachment

Yep, sorry, I posted the wrong patch. I've replaced it now.


---

Comment by zimmerma created at 2008-10-18 17:51:11

Robert's new patch is ok, thus I give a positive review for it.
However I cannot review my own patches...


---

Comment by cremona created at 2008-10-19 20:43:57

N.B. To apply the second patch properly I had to rename it to trac_4281_2.patch:  applying the patch failed when the suffix was patch2.

Apart from that, the sequence of patches applies fine and all tests in elliptic_curves pass.

I also learnt from robertwb's patch one way in which loads(dumps(*)) can fail, so will return to the other ticket...


---

Comment by wuthrich created at 2008-10-20 09:37:26

Strictly speaking there is still something to do. It checks if E and p are equal. In a perfect implementation this should be an elliptic curve over a local field and we should check if they are isomorphic over this field, not over Q.

But I agree that the patch fixes this by now and the ticket should be closed.


---

Comment by cremona created at 2008-10-20 09:44:46

Replying to [comment:8 wuthrich]:
> Strictly speaking there is still something to do. It checks if E and p are equal. In a perfect implementation this should be an elliptic curve over a local field and we should check if they are isomorphic over this field, not over Q.
> 

When we have a type to hold elliptic curves over local fields then this can perhaps be changed.  I also did not bother to compare the (possibly) cached power series which are part of the class's data.  As I see it, this _cmp_ function is only there for technical Pythonic reasons, and serious mathematical functionality would not be implemented via the == operator.


> But I agree that the patch fixes this by now and the ticket should be closed.

Good!  Thanks.


---

Comment by mabshoff created at 2008-10-20 14:01:54

Resolution: fixed


---

Comment by mabshoff created at 2008-10-20 14:01:54

Merged all three patches in Sage 3.2.alpha0

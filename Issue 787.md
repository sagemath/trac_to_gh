# Issue 787: quotient spaces of vector spaces

Issue created by migration from Trac.

Original creator: nbruin

Original creation time: 2007-10-02 13:41:40

Assignee: was

If V is a subspace of W then W.quotient(V) should give the quotient space U=W/V.

Left TODO:
  - overload "/" constructor ?
  - provide a section map U->W ?
  - install appropriate coercions ?


---

Attachment

implementation


---

Comment by was created at 2007-10-04 18:45:53

I think this should be replaced by Soroosh's code, which does this and much more.


---

Comment by was created at 2007-10-04 18:45:53

Resolution: duplicate


---

Comment by was created at 2007-10-05 07:54:16


```
What? and ditch my 2 lines of haiku-like sage code?

Seriously, though. The attached patch contains quite a bit more than
"quotient", as you are probably woefully aware of. Easiest is probably

 - apply the patch
 - delete "quotient" from sage/modules/free_module.py

Cheers,
```



---

Comment by was created at 2007-10-05 07:54:16

Resolution changed from duplicate to 


---

Comment by was created at 2007-10-05 07:54:16

Changing status from closed to reopened.


---

Comment by mabshoff created at 2007-10-18 14:10:11

We need to figure out if this still applies.

Cheers,

Michael


---

Comment by was created at 2007-11-03 15:00:18

This has lingered too long -- I need to deal with it.


---

Comment by was created at 2007-11-18 03:56:54

NOT ready: I still think "I think this should be replaced by Soroosh's code, which does this and much more."  I don't know the status of Soroosh's code.


---

Comment by mabshoff created at 2007-11-18 14:24:06

Soroosh's code, i.e. #1029 got merged. So should we invalidate this ticket?

Cheers,

Michael


---

Comment by was created at 2007-11-25 18:16:07

Almost done:


```
was_: sage: R = QQ^3; S = R.span([This is the Trac macro *1,2,3* that was inherited from the migration](https://trac.sagemath.org/wiki/WikiMacros#1,2,3-macro))
[10:14am] was_: sage: w = R.quotient(S)
[10:14am] was_: sage: w = R / S
[10:14am] was_: But the last goes boom.
[10:14am] was_: It would be 3-4 lines of code to fix that.
[10:14am] was_: Once that is fixed, then 787 is done
```



---

Comment by was created at 2007-12-01 20:41:53

Changing status from reopened to new.


---

Comment by was created at 2007-12-01 20:41:59

Changing status from new to assigned.


---

Comment by was created at 2007-12-01 20:43:55

A quick comment.  Even as is this is WRONG -- the algorithm used is buggy, evidently, or something, since


```
sage: A = QQ^3; V = A.span([[1,2,3], [4,5,6]])
sage: Q = V.quotient( V.span([V.0 + V.1]) ); Q
sage: Q[1](V.0 + V.1)
(1)
```


But Q[1] is the quotient map so should have `V.0 + V.1` in its kernel.


---

Attachment

This I think correctly really implements quotients of vector spaces.


---

Attachment

This is also needed (it fixes a docstring)


---

Comment by was created at 2007-12-02 03:12:33

this is also needed.


---

Attachment

instead of applying those three patches, this is a clean bundle.


---

Comment by mabshoff created at 2007-12-02 04:50:07

Resolution: fixed


---

Comment by mabshoff created at 2007-12-02 04:50:07

Merged in 2.8.15.alpha2.


---

Comment by roed created at 2007-12-02 05:07:54

Changes _repr_


---

Attachment

This was slightly buggy -- see Trac #1368 for a fix.

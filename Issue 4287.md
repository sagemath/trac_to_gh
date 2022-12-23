# Issue 4287: [with patch, needs review] improve elliptic curve doctest (part 5)

Issue created by migration from https://trac.sagemath.org/ticket/4287

Original creator: zimmerma

Original creation time: 2008-10-14 19:58:56

Assignee: was

CC:  robertwb

This is for the file formal_group.py. Note that adding a s == loads(dumps(s)) test revealed a
failure:

```
sage: E = EllipticCurve('11a')
sage: F = E.formal_group()
sage: F == loads(dumps(F))
False
```



---

Attachment


---

Comment by cremona created at 2008-10-19 20:02:25

Patch looks good and applies ok.  But as Paul says, we need to see why load(dumps(F))!=F for a formal group F.

I don't know how to fix this.


---

Attachment


---

Comment by cremona created at 2008-10-19 21:03:19

Replying to [comment:1 cremona]:
> Patch looks good and applies ok.  But as Paul says, we need to see why load(dumps(F))!=F for a formal group F.
> 
> I don't know how to fix this.

I didn't know, but now I do.  There was nothing wrong with loads() or dumps() for formal groups, but they were missing a _cmp_ function so the "==" comparison was not giving the expected answer.
The second patch (modelled on a similar one by robertwb for ell_tate_curve.py) seems to do the trick.  All tests pass in elliptic_curves.


---

Comment by cremona created at 2008-10-21 20:13:15

Robert (robertwb), I CC'd you on this hoping that you could say that I fixed this appropriately?  I was using a similar patch of yours as a model.  John


---

Comment by robertwb created at 2008-10-22 14:51:56

Yes, that looks good to me. (As does the other patch--though I only read it at SD 10, I didn't actually try it out yet).


---

Comment by AlexGhitza created at 2008-11-22 07:40:48

The two patches look good and apply cleanly against my 3.2.


---

Comment by mabshoff created at 2008-11-23 07:57:00

Merged in Sage 3.2.1.alpha0


---

Comment by mabshoff created at 2008-11-23 07:57:00

Resolution: fixed

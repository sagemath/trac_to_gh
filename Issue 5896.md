# Issue 5896: [with patch, needs trivial review] Documentation fix for lcalc interface.

Issue created by migration from Trac.

Original creator: craigcitro

Original creation time: 2009-04-26 00:43:03

Assignee: craigcitro

The documentation for `lcalc.twist_values` and `lcalc.twist_zeros` is wrong. It claims that the function computes all twists for `(d/.)` with `dmin <= d <= dmax`, but in fact, it computes it for all `(d/.)` such that the *conductor* lies between `dmin` and `dmax`. 

Trivial patch to fix this is attached.


---

Comment by cremona created at 2009-04-27 09:09:15

Minor quibble:  in the lcalc docs it says "Notice that with the --twist-quadratic option one is specifying the discriminant
which can be negative, while with the --twist-primitive option one is
specifying the conductor which should be positive. "   So one could argue that the character (-3/-) has discriminant -12 and conductor 12.

Since users might expect similar, would it be better to change "conductor `N`" to "discriminant `D`" in both places in the patch?


---

Comment by craigcitro created at 2009-04-27 09:36:03

That's a good point. The example I was playing with had a positive discriminant -- I honestly just didn't think of it. :) New patch.


---

Comment by craigcitro created at 2009-04-27 09:37:47

I'm suspicious of the patch I just attached. New one coming right up.


---

Attachment

Ok, it's ready to go.


---

Comment by cremona created at 2009-04-27 09:42:19

Would you believe, I picked up the suspicious patch, observed that it failed to apply, came back to the ticket and found that you had already replaced it!

This one is fine.  Positive review!  (moral: never say something is trivial....)


---

Comment by craigcitro created at 2009-04-27 09:58:07

> moral: never say something is trivial....

especially when trying to use english to express mathematics. :)


---

Comment by mabshoff created at 2009-04-30 01:48:29

Resolution: fixed


---

Comment by mabshoff created at 2009-04-30 01:48:29

Merged in Sage 3.4.2.rc0.

Cheers,

Michael

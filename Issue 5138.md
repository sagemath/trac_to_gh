# Issue 5138: implement computing manin constants of elliptic curves

Issue created by migration from https://trac.sagemath.org/ticket/5138

Original creator: was

Original creation time: 2009-01-30 15:59:11

Assignee: was




---

Comment by cremona created at 2009-01-30 17:08:46

Logic looks ok, but patch does not apply to 3.3.alpha2 cleanly.  Does it need alpha3?  If so a proper review will have to wait (at least until I get home).

Have you remembered 990h where the optimal curve is not #1?


---

Comment by was created at 2009-01-30 17:26:57

> Have you remembered 990h where the optimal curve is not #1? 

No, I forgot about that.  Is that the only example?  I will add a new command optimal_curve() that finds the optimal curve using your database and includes a workaround for 990h (and any other examples). 

> Logic looks ok, but patch does not apply to 3.3.alpha2 cleanly. 
> Does it need alpha3? If so a proper review will have to wait 
>(at least until I get home). 

I did it against alpha0.  I'll rebase it for alpha3.


---

Comment by cremona created at 2009-01-30 17:29:30

Replying to [comment:3 was]:
> > Have you remembered 990h where the optimal curve is not #1? 
> 
> No, I forgot about that.  Is that the only example?  I will add a new command optimal_curve() that finds the optimal curve using your database and includes a workaround for 990h (and any other examples). 

That's the only example, luckily.

> 
> > Logic looks ok, but patch does not apply to 3.3.alpha2 cleanly. 
> > Does it need alpha3? If so a proper review will have to wait 
> >(at least until I get home). 
> 
> I did it against alpha0.  I'll rebase it for alpha3. 

OK, I'll look at it again over the weekend.


---

Comment by was created at 2009-02-01 08:36:03

Thanks for pointing out the 990h issue which I had forgot.  I found a bug related to that (but not this ticket) and posted a fix at #5149.


---

Attachment


---

Comment by was created at 2009-02-01 09:26:01

The attached patch implements computation of the Manin constant with some caveats that are clearly spelled out in the docstrings.  Also, it fixes a serious bug in an internal function (_multiple_of_degree_of_isogeny_to_optimal_curve, which was just nonsense before).


---

Comment by cremona created at 2009-02-01 11:19:18

Patch applies cleanly to 3.3.alpha2 + #5139.  Tests pass BUT:

```
sage: Ellsage: EllipticCurve('990a1').optimal_curve()
---------------------------------------------------------------------------
RuntimeError          
```

since on line 3099 you set the number to 3 when N=990 for all isogeny classes, not just class h.

Somewhere in the database code I think we have utilities for splitting the label into its 3 components, by the way, which might be more transparent than (e.g.) stripping off the last character to get the number.


---

Comment by was created at 2009-02-01 21:16:23

Thanks John -- excellent catch.  And, I changed the code to use the code from database/cremona, as you suggested.


---

Attachment

Looks good!


---

Comment by mabshoff created at 2009-02-02 02:46:25

Resolution: fixed


---

Comment by mabshoff created at 2009-02-02 02:46:25

Merged both patches in Sage 3.3.alpha4.

Cheers,

Michael

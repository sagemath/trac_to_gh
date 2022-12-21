# Issue 2810: Use new generic code in elliptic_curve_finite_field

Issue created by migration from Trac.

Original creator: cremona

Original creation time: 2008-04-05 16:47:47

Assignee: mabshoff

After merging the new generic group functions (#210) there is no need for the specific versions implemented for elliptic curve groups.  This patch removes those and adjusts the code accordingly.

Based on 3.0.alpha1.



---

Attachment


---

Comment by mabshoff created at 2008-04-05 17:03:52

Changing component from Cygwin to algebra.


---

Comment by mabshoff created at 2008-04-05 17:03:52

Changing assignee from mabshoff to tbd.


---

Comment by AlexGhitza created at 2008-04-05 19:06:54

Looks good.

It causes a small doctest failure on line 95 of schemes/elliptic_curves/gp_cremona.py, since in elliptic_curve_finite_field you have gotten rid of _cremona_abgrp_data().  I think that doctest should just be removed from gp_cremona.py anyway, but I don't know whether you have good reasons to keep it around.

Anyway, after this doctest failure gets fixed one way or another I'm happy to give this a positive review.


---

Comment by cremona created at 2008-04-05 20:34:40

Sorry, I forgot to trim gp_cremona.py.

The only useful bits left in there now that the elliptic curves mod p construction is redundant are (1) analytic rank and (2) isogenies.

In both cases I regrard these as temporary, waiting bettwe implementations in Sage.

For the moement you can delete that one test which refers to ._cremona_abgrp_data().  But in fact you can also delete ellinit(e,p) and ellzp(e,p) too, and then that might require further trimming in other elliptic curves files.

I'll do it tomorrow.


---

Comment by cremona created at 2008-04-05 22:23:06

Replying to [comment:4 cremona]:
> Sorry, I forgot to trim gp_cremona.py.
> 
> The only useful bits left in there now that the elliptic curves mod p construction is redundant are (1) analytic rank and (2) isogenies.
> 
> In both cases I regrard these as temporary, waiting bettwe implementations in Sage.
> 
> For the moement you can delete that one test which refers to ._cremona_abgrp_data().  But in fact you can also delete ellinit(e,p) and ellzp(e,p) too, and then that might require further trimming in other elliptic curves files.
> 

On second thoughts we should still keep those in -- they provide the Weil pairing, which people regularly ask for, and it just needs a wrapper to my gp code to do that.

> I'll do it tomorrow.


---

Comment by malb created at 2008-04-05 22:57:05

*Review*
 * patch applies cleanly, looks good
 * I'll provide a fix for the `._cremona_abgrp_data()` in a sec.
 * I say apply.


---

Attachment


---

Comment by mabshoff created at 2008-04-05 23:38:38

Doctests pass with both patches applied.

Cheers,

Michael


---

Comment by mabshoff created at 2008-04-05 23:38:55

Merged in Sage 3.0.alpha2


---

Comment by mabshoff created at 2008-04-05 23:38:55

Resolution: fixed

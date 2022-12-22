# Issue 3109: elliptic curves -- implement P.divide(n) for P a point on an elliptic curve and n an integer

Issue created by migration from Trac.

Original creator: was

Original creation time: 2008-05-06 02:19:46

Assignee: was

Implement P.divide(n) for P a point on an elliptic curve and n an integer.  This will:

 1. try to find an explicit point Q defined over the same field as P such that n*Q == P.
 2. If no such Q exists, raise a ValueError.

Also, implement P.is_divisible_by(n) trivially in terms of the above, and document
the connection between the two functions.  Also, have both implemented in terms of
a third function that just finds the polynomial whose root is x(Q), so we
can implement is_divisible_by more efficiently. 

An algorithm to do this is described at the end of section 3 of 
    http://wstein.org/papers/kolyconj/

If you see this ticket and think of doing this, please immediately contact me (wstein`@`gmail.com) before, since I'm planning on doing this very soon.


---

Comment by was created at 2008-05-06 02:20:01

Changing type from defect to enhancement.


---

Attachment


```
{
Cremona:
>  For ages Magma would only do Inverse(MultiplicationBymMap(m))(P) which
>  would throw a run-time error if there were no solutions and give one
>  solution only if there were any.  So I wronte my own, until they got
>  around to DivisionPoints(P,m) which returns a list, possibly empty.

Something like that is next on my list.  Maybe instead of P.divide(m),
which is what I planned, for consistency 
I should do P.division_points(m), which can return a possibly empty list.    
```



---

Comment by was created at 2008-05-07 04:55:01

this adds lots of docs and fixes bugs.  finishes implementing full_division_polynomial and multiplication by n.


---

Attachment


---

Attachment


---

Comment by cremona created at 2008-05-07 07:22:25

Review under way.


---

Comment by cremona created at 2008-05-07 08:21:12

I applied the 3 patches in succession with no problems, and all the doctests in sage/schemes/elliptic_curves pass.

All very well written and commented and documented with excellent doctests.  I do have two issues, one more important than the other:

* (less important) We currently have no support for the coordinate ring of an elliptic curve (which would be the quotient ring K[x,y]/(F) where F is the bivariate polynomial defining E, and K is the field of definition.  This lack is rather noticable in the code, where this ring has to be created on the fly to do some reduction and is then thrown away.  A better solution, surely, would be to define a function E.coordinate_ring() and have these division polynomials live there.  I suspect that this suggestion would get a response (probably from David Kohel) that this should all be done as part of much more general scheme machinery, which is correct but will discourage someone (like me) from actually doing what would be pretty simple and useful.

* (more important) You restrict to short Weierstrass equations!  Why?  Users will want the general case.  Don't be nervous about the horrible more general recursion formulae (where as yo uobserve, there are typos in Solverman even in the simple case a1=a2=a3=0) since you can find them *all" in Sage already, not *once* but *twice* already!  See my gp script ell_divpt.gp and my C++ source file qcurves/divpol.cc

I really really think that we should implement this more general version for division polynomials now, even though your code for P.division_points() cleverly gets around it.

To end on a more positive note: this is very well written and a model for others to follow!


---

Comment by was created at 2008-05-07 15:38:58

Regarding the referee's report:

1. Regarding the coordinate ring, the issue is precisely what you say.  However I think that we shouldn't define coordinate ring code until we use it in a couple of places to see what the real issues are.   E.g., term orders, variable order, etc.  I think that should come *later* after the code I've defined has been used and works well and is well tested.  That should only be factored out when it is understood, not the other way around.  If I had written coordinate ring 3 days ago, it would have been completely useless for this code anyways, since I would have got the variable and term orders wrong.   AND maybe the variable and term order needed here is wrong for general affine coordinate rings.

2. Regarding only doing the short Weierstrass case.  It's all I need.  The more general case would be fine to do but should be a separate enhancement ticket.   And if it slows things down a lot -- and this *does* matter, then I will be unhappy.


---

Attachment

some slight refactoring in ell_point.py


---

Comment by cremona created at 2008-05-07 15:45:42

Comments on the comments:

1. I agree entirely.  I really believe that we need to get the basics right before being too fancy, since however clever the structures are one still has to get the formulas right!

2. So be it.  I doubt there would be a time penalty.  I may just do that myself (talk is cheap etc) but that should not delay this one.

Go for it!


---

Comment by was created at 2008-05-07 15:47:43

John said:
> (where as yo uobserve, there are typos in Solverman even in the simple case a1=a2=a3=0)

I just want to point out that there were no typos in Silverman in that case.  What is true
is that the formula he gives is right except it does not give the multiplication by m
map in exact one case -- the y-coordinate for m=2.  That's a special case the exercise
does not treat correctly.  It's not a typo but a mistake.  But for all other m it is right
and there are no typos.

Regarding your comments on my comments:
Yep, you should definitely go for it!  I just wrote this code since I need it for some research
I'm doing _now_.  Also, since it is for research I care a *lot* that it is right and that I understand it, which is partly why it is very well documented and tested.  If it is wrong, it is going to confuse me a lot later.  Oh, speed matters some too.


---

Comment by mabshoff created at 2008-05-07 16:09:17

Merged all four patches in Sage 3.0.2.alpha0


---

Comment by mabshoff created at 2008-05-07 16:09:17

Resolution: fixed

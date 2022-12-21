# Issue 598: implement substitute for monoids

Issue created by migration from Trac.

Original creator: was

Original creation time: 2007-09-06 00:56:30

Assignee: somebody


```
On 9/5/07, Joel B. Mohler <joel`@`kiwistrawberry.us> wrote:
\> Yes, so I found FreeMonoid after sending my first e-mail and was testing it
> out.  I think I may have found something that is not implemented:
> 
> sage: a=FreeMonoid(1,'a').0
> sage: a*a
> a^2
> sage: a.substitute(5)
> a  # should be 5?
> sage: a.substitute(a=5)
> a  # should be 5?
> 
> I would have expected those last two results to be 5 -- am I missing
> something? 

The whole "substitute" architecture was implemented in SAGE
long after monoids were implemented.  So you'll have to implement
monoid substitution. 

> I guess substituting isn't an entirely common operation for free
> monoids, but it seems to be a sensibly defined operation.  Then again, maybe
> not:
> 
> sage: M.<x,y> = FreeMonoid(2)
> sage: (x*y).substitute(x=1)
> x*y  # I would think that this is 1*y
> 



> I find that result unsatisfactory as well, but I sure don't have a good idea
> about what ring (?) the result '1*y' would be a part of.

Just do the arithmetic.    All monoids have a 1 by definition, so 1*y is just "y"
in that monoid.

William
```



---

Comment by was created at 2007-09-06 00:56:45

Changing assignee from somebody to jbmohler.


---

Comment by mhansen created at 2009-01-22 14:24:15

Changing status from new to assigned.


---

Comment by mhansen created at 2009-01-22 14:24:15

Changing assignee from jbmohler to mhansen.


---

Attachment


---

Comment by mhansen created at 2010-01-16 19:06:55

Changing status from new to needs_review.


---

Comment by zimmerma created at 2010-03-14 12:11:12

A positive review for me.

Note: I did all doctests, and got exactly 22 Segfaults, as with vanilla 4.3.3 (see #7773).
Thus if a new failure occurred within one of those 22 doctests, I couldn't see it.


---

Comment by zimmerma created at 2010-03-14 12:11:12

Changing status from needs_review to positive_review.


---

Comment by jhpalmieri created at 2010-04-15 05:20:29

Resolution: fixed


---

Comment by jhpalmieri created at 2010-04-15 05:20:29

Merged in 4.4.alpha0.

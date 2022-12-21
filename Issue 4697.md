# Issue 4697: change integration error message

Issue created by migration from Trac.

Original creator: was

Original creation time: 2008-12-04 21:55:14

Assignee: burcin

Fix the following instance by a trivial change to raising an exception.  This causes tons of confusion for (new) users, since there isn't any way to easily "discover" what to do.


```
On Dec 4, 3:07 pm, "William Stein" <wst...`@`gmail.com> wrote:
> Do you think it would be better if instead of
>
> sage: print integrate(integrate(f,y,x^3,x^0.5),y,0,1)
> ... Is  x  positive or negative?
>
> one saw:
> ... Is  x  positive or negative?  (Try using the assume command.)

I think the latter is more intuitive; in fact, I would go as far as to
do something like this:

 ... Is x positive or negative? (Try the assume(x>0) command before
 integral evaluation)

Thanks,

```



---

Attachment

Based on 3.3.alpha0


---

Comment by kcrisman created at 2009-01-29 01:04:06

This patch improves the error message Sage sends along with the Maxima constraint request.  The message is rather longish, but here probably extreme clarity is best, based on the original reporter's point about new users.  Some doctests for the _expect_expr function are also added.

This passes testing interfaces/maxima.py, and should be okay on calculus.py (which I can't test because it always times out); I couldn't find any other references to this error message but I think I got them all.


---

Comment by mabshoff created at 2009-01-29 01:14:15

With that patch applied to my 3.3.alpha3 merge tree all doctests pass.

Cheers,

Michael


---

Comment by mabshoff created at 2009-01-29 01:16:34

This was a positive review by the way :) - I just forgot to add it to the doctest comment. Nice docstring and doctesting by the way, too.

Cheers,

Michael


---

Comment by mabshoff created at 2009-01-29 01:17:30

Merged in Sage 3.3.alpha3.

Cheers,

Michael


---

Comment by mabshoff created at 2009-01-29 01:17:30

Resolution: fixed

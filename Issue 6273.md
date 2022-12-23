# Issue 6273: Improve random_element for number field orders and ideals (easy)

Issue created by migration from https://trac.sagemath.org/ticket/6273

Original creator: davidloeffler

Original creation time: 2009-06-13 10:36:05

Assignee: was

At the moment, random_element for number field orders returns a random integer coerced into the order, which isn't very useful. A much better solution would be to use the random_element method of the underlying free ZZ-module. 

More generally, one could ask for the same functionality for fractional ideals (and the above would be the special case for the ideal (1).)


---

Comment by cremona created at 2009-06-13 19:44:06

I have implemented this.  using the random_element() function for ZZ and integral bases.  It works for absolute and relative orders and ideals.

I started out using the random_element() function for the module class, but that did not work in the relative situation.  It is a little strange that the classes for orders and ideals do not derive from free ZZ-modules.


---

Comment by cremona created at 2009-06-13 19:44:26

Changing keywords from "" to "number field ideal order".


---

Comment by was created at 2009-06-14 10:30:39

REVIEW:

I think it would be better to do

```
 def random_element(self, *args, **kwds)
```

then in the docstring say that the inputs are identical to ZZ.random_element, whatever those are.  This will if ZZ.random_element is ever improved, changed, or extended in any way (and let's hope it is), then this docstring won't have to change. 

Then in the call to ZZ.random_element, just do ZZ.random_element(*args, **kwds).  This shorter and more robust.

 -- William


---

Comment by cremona created at 2009-06-14 15:36:08

Replying to [comment:3 was]:
> REVIEW:
> 
> I think it would be better to do
> {{{
>  def random_element(self, *args, **kwds)
> }}}
> then in the docstring say that the inputs are identical to ZZ.random_element, whatever those are.  This will if ZZ.random_element is ever improved, changed, or extended in any way (and let's hope it is), then this docstring won't have to change. 
> 
> Then in the call to ZZ.random_element, just do ZZ.random_element(*args, **kwds).  This shorter and more robust.
> 
>  -- William

OK, I'll do that.  John


---

Attachment

The revised patch does what was asked for in the review!


---

Comment by ncalexan created at 2009-06-15 20:57:10

In the relative case, the parents are wrong.  I am fixing this right now.


---

Comment by cremona created at 2009-06-15 20:58:43

Sorry about that.  I'll review your fix as soon as I can.  John


---

Attachment

The new patch sorts out the parent problem ok, with suitable new doctests.  I note that you now delegate the random function for orders to that of ideals -- this means that the new code is *not* used for non-maximal order, unfortunately.  But then the same was true for my version.

So I would have given this a positive review, while noting that at some point non-maximal orders will need to be dealt with too.

Unfortunately:

```
sage -t  "devel/sage-6273/sage/rings/number_field/number_field_ideal.py"
**********************************************************************
File "/home/john/sage-4.0.2.rc0/devel/sage-6273/sage/rings/number_field/number_field_ideal.py", line 1045:
    sage: I.basis()
Expected:
    [3, -a + 1, (-3/2*b - 1497/2)*a, (-1/2*b - 499/2)*a - b - 499]
Got:
    [3, a + 2, (3/2*b + 1497/2)*a, (b + 499)*a - b - 499]
```

so it's still "needs work"


---

Comment by ncalexan created at 2009-06-15 22:38:02

Replying to [comment:8 cremona]:
> The new patch sorts out the parent problem ok, with suitable new doctests.  I note that you now delegate the random function for orders to that of ideals -- this means that the new code is *not* used for non-maximal order, unfortunately.  But then the same was true for my version.
> 
> So I would have given this a positive review, while noting that at some point non-maximal orders will need to be dealt with too.
> 
> Unfortunately:
> {{{
> sage -t  "devel/sage-6273/sage/rings/number_field/number_field_ideal.py"
> **********************************************************************
> File "/home/john/sage-4.0.2.rc0/devel/sage-6273/sage/rings/number_field/number_field_ideal.py", line 1045:
>     sage: I.basis()
> Expected:
>     [3, -a + 1, (-3/2*b - 1497/2)*a, (-1/2*b - 499/2)*a - b - 499]
> Got:
>     [3, a + 2, (3/2*b + 1497/2)*a, (b + 499)*a - b - 499]
> }}}
> so it's still "needs work"

Let's just comment out both basis lines (since basis works, and it's essentially random).  Can you make non-maximal orders work with the previous code?  If so, do it and I will review.


---

Attachment

Replaces both previous


---

Comment by cremona created at 2009-06-16 09:54:45

I removed the lines showing the bases (which were not part of the test exactly, just there for illustration).  I reinstated my original for orders, since it works for non-maximal orders, and added a new doctest to show that;  but I kept in the additional doctests from the review patch to show that theparent are now correct (which I also borrowed from the review patch).

This one tests ok on both 32- and 64-bit, and I hope contains the best of both earlier patches with none of the problems!  And in view of the trouble this took to get right, I removed the "(easy)" from the ticket's title!


---

Comment by ncalexan created at 2009-06-16 17:54:12

I'm a fan!


---

Comment by rlm created at 2009-06-24 09:59:13

Resolution: fixed

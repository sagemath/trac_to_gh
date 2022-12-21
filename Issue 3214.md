# Issue 3214: gcd needs improved coersion

Issue created by migration from Trac.

Original creator: novoselt

Original creation time: 2008-05-16 02:25:48

Assignee: somebody

CC:  robertwb craigcitro cremona burcin

I got very confused by the first line since I used to use gcd for clearing denominators:


```
sage: gcd((1, 2/3, 1/6, 1/6))
1
sage: gcd((2/3, 1/6, 1/6))
1/6
sage: gcd((2/3, 1, 1/6, 1/6))
Traceback (most recent call last):
...
TypeError: Argument 'other' has incorrect type (expected sage.rings.rational.Rational, got sage.rings.integer.Integer)
sage: gcd((2/3, 2/2, 1/6, 1/6))
1/6
```


I'd expect all calls above to return 1/6.


---

Comment by mabshoff created at 2008-10-27 06:12:07

Resolution: fixed


---

Comment by mabshoff created at 2008-10-27 06:12:07

This works now:

```
----------------------------------------------------------------------
----------------------------------------------------------------------
| Sage Version 3.2.alpha1, Release Date: 2008-10-26                  |
| Type notebook() for the GUI, and license() for information.        |
sage: gcd((2/3, 1, 1/6, 1/6))
1/6
```


Cheers,

Michael


---

Comment by mabshoff created at 2008-10-27 06:19:01

Resolution changed from fixed to 


---

Comment by mabshoff created at 2008-10-27 06:19:01

But the first case is still broken. This might not be coercion related, though.

Cheers,

Michael


---

Comment by mabshoff created at 2008-10-27 06:19:01

Changing status from closed to reopened.


---

Comment by mabshoff created at 2008-11-30 23:52:45

This seems critical enough to elevate its priority. Also CC some people who might be able and willing to fix it :)

Cheers,

Michael


---

Comment by mabshoff created at 2008-11-30 23:52:53

Changing priority from minor to critical.


---

Comment by AlexGhitza created at 2008-12-28 13:06:46

It is indeed not coercion-related.  The computation of the gcd is done in a loop, from which one exits as soon as a gcd of 1 is obtained (ignoring the rest of the elements).  In the case of elements with denominators (such as rational numbers or rational functions) this gives rise to the wrong answers reported above.

The attached trivial patch fixes this so that correct answers are returned.


---

Comment by mabshoff created at 2008-12-28 15:35:25

Changing priority from critical to blocker.


---

Comment by mabshoff created at 2008-12-28 15:35:25

Arg, this really ought to go into 3.3.

Thanks for tracking this down Alex,

Michael


---

Comment by cremona created at 2008-12-28 16:57:03

Hmmm.  It seems a real pity to just delete the quick exit line since in most circumstances as soon as you have a unit you can return 1.  This will result in a lot of calls to vi.gcd(g) where vi is random and g==1, so those had better be caught efficiently in the member gcd() function.  (Incidentally, there was a reason for putting vi.gcd(g) and not g.gcd(vi), which I now forget.) 

It's another field-of-fractions thing;  in the example we are not really treating the rationals as elements of QQ, but as scaled elements of ZZ, where x.div(y) means y/x in ZZ even though x,y may be in QQ.  Testing for .is_unit() certainly would not be appropriate.  I cannot see a better way than what the patch does, unless we give up the nice behaviour that the gcd of a set of rationals is defined to be a generator of the ZZ-module they span.


---

Comment by robertwb created at 2008-12-29 19:59:36

I agree that the quick exit shouldn't be deleted. I would propose either constructing a sequence (so all elements live in the same domain to begin with) or having the exit verify that the parents are all the same type (much faster than calling gcd).


---

Comment by AlexGhitza created at 2008-12-30 09:25:37

Robert, I'm not sure I understand your suggestion.  The current code already constructs a sequence.  The problem is that when the universe of that sequence is QQ, bailing out of the loop as soon as one gets 1 is wrong.

If QQ were the only obstruction this would be easy to fix, but the same will happen with other fraction fields (number fields, p-adics, rational functions, etc.)

I'm actually getting more and more convinced that I don't like this use of gcd for fraction fields anyway; but I'll take this to sage-devel and see what people think.


---

Comment by robertwb created at 2008-12-30 09:39:39

You have a good point. I've never used this function for elements of a fraction field, so I'm not even sure what the intended behavior/use cases are.

Please post to sage-devel, hopefully it will shed some light on what should happen here.


---

Attachment

OK, following the discussion at http://groups.google.com/group/sage-devel/browse_thread/thread/35abc577b5ba78e7/170c0da22b9a36b9#170c0da22b9a36b9 I am implementing a trivial gcd() method for rational numbers and renaming the current rational gcd() to content().
The (newly) attached patch also touches a few other files in the sage library that are affected by this.

There is one doctest failure that I don't know how to deal with, in the symbolic gcd of ginac; sage -t symbolic/expression.pyx exposes this.


---

Comment by cremona created at 2009-01-13 21:45:57

I applied the patch successfully to 3.2.3.   Alex has done a good job of testing -- I did not do a testall, just tested all in sage/rings.

It took me a few seconds (well, minutes) to see that gcd(nums)/lcm(denoms) was the right answer.  nice!

I found it hard to use the content function though.  None of these work if L is a list of integers or rationals:  L.content(), content(L), QQ.content(L), ZZ.content(L).  Can we not have these?  Also if v is an element of `ZZ^n` then v.content() would also be useful.  I could perhaps be persuaded to put these enhancements into a different ticket.

I don't know what to do about the ginac failure:

```
sage: var('x,y',ns=1)
(x, y)
sage: f = -289*x*y - 17*x^2*y + 3/7*x^5*y + x^7 + 17*x^6 + 2/3*x^2 - 51/7*y^2 + 34/3*x + 2/7*y
sage: g = -289*x*y + 3/7*x^5*y - 17*x^13*y + x^18 + 2/3*x^13 + 17*x^6 - 51/7*y^2 + 34/3*x + 2/7*y
sage: f.gcd(g)
<boom>
```

It fails trying to convert a non-integral rational to an integer.  Simpler polys in place of f anf g work fine.  As I don't even know what ginac is or does I'm stuck!


---

Comment by mabshoff created at 2009-02-02 02:22:12

Burcin,

can you take a look at this since the pynac issue is holding up this patch?

Somebody else ought to change the summary of this ticket since this is not related to coercion at all.

Cheers,

Michael


---

Comment by AlexGhitza created at 2009-02-02 03:32:28

Changed the summary to something a little more descriptive.

The right time to work on fixing the pynac issue would have been SD12 since both Burcin and I were there, but (as always) other stuff got in the way.  Anyway, I really don't know how to even start fixing this issue, so hints (or fixes) would be highly appreciated.


---

Attachment

I finally found time to look at this.

attachment:trac_3214-py_gcd.patch fixes the doctest problem. It is not a very clean solution, but since we are going to switch to using Sage/Singular for gcd's it's not worth investing more time in this.

If someone can look over my 2 line patch, and change the subject to "positive review", maybe this can still make it to 3.3.


---

Comment by AlexGhitza created at 2009-02-08 22:09:29

Looks good.

Thanks a lot, Burcin.


---

Comment by mabshoff created at 2009-02-09 08:25:18

Merged both patches in Sage 3.3.rc0.

Cheers,

Michael


---

Comment by mabshoff created at 2009-02-09 08:25:18

Resolution: fixed

# Issue 3979: Power series composition messes up precision

Issue created by migration from https://trac.sagemath.org/ticket/3979

Original creator: kedlaya

Original creation time: 2008-08-28 20:16:02

Assignee: burcin

CC:  chapoton

Keywords: power series, composition, precision

The composition of two power series is sometimes returned with the wrong precision. A trivial example:

```
sage: pow.<u> = PowerSeriesRing(Rationals()); print (1 + O(u^4))(u)
1
```

where the return value should have precision 4 rather than infinity. A more nontrivial example:

```
sage: pow.<u> = PowerSeriesRing(Rationals()); print (1 + u^2 + O(u^4))(u^2)
1 + u^4 + O(u^10)
```

where the return value should have precision 8 instead of 10.


---

Comment by kedlaya created at 2009-01-23 19:55:21

A closely related issue is #5075.


---

Comment by burcin created at 2009-04-16 11:38:17

Changing component from calculus to basic arithmetic.


---

Comment by burcin created at 2009-04-16 11:38:17

Changing assignee from burcin to somebody.


---

Comment by fwclarke created at 2011-07-18 12:11:24

Changing status from new to needs_review.


---

Comment by fwclarke created at 2011-07-18 12:11:24

Changing priority from major to critical.


---

Comment by fwclarke created at 2011-07-18 12:11:24

Changing component from basic arithmetic to algebra.


---

Attachment

In the attached patch I have completely rewritten `sage.rings.power_series_poly.__call__`.  Several errors in the old version have been corrected.  The new version more closely follows the corresponding function for polynomials, in particular referring to variables by name is now possible.

In order to make the `__call__` function work correctly it was necessary to change the behaviour of `sage.rings.power_series_poly.valuation`.  At the moment


```
sage: R.<x> = QQ[]
sage: O(x^3).valuation()
+Infinity
```

If we interpret `O(x^3)` as `x^3` times an unknown power series, then the valuation could be anywhere between 3 and infinity, but 3 is a much better, and more cautious, estimate than infinity.  It is also very strange to have a series whose valuation is greater than its precision.  The new convention is also consistent with what happens for p-adic integers:


```
sage: O(7^3).valuation()
3
```

In the course of checking the power series code, a minor mistake in the polynomial code has been found and corrected.

A doctest in `sage/rings/morphism.pyx` needed adjusting.

I have also deleted the doctest in `sage.rings.power_series_mpoly.__call__` for two reason's : (1) it doesn't use this function; (2) it makes no sense anyway.  Besides the first line of the file is


```
# NOT ready to be used -- possibly should be deleted.
```



---

Comment by fwclarke created at 2011-07-18 12:13:18

Replying to [comment:1 kedlaya]:
> A closely related issue is #5075.

Related, but I don't believe it's the same.  The problem in #5075 is still there after the patch.


---

Comment by kedlaya created at 2011-08-01 07:53:33

Changing status from needs_review to needs_work.


---

Comment by kedlaya created at 2011-08-01 07:53:33

The patch looks reasonable on its own. However, changing the call syntax for power series generates quite a number of doctest failures elsewhere, by triggering the error message

```
ValueError: Cannot substitute this value
```

Here are the examples I found in the rings and schemes directories; there may be more elsewhere that I didn't find. (This used 4.7.1.rc1, but I don't think the version much matters.)

```
sage -t  "devel/sage/sage/rings/multi_power_series_ring.py"
sage -t  "devel/sage/sage/rings/laurent_series_ring_element.pyx"
sage -t  "devel/sage/sage/rings/multi_power_series_ring_element.py"
sage -t  "devel/sage/sage/rings/power_series_ring.py"
sage -t  "devel/sage/sage/schemes/hyperelliptic_curves/hyperelliptic_generic.py"
sage -t  "devel/sage/sage/schemes/hyperelliptic_curves/hyperelliptic_padic_field.py"
sage -t  "devel/sage/sage/schemes/elliptic_curves/ell_wp.py"
sage -t  "devel/sage/sage/schemes/elliptic_curves/formal_group.py"
sage -t  "devel/sage/sage/schemes/elliptic_curves/ell_rational_field.py"
sage -t  "devel/sage/sage/schemes/elliptic_curves/padic_lseries.py"
sage -t  "devel/sage/sage/schemes/elliptic_curves/padics.py"
```


This patch can't receive a positive review with all these broken doctests. The best thing would be to fix them all now, but if that is infeasible, I would propose the following.

1. Deprecate the old syntax: accept it while raising a `DeprecationWarning`.

2. Once this ticket is closed, open a second ticket to modify the syntax in the other doctests.

3. Once the second ticket is closed, open a third ticket to remove the old syntax.


---

Comment by fwclarke created at 2011-08-17 19:12:50

Replying to [comment:5 kedlaya]:

Yes, I'm sorry to have missed those failures.

I've been able to fix most of them.  The code in `schemes/elliptic_curves/formal_group.py` was problematic since iterated univariate power series were used to approximate a power series ring in two variables, but this should be simple to fix with the multiple variable power series available in 4.7.1.  More difficult to deal with may be the failures in `schemes/hyperelliptic_curves/hyperelliptic_padic_field.py` since the problem here is with substitutions in power series with a known p-adic radius of convergence.

I'll get back to this in a couple of weeks.


---

Comment by fwclarke created at 2011-09-21 17:36:50

Apply only this file


---

Attachment

I have attached a revised patch.  All the previous failures have been dealt with.  Some changes were essentially trivial, but more major were:

 1. Formal groups for elliptic curves have been rewritten to exploit the multi-variable power series code available since 4.7.1

 2. `local_coordinates_at_weierstrass` in `sage/schemes/hyperelliptic_curves/hyperelliptic_generic.py` has been substantially simplified.

 3. At several places in `sage/schemes/hyperelliptic_curves/hyperelliptic_padic_field.py` substitution in a power series has had to be replaced by substitution in the underlying polynomial.  This works for now because in these instances the p-adic radius of convergence is known.


---

Comment by fwclarke created at 2011-09-21 17:53:07

Changing status from needs_work to needs_review.


---

Comment by lftabera created at 2011-10-11 13:41:42

Changing status from needs_review to needs_work.


---

Comment by lftabera created at 2011-10-11 13:41:42

Some problems I have found

This should work


```
sage: x=polygen(QQ)
sage: f = 1 + 3*x + O(x^2)
sage: f(x)
...
ValueError
```


This should raise an error:


```
sage: x = LaurentSeriesRing(QQ,'x').gen()
sage: f = x + O(x^2)
sage: f(~x)
O(x^-2)
```


You cannot substitute x by 1/x on a power series unless it is a Laurent polynomial.

Suggestions, comments:

On file laurent_series_ring_element.pyx

`@`446 def laurentpolynomial(...

Improve the documentation. By what is written it seems that the output should be a Laurent polynomial but the method actually returns a Laurent power series. 

`@`1141  __call__ documentation, specify that x needs to have a valuation at least 1.

`@`1165  raise ValueError, "must not specify %s keyword and positional argument" % name

Add a doctest to the __call__ method with both keywords and positional arguments one that works (name!= keyword) and one that raises the error, other possibilities welcomed.

On file multi_power_series_ring

`@`964,989 improve documentation, not clear if the input can be polynomials, powerseries, powerseries + bigoh or in which ring is the result. If we can use big_Oh in the input etc. Maybe for another ticket.

On file local_generic_element.pyx

`@`140 I would write: Returns self up to reduced precision `prec`.

On file polynomial_element.pyx

`@`461-467 doctest should go in the TESTS section.

`@`567  raise ValueError, "must not specify %s keyword and positional argument" % name

On file power_series_mpoly

`@`74 Add documentation and a valid example to the __call__ method.  Each method or function that is modified need to have a correct documentation and doctest.

On file power_series_poly

`@`290 raise ValueError, "must not specify %s keyword and positional argument" % name

`@`936 This is a bug and should be fixed. This is a regression since this works without the patch (except for the incorrect precision).

On file scheme.py

`@`178 temp2 = temp.exp().change_ring(ZZ)

Is there a reason you want a powerseries in ZZ instead of QQ?


---

Comment by fwclarke created at 2011-10-12 11:16:22

Replying to [comment:8 lftabera]:

Thanks for your careful look at the patch.  Most of the problems can be fixed quite easily, though the one at line 936 in `power_series_poly` could be more difficult.  I hope to submit a new patch soon.

> On file power_series_mpoly `@`74 Add documentation and a valid example to the __call__ method.  Each method or function that is modified need to have a correct documentation and doctest.

The reason I  removed rather than corrected the doctest in `power_series_mpoly` was that it does *not* test this `__call__` function but the one in  `power_series_poly` (I've seen too many such doctests).  In fact I'm not sure that this file is used at all.  In fact the first line is


```
# NOT ready to be used -- possibly should be deleted.
```

However I didn't have the confidence to delete it myself, and add other issues to an already complicated patch.  

Adding documentation to this function would be hard to do since the whole file is so poorly documented that I can't understand what it's for.


---

Comment by cremona created at 2011-11-03 15:14:15

Apologies for hijacking this ticket for this:  Francis, what is your email address?   F.Clarke`@`swansea.ac.uk is bouncing!  John (john.cremona`@`gmail.com)


---

Comment by fwclarke created at 2012-05-13 09:41:31

Replaces previous revised patch


---

Attachment

Replying to [comment:8 lftabera]:

Finally I have a revised patch.  I have applied all your suggestions with two exceptions.  Comments on some of them follow:

> On file laurent_series_ring_element.pyx `@`446 

Rather than changing the documentation I have changed the code, so it does now return a Laurent polynomial.

> On file multi_power_series_ring  `@`964,989

I've left this for another ticket, as you suggested.

> On file power_series_mpoly `@`74 

I've left this unchanged, for reasons explained [comment:9 above]. 

> On file scheme.py `@`178

I've undone this change.  It belongs in another ticket.


---

Comment by fwclarke created at 2012-05-13 09:56:54

Changing status from needs_work to needs_review.


---

Comment by fwclarke created at 2012-05-13 10:05:36

Note that the patch corrects a bug raised in #12931.


---

Comment by chapoton created at 2012-08-26 09:06:37

Trying to help the bot:

Apply only trac_3979_power_series_substitution_rev2.patch


---

Comment by chapoton created at 2012-08-26 09:29:14

The patch must be rebased on a recent version.


---

Comment by chapoton created at 2012-08-26 09:29:14

Changing status from needs_review to needs_work.


---

Comment by fwclarke created at 2012-08-26 21:47:56

Rebased for 5.2


---

Comment by fwclarke created at 2012-08-26 21:51:30

Changing status from needs_work to needs_review.


---

Attachment

Replying to [comment:15 chapoton]:
> The patch must be rebased on a recent version.

I've attached new patch.  

I hope it can be reviewed before this has to be done again.


---

Comment by chapoton created at 2012-08-27 11:41:15

Apply only trac_3979_power_series_substitution_rev3.patch


---

Comment by chapoton created at 2012-08-27 17:08:27

Apply only trac_3979_power_series_substitution_rev4.patch


---

Comment by chapoton created at 2012-08-27 19:28:24

I would like to see, when possible, a more specific error instead of

```
raise ValueError, "Cannot substitute this value" 
```

In particular, when this is because of negative valuation, one should say it.


---

Comment by fwclarke created at 2012-08-27 21:40:09

apply after trac_3979_power_series_substitution_rev4.patch


---

Attachment

Replying to [comment:21 chapoton]:
> I would like to see, when possible, a more specific error instead of
> {{{
> raise ValueError, "Cannot substitute this value" 
> }}}
> In particular, when this is because of negative valuation, one should say it.

A good point.  The new patch (to be applied after trac_3979_power_series_substitution_rev4.patch) gives a more explicit error message.


---

Attachment


---

Comment by chapoton created at 2012-09-24 18:59:29

Changing status from needs_review to positive_review.


---

Comment by chapoton created at 2012-09-24 18:59:29

This looks good to me. The patches applies smoothly on 5.4beta1. All tests pass. This ticket solves some embarassing problems and is much wanted. Positive review !


---

Comment by chapoton created at 2012-09-26 10:51:09

The bot is back and is unhappy because the patch removes one test in rings/power_series_mpoly.pyx

This should be easy to correct, if really required to close the ticket.


---

Comment by fwclarke created at 2012-09-26 17:28:38

Replying to [comment:25 chapoton]:
> The bot is back and is unhappy because the patch removes one test in rings/power_series_mpoly.pyx
> 
> This should be easy to correct, if really required to close the ticket.

As I said in July last year:

   I have also deleted the doctest in `sage.rings.power_series_mpoly.__call__` for two reasons : (1) it doesn't use this function; (2) it makes no sense anyway. Besides the first line of the file is

```
# NOT ready to be used -- possibly should be deleted.
```


And I explained this more fully a year ago:

   The reason I removed rather than corrected the doctest in `power_series_mpoly` was that it does not test this `__call__` function but the one in `power_series_poly` (I've seen too many such doctests). In fact I'm not sure that this file is used at all. In fact the first line is

```
# NOT ready to be used -- possibly should be deleted.
```

   However I didn't have the confidence to delete it myself, and add other issues to an already complicated patch.  

   Adding documentation to this function would be hard to do since the whole file is so poorly documented that I can't understand what it's for.

I have now understood how to create an element of the relevant type (something that isn't done anywhere else, as far as I can see):

```
sage: S.<x> = QQ[]
sage: R = sage.rings.power_series_ring.PowerSeriesRing_generic(S, 
            't', use_lazy_mpoly_ring=True)
sage: t = R.gen()
sage: f = 3 - x*t^3 + O(t^5)
sage: type(f)
<type 'sage.rings.power_series_mpoly.PowerSeries_mpoly'>
sage: f(2)
-2*t^3 + 3
sage: f(2, t^2)
3 - 2*t^6
```

The final answers are wrong (they shouldn't have infinite precision), inconsistent (the first is a polynomial, the second a power series), and the syntax is non-standard.  Compare

```
sage: T.<u> = S[[]]
sage: g = 3 - x*u^3 + O(u^5)
sage: g(u^2, 2)
3 - 2*u^6 + O(u^10)
sage: g(u^2)
3 - x*u^6 + O(u^10)
```

Of course `g(2)` raises an error.

However, I have made a supplementary patch which reinserts into `power_series_mpoly.pyx` a doctest based on the above.  This should appease the patchbot, and though problematic it is less bad than before.  The alternative would be to rewrite much of the code in `power_series_mpoly.pyx`, which would seem to be a waste of time if it is destined for deletion.


---

Comment by fwclarke created at 2012-09-26 17:36:55

Apply after trac_3979_power_series_substitution_rev4_extra.patch


---

Attachment


---

Comment by fwclarke created at 2012-09-27 12:06:52

Apply only this patch


---

Attachment

The patchbot tried (and failed) to apply only patches 2 and 3 out of three

So I have merged them all into one patch.  Hope this works.


---

Comment by jdemeyer created at 2012-09-28 07:46:08

Resolution: fixed

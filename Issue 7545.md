# Issue 7545: Gaussian Integers

Issue created by migration from https://trac.sagemath.org/ticket/7545

Original creator: wuthrich

Original creation time: 2009-11-27 17:03:48

Assignee: davidloeffler

CC:  kcrisman vdelecroix katestange

Keywords: gaussian integers, Z[i], quadratic number ring

When teaching Gaussian Integers, I decided to modify sage slightly for my students. For them Z[i] is the ring of a+b*i with a and b integers and they learn that one can compute gcd's and that the unique factorisation holds.


---

Comment by wuthrich created at 2009-11-27 17:05:16

patch exported in 4.3.alpha0.


---

Attachment

The added patch will add a file 'gaussian_integer.py' which adds `GaussianIntegers` and `GaussianNumberField` to sage. The elements of the `GaussianIntegers` are elements in a quadratic Order, but they have a few more functions. Like `factor`, `gcd`, `is_prime`, `quo_rem`,... Also they are printed as `a + b*i` not as `b*i + a`. Also the coefficients of integers are in `ZZ`, not in `QQ` as for general quadratic orders.

I am not sure if I should propose this ticket for review and inclusion in sage. It maybe against the more general framework in number fields and will create silly exceptions. Also I still have not learned to do this in cython, so it is nowhere as efficient as it should be.

One might also want to change further things, like the function `gcd`. Also `QuadarticField(-1)` should give back `GaussianNumberFields` etc. 

A futher issue is 'i'. By default i is a symbol expression. If someone types `GaussianInteger()` he will probably assume that 'i' is in it afterwards. But changing this would probably not be a good idea.

Anyway, the patch is here to be looked at as it may inspire some further work in this direction.


---

Comment by wuthrich created at 2009-11-27 17:21:52

Changing status from new to needs_info.


---

Comment by robertwb created at 2009-11-29 07:37:37

I think this could be very useful to have. (In fact, it would be cool if the default i was in ZZ[i], and coerced down to the symbolics...) If an embedding into CC is specified then it would probably play better with symbolics.


---

Comment by mhansen created at 2009-11-29 14:56:27

The default `I` is currently just a wrapper around the QQ[I] one.


---

Comment by kcrisman created at 2010-08-10 19:40:51

The Pynac/symbolic one is, yes.  In fact, it looks a lot like the one in this patch already:

```
    K = QuadraticField(-1, 'I', embedding=CC.gen(), latex_name='i')
    pynac_I = K.gen()
```

which by the way appears to be a bug of sorts; `embedding` should be `True` or `False` in this case, which then passes things to `NumberField`, where `embedding` should be the image of the generator in an ambient field.  I don't know if should be considered a bug in `QuadraticField` or in the Pynac implementation, though.  What's actually passed to `NumberField` is `CLF(-1).sqrt()`.

(Parenthetical: sage.rings.all says

```
# i = I = QuadraticField(-1, 'I').gen()
I = CC.gen()
```

So I wonder if there is any conflict between these that would need to get sorted out.  Apparently it just gets overwritten during the import process when Sage starts up.)

Anyway, in sage.symbolic.pynac we have further that

```
    I = new_Expression_from_GEx(ring.SR, g_I)
```

So is it possible to make `I` no longer be this Pynac-wrapped generator of the appropriate quadratic field, but instead stay an element of the number field 'coerced' as robertwb says when appropriate (such as with `2.*I`)?  

I would be very happy to take Chris' excellent start and turn it into that, because I could definitely use it this spring in my own class.  But I'd need help because I don't know how the coercion stuff works at all.


---

Comment by kcrisman created at 2013-05-10 16:20:12

#13213 seems to be nearly ready, which I think might make dealing with these things more tractable - ?


---

Comment by vdelecroix created at 2013-05-10 17:05:28

Actually #13213 is not complete enough to start implementing this, we need #13256 as well !

`GaussianIntegers` should definitely inherit from `sage.rings.number_field.order.Order` and its elements from `sage.rings.number_field.number_field_element_quadratic.OrderElement_quadratic`. By the way, the Gaussian integers is not the only integer ring which is a euclidean ring ! This is True for negative discriminants -1 (Gaussian integers), -2, -3, -7 and -11. Moreover, some of the quadratic fields with positive discriminant are also norm-euclidean (see the [related page](http://en.wikipedia.org/wiki/Euclidean_domain#Norm-Euclidean_fields) on wikipedia).


---

Comment by kcrisman created at 2013-05-10 17:29:41

> Actually #13213 is not complete enough to start implementing this, we need #13256 as well !
Thanks for pointing this out.
> By the way, the Gaussian integers is not the only integer ring which is a euclidean ring ! This is True for negative discriminants -1 (Gaussian integers), -2, -3, -7 and -11. Moreover, some of the quadratic fields with positive discriminant are also norm-euclidean (see the [related page](http://en.wikipedia.org/wiki/Euclidean_domain#Norm-Euclidean_fields) on wikipedia).
Of course!  I am thinking of these primarily for pedagogical purposes - my druthers would be to have these and the Eisenstein integers, that's as much as I'll ever use at the undergraduate level.

If you'd like to start this (as I believe you understand technical details of Sage coercion, which I do not really) by rebasing the current patch to those tickets in the way you indicate, I should have some time this summer and some motivation to help out.


---

Comment by katestange created at 2013-10-05 16:25:40

The patches discussed seem to be ready.


---

Comment by jdemeyer created at 2014-12-22 09:16:19

Looking at this ticket, I fail to see the need for a whole new implementation of `Z[i]`. If `NumberField(x^2+1, 'I').ring_of_integers()` doesn't suit you, we should fix the latter such that it does.

I do agree with just defining the name `GaussianIntegers` to be a synonym of `NumberField(x^2+1, 'I').ring_of_integers()`.


---

Comment by kcrisman created at 2014-12-22 13:40:49

> I do agree with just defining the name GaussianIntegers to be a synonym of NumberField(x^2+1, 'I').ring_of_integers().

Some stuff already works with this.  However, it is definitely insufficient.
* I can't figure out how to get something prime (I can get the factorization and whether it's a unit, but that's not the same thing).
* What is this?

```
sage: GaussianIntegers([199,0]).quo_rem(GaussianIntegers([100,0]))
(199/100, 0)
```

* There is no `gcd` implemented either.

So I don't think it could just be a synonym, but would it be possible to only slightly extend the class, maybe?  I would be, as mentioned before, very motivated to review something like this, not sure if just adapting the current patch (well, the stuff that is missing) to just extend the current thing is possible or the way to go.


---

Comment by jdemeyer created at 2014-12-22 13:45:10

Replying to [comment:13 kcrisman]:
> * There is no `gcd` implemented either.
There is if somebody reviews #17294.


---

Comment by jdemeyer created at 2014-12-22 13:47:13

Replying to [comment:13 kcrisman]:
> * I can't figure out how to get something prime
Do you mean that you're missing an `is_prime()` method?


---

Comment by jdemeyer created at 2014-12-22 14:00:21

I created #17538 for `is_prime()`.


---

Comment by kcrisman created at 2014-12-22 14:18:53

And does the Euclidean algorithm work as intended here?  I would definitely say that those two tickets would be very useful.


---

Comment by kcrisman created at 2015-03-18 02:54:58

> I do agree with just defining the name `GaussianIntegers` to be a synonym of `NumberField(x^2+1, 'I').ring_of_integers()`.
Finally returning to this as I'm teaching it again... Would it be better to have it be a synonym of `NumberField(x^2+1, 'I', embedding=CC.gen()).ring_of_integers()` so that one can do numerical approximation?  (Or would that cause other problems?)


---

Comment by kcrisman created at 2015-03-18 02:57:32

Alternately, should we use `QuadraticField`?

Also, what about the questions in the original post - would these nowadays be fixed by just doing the 'obvious'?  I think that for pedagogical purposes at least, and hopefully general purposes, these would both be useful.
> Also they are printed as a + b*i not as b*i + a. 

> Also the coefficients of integers are in ZZ, not in QQ as for general quadratic orders.


---

Comment by jdemeyer created at 2015-03-18 07:32:27

Replying to [comment:19 kcrisman]:
> Alternately, should we use `QuadraticField`?
The best choice would be

```
ZI = QuadraticField(-1, 'I').ring_of_integers()
```


> Also they are printed as a + b*i not as b*i + a.
This is an indeed an "issue". However, it certainly does not justify adding a whole new class just to print things differently. One should add some kind of option to `NumberField` to `_repr_()` things in a different order.


---

Comment by jdemeyer created at 2015-03-18 07:33:54

Replying to [comment:19 kcrisman]:
> Also the coefficients of integers are in ZZ, not in QQ as for general quadratic orders.
The coefficients of the `ring_of_integers()` are in ZZ, so this is not a problem.


---

Comment by wuthrich created at 2015-03-18 10:55:44

Maybe I should clarify the original aim of this ticket and the preliminary code: It was for educational purpose. The code there was in no way optimized, but it illustrated what I taught at the time. I don't think that code should go in. Some of the comments above relate to outdated things. After all this ticket is now 5 years old.

Regardless of that. I believe we should have that the standard `I` in sage is an element in the ring of integers of the `QuadraticField`. It may be worth to have this particular field and its ring as a class for the following reason:
* I would really want the printing to change and I am not sure I want to fight for a change for arbitrary number fields.
* I think the global name `GaussianIntegers` could be worth having for educational purposes.
* Maybe there are things from pari's `I` that one can use to increase the speed. Presumably pari's `I` is not just a wrap around `Mod(x,x^2+1)` but I don't know about this.
* It is also one of two in the intersection of `CyclotomicFields` and `QuadraticField`. 
* It could interact with the symbolic `I` and other instances of it.
In any case, this should not be more than a wrapper around optimized code in other places.

What I consider a bug is

```
sage: K = QuadraticField(-1)
sage: I in K
False
```



---

Comment by jdemeyer created at 2015-03-18 11:38:14

Replying to [comment:22 wuthrich]:
> * I think the global name `GaussianIntegers` could be worth having for educational purposes.
I agree. That change could be done _now_ even without this ticket.

> * Maybe there are things from pari's `I` that one can use to increase the speed.
I don't think so. PARI's `I` is really meant for complex numbers, not for doing number theory. PARI's `I` is a very different thing than `Mod(x, x^2+1)`.


---

Comment by jdemeyer created at 2015-03-18 11:39:38

I still think that `GaussianIntegers` should be exactly the same as `QuadraticField(-1).ring_of_integers()`.


---

Comment by jdemeyer created at 2015-03-18 11:45:12

Replying to [comment:22 wuthrich]:
> I am not sure I want to fight for a change for arbitrary number fields.

Don't _fight_, just _ask_... I did just that on `sage-nt`. Note that changing the print order will probably break a huge amounts of doctests, so it won't be fun.


---

Comment by wuthrich created at 2015-03-18 11:54:57

> Don't _fight_, just _ask_... I did just that on `sage-nt`. Note that changing the print order will probably break a huge amounts of doctests, so it won't be fun.

For cyclotomic fields it would make sense to change too. I guess. Thanks for asking :)

Good to know about pari's I. How do you feel about the interaction in sage with the symbolic I. As a student I would be very confused if I was not in GaussianIntegers.


---

Comment by wuthrich created at 2015-03-18 12:03:23

Just noticed now that the pun were better had I written 
 "As a student I would be very confused if I were not in `GaussianIntegers`."


---

Comment by kcrisman created at 2015-03-18 14:43:56

So I think that we have a few separate issues.
* Add prime elements, not just ideals (done)
* Add gcd (ticket #17294)
* Add alias for `GaussianIntegers` (this ticket)
* Worry about printing order
* Figure out how to get `I in GaussianIntegers` to work, if at all possible, or document the heck out of it if not

Can anyone think of anything else that would be needed for pedagogical purposes?  I can only think of
* Plotting Gaussian integers, especially primes, like http://www.jasondavies.com/gaussian-primes/ (though I have some nice interacts of my own for this)

> Just noticed now that the pun were better had I written 
>  "As a student I would be very confused if I were not in `GaussianIntegers`."
Very nice indeed.


---

Comment by kcrisman created at 2015-03-18 14:44:10

(Also separate ticket: Eisenstein Integers!)


---

Comment by wuthrich created at 2015-03-18 15:11:59

Alias or its own class is still a question, I believe. Do we want `CyclotomicField(4)` and `QuadraticField(-1)` to return the same thing ? We agree that in either case it should be minimal.

Why `I` is a symbolic expression in sage now is a mystery to me. Surely it should be in Z[i], just like 2 is in Z. That `I^2` is a symbolic expression and not an integer seems particularly inconvenient.

Eisenstein integer could be dealt with on this same ticket. We only have to decide if the generator is a 3rd or a 6th root of unity.


---

Comment by vdelecroix created at 2015-03-22 11:04:18

Replying to [comment:30 wuthrich]:
> Why `I` is a symbolic expression in sage now is a mystery to me. Surely it should be in Z[i], just like 2 is in Z. That `I^2` is a symbolic expression and not an integer seems particularly inconvenient.

Agreed: this is *very* annoying. And actually, defining `I` as the generator of `ZZ[I]` might work out of the box

```
sage: good_I = QuadraticField(-1,'I').gen()
sage: (good_I + 1.0).parent()
Complex Field with 53 bits of precision
sage: (good_I + 1/2).parent()
Number Field in I with defining polynomial x^2 + 1
sage: good_I == I        # not perfect
I == I
sage: bool(good_I == I)  # but not that bad
True
```



---

Comment by jdemeyer created at 2015-03-22 11:05:48

Please open a _different_ ticket for the issue of `I`.


---

Comment by vdelecroix created at 2015-03-22 11:16:13

Replying to [comment:32 jdemeyer]:
> Please open a _different_ ticket for the issue of `I`.

#18036


---

Comment by jdemeyer created at 2016-01-03 18:22:24

Changing status from needs_info to needs_review.


---

Comment by jdemeyer created at 2016-01-03 18:22:24

New commits:


---

Comment by git created at 2016-01-19 10:31:44

Branch pushed to git repo; I updated commit sha1. This was a forced push. New commits:


---

Comment by jdemeyer created at 2016-01-25 21:11:36

Changing status from needs_review to needs_work.


---

Comment by git created at 2016-01-26 07:07:41

Branch pushed to git repo; I updated commit sha1. New commits:


---

Comment by jdemeyer created at 2016-01-26 07:08:28

Changing status from needs_work to needs_review.


---

Comment by chapoton created at 2016-02-24 19:42:46

Changing status from needs_review to positive_review.


---

Comment by chapoton created at 2016-02-24 19:42:46

ok, looks good to me.


---

Comment by kcrisman created at 2016-02-24 20:43:42

Thank you!!!


---

Comment by vbraun created at 2016-02-25 20:08:54

Resolution: fixed

# Issue 8972: Inversion and fraction fields for power series rings

Issue created by migration from https://trac.sagemath.org/ticket/8972

Original creator: SimonKing

Original creation time: 2010-05-15 15:46:05

Assignee: AlexGhitza

CC:  tscrim mkoeppe nbruin jhpalmieri dkrenn bruno tmonteil vdelecroix @davewittemorris

Keywords: power series ring, fraction field

This ticket is about at least three bugs related with inversion of elements of power series rings.

Here is the first:

```
sage: R.<x> = ZZ[[]]
sage: (1/x).parent()
Laurent Series Ring in x over Integer Ring
sage: (x/x).parent()
Power Series Ring in x over Integer Ring
```

_Both_ parents are wrong. Usually, the parent of ``a/b`` is the fraction field of the parent of ``a,b``, even if ``a==b``. And neither above parent is a field.

Next bug:

```
sage: (1/(2*x)).parent()
ERROR: An unexpected error occurred while tokenizing input
The following traceback may be corrupted or invalid
The error message is: ('EOF in multi-line statement', (919, 0))

---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)
... very long traceback
TypeError: no conversion of this rational to integer
```


And the third:

```
sage: F = FractionField(R)
sage: 1/x in F
False
```



---

Comment by SimonKing created at 2010-05-15 16:52:17

OK, here is a patch.

Idea: 

* Introduce a fraction_field method to power series rings that returns the Laurent series ring over the fraction field of the base ring. I hope that the base_extend method for Laurent polynomials works stably enough, otherwise it should be rewritten.
* In the division method of power serise, construct the fraction field of the parent, move numerator and denominator into the fraction field, and divide there. The original form of the method is preserved as a fail safe.

With the patch, I get:

```
sage: P.<t> = ZZ[]
sage: R.<x> = P[[]]
sage: FractionField(R)
Laurent Series Ring in x over Fraction Field of Univariate Polynomial Ring in t over Integer Ring
```


O dear. I just realise that there will be more work. There is a segmentation fault, as follows:

```
sage: R1.<x> = ZZ[[]]
sage: F = FractionField(R1)
sage: F
Laurent Series Ring in x over Rational Field
sage: F(x)
x
sage: ~F(x)
/home/king/SAGE/sage-4.3.1/local/bin/sage-sage: line 206:  4437 Segmentation fault      sage-ipython "$@" -i
```


So, the division of elements of a Laurent series ring fails with a segmentation fault. By consequence, division of power series segfaults as well, with the patch. "Needs work", I presume.


---

Comment by SimonKing created at 2010-05-15 16:52:17

Changing status from new to needs_work.


---

Comment by SimonKing created at 2010-05-15 17:21:29

Strangely, without the patch, the construction works:

```
sage: R.<x> = ZZ[[]]
sage: F = LaurentSeriesRing(FractionField(R.base()),R.variable_names())
sage: 1/F(x)
x^-1
```


The patch does this construction as well -- but segfaults. There seems to be a nasty side effect.


---

Comment by SimonKing created at 2010-05-15 18:11:28

The segfault problem seems to come from the fact that the div method for Laurent series relies on the div method for power series -- and with my patch, the div method for power series uses the div method for Laurent series. Not good. But that seems solvable.


---

Attachment

Bugfixes for fraction field and inverses of power series over non-fields


---

Comment by SimonKing created at 2010-05-15 19:26:36

Changing status from needs_work to needs_review.


---

Comment by SimonKing created at 2010-05-15 19:26:36

OK, I replaced the old patch, and now it seems to work!

For example:

```
sage: P.<t> = ZZ[]
sage: R.<x> = P[[]]
sage: 1/(t*x)
1/t*x^-1
sage: (1/x).parent() is FractionField(R)
True
sage: Frac(R)
Laurent Series Ring in x over Fraction Field of Univariate Polynomial Ring in t over Integer Ring
```


The doc tests for the two modified files pass. So, ready for review!


---

Comment by SimonKing created at 2010-05-15 19:33:55

PS: Even the following works:

```
sage: 1/(t+x)
1/t - 1/t^2*x + (-1/-t^3)*x^2 + (1/-t^4)*x^3 + 1/t^5*x^4 - 1/t^6*x^5 + 1/t^7*x^6 - 1/t^8*x^7 + 1/t^9*x^8 + (1/-t^10)*x^9 + 1/t^11*x^10 + (1/-t^12)*x^11 + 1/t^13*x^12 + (1/-t^14)*x^13 + (-1/-t^15)*x^14 + (1/-t^16)*x^15 + (-1/-t^17)*x^16 + (1/-t^18)*x^17 + 1/t^19*x^18 - 1/t^20*x^19 + O(x^20)
```



---

Comment by robertwb created at 2010-05-15 21:01:39

I'm wary of such a big change until we have some timing tests in place. In particular, I'm worried about potential slowdowns in the Monsky-Washnitzer code.


---

Comment by SimonKing created at 2010-05-15 22:35:49

Replying to [comment:6 robertwb]:
> I'm wary of such a big change until we have some timing tests in place. In particular, I'm worried about potential slowdowns in the Monsky-Washnitzer code. 

You are right, timing should be taken into account, and this is something my patch doesn't provide. Without the patch:

```
sage: R.<x> = ZZ[[]]
sage: timeit('a=1/(1+x)')
625 loops, best of 3: 1.08 ms per loop
```

With the patch

```
sage: R.<x> = ZZ[[]]
sage: timeit('a=1/(1+x)')
125 loops, best of 3: 6 ms per loop
```

So, it is slower by more than a factor five.


---

Comment by SimonKing created at 2010-05-15 23:52:31

Concerning timings, I see a couple of things that might help improve the div method:

 1. My patch calls the fraction_field method; _in addition_ the original code calls the laurent_series_ring method. But the purpose of both is the same. So, only one should be done.
 1. The fraction_field method should better be cached; this would save a lot of time, since the fradtion field construction involves the construction of a Laurent series ring and the construction of the fraction field of the base ring.
 1. Currently the div methods of power series and of Laurent series call each other; I don't know if this is done efficiently (e.g., avoiding Python calls). I could imagine that this can be stratified.

So, something to do for tomorrow. And I guess the ticket is again "needs work".


---

Comment by SimonKing created at 2010-05-15 23:52:31

Changing status from needs_review to needs_work.


---

Comment by SimonKing created at 2010-05-16 00:14:52

Replying to [comment:8 SimonKing]:
> Concerning timings, I see a couple of things that might help improve the div method:

One more thing: The old code is quick if the result actually belongs to the power series ring, which is quite often the case; if this is not the case then often an error results. And I guess the parent should always be the fraction field, eventually.

What I just tested (but I really should get some sleep now...) is to cache the fraction_field method, and to _try_ to use the old code if the valuation of the denominator is not bigger than the valuation of the numerator; if this fails, then put numerator and denominator into the fraction field, and try again.

Doing so brings the above timing to about 2ms, which is still a loss of factor two, but two is less than 5 or 6. I'll submit another patch after trying to lift the dependency of the two div methods on each other.


---

Attachment

Improving the timings, to be applied after the bug fix patch


---

Comment by SimonKing created at 2010-05-16 22:59:04

Changing status from needs_work to needs_review.


---

Comment by SimonKing created at 2010-05-16 22:59:04

The second patch does several things:

 1. It turned out that in several places it is assumed that the quotient of two power series is a power series, not a Laurent series. I tried to take care of this.

 2. I improved the timings, so that (according to the timings below) the performance is competitive (sometimes clearly better, sometimes very little worse) then the original performance.

The reason why the old timings were good was some kind of lazyness: The result of a division was not in the fraction field (as it should be!), but in a simpler ring, so that subsequent computations became easier. On the other hand, transformation into a Laurent polynomial was quite expensive, since there _always_ was a transformation into the Laurent Series Ring's underlying Power Series Ring -- even if the given data already belong to it.

Solution (as usual): Add an optional argument "check" to the init method of Laurent Series.

And then I tried to benefit from keeping the results as simple as possible (like the old code did), but in a more proper way. Let ``f`` be a Laurent series in a Laurent series ring ``L``. In the old code, one always had ``L.power_series_ring() is f.valuation_zero_part().parent()``. I suggest to relax this condition: It is sufficient to have a coercion:

```
sage: R.<x> = ZZ[[]]
sage: f = 1/(1+2*x)
sage: f.parent()
Laurent Series Ring in x over Rational Field
sage: f.parent().power_series_ring()
Power Series Ring in x over Rational Field
sage: f.power_series().parent()
Power Series Ring in x over Integer Ring
```


*__Timings__*

Without the two patches:

```
sage: R.<x> = ZZ[[]]
sage: timeit('a=1/x')
625 loops, best of 3: 291 µs per loop
sage: timeit('a=(1+x)/x')
625 loops, best of 3: 295 µs per loop
sage: timeit('a=1/(1+x)')
625 loops, best of 3: 1.07 ms per loop
sage: timeit('a=(1+x)/(1-x)')
625 loops, best of 3: 1.07 ms per loop
sage: y = (3*x+2)/(1+x)
sage: y=y/x
sage: z = (x+x^2+1)/(1+x^4+2*x^3+4*x)
sage: z=y/x
sage: timeit('y+z')
625 loops, best of 3: 213 µs per loop
sage: timeit('y*z')
625 loops, best of 3: 118 µs per loop
sage: timeit('y-z')
625 loops, best of 3: 212 µs per loop
sage: timeit('y/z')
ERROR: An unexpected error occurred while tokenizing input
The following traceback may be corrupted or invalid
The error message is: ('EOF in multi-line statement', (27, 0))

---------------------------------------------------------------------------
ArithmeticError                           Traceback (most recent call last)
...
ArithmeticError: division not defined
```


With the two patches:

```
sage: R.<x> = ZZ[[]]
sage: timeit('a=1/x')
625 loops, best of 3: 220 µs per loop
sage: timeit('a=(1+x)/x')
625 loops, best of 3: 228 µs per loop
sage: timeit('a=1/(1+x)')
625 loops, best of 3: 1.25 ms per loop
sage: timeit('a=(1+x)/(1-x)')
625 loops, best of 3: 1.26 ms per loop
sage: y = (3*x+2)/(1+x)
sage: y=y/x
sage: z = (x+x^2+1)/(1+x^4+2*x^3+4*x)
sage: z=y/x
sage: timeit('y+z')
625 loops, best of 3: 191 µs per loop
sage: timeit('y*z')
625 loops, best of 3: 92.6 µs per loop
sage: timeit('y-z')
625 loops, best of 3: 191 µs per loop
sage: timeit('y/z')
25 loops, best of 3: 9.35 ms per loop
```


So, my patches not only fix some bugs, but they also slightly improve the performance.

I tested all files that I have changed, but I can not exclude errors in other files.

I forgot to insert my name as an author, but presumably there will be a revision needed anyway, after comments of referees...


---

Comment by SimonKing created at 2010-05-17 07:27:50

I forgot one remark:

I don't know how this happens, but the ``truncate`` method of Laurent series behaves different than before, although the ``truncate`` method of power series did not change:

```
sage: A.<t> = QQ[[]]
sage: f = (1+t)^100
sage: f.truncate(5)
3921225*t^4 + 161700*t^3 + 4950*t^2 + 100*t + 1
sage: f.truncate(5).parent()
Univariate Polynomial Ring in t over Rational Field
sage: g = 1/f
sage: g.truncate(5)
1 - 100*t + 5050*t^2 - 171700*t^3 + 4421275*t^4 + O(t^5)
sage: g.truncate(5).parent()
Laurent Series Ring in t over Rational Field
```


In other words, ``g.truncate(5)`` is now returning a Laurent series, but without the patch it used to return return a univariate polynomial, similar to ``f.truncate(5)``.

I don't know if this is acceptable, and also I don't understand how that happened. Shall I change it?


---

Comment by SimonKing created at 2010-05-17 08:17:01

Replying to [comment:11 SimonKing]:
> I forgot one remark:
> 
> I don't know how this happens, but the ``truncate`` method of Laurent series behaves different than before, although the ``truncate`` method of power series did not change:

Outch, now I see my mistake.

 * The documentation of ``LaurentSeries.truncate`` states that indeed it returns a Laurent series. It does not have a doc test, so, I will add one.

 * The old doc test of ``PowerSeries.truncate`` fails with my patch. The reason is that the _power_ series constructed in this doc test is now in fact a _Laurent_ series; this is what made me believe that the behaviour of the method has changed. So, I only have to change the doc test.

But before submitting a patch to add/correct these doc tests, I'll wait for input of a referee.


---

Comment by robertwb created at 2010-05-18 06:35:43

Do you have any timings for power series sqrt()?


---

Comment by SimonKing created at 2010-05-18 08:14:14

Replying to [comment:13 robertwb]:
> Do you have any timings for power series sqrt()? 

Tentatively.

Without the patch:

```
sage: P.<t> = QQ[[]]
sage: p = 9 - 33*t - 13*t^2 - 155*t^3 - 429*t^4 - 137*t^5 + 170*t^6 + 81*t^7 - 132*t^8 + 179*t^9 + O(t^10)
sage: p.sqrt()
3 - 11/2*t - 173/24*t^2 - 5623/144*t^3 - 174815/1152*t^4 - 8187925/20736*t^5 - 12112939/9216*t^6 - 7942852751/1492992*t^7 - 1570233970141/71663616*t^8 - 12900142229635/143327232*t^9 + O(t^10)
sage: timeit('q = p.sqrt()')
25 loops, best of 3: 13.3 ms per loop
sage: timeit('q = (p^2).sqrt()')
25 loops, best of 3: 13.6 ms per loop
sage: timeit('q = (p^4).sqrt()')
25 loops, best of 3: 14.5 ms per loop
sage: PZ = ZZ[['t']]
sage: timeit('q = (PZ(p)^2).sqrt()')
ERROR: An unexpected error occurred while tokenizing input
The following traceback may be corrupted or invalid
The error message is: ('EOF in multi-line statement', (27, 0))
...
TypeError: no conversion of this rational to integer
sage: p = 9 - 33*t - 13*t^2 - 155*t^3 - 429*t^4 - 137*t^5 + 170*t^6 + 81*t^7 - 132*t^8 + 179*t^9
sage: timeit('q = p.sqrt()')
25 loops, best of 3: 20.7 ms per loop
sage: timeit('q = (p^2).sqrt()')
25 loops, best of 3: 21.9 ms per loop
```


With the patch:

```
sage: P.<t> = QQ[[]]
sage: p = 9 - 33*t - 13*t^2 - 155*t^3 - 429*t^4 - 137*t^5 + 170*t^6 + 81*t^7 - 132*t^8 + 179*t^9 + O(t^10)
sage: p.sqrt()
3 - 11/2*t - 173/24*t^2 - 5623/144*t^3 - 174815/1152*t^4 - 8187925/20736*t^5 - 12112939/9216*t^6 - 7942852751/1492992*t^7 - 1570233970141/71663616*t^8 - 12900142229635/143327232*t^9 + O(t^10)
sage: timeit('q = p.sqrt()')
25 loops, best of 3: 15.5 ms per loop
sage: timeit('q = (p^2).sqrt()')
25 loops, best of 3: 15.7 ms per loop
sage: timeit('q = (p^4).sqrt()')
25 loops, best of 3: 16.6 ms per loop
sage: PZ = ZZ[['t']]
sage: timeit('q = (PZ(p)^2).sqrt()')
25 loops, best of 3: 19.2 ms per loop
sage: p = 9 - 33*t - 13*t^2 - 155*t^3 - 429*t^4 - 137*t^5 + 170*t^6 + 81*t^7 - 132*t^8 + 179*t^9
sage: timeit('q = p.sqrt()')
25 loops, best of 3: 23.8 ms per loop
sage: timeit('q = (p^2).sqrt()')
25 loops, best of 3: 24.5 ms per loop
```


So, over QQ, there is a slight regression (both with exact and inexact input). Over ZZ, it only works with my patch, even for a polynomial that is quadratic by definition.

I will have a closer look at sqrt - perhaps I'll find something.


---

Comment by SimonKing created at 2010-05-18 09:08:17

Replying to [comment:14 SimonKing]:
> I will have a closer look at sqrt - perhaps I'll find something.

It seems so. 

First, the reason why the old version failed for a power series over ZZ is the fact that the invert method raises an error if the result has coefficients in QQ rather than ZZ. I guess this must change.

Second, there is a division inside the sqrt method. By my patch, this division returns a Laurent series, which slows things slightly down. If I do ``a*s.__invert__()`` instead of ``a/s`` then the timings are as good as with the old code.

So, there will soon be a third patch...


---

Attachment

Improving timings for sqrt, further bug fixes, more doc tests. To be applied after the two other patches


---

Comment by SimonKing created at 2010-05-18 11:06:29

It was worth it!

First, I found one division bug for Laurent series left, which is now fixed (and doc tested):

```
sage: L.<x> = LaurentSeriesRing(ZZ)
sage: 1/(2+x)
1/2 - 1/4*x + 1/8*x^2 - 1/16*x^3 + 1/32*x^4 - 1/64*x^5 + 1/128*x^6 - 1/256*x^7 + 1/512*x^8 - 1/1024*x^9 + 1/2048*x^10 - 1/4096*x^11 + 1/8192*x^12 - 1/16384*x^13 + 1/32768*x^14 - 1/65536*x^15 + 1/131072*x^16 - 1/262144*x^17 + 1/524288*x^18 - 1/1048576*x^19 + O(x^20)
```

This used to result in an error.

Second, I added more doc tests (and inserted my name to the author list).

Third, the new timings for sqrt are fully competitive (even very slightly faster than before), and we still have the bug fix:

```
Loading Sage library. Current Mercurial branch is: powerseries
sage: P.<t> = QQ[[]]
sage: p = 9 - 33*t - 13*t^2 - 155*t^3 - 429*t^4 - 137*t^5 + 170*t^6 + 81*t^7 - 132*t^8 + 179*t^9 + O(t^10)
sage: p.sqrt()
3 - 11/2*t - 173/24*t^2 - 5623/144*t^3 - 174815/1152*t^4 - 8187925/20736*t^5 - 12112939/9216*t^6 - 7942852751/1492992*t^7 - 1570233970141/71663616*t^8 - 12900142229635/143327232*t^9 + O(t^10)
sage: timeit('q = p.sqrt()')
25 loops, best of 3: 13.2 ms per loop
sage: timeit('q = (p^2).sqrt()')
25 loops, best of 3: 13.5 ms per loop
sage: timeit('q = (p^4).sqrt()')
25 loops, best of 3: 14.5 ms per loop
sage: PZ = ZZ[['t']]
sage: timeit('q = (PZ(p)^2).sqrt()')
25 loops, best of 3: 16.4 ms per loop
sage: p = 9 - 33*t - 13*t^2 - 155*t^3 - 429*t^4 - 137*t^5 + 170*t^6 + 81*t^7 - 132*t^8 + 179*t^9
sage: timeit('q = p.sqrt()')
25 loops, best of 3: 20.6 ms per loop
sage: timeit('q = (p^2).sqrt()')
25 loops, best of 3: 21.7 ms per loop
```


The trick is that I do ``s*a.__invert__()`` instead of ``s/a``, where ``s`` and ``a`` are power series. This helps, because (after a little change) the invert method returns a power series whenever possible -- and since I know that ``a.valuation()>=0``, I can use fast multiplication of power series rather than slow multiplication of Laurent series.


---

Comment by SimonKing created at 2010-05-18 11:48:01

Changing status from needs_review to needs_work.


---

Comment by SimonKing created at 2010-05-18 11:48:01

O dear, I have to mark it "needs work", because the following fails:

```
sage: R.<x> = ZZ[[]]
sage: y = (3*x+2)/(1+x)
sage: y=y/x
```



---

Attachment

Bugfix for LaurentSeries._div_; to be applied after the other three patches


---

Comment by SimonKing created at 2010-05-18 12:06:12

Replying to [comment:17 SimonKing]:
> sage: y=y/x

OK, the last (hopefully the last...) patch fixes this. I was verifying the timings for basic arithmetic (the timings without patches are posted above), and here is the positive result:

```
sage: R.<x> = ZZ[[]]
sage: timeit('a=1/x')
625 loops, best of 3: 218 µs per loop
sage: timeit('a=(1+x)/x')
625 loops, best of 3: 228 µs per loop
sage: timeit('a=1/(1+x)')
625 loops, best of 3: 1.22 ms per loop
sage: timeit('a=(1+x)/(1-x)')
625 loops, best of 3: 1.24 ms per loop
sage: y = (3*x+2)/(1+x)
sage: y=y/x
sage: z = (x+x^2+1)/(1+x^4+2*x^3+4*x)
sage: z=y/x
sage: timeit('y+z')
625 loops, best of 3: 189 µs per loop
sage: timeit('y*z')
625 loops, best of 3: 92.6 µs per loop
sage: timeit('y-z')
625 loops, best of 3: 189 µs per loop
sage: timeit('y/z')
125 loops, best of 3: 7.1 ms per loop
```


Now, ready for review, and I'll do something else...


---

Comment by SimonKing created at 2010-05-18 12:06:12

Changing status from needs_work to needs_review.


---

Comment by robertwb created at 2010-05-25 06:40:14

Minor cosmetic changes, apply on top of previous.


---

Attachment

Nice work. Apply all 5 patches.


---

Comment by robertwb created at 2010-05-25 06:40:43

Changing status from needs_review to positive_review.


---

Comment by drkirkby created at 2010-06-05 08:21:26

The reviewer field was not filled in. I just added it. 

Dave


---

Comment by drkirkby created at 2010-06-05 10:28:24

Sorry about the spelling mistake!


---

Comment by mhansen created at 2010-06-06 07:42:51

Resolution: fixed


---

Comment by mhansen created at 2010-06-06 08:19:19

I had to back these patches out since they caused lots of errors in schemes/elliptic_curves.


---

Comment by mhansen created at 2010-06-06 08:19:19

Changing status from closed to needs_work.


---

Comment by SimonKing created at 2010-06-06 12:46:15

Hi Mike!

That probably means that the elliptic curves code expects the result of a division of two power series to be another power series. But now, the division yields a Laurent series.

I see two possibilities to proceed:

 1. Search for all occurences of power series in Sage, see if a division occurs, and change it so that things still work.
 2. Change/extend the methods provided by Laurent series so that they match those provided by power series. In that way, the code in schemes/elliptic_curves still has a chance to work.

I'll see what I can do.

Best regards,
Simon


---

Comment by SimonKing created at 2010-06-06 15:20:56

I think the problem boils down to two problems:

 1. Laurent series have no attribute ``exp``, unlike power series.

 2. In some situations, there still occurs a formal fraction field when it should be a Laurent series ring. The result is an attribute error.

For the first situation, I suggest to implement ``exp`` for Laurent series of non-negative valuation (using exp of the underlying power series). For the second situation, I have to analyse what goes wrong.


---

Comment by SimonKing created at 2010-06-06 17:04:23

The problem is that some code _expects_ the fraction field of a power series ring to be a formal fraction field. So, assume that one changes it, so that the fraction field is in fact a Laurent polynomial ring. When creating elements of the fraction field, the code fails, because it tries to initialise the element by numerator and denominator -- but Laurent series are initialised by a power series and an integer.

A possible solution would be to make the init method of Laurent series accept numerator and denominator. But I think that's a nasty hack, because what happens if the arguments are one power series and one integer? Is the integer supposed to be the valuation of the Laurent series, or the denominator of a formal fraction field element?


---

Comment by SimonKing created at 2010-06-06 20:34:01

It is really frustrating how many doc tests fail. I solved the problem with ``exp`` and one other attribute error. But there remain many problems: `ZeroDivisionError`, wrong precision of the result (!), and so on.


---

Comment by SimonKing created at 2010-06-07 00:22:56

In most cases, the problems seem to come from using `f/g` on power series in situations where `g` is of valuation zero. This used to return a power series, which I consider the wrong answer (it should be a Laurent series). Now, if one wants `f/g` as a power series, one should use `f * ~g` instead.

I am now confident that I'll soon be able to submit another patch that resolves it.


---

Comment by SimonKing created at 2010-06-07 09:31:41

After fixing what I mentioned above, I get for `sage -testall`:

```
The following tests failed:


        sage -t  "devel/sage/sage/crypto/lfsr.py"
        sage -t  "devel/sage/sage/modular/modform/find_generators.py"
        sage -t  "devel/sage/sage/schemes/hyperelliptic_curves/hyperelliptic_padic_field.py"
```


This seems doable.

Perhaps I was too strict when I implemented `_div_`: I wanted that the result _always_ lives in the fraction field, and I wanted that an error is raised if no fraction field exists. But I guess it is better to proceed as it is known from other rings that are no integral domains:

```
sage: K = ZZ.quo(15)
sage: parent(K(3)/K(4))
Ring of integers modulo 15
sage: parent(K(4)/K(3))
---------------------------------------------------------------------------
ZeroDivisionError                         Traceback (most recent call last)
...
ZeroDivisionError: Inverse does not exist.
```


So, rule:

 1. _If_ a fraction field exists then the result of a division must live in it (example: 1/1 is a rational, not an integer).
 2. If no fraction field exists, then devision shall yield an element of the original ring, if that's possible, and raise a `ZeroDivisionError` otherwise.


---

Comment by SimonKing created at 2010-06-07 18:21:08

Fixing some remaining bugs of Laurent/power series arithmetic; fixing doc tests on elliptic curves.


---

Attachment

I think the problems are now solved. With the last patch, that is to be applied after all others, `sage -testall` works without errors (at least in version sage-4.4.2).

*__Changes introduced by the patch__*

 * In some cases, if the code expects a power series, I replaced `a/b` for power series `a,b` by `a*~b`. Namely, the latter returns a power series (not a Laurent series), if possible. 

 * I added a method `exp` for Laurent series, that returns the exponential if the Laurent series happens to be a power series.

 * With my previous patches, the underlying data of a Laurent series is not necessarily a power series. Therefore `add_bigoh` (similarly `_rmul_` and `_lmul_`) did in some cases not work. This is now fixed and doctested.

 * Some Power Series Rings still returned a _formal_ fraction field. This is now fixed, they return a Laurent series ring.

 * If `a,b` are elements of a power series ring `R`, the rule is now:

   1. If `R` is an integral domain, then `a/b` always belongs to `Frac(R)`. This is similar to `1/1` being rational, not integer.

   2. If `R` is no integral domain, then `a/b` is an element of `R` or of the Laurent series ring over the base ring of `R`, if `b` is invertible. This is similar to division in `ZZ.quo(15)`.

   3. If possible, `~b` is a power series (possibly over the fraction field of the base of `R`). So, we always have `~b==1/b`, but the parents may be different. I hope this is acceptable.

 * A change in the default `_div_` method of `RingElement`: Previously, the default for `a._div_(b)` was to return `a.parent().fraction_field()(a,b)`. But this may be a problem (e.g., if the fraction field is not a formal fraction field but a Laurent series ring). Therefore, if the old default results in an error, `a.parent().fraction_field(a)/a.parent().fraction_field(b)` is tried.

*__Timings__*

Robert was worried about potential slowdowns in the Monsky-Washnitzer code. It seems to me that my patches actually provide a considerably speedup.

Without my patches:

```
sage -t  "devel/sage-powerseries/sage/schemes/elliptic_curves/monsky_washnitzer.py"
         [3.9 s]

----------------------------------------------------------------------
All tests passed!
Total time for all tests: 3.9 seconds
```


With my patches:

```
sage -t  "devel/sage-powerseries/sage/schemes/elliptic_curves/monsky_washnitzer.py"
         [2.3 s]

----------------------------------------------------------------------
All tests passed!
Total time for all tests: 2.3 seconds
```


So, the code seems to become faster by more than 33%!

Ready for review again...


---

Comment by SimonKing created at 2010-06-07 18:55:23

Changing status from needs_work to needs_review.


---

Comment by SimonKing created at 2010-06-07 21:53:01

I upgraded to sage-4.4.3.

I verified that all patches still apply.

With the patches, `sage -testall` passes.

On sage-devel, Robert asked how stable my Monsky-Washnitzer timing is. Here is the answer:

Without the patches, I was running `sage -t  "devel/sage/sage/schemes/elliptic_curves/monsky_washnitzer.py"` 5 times, and got
 
  7.9 s, 2.4 s, 2.4 s, 2.4 s, 2.4 s

With the patches, I obtain

  2.4 s, 2.5 s, 2.4 s, 2.4 s, 2.4 s

So, the timing did not improve, except for the first run. But at least there was no slowdown.


---

Comment by SimonKing created at 2010-11-30 07:47:32

Accidentally, I found that this ticket is rotting.

Recall that it used to be "fixed", but then it was reopened by mhansen, since there was a problem in sage-4.4.alpha0. Subsequently, I fixed these problems, but still the resolution is set to "fixed".

I guess this is why nobody took care of the ticket afterwards.

I don't know if the patch would still apply (probably not), but at least I verified that the original problem did not disappear.


---

Comment by mvngu created at 2010-11-30 09:00:13

Changing status from closed to new.


---

Comment by mvngu created at 2010-11-30 09:00:13

Resolution changed from fixed to 


---

Comment by mvngu created at 2010-11-30 09:00:31

Changing status from new to needs_review.


---

Comment by gagansekhon created at 2011-01-08 03:04:48

Changing status from needs_review to needs_work.


---

Comment by gagansekhon created at 2011-01-08 03:04:48

test of sage/modular/modform/find_generators.py failed. 

```
./sage -t sage/modular/modform/find_generators.py
sage -t  "devel/sage-main/sage/modular/modform/find_generators.py"
**********************************************************************
File "/Applications/sage4.6/devel/sage-main/sage/modular/modform/find_generators.py", line 74:
    sage: span_of_series(v)
Exception raised:
    Traceback (most recent call last):
      File "/Applications/sage4.6/local/bin/ncadoctest.py", line 1231, in run_one_test
        self.run_one_example(test, example, filename, compileflags)
      File "/Applications/sage4.6/local/bin/sagedoctest.py", line 38, in run_one_example
        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)
      File "/Applications/sage4.6/local/bin/ncadoctest.py", line 1172, in run_one_example
        compileflags, 1) in test.globs
      File "<doctest __main__.example_1[8]>", line 1, in <module>
        span_of_series(v)###line 74:
    sage: span_of_series(v)
      File "/Applications/sage4.6/local/lib/python/site-packages/sage/modular/modform/find_generators.py", line 116, in span_of_series
        B = [V(g.padded_list(n)) for g in v]
      File "element.pyx", line 306, in sage.structure.element.Element.__getattr__ (sage/structure/element.c:2666)
      File "parent.pyx", line 272, in sage.structure.parent.getattr_from_other_class (sage/structure/parent.c:2840)
      File "parent.pyx", line 170, in sage.structure.parent.raise_attribute_error (sage/structure/parent.c:2611)
    AttributeError: 'sage.rings.laurent_series_ring_element.LaurentSeries' object has no attribute 'padded_list'
**********************************************************************
File "/Applications/sage4.6/devel/sage-main/sage/modular/modform/find_generators.py", line 79:
    sage: span_of_series(v,10)
Exception raised:
    Traceback (most recent call last):
      File "/Applications/sage4.6/local/bin/ncadoctest.py", line 1231, in run_one_test
        self.run_one_example(test, example, filename, compileflags)
      File "/Applications/sage4.6/local/bin/sagedoctest.py", line 38, in run_one_example
        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)
      File "/Applications/sage4.6/local/bin/ncadoctest.py", line 1172, in run_one_example
        compileflags, 1) in test.globs
      File "<doctest __main__.example_1[9]>", line 1, in <module>
        span_of_series(v,Integer(10))###line 79:
    sage: span_of_series(v,10)
      File "/Applications/sage4.6/local/lib/python/site-packages/sage/modular/modform/find_generators.py", line 116, in span_of_series
        B = [V(g.padded_list(n)) for g in v]
      File "element.pyx", line 306, in sage.structure.element.Element.__getattr__ (sage/structure/element.c:2666)
      File "parent.pyx", line 272, in sage.structure.parent.getattr_from_other_class (sage/structure/parent.c:2840)
      File "parent.pyx", line 170, in sage.structure.parent.raise_attribute_error (sage/structure/parent.c:2611)
    AttributeError: 'sage.rings.laurent_series_ring_element.LaurentSeries' object has no attribute 'padded_list'
**********************************************************************
1 items had failures:
   2 of  14 in __main__.example_1
***Test Failed*** 2 failures.
For whitespace errors, see the file /Users/sekhon/.sage//tmp/.doctest_find_generators.py
	 [4.0 s]
 
----------------------------------------------------------------------
The following tests failed:


	sage -t  "devel/sage-main/sage/modular/modform/find_generators.py"
Total time for all tests: 4.0 seconds
```



---

Comment by SimonKing created at 2011-02-18 08:13:54

'''
Apply trac-8972_fraction_of_power_series_combined.patch

(for the patchbot)


---

Comment by SimonKing created at 2011-02-18 08:15:03

For simplicity, I produced a patch that combines all previous patches and is rebased to sage-4.6.2.alpha4.

I will now try to take care about the failing doc tests.


---

Comment by SimonKing created at 2011-02-18 13:00:53

I managed to fix the remaining issues, and all tests pass (unless a last minute change that I just did was a bad idea). Hence, this ticket needs review again. 

Since the computation time was a point of critique, let me give you some timings:

Without the patch:

```
# Basic arithmetic
sage: R.<x> = ZZ[[]]
sage: timeit('a=1/(1+x)')
625 loops, best of 3: 803 µs per loop
sage: timeit('a=1/x')
625 loops, best of 3: 279 µs per loop
sage: timeit('a=(1+x)/x')
625 loops, best of 3: 285 µs per loop
sage: timeit('a=1/(1+x)')
625 loops, best of 3: 801 µs per loop
sage: y = (3*x+2)/(1+x)
sage: y=y/x
sage: z = (x+x^2+1)/(1+x^4+2*x^3+4*x)
sage: z=y/x
sage: timeit('y+z')
625 loops, best of 3: 167 µs per loop
sage: timeit('y*z')
625 loops, best of 3: 100 µs per loop
sage: timeit('y-z')
625 loops, best of 3: 166 µs per loop

# square roots
sage: P.<t> = QQ[[]]
sage: p = 9 - 33*t - 13*t^2 - 155*t^3 - 429*t^4 - 137*t^5 + 170*t^6 + 81*t^7 - 132*t^8 + 179*t^9 + O(t^10)
sage: p.sqrt()
3 - 11/2*t - 173/24*t^2 - 5623/144*t^3 - 174815/1152*t^4 - 8187925/20736*t^5 - 12112939/9216*t^6 - 7942852751/1492992*t^7 - 1570233970141/71663616*t^8 - 12900142229635/143327232*t^9 + O(t^10)
sage: timeit('q = p.sqrt()')
625 loops, best of 3: 767 µs per loop
sage: timeit('q = (p^2).sqrt()')
625 loops, best of 3: 791 µs per loop
sage: timeit('q = (p^4).sqrt()')
625 loops, best of 3: 828 µs per loop
sage: PZ = ZZ[['t']]
sage: timeit('q = (PZ(p)^2).sqrt()')
<BOOM>
sage: p = 9 - 33*t - 13*t^2 - 155*t^3 - 429*t^4 - 137*t^5 + 170*t^6 + 81*t^7 - 132*t^8 + 179*t^9
sage: timeit('q = p.sqrt()')
625 loops, best of 3: 1 ms per loop
sage: timeit('q = (p^2).sqrt()')
625 loops, best of 3: 1.04 ms per loop
sage: timeit('q = (p^2).sqrt()')
625 loops, best of 3: 1.04 ms per loop
```


With the patch:

```
# Basic arithmetic
sage: R.<x> = ZZ[[]]
sage: timeit('a=1/(1+x)')
625 loops, best of 3: 897 µs per loop
sage: timeit('a=1/x')
625 loops, best of 3: 173 µs per loop
sage: timeit('a=(1+x)/x')
625 loops, best of 3: 179 µs per loop
sage: timeit('a=1/(1+x)')
625 loops, best of 3: 911 µs per loop
sage: timeit('a=(1+x)/(1-x)')
625 loops, best of 3: 900 µs per loop
sage: y = (3*x+2)/(1+x)
sage: y=y/x
sage: z = (x+x^2+1)/(1+x^4+2*x^3+4*x)
sage: z=y/x
sage: timeit('y+z')
625 loops, best of 3: 38.4 µs per loop
sage: timeit('y*z')
625 loops, best of 3: 23.6 µs per loop
sage: timeit('y-z')
625 loops, best of 3: 23.6 µs per loop
sage: timeit('y/z')
625 loops, best of 3: 309 µs per loop

# square roots
sage: P.<t> = QQ[[]]
sage: p = 9 - 33*t - 13*t^2 - 155*t^3 - 429*t^4 - 137*t^5 + 170*t^6 + 81*t^7 - 132*t^8 + 179*t^9 + O(t^10)
sage: p.sqrt()
3 - 11/2*t - 173/24*t^2 - 5623/144*t^3 - 174815/1152*t^4 - 8187925/20736*t^5 - 12112939/9216*t^6 - 7942852751/1492992*t^7 - 1570233970141/71663616*t^8 - 12900142229635/143327232*t^9 + O(t^10)
sage: timeit('q = p.sqrt()')
625 loops, best of 3: 938 µs per loop
sage: timeit('q = (p^2).sqrt()')
625 loops, best of 3: 962 µs per loop
sage: timeit('q = (p^4).sqrt()')
625 loops, best of 3: 1 ms per loop
sage: PZ = ZZ[['t']]
sage: timeit('q = (PZ(p)^2).sqrt()')
125 loops, best of 3: 2.39 ms per loop
sage: p = 9 - 33*t - 13*t^2 - 155*t^3 - 429*t^4 - 137*t^5 + 170*t^6 + 81*t^7 - 132*t^8 + 179*t^9
sage: timeit('q = p.sqrt()')
625 loops, best of 3: 1.22 ms per loop
sage: timeit('q = (p^2).sqrt()')
625 loops, best of 3: 1.26 ms per loop
```


So, in some cases the patch brings a big speedup (such as 38.4 µs versus 167 µs), in other cases it brings a mild slowdown (such as 962 µs versus 791 µs)

Obvious question to the referee: Should I try to squeeze even more µs out of it, or can it stay as it is (assuming that the long tests pass, as I will try now).


---

Comment by SimonKing created at 2011-02-18 13:00:53

Changing status from needs_work to needs_review.


---

Comment by SimonKing created at 2011-02-18 13:53:33

FWIW: Long tests pass.


---

Comment by SimonKing created at 2011-02-18 14:00:48

Apply trac-8972_fraction_of_power_series_combined.patch


---

Comment by SimonKing created at 2011-02-18 14:03:18

Don't be irritated by the patchbot. The patch is for 4.6.2.alpha4, not for 4.6.1


---

Comment by kedlaya created at 2011-06-17 15:59:44

This fails to apply against 4.7, so more rebasing is needed.

```
cd "/home/kedlaya/Downloads/sage-4.7/devel/sage" && hg import   "/home/kedlaya/Downloads/trac-8972_fraction_of_power_series_combined.patch"
applying /home/kedlaya/Downloads/trac-8972_fraction_of_power_series_combined.patch
patching file sage/modular/overconvergent/genus0.py
Hunk #1 FAILED at 1653
1 out of 1 hunks FAILED -- saving rejects to file sage/modular/overconvergent/genus0.py.rej
patching file sage/rings/power_series_poly.pyx
Hunk #4 FAILED at 843
Hunk #5 succeeded at 876 with fuzz 2 (offset 11 lines).
1 out of 5 hunks FAILED -- saving rejects to file sage/rings/power_series_poly.pyx.rej
patching file sage/rings/power_series_ring_element.pyx
Hunk #11 FAILED at 1771
Hunk #12 FAILED at 1783
2 out of 12 hunks FAILED -- saving rejects to file sage/rings/power_series_ring_element.pyx.rej
abort: patch failed to apply
```



---

Comment by kedlaya created at 2011-06-17 15:59:44

Changing status from needs_review to needs_work.


---

Comment by SimonKing created at 2012-03-29 14:00:14

Remove assignee AlexGhitza.


---

Comment by SimonKing created at 2012-03-29 14:00:14

Apparently the trac is locked in "bold face mode". Trying to ''' change it.


---

Attachment

Replaces all previous patches


---

Comment by SimonKing created at 2012-03-29 14:51:23

Changing status from needs_work to needs_review.


---

Comment by SimonKing created at 2012-03-29 14:51:23

I have rebased the patch. The test suite needs to be run, but the patch should now apply to sage-5.0.beta10. Here is some supporting evidence:

*__First section: The bugs to be fixed__*

_sage-5.0.beta10-gcc without the patch_

```
sage: R.<x> = ZZ[[]]
sage: (1/x).parent()  # bug
Laurent Series Ring in x over Integer Ring
sage: (x/x).parent()  # bug
Power Series Ring in x over Integer Ring
sage: (1/(2*x)).parent()  # bug
Traceback (most recent call last):
...
TypeError: no conversion of this rational to integer
sage: F = FractionField(R)
sage: 1/x in F    # bug
False
sage: F           # I think a Laurent series ring would be better
Fraction Field of Power Series Ring in x over Integer Ring
sage: F(x)
x
sage: ~F(x)   # was a problem with an early form of my patches.
1/x
```


_sage-5.0.beta10-gcc with the patch_

```
age: R.<x> = ZZ[[]]
sage: (1/x).parent()   # bug fixed
Laurent Series Ring in x over Rational Field
sage: (x/x).parent()   # bug fixed
Laurent Series Ring in x over Rational Field
sage: (1/(2*x)).parent() # bug fixed
Laurent Series Ring in x over Rational Field
sage: F = FractionField(R)
sage: 1/x in F         # bug fixed
True
sage: F                # I think that's much better!
Laurent Series Ring in x over Rational Field
sage: F(x)
x
sage: ~F(x)            # new bug avoided
x^-1
```


*__Second section: Timings__*

Here I am collecting the examples that were studied in the comments above.

_sage-5.0.beta10-gcc without the patch_

```
sage: R.<x> = ZZ[[]]
sage: timeit('a=1/(1+x)')
625 loops, best of 3: 445 µs per loop
sage: timeit('a=1/x')
625 loops, best of 3: 283 µs per loop
sage: timeit('a=(1+x)/x')
625 loops, best of 3: 290 µs per loop
sage: timeit('a=(1+x)/(1-x)')
625 loops, best of 3: 450 µs per loop
sage: y = (3*x+2)/(1+x)
sage: y=y/x
sage: z = (x+x^2+1)/(1+x^4+2*x^3+4*x)
sage: z=y/x
sage: timeit('y+z')
625 loops, best of 3: 104 µs per loop
sage: timeit('y*z')
625 loops, best of 3: 76.2 µs per loop
sage: timeit('y-z')
625 loops, best of 3: 103 µs per loop
sage: timeit('y/z')    # bug
Traceback (most recent call last):
...
ArithmeticError: division not defined
sage: P.<t> = QQ[[]]
sage: p = 9 - 33*t - 13*t^2 - 155*t^3 - 429*t^4 - 137*t^5 + 170*t^6 + 81*t^7 - 132*t^8 + 179*t^9 + O(t^10)
sage: p.sqrt()
3 - 11/2*t - 173/24*t^2 - 5623/144*t^3 - 174815/1152*t^4 - 8187925/20736*t^5 - 12112939/9216*t^6 - 7942852751/1492992*t^7 - 1570233970141/71663616*t^8 - 12900142229635/143327232*t^9 + O(t^10)
sage: timeit('q = p.sqrt()')
625 loops, best of 3: 810 µs per loop
sage: timeit('q = (p^2).sqrt()')
625 loops, best of 3: 829 µs per loop
sage: timeit('q = (p^4).sqrt()')
625 loops, best of 3: 890 µs per loop
sage: PZ = ZZ[['t']]
sage: timeit('q = (PZ(p)^2).sqrt()')    # bug
ERROR: An unexpected error occurred while tokenizing input
The following traceback may be corrupted or invalid
The error message is: ('EOF in multi-line statement', (2017, 0))
Traceback (most recent call last):
...
TypeError: no conversion of this rational to integer
sage: p = 9 - 33*t - 13*t^2 - 155*t^3 - 429*t^4 - 137*t^5 + 170*t^6 + 81*t^7 - 132*t^8 + 179*t^9
sage: timeit('q = p.sqrt()')
125 loops, best of 3: 1.07 ms per loop
sage: timeit('q = (p^2).sqrt()')
625 loops, best of 3: 1.12 ms per loop
sage: timeit('q = (p^2).sqrt()')
625 loops, best of 3: 1.12 ms per loop
```


_sage-5.0.beta10-gcc with the patch_

```
sage: R.<x> = ZZ[[]]
sage: timeit('a=1/(1+x)')
625 loops, best of 3: 506 µs per loop
sage: timeit('a=1/x')
625 loops, best of 3: 153 µs per loop
sage: timeit('a=(1+x)/x')
625 loops, best of 3: 160 µs per loop
sage: timeit('a=(1+x)/(1-x)')
625 loops, best of 3: 516 µs per loop
sage: y = (3*x+2)/(1+x)
sage: y=y/x
sage: z = (x+x^2+1)/(1+x^4+2*x^3+4*x)
sage: z=y/x
sage: timeit('y+z')
625 loops, best of 3: 37.8 µs per loop
sage: timeit('y*z')
625 loops, best of 3: 26.9 µs per loop
sage: timeit('y-z')
625 loops, best of 3: 20.6 µs per loop
sage: timeit('y/z')      # bug fixed
625 loops, best of 3: 277 µs per loop
sage: P.<t> = QQ[[]]
sage: p = 9 - 33*t - 13*t^2 - 155*t^3 - 429*t^4 - 137*t^5 + 170*t^6 + 81*t^7 - 132*t^8 + 179*t^9 + O(t^10)
sage: p.sqrt()
3 - 11/2*t - 173/24*t^2 - 5623/144*t^3 - 174815/1152*t^4 - 8187925/20736*t^5 - 12112939/9216*t^6 - 7942852751/1492992*t^7 - 1570233970141/71663616*t^8 - 12900142229635/143327232*t^9 + O(t^10)
sage: timeit('q = p.sqrt()')
625 loops, best of 3: 847 µs per loop
sage: timeit('q = (p^2).sqrt()')
625 loops, best of 3: 872 µs per loop
sage: timeit('q = (p^4).sqrt()')
625 loops, best of 3: 932 µs per loop
sage: PZ = ZZ[['t']]
sage: timeit('q = (PZ(p)^2).sqrt()')    # bug fixed
125 loops, best of 3: 1.46 ms per loop
sage: p = 9 - 33*t - 13*t^2 - 155*t^3 - 429*t^4 - 137*t^5 + 170*t^6 + 81*t^7 - 132*t^8 + 179*t^9
sage: timeit('q = p.sqrt()')
625 loops, best of 3: 1.11 ms per loop
sage: timeit('q = (p^2).sqrt()')
625 loops, best of 3: 1.17 ms per loop
sage: timeit('q = (p^2).sqrt()')
625 loops, best of 3: 1.17 ms per loop
```


I think, given that various bugs are fixed, and I think the timings tend to be better (not in all examples, but it seems to me that the loss is less than the gain), I guess it is "needs review", modulo doc test suite.

Apply trac-8972_fraction_of_power_series_combined.patch


---

Comment by davidloeffler created at 2012-03-29 17:20:10

Changing status from needs_review to needs_work.


---

Comment by davidloeffler created at 2012-03-29 17:20:10

The patchbot reports a doctest failure with 5.0.beta11:

```
sage -t  -force_lib devel/sage-8972/sage/rings/multi_power_series_ring_element.py
**********************************************************************
File "/storage/masiao/sage-5.0.beta11-patchbot/devel/sage-8972/sage/rings/multi_power_series_ring_element.py", line 139:
    sage: h = 1/f; h
Exception raised:
    Traceback (most recent call last):
      File "/storage/masiao/sage-5.0.beta11-patchbot/local/bin/ncadoctest.py", line 1231, in run_one_test
        self.run_one_example(test, example, filename, compileflags)
      File "/storage/masiao/sage-5.0.beta11-patchbot/local/bin/sagedoctest.py", line 38, in run_one_example
        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)
      File "/storage/masiao/sage-5.0.beta11-patchbot/local/bin/ncadoctest.py", line 1172, in run_one_example
        compileflags, 1) in test.globs
      File "<doctest __main__.example_0[46]>", line 1, in <module>
        h = Integer(1)/f; h###line 139:
    sage: h = 1/f; h
      File "element.pyx", line 1799, in sage.structure.element.RingElement.__div__ (sage/structure/element.c:13260)
      File "coerce.pyx", line 738, in sage.structure.coerce.CoercionModel_cache_maps.bin_op (sage/structure/coerce.c:6583)
      File "coerce.pyx", line 1210, in sage.structure.coerce.CoercionModel_cache_maps.get_action (sage/structure/coerce.c:11424)
      File "coerce.pyx", line 1378, in sage.structure.coerce.CoercionModel_cache_maps.discover_action (sage/structure/coerce.c:13135)
      File "ring.pyx", line 1420, in sage.rings.ring.CommutativeRing._pseudo_fraction_field (sage/rings/ring.c:9929)
        return self.fraction_field()
      File "/storage/masiao/sage-5.0.beta11-patchbot/local/lib/python/site-packages/sage/rings/power_series_ring.py", line 672, in fraction_field
        return LaurentSeriesRing(self.base().fraction_field(),self.variable_names())
      File "/storage/masiao/sage-5.0.beta11-patchbot/local/lib/python/site-packages/sage/rings/laurent_series_ring.py", line 91, in LaurentSeriesRing
        R = LaurentSeriesRing_field(base_ring, name, sparse)
      File "/storage/masiao/sage-5.0.beta11-patchbot/local/lib/python/site-packages/sage/rings/laurent_series_ring.py", line 400, in __init__
        LaurentSeriesRing_generic.__init__(self, base_ring, name, sparse)
      File "/storage/masiao/sage-5.0.beta11-patchbot/local/lib/python/site-packages/sage/rings/laurent_series_ring.py", line 121, in __init__
        commutative_ring.CommutativeRing.__init__(self, base_ring, names=name, category=_Fields)
      File "ring.pyx", line 1365, in sage.rings.ring.CommutativeRing.__init__ (sage/rings/ring.c:9627)
        Ring.__init__(self, base_ring, names=names, normalize=normalize,
      File "ring.pyx", line 156, in sage.rings.ring.Ring.__init__ (sage/rings/ring.c:1903)
        Parent.__init__(self, base=base, names=names, normalize=normalize,
      File "parent.pyx", line 532, in sage.structure.parent.Parent.__init__ (sage/structure/parent.c:4484)
      File "parent_gens.pyx", line 331, in sage.structure.parent_gens.ParentWithGens._assign_names (sage/structure/parent_gens.c:3052)
      File "parent_gens.pyx", line 213, in sage.structure.parent_gens.normalize_names (sage/structure/parent_gens.c:2360)
    IndexError: the number of names must equal the number of generators
**********************************************************************
```



---

Comment by SimonKing created at 2012-03-30 08:55:08

Arrgh. That's nasty. The reason for the doctest problems is that meanwhile there are multivariate power series rings -- but there are still no multivariate Laurent series rings.

Spontaneously, I suggest a temporary work-around: In the case of multivariate case, the old behaviour (namely: using a formal fraction field) should be used, until multivariate Laurent series are available.


---

Comment by SimonKing created at 2012-03-30 09:25:19

My spontaneous suggestion does not work easily. Sorry.


---

Comment by robharron created at 2013-03-14 06:53:58

I think it would be great for this ticket to come back to life! Is it possible to just take the current power series classes append _old to all the class names and have the multivariable power series inherit from those?

(Since no one has posted a ticket for creating multivariable Laurent series, let me ask here what is wrong with making them a multivariable power series ring with a univariate Laurent series ring in the background?)


---

Comment by pbruin created at 2014-05-04 19:44:38

Converted the patch into a Git branch and resolved merge conflicts.  Fixed a few relatively straightforward doctest failures in the second commit.  Summary of remaining failures:

```
sage -t --long src/sage/schemes/hyperelliptic_curves/hyperelliptic_padic_field.py  # 4 doctests failed
sage -t --long src/sage/tests/french_book/polynomes.py  # 2 doctests failed
sage -t --long src/sage/rings/multi_power_series_ring_element.py  # 4 doctests failed
```



---

Comment by chapoton created at 2014-07-09 19:55:39

just rebased on 6.3.beta5
----
New commits:


---

Comment by git created at 2014-09-07 12:01:38

Branch pushed to git repo; I updated commit sha1. New commits:


---

Comment by chapoton created at 2014-12-27 08:38:35

Failures in src/sage/schemes/hyperelliptic_curves/hyperelliptic_padic_field.py seem to be just about slight changes in precision (either gain or loss by one). Maybe one can just correct the result of the doctests. 

Failures in src/sage/rings/multi_power_series_ring_element.py are more serious: they come from trying to build a Laurent series ring in several variables, that we currently do not have !


---

Comment by rws created at 2015-01-24 16:57:38

I have a question about the description of this issue. Please forgive that I'm no algebraist.

```
sage: (1/(2*x)).parent()
...
TypeError: no conversion of this rational to integer
```

Isn't this correct, with the ring over ZZ? With QQ there is no error.

If so, the description should be corrected.


---

Comment by git created at 2015-02-01 10:37:45

Branch pushed to git repo; I updated commit sha1. New commits:


---

Comment by git created at 2015-02-01 12:22:46

Branch pushed to git repo; I updated commit sha1. New commits:


---

Comment by kedlaya created at 2016-08-18 13:46:50

Since the power series issue is somewhat separate, I created #21283 to deal with it on its own.


---

Comment by git created at 2021-01-19 23:26:41

Branch pushed to git repo; I updated commit sha1. This was a forced push. New commits:


---

Comment by @mjungmath created at 2021-01-19 23:28:21

Approach might be too naive, but it seems to solve the first and the last bug without compromising the timing.


---

Comment by @mjungmath created at 2021-01-19 23:28:21

Changing status from needs_work to needs_review.


---

Comment by git created at 2021-01-19 23:48:47

Branch pushed to git repo; I updated commit sha1. New commits:


---

Comment by git created at 2021-01-20 08:31:51

Branch pushed to git repo; I updated commit sha1. This was a forced push. New commits:


---

Comment by @mjungmath created at 2021-01-20 08:33:22

This should do.


---

Comment by pbruin created at 2021-01-20 08:35:08

Replying to [comment:64 gh-mjungmath]:
> Approach might be too naive, but it seems to solve the first and the last bug without compromising the timing.
Does this also address the dependency #21283?


---

Comment by @mjungmath created at 2021-01-20 08:36:04

Replying to [comment:70 pbruin]:
> Replying to [comment:64 gh-mjungmath]:
> > Approach might be too naive, but it seems to solve the first and the last bug without compromising the timing.
> Does this also address the dependency #21283?

Nope. I just wanted to see what the patchbot has to say before I modify the ticket description. Here we go.


---

Comment by @mjungmath created at 2021-01-20 12:13:15

Yay! Patchbot is green! :)


---

Comment by @mjungmath created at 2021-01-23 01:08:34

Would be nice to have this ticket reviewed. Thanks. :)


---

Comment by @mjungmath created at 2021-02-15 10:20:29

Patchbot seems still be satisfied with beta7. It'd be nice to have this change in version 9.3 though. Otherwise, a rebase might become necessary soon...


---

Comment by tscrim created at 2021-02-16 00:53:46

There are a few details that still fixing:

This seems strange:

```
:doc:`laurent_series_ring_element`.
```

Wouldn't it be better to be a specific reference to the class? Although I am not sure it is worth the direct reference.

This is wrong:

```
        If we try a non-zero, non-unit leading coefficient, we end up in the in
        the fraction field, i.e. Laurent series ring::
```

Even for units, you still end up in the fraction field.


```diff
-However, this must fail if the underlying ring is no integral domain::
+However, this must fail if the underlying ring is not an integral domain::
```



---

Comment by @mjungmath created at 2021-02-16 11:24:13

Thank you Travis for taking a look!

Replying to [comment:82 tscrim]:
> There are a few details that still fixing:
> 
> This seems strange:
> {{{
> :doc:`laurent_series_ring_element`.
> }}}
> Wouldn't it be better to be a specific reference to the class? Although I am not sure it is worth the direct reference.

Alright, I'll change it.
 
> This is wrong:
> {{{
>         If we try a non-zero, non-unit leading coefficient, we end up in the in
>         the fraction field, i.e. Laurent series ring::
> }}}
> Even for units, you still end up in the fraction field.

Oh right. I think the previous author already meant constant terms instead of leading terms. At least that would make more sense.

> 
> {{{#!diff
> -However, this must fail if the underlying ring is no integral domain::
> +However, this must fail if the underlying ring is not an integral domain::
> }}}

Will do.


---

Comment by git created at 2021-02-16 11:51:58

Branch pushed to git repo; I updated commit sha1. New commits:


---

Comment by @mjungmath created at 2021-02-16 11:52:08

That should be better.


---

Comment by tscrim created at 2021-02-16 23:25:11

Changing status from needs_review to positive_review.


---

Comment by tscrim created at 2021-02-16 23:25:11

Thanks. LGTM.


---

Comment by vbraun created at 2021-03-01 00:21:07

Resolution: fixed

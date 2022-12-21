# Issue 9555: Series expansions at singularities don't work

Issue created by migration from Trac.

Original creator: fredrik.johansson

Original creation time: 2010-07-20 12:12:22

Assignee: burcin

CC:  kcrisman rws jakobkroeker

Calling the series() method on a symbolic expression at a singularity (algebraic, logarithmic, essential) returns nonsense, inconsistent results, or raises an exception:

Examples:


```
sage: sqrt(x).series(x,0)
Order(1)
sage: sqrt(x).series(x,1)
Order(x)
sage: sqrt(x).series(x,2)
---------------------------------------------------------------------------
RuntimeError                              Traceback (most recent call last)

/home/fredrik/sage/<ipython console> in <module>()

/home/fredrik/sage/local/lib/python2.6/site-packages/sage/symbolic/expression.so in sage.symbolic.expression.Expression.series (sage/symbolic/expression.cpp:12811)()

RuntimeError: power::eval(): division by zero
```



```
sage: (log(x) + x).series(x,0)
Order(1)
sage: (log(x) + x).series(x,1)
(log(x)) + Order(x)
sage: (log(x) + x).series(x,2)
(log(x)) + 1*x
```



```
sage: exp(1/x).series(x,0)
Order(1)
sage: exp(1/x).series(x,1)
---------------------------------------------------------------------------
RuntimeError                              Traceback (most recent call last)

/home/fredrik/sage/<ipython console> in <module>()

/home/fredrik/sage/local/lib/python2.6/site-packages/sage/symbolic/expression.so in sage.symbolic.expression.Expression.series (sage/symbolic/expression.cpp:12811)()

RuntimeError: power::eval(): division by zero
sage: exp(1/x).series(x,2)
---------------------------------------------------------------------------
RuntimeError                              Traceback (most recent call last)

/home/fredrik/sage/<ipython console> in <module>()

/home/fredrik/sage/local/lib/python2.6/site-packages/sage/symbolic/expression.so in sage.symbolic.expression.Expression.series (sage/symbolic/expression.cpp:12811)()

RuntimeError: power::eval(): division by zero
```



---

Comment by fredrik.johansson created at 2010-07-20 12:17:11

Another example:


```
sage: (x^n).series(x,0)
Order(1)
sage: (x^n).series(x,1)
(0^n) + Order(x)
sage: (x^n).series(x,2)
---------------------------------------------------------------------------
RuntimeError                              Traceback (most recent call last)

/home/fredrik/sage/<ipython console> in <module>()

/home/fredrik/sage/local/lib/python2.6/site-packages/sage/symbolic/expression.so in sage.symbolic.expression.Expression.series (sage/symbolic/expression.cpp:12811)()

RuntimeError: power::eval(): division by zero
```



---

Comment by jlhsage created at 2011-06-26 20:57:57

This problem shows up in pure ginac-1.60, as you can check in their ginsh shell.  I posted about this error on the ginac-devel list, and their reply is here:

http://www.cebix.net/pipermail/ginac-devel/2011-June/001946.html

Essentially, they don't claim to work with fractional power series.  Here's the reply:

> GiNaC can only compute Taylor and Laurent series. Yours is a Puiseux 
> series: a series not in integer powers of x but in rational powers of x.
>
> The Puiseux expansion of sqrt(x) is, well, x<sup>(1/2)</sup>.
>
> You may try to set x=y<sup>q</sup> and compute the Laurent expansion in y. Setting 
> q=2 in your case would give the desired result:
>
> {{{
> series(sqrt(x), x, 0, 3)
>      = series(sqrt(y^2), y, 0, 3*2)
>      = y
>      = x^(1/2).
> }}}
>
> Note that the member functions degree() and ldegree() currently return 
> int, so this would have to be generalized somehow, when implementing 
> Puiseux series directly in GiNaC.
>
> Bye
>    -richy.


Note that Richy's suggestion about using `x=y^2` doesn't work either in ginsh.
Does anybody know how maxima resolves this issue?


---

Comment by kcrisman created at 2011-06-28 19:09:44

Maxima:

```
(%i1) taylor(sqrt(x),x,0,3);
(%o1)/T/                        sqrt(x) + . . .
(%i3) taylor(%e^(-x)/x,x,0,5);
                                 2    3    4     5
                    1       x   x    x    x     x
(%o3)/T/            - - 1 + - - -- + -- - --- + --- + . . .
                    x       2   6    24   120   720
```

The first one in particular seems odd.  Maybe that should be considered a bug?  I've submitted [this Maxima bug](https://sourceforge.net/tracker/?func=detail&aid=3341693&group_id=4933&atid=104933). 


----
Anyway, perhaps that's not relevant.   There's a pretty relevant followup to the discussion referenced above:

```

> Actually, ginac cannot do a series on x^n or on sqrt(x^2).  Here's the
> ginsh output:
>
>  > series(x^n,x,1);
> (0^n)+Order(x)
>  > series(x^n,x,2);
> power::eval(): division by zero
>  > series(sqrt(x^2),x,3);
> power::eval(): division by zero

Oh, you're so right! Actually, that's because the result of 
series(sqrt(x^2),x==0,3) is not necessarly x: it could just as well be 
-x. The presence of the branch point makes it more tricky.

Sorry for not being able to help.
```


That doesn't resolve things here.  My guess is that the current behavior in Ginac could actually be considered correct, so that we should just add some documentation saying so?


---

Comment by jlhsage created at 2011-06-29 01:20:44

We should probably fix pynac/ginac to not give an error.  From the referenced ginac-devel thread, the correct response to series(x^{1/2}} at 0 is a Puiseux series and:

> The Puiseux expansion of sqrt(x) is, well, x^(1/2).

which ginac is not currently able to do, but which maxima in fact returns correctly as x^(1/2).
Also, here's maxima on the series of x^2 at 0:

(%i1) taylor(x^2,x,0,3);
                                   2
(%o1)/T/                          x  + . . .

which again looks to be correct.  So far there is not much response to the referenced thread on ginac-devel so we may have to fix this ourselves, and we might start by understanding how maxima recognizes Puiseux conditions.  Towards that end I've started reading maxima's series.lisp code but, being a newbie to maxima development, pointers from the maxima experts would be very helpful.

John Hoebing


---

Comment by kcrisman created at 2011-06-29 01:59:33

Well, you can certainly implement Puiseux series.  See #4618, where this is already requested.

But having a command called "taylor" return things that are not Taylor series is ... problematic.  And I don't think that Maxima is recognizing this necessarily.

```
>], ...)
     `taylor (<expr>, <x>, <a>, <n>)' expands the expression <expr> in
     a truncated Taylor or Laurent series in the variable <x> around
     the point <a>, containing terms through `(<x> - <a>)^<n>'.
```

nothing about Puiseux, nor do any examples.

Now, our `.series()` is not named quite that way, so I suppose it's possible we could have that.  I still think it might be a little confusing, so I would at the very least recommend that implementing P. series be at #4618 and then adding a keyword or something (even default, but maybe so that it could be disabled) here for the `.series()` method would be what we would do here.


---

Comment by burcin created at 2011-06-29 13:28:52

Replying to [comment:5 kcrisman]:

> But having a command called "taylor" return things that are not Taylor series is ... problematic.  And I don't think that Maxima is recognizing this necessarily.
 {{{
 >], ...)
      `taylor (<expr>, <x>, <a>, <n>)' expands the expression <expr> in
      a truncated Taylor or Laurent series in the variable <x> around
      the point <a>, containing terms through `(<x> - <a>)^<n>'.
 }}}
> nothing about Puiseux, nor do any examples.

+1
 
> Now, our `.series()` is not named quite that way, so I suppose it's possible we could have that.

The `taylor()` method is cruft left over from pre-pynac symbolics. We should depreciate it in favor of the `series()` method. It's perfectly acceptable to give Puiseux series as a result of a call to `.series()`. I expect this to be done in #6119, where we add an `algorithm=` option to `.series()`. The default behavior can be to call pynac and fall back to maxima if that returns an error.

This ticket can then be about fixing pynac/ginac to allow these series expansions, in which case, it should be moved to the issue tracker on bitbucket:

https://bitbucket.org/burcin/pynac/issues


---

Comment by kcrisman created at 2011-06-29 13:38:31

> > Now, our `.series()` is not named quite that way, so I suppose it's possible we could have that.
> 
> The `taylor()` method is cruft left over from pre-pynac symbolics. We should depreciate it in favor of the `series()` method. 

I don't know if I'd go that far.  I think that especially the top-level `taylor()` (which calls `SR.taylor()`) is very useful; having the top command be `series()` is more confusing, as there are lots of series out there.

That said, `SR.taylor()` should probably be calling Pynac at this point, probably just the `.series()` method (without Puiseaux).   I agree that the code itself is cruft, just not the name :)


---

Comment by burcin created at 2011-06-29 13:48:21

Replying to [comment:7 kcrisman]:

> > The `taylor()` method is cruft left over from pre-pynac symbolics. We should depreciate it in favor of the `series()` method. 
> 
> I don't know if I'd go that far.  I think that especially the top-level `taylor()` (which calls `SR.taylor()`) is very useful; having the top command be `series()` is more confusing, as there are lots of series out there.

OK. I can see the educational appeal of a `taylor()` method.

> That said, `SR.taylor()` should probably be calling Pynac at this point, probably just the `.series()` method (without Puiseaux).   I agree that the code itself is cruft, just not the name :)

This would work, given the current behavior of Pynac/GiNaC's `series()` function. It would cause problems in the future if that ever changes. We should also add some doctests to make sure it only returns Taylor expansions.

This can also be done as a part of #6119. Then, instead of a deprecation message we give an error pointing to the `.series()` method.


---

Comment by kcrisman created at 2011-06-29 13:50:07

> > That said, `SR.taylor()` should probably be calling Pynac at this point, probably just the `.series()` method (without Puiseaux).   I agree that the code itself is cruft, just not the name :)
> 
> This would work, given the current behavior of Pynac/GiNaC's `series()` function. It would cause problems in the future if that ever changes. We should also add some doctests to make sure it only returns Taylor expansions.

Well, I would envision it would have a special keyword that would require returning only Taylor series.  Presumably `.series()` should also have this, don't you think?  Even if that weren't the default behavior.

> This can also be done as a part of #6119. Then, instead of a deprecation message we give an error pointing to the `.series()` method.

Sounds good.


---

Comment by kcrisman created at 2014-12-06 20:27:29

I completely forgot about this ticket when I reported http://sourceforge.net/p/maxima/bugs/2850/  Maxima (and we) need better documentation about this stuff.  That said, I may have changed my mind about this.  Maybe we can make `taylor` clearly only Taylor or something...  Incidentally, someone said that another name for these series at singular points are Frobenius series.

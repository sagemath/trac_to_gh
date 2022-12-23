# Issue 7742: add a compose function to sage

Issue created by migration from https://trac.sagemath.org/ticket/7742

Original creator: was

Original creation time: 2009-12-19 20:15:55

Assignee: AlexGhitza


```

def compose(f, n, a):
    """
    Return f(f(...f(a)...)), where the composition occurs n times.
    
    INPUT:
        - `f` -- anything that is callable
        - `n` -- a nonnegative integer
        - `a` -- any input for `f`

    OUTPUT:
        result of composing `f` with itself `n` times and applying to `a`.

    EXAMPLES::

        sage: def f(x): return x^2 + 1
        sage: x = var('x')
        sage: compose(f, 3, x)
        ((x^2 + 1)^2 + 1)^2 + 1
    """
    n = Integer(n)
    if n <= 0: return a
    a = f(a)
    for i in range(n-1): a = f(a)
    return a

```



---

Comment by hivert created at 2009-12-19 22:13:07

Replying to [ticket:7742 was]:
>     n = Integer(n)

Converting to int should be sufficient... Or the implementation below should'nt be very useful :-).

>     if n <= 0: return a

I'd rather sage to raise a `ValueError` if `n < 0` than returning silently a wrong value...

Florent


---

Comment by colah created at 2009-12-20 16:20:31

Replying to [comment:1 hivert]:
> Replying to [ticket:7742 was]:
> >     n = Integer(n)
> 
> Converting to int should be sufficient... Or the implementation below should'nt be very useful :-).
> 
> >     if n <= 0: return a
> 
> I'd rather sage to raise a `ValueError` if `n < 0` than returning silently a wrong value...
> 
> Florent

We probably want to return an inverse function, if possible, when n<0... I'm also wondering if there is a generalisation of this to all real numbers.


---

Comment by was created at 2009-12-20 21:38:05


```
Hi,

There is a function in Mathematica that does exactly what you want and it's called Nest. I've reimplemented it in python as general effort to port some functional tools that I like to python. Please check this link if you are interested on it:

http://bitbucket.org/juliusc/functional/src/tip/functional/functional_mathematica.py

Hope this helps,
Carlos
```



---

Comment by was created at 2009-12-20 21:38:16

Hi,

There is a function in Mathematica that does exactly what you want and it's called Nest. I've reimplemented it in python as general effort to port some functional tools that I like to python. Please check this link if you are interested on it:

http://bitbucket.org/juliusc/functional/src/tip/functional/functional_mathematica.py

Hope this helps,
Carlos


---

Comment by was created at 2009-12-20 21:38:47

> We probably want to return an inverse function, if possible, when n<0..

Note that usually the inverse isn't available.


---

Comment by ncohen created at 2009-12-21 07:30:47

What about doing it in log(n) compositions, like when you try to compute x^12 ? :-)

Nathann


---

Comment by was created at 2009-12-21 08:02:49

Replying to [comment:6 ncohen]:
> What about doing it in log(n) compositions, like when you try to compute x^12 ? :-)

That's an interesting idea.  For a Python function that will make absolutely no difference.  For a symbolic callable expression it would make a noticeable difference though.   So we should definitely think about it. 

I think the most important thing though is to implement something with a clear interface and definition now and get it into sage. Then we can make it faster whenever we want.


---

Comment by ncohen created at 2009-12-21 08:12:51

I completely agree ! That's what we are doing in graph theory : first implement, then try to think about how to optimize it :-)

I this case it should not be too different from these few lines ( if I make none of my usual mistakes )


```
if n==0:
    return "identity function"( no idea how it is called in Sage )

if n%2 == 1:
    ff = compose(f, (n-1)/2, a)
    return f(ff(ff(a)))
else:
    ff = compose(f, n/2, a)
    return ff(ff(a))
```


But perhaps the function "compose" should be a method of these symbolic callable expressions you mentionned, which would be called by this "compose" function : it may be interesting to compute symbolically the n^th composed of a function without evaluating it  :-)


---

Attachment

Adds the compose function.


---

Comment by colah created at 2010-03-14 04:03:34

I ran into some problems producing the patch. On mhansen's suggestion, I added     
{{from sage.rings.integer import Integer}}
at the beginning of the function instead of the beginning of misc.py and it worked... But I don't know why and am concerned that it adds unnecessary overhead...


---

Comment by colah created at 2010-03-14 04:04:12

Changing status from new to needs_review.


---

Comment by zimmerma created at 2010-03-14 18:03:14

I have two comments: (1) the patch contains twice the new function, and (2) it would be nice to
be able to write `compose(f,x,n)` for a symbolic variable n (or any expression). Only when
n is an integer would the "nesting" be evaluated. Comment (1) needs more work, comment (2) could
be a separate ticket, but if easy it would be nice to do it.

Additional comment: please rename the patch as trac_7742.patch.


---

Comment by zimmerma created at 2010-03-14 18:03:14

Changing status from needs_review to needs_work.


---

Comment by flawrence created at 2010-11-04 13:51:03

The new patch addresses many of the above concerns (other than symbolic n), and splits the functionality into three functions:

* compose(f,g) which composes functions such that compose(f,g)(x) = f(g(x))

* self_compose(f, n) which composes a function with itself such that self_compose(f,n)(x) = f(...(f(x))...)

* nest(f, n, a) which effectively self_composes and evaluates (but does it slightly faster than a self_compose)

Questions:

* compose(f,g)(x) = f(g(x)) - is this the most common convention among mathematicians? or should the RHS be g(f(x))?

* Is (f, n, a) or (f, a, n) the best order of parameters for nest?

* Is there somewhere more suitable than misc/misc.py for these functions?


---

Comment by flawrence created at 2010-11-04 13:51:03

Changing status from needs_work to needs_review.


---

Comment by jrp created at 2010-11-16 22:50:11

What version of Sage are you targeting?  I tried applying both of these (individually) to 4.6.0 and to 4.5.3 and couldn't apply them.


---

Comment by jrp created at 2010-11-16 22:50:11

Changing status from needs_review to needs_work.


---

Attachment

adds compose, self_compose and nest functions. actually replaces previous patch this time


---

Comment by flawrence created at 2010-11-17 04:45:03

Changing status from needs_work to needs_review.


---

Comment by flawrence created at 2010-11-17 04:45:03

Sorry, the second patch accidentally relied on the first (which needed rebasing).  I've fixed it and the second patch should now apply and work for both 4.6.0 and 4.6.1alpha0.


---

Comment by zimmerma created at 2010-11-17 11:51:15

Changing status from needs_review to needs_work.


---

Comment by zimmerma created at 2010-11-17 11:51:15

This needs more work, since the function `self_compose` fails for n=0:

```
sage: function('f');
sage: h=self_compose(f,0)
---------------------------------------------------------------------------
ValueError                                Traceback (most recent call last)

/localdisk/tmp/sage-4.6/<ipython console> in <module>()

/localdisk/tmp/sage-4.6/local/lib/python2.6/site-packages/sage/misc/misc.pyc in self_compose(f, n)
    890     # all necessary powers of two (f, f^2, f^4), storing them in a list
    891     fs = [f]
--> 892     for i in xrange(int(floor(log(n, 2)))):
    893         fs.append(compose(fs[i], fs[i]))
    894     

ValueError: math domain error
```

Paul


---

Comment by zimmerma created at 2010-11-17 11:58:53

Replying to [comment:12 flawrence]:

> * compose(f,g)(x) = f(g(x)) - is this the most common convention among mathematicians? or should the RHS be g(f(x))?

compose(f,g) seems good to me.

> * Is (f, n, a) or (f, a, n) the best order of parameters for nest?

I prefer (f,n,a) since this is coherent with `self_compose(f,n)`.

> * Is there somewhere more suitable than misc/misc.py for these functions?

I don't know.

Also if a symbolic n is not allowed (yet) in `self_compose`, some type-checking
should be done:

```
sage: function('f')
sage: var('m')
sage: self_compose(f,m)(x)
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)

/localdisk/tmp/sage-4.6/<ipython console> in <module>()

/localdisk/tmp/sage-4.6/local/lib/python2.6/site-packages/sage/misc/misc.pyc in self_compose(f, n)
    890     # all necessary powers of two (f, f^2, f^4), storing them in a list
    891     fs = [f]
--> 892     for i in xrange(int(floor(log(n, 2)))):
    893         fs.append(compose(fs[i], fs[i]))
    894     

/localdisk/tmp/sage-4.6/local/lib/python2.6/site-packages/sage/symbolic/expression.so in sage.symbolic.expression.Expression.__float__ (sage/symbolic/expression.cpp:5398)()

TypeError: unable to simplify to float approximation
```


Paul


---

Comment by jrp created at 2010-11-18 01:26:07

At the moment the powers-of-two speed up isn't helping even in the symbolic case, because the implementation is to return lambda x: f(g(x)).  If both inputs to compose are symbolic, then I think we want to just return f(g(x)) instead.


---

Comment by jrp created at 2010-11-18 01:45:57

Replying to [comment:17 jrp]:
> At the moment the powers-of-two speed up isn't helping even in the symbolic case, because the implementation is to return lambda x: f(g(x)).  If both inputs to compose are symbolic, then I think we want to just return f(g(x)) instead.

Given that symbolic functions have named variables, is this the correct behavior?


sage: f(x) = x+1
sage: g(y) = y+1
sage: compose(f,g)
y + 2
sage: compose(g,f)
x + 2


---

Comment by flawrence created at 2010-11-18 03:15:02

Replying to [comment:18 jrp]:
> Replying to [comment:17 jrp]:
> > At the moment the powers-of-two speed up isn't helping even in the symbolic case, because the implementation is to return lambda x: f(g(x)).  If both inputs to compose are symbolic, then I think we want to just return f(g(x)) instead.
> 
> Given that symbolic functions have named variables, is this the correct behavior?
> 
> 
> sage: f(x) = x+1
> sage: g(y) = y+1
> sage: compose(f,g)
> y + 2
> sage: compose(g,f)
> x + 2
I don't actually know anything about symbolic functions in Sage.  As such, all doctests and examples in the patch are for regular python functions not symbolic functions.  The compose functions in the patch use lambda functions, which may or may not break symbolic functions.

With normal python functions (such as those in the doctest), the powers-of-two provides a major speedup for large n over the other techniques I tried, both for the function composition and for the evaluation of the resulting function (benchmarked using "timeit").  In fact, without a powers-of-two-type algorithm, the self_compose function regularly hit the recursion limit and crashed for large n (above 500 or 1000).  But I don't know if anyone is interested in large n cases.


---

Comment by jrp created at 2010-11-18 07:38:20

Replying to [comment:19 flawrence]:

> With normal python functions (such as those in the doctest), the powers-of-two provides a major speedup for large n over the other techniques I tried, both for the function composition and for the evaluation of the resulting function (benchmarked using "timeit").  In fact, without a powers-of-two-type algorithm, the self_compose function regularly hit the recursion limit and crashed for large n (above 500 or 1000).

I ran the following:

```
sage: def f(x):
....:     return x + 1
....: 
sage: g = self_compose(f,10000)
sage: g
<function <lambda> at 0xb0aa80c>
sage: timeit('g(0)')
25 loops, best of 3: 9.41 ms per loop
sage: timeit('nest(f,10000,0)')
125 loops, best of 3: 6.35 ms per loop
```

Since nest just loops through xrange and doesn't use powers of two, maybe the slowdown before was due to the recursion.  But in any case, it definitely helps with the symbolic ones.

> The compose functions in the patch use lambda functions, which may or may not break symbolic functions.

I'm attaching a patch to check for symbolic functions and (hopefully) do the right thing.  I also make self_compose(f,0) return the identity.


---

Comment by zimmerma created at 2010-11-18 07:49:57

> Given that symbolic functions have named variables, is this the correct behavior?

```
sage: f(x) = x+1
sage: g(y) = y+1
sage: compose(f,g)
y + 2
sage: compose(g,f)
x + 2
```


[please use { { { and } } } to quote Sage examples]

I can't reproduce this. I get with the patch from Felix:

```
sage: f(x) = x+1
sage: g(y) = y+1
sage: compose(f,g)
<function <lambda> at 0x1787c80>
sage: compose(f,g)(x)
x + 2
```

which seems ok to me.

Paul


---

Comment by jrp created at 2010-11-18 19:10:06

Special treatment of symbolic functions.


---

Attachment

I realized that what really matters is the type of the first function in the composition - i.e., the type of g in compose(f,g).


---

Comment by jrp created at 2010-11-18 19:11:30

Changing status from needs_work to needs_review.


---

Comment by zimmerma created at 2010-11-18 19:15:42

jrp, you didn't answer comment 21. What was wrong with Felix patch?

Paul


---

Comment by jrp created at 2010-11-18 19:34:51

Paul - I wanted it to automatically do the right thing when g is a symbolic function.  I agree that this isn't very important since we can already just call compose(f,g)(x).  More important is that with symbolics, now the powers-of-two optimization will work.  (I don't think it did before, but will think more on this).


---

Comment by zimmerma created at 2010-11-18 20:51:06

I am not very happy with the fact that when f is an expression, the code assumes it has exactly
one symbolic variable:

```
sage: f = 2
sage: self_compose(f,0)
<function <lambda> at 0x41031b8>
sage: self_compose(f,1)
2
sage: self_compose(f,2)
<function <lambda> at 0x7fa8ac2b0d70>
```

or

```
sage: f = x+y
sage: self_compose(f,0)
x
sage: self_compose(f,1)
x + y
sage: self_compose(f,2)
x + 2*y
```

Consider also:

```
sage: f = pi+1
sage: self_compose(f,0)
---------------------------------------------------------------------------
IndexError                                Traceback (most recent call last)

/tmp/cado-nfs-1.0-rc1/<ipython console> in <module>()

/usr/local/sage-4.6/sage/local/lib/python2.6/site-packages/sage/misc/misc.pyc in self_compose(f, n)
    911     if n == 0:
    912         if type(f) == sage.symbolic.expression.Expression:
--> 913             return f.parent()(f.variables()[0])
    914         else:
    915             return lambda x: x

IndexError: tuple index out of range
```


I would prefer that symbolic expressions such as `f=x+1` are not allowed,
and we should write instead `f(x)=x+1` or `f = lambda x : x+1`.

Paul


---

Comment by zimmerma created at 2010-11-18 20:51:06

Changing status from needs_review to needs_work.


---

Comment by jrp created at 2010-11-22 20:09:46

Replying to [comment:25 zimmerma]:
> I would prefer that symbolic expressions such as `f=x+1` are not allowed,
> and we should write instead `f(x)=x+1` or `f = lambda x : x+1`.

I now think it's best to leave compose,self_compose, and nest agnostic to the type of f; the user can supply anything callable and we won't attempt to turn it back into a symbolic function.

Then as a separate issue, symbolic functions can grow an f.self_compose(n) function that plays nice with types.


---

Comment by jrp created at 2010-11-22 20:16:08

Replying to [comment:19 flawrence]:
> With normal python functions (such as those in the doctest), the powers-of-two provides a major speedup for large n over the other techniques I tried, both for the function composition and for the evaluation of the resulting function (benchmarked using "timeit").  In fact, without a powers-of-two-type algorithm, the self_compose function regularly hit the recursion limit and crashed for large n (above 500 or 1000).  But I don't know if anyone is interested in large n cases.

With normal python functions, I don't think there is any gain from powers of two.

With the self_compose from adds-compose-etc.patch:


```
sage: f = lambda x: x + 1
sage: g = x + 1
sage: f1 = self_compose(f,10000)
sage: g1 = self_compose(g,10000)
sage: timeit('self_compose(f,10000)')
625 loops, best of 3: 66.6 µs per loop
sage: timeit('self_compose(g,10000)')
625 loops, best of 3: 66.9 µs per loop
sage: timeit('f1(0)')                
25 loops, best of 3: 9.32 ms per loop
sage: timeit('g1(0)')
5 loops, best of 3: 375 ms per loop
sage: timeit('nest(f,10000,0)')
125 loops, best of 3: 6.46 ms per loop
sage: timeit('nest(g,10000,0)')
5 loops, best of 3: 379 ms per loop
sage: def new_self_compose(f,n):
....:     return lambda a: nest(f,n,a)
....: 
sage: timeit('new_self_compose(f,10000)')
625 loops, best of 3: 1.17 µs per loop
sage: timeit('new_self_compose(g,10000)')
625 loops, best of 3: 2.68 µs per loop
```


Since self_compose is implemented via `lambda x: f(g(x))`, we have to eventually pass the argument through `f` the correct number of times.

Let's move the powers of two, and the symbolics handling, into a method of symbolic functions.  Then the compose tools for python functions can have fast, dirt-simple implementations.


---

Attachment

adds compose, self_compose and nest functions. self_compose is a wrapper for nest.  a self-contained patch.


---

Comment by flawrence created at 2010-11-23 05:01:53

Changing status from needs_work to needs_review.


---

Comment by flawrence created at 2010-11-23 05:01:53

Changing component from basic arithmetic to misc.


---

Comment by flawrence created at 2010-11-23 05:01:53

Replying to [comment:27 jrp]:
> With normal python functions, I don't think there is any gain from powers of two.
> 
> With the self_compose from adds-compose-etc.patch:
(snip)
> Since self_compose is implemented via `lambda x: f(g(x))`, we have to eventually pass the argument through `f` the correct number of times.

Yes, `nest` is always faster than `self_compose` if you actually want to evaluate the function.  However the functions do different things: `nest` isn't really a compose function, since it returns f^n(x) not f^n.  `self_compose` is more useful than `nest` if you want to forget about f and only want to apply `f^n`.  In hindsight, `self_compose` should actually look like this, which I agree would be faster to construct and to evaluate than the powers of two method:

```

def self_compose(f,n):
    return lambda x: nest(f,n,x)
}}} 
> Let's move the powers of two, and the symbolics handling, into a method of symbolic functions.  Then the compose tools for python functions can have fast, dirt-simple implementations.
I agree that we should scrap the powers of two, and not go out of our way to support symbolics in this ticket.  I'm uploading a patch that makes the change detailed above.  I'm not going to have any more time to work on this for at least a month, so someone else will have to finish the ticket if further changes are required.

The new patch works for n = 0, but still does not check whether n is symbolic.  I don't think this is the worst thing in the world: the documentation does state that n should be a nonnegative integer, and if it is symbolic then the error raised is appropriate IMO:
{{{

sage: _ = var('x y')
sage: nest(sin,x,y)
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)

/Applications/sage/devel/sage-dev/<ipython console> in <module>()

/Applications/sage/local/lib/python2.6/site-packages/sage/misc/misc.pyc in nest(f, n, x)
    939     
    940     """
--> 941     for i in xrange(n):
    942         x = f(x)
    943     return x

/Applications/sage/local/lib/python2.6/site-packages/sage/symbolic/expression.so in sage.symbolic.expression.Expression.__int__ (sage/symbolic/expression.cpp:4375)()

/Applications/sage/local/lib/python2.6/site-packages/sage/symbolic/expression.so in sage.symbolic.expression.Expression.n (sage/symbolic/expression.cpp:17185)()

TypeError: cannot evaluate symbolic expression numerically
}}}


---

Comment by flawrence created at 2010-11-23 05:01:53

Changing type from defect to enhancement.


---

Comment by zimmerma created at 2010-11-24 07:12:56

Changing status from needs_review to positive_review.


---

Comment by jdemeyer created at 2010-12-02 13:54:04

Please state clearly in the ticket description which patches have to be applied.


---

Comment by jdemeyer created at 2010-12-02 13:54:04

Changing status from positive_review to needs_info.


---

Comment by zimmerma created at 2010-12-03 22:36:12

Changing status from needs_info to needs_review.


---

Comment by zimmerma created at 2010-12-03 22:36:48

Changing status from needs_review to positive_review.


---

Comment by jdemeyer created at 2011-01-26 18:32:41

This needs to be rebased to sage-4.6.2.alpha2.  You might also want to check for conflicts with #8456 (so it might be safer to base your patch to sage-4.6.2.alpha2 + #8456).


---

Comment by jdemeyer created at 2011-01-26 18:32:41

Changing status from positive_review to needs_work.


---

Comment by zimmerma created at 2011-01-26 20:33:06

does anybody know why this patch with positive review was not included in 4.6.1?

Paul


---

Comment by jdemeyer created at 2011-01-26 21:42:45

Replying to [comment:35 zimmerma]:
> does anybody know why this patch with positive review was not included in 4.6.1?
I know because I was the one making that decision.

Most likely, the 4.6.1 release cycle was in bug-fix-only status at the time when this patch got positive_review.  Unfortunately, 4.6.1 stayed in that status for quite a while (much longer than usual Sage releases) because there were a lot of changes in the Sage build scripts giving rise to many system-specific issues which had to be tracked down.


---

Comment by jdemeyer created at 2011-02-16 09:37:33

Anybody wants to look at this?...


---

Attachment

Rebased for 4.6.2.rc0


---

Comment by flawrence created at 2011-02-19 07:16:37

Only change since the positive review was updating the change to sage/misc/all.py


---

Comment by flawrence created at 2011-02-19 07:16:37

Changing status from needs_work to needs_review.


---

Comment by zimmerma created at 2011-02-19 08:48:44

Changing status from needs_review to needs_work.


---

Comment by zimmerma created at 2011-02-19 08:48:44

a minor point: it would be good to check that n is indeed a nonnegative integer in
`self_compose` and `nest`, otherwise we can get strange results:

```
sage: self_compose(sin, -3)(x) 
x
sage: self_compose(sin, x)(x)
...
TypeError: cannot evaluate symbolic expression numerically
```


Paul


---

Attachment

checks that n is a nonnegative integer


---

Comment by flawrence created at 2011-02-19 10:42:12

Changing status from needs_work to needs_review.


---

Comment by flawrence created at 2011-02-19 10:42:12

Replying to [comment:39 zimmerma]:
> a minor point: it would be good to check that n is indeed a nonnegative integer in
> `self_compose` and `nest`, otherwise we can get strange results

Done:


```
sage: self_compose(sin, -3)
...
ValueError: n must be a nonnegative integer, not -3.
sage: self_compose(sin, x)
...
TypeError: n (=x) must be of type (<type 'int'>, <type 'long'>, <type 'sage.rings.integer.Integer'>).
```



---

Comment by zimmerma created at 2011-02-19 14:14:35

positive review, thank you Christoph and Felix for that nice work!

Paul


---

Comment by zimmerma created at 2011-02-19 14:14:35

Changing status from needs_review to positive_review.


---

Comment by zimmerma created at 2011-02-19 14:16:19

and thank you for the extra rebase work, I hope this time the patch will be included soon...

Paul


---

Comment by jdemeyer created at 2011-03-17 19:22:27

Resolution: fixed

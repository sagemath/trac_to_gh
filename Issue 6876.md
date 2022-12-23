# Issue 6876: plotting prime_pi and nth_prime fails

Issue created by migration from https://trac.sagemath.org/ticket/6876

Original creator: whuss

Original creation time: 2009-09-03 11:30:15

Assignee: was

CC:  kcrisman

Plotting *prime_pi* gives the following error:


```
sage: plot(prime_pi(x), (x, 1, 100))
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)

/home/huss/.sage/temp/bernoulli/12905/_home_huss__sage_init_sage_0.py in <module>()

/local/data/huss/software/sage-4.1.1/local/lib/python2.6/site-packages/sage/functions/prime_pi.so in sage.functions.prime_pi.PrimePi.__call__ (sage/functions/prime_pi.c:1038)()

/local/data/huss/software/sage-4.1.1/local/lib/python2.6/site-packages/sage/symbolic/expression.so in sage.symbolic.expression.Expression.__int__ (sage/symbolic/expression.cpp:4389)()

/local/data/huss/software/sage-4.1.1/local/lib/python2.6/site-packages/sage/symbolic/expression.so in sage.symbolic.expression.Expression.__float__ (sage/symbolic/expression.cpp:5526)()

TypeError: float() argument must be a string or a number
```


It also does not work without the variable:


```
sage: plot(prime_pi, (1, 100))
ERROR: An unexpected error occurred while tokenizing input
The following traceback may be corrupted or invalid
The error message is: ('EOF in multi-line statement', (35, 0))

---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)

/home/huss/.sage/temp/bernoulli/12905/_home_huss__sage_init_sage_0.py in <module>()

/local/data/huss/software/sage-4.1.1/local/lib/python2.6/site-packages/sage/plot/misc.pyc in wrapper(*args, **kwds)
    238                     kwds[new_name] = kwds[old_name]
    239                     del kwds[old_name]
--> 240             return func(*args, **kwds)
    241
    242         from sage.misc.sageinspect import sage_getsource

/local/data/huss/software/sage-4.1.1/local/lib/python2.6/site-packages/sage/plot/misc.pyc in wrapper(*args, **kwds)
    133                 options['__original_opts'] = kwds
    134             options.update(kwds)
--> 135             return func(*args, **options)
    136
    137

/local/data/huss/software/sage-4.1.1/local/lib/python2.6/site-packages/sage/plot/plot.pyc in plot(funcs, *args, **kwds)
   2052     do_show = kwds.pop('show',False)
   2053     if hasattr(funcs, 'plot'):
-> 2054         G = funcs.plot(*args, **original_opts)
   2055     # if we are using the generic plotting method
   2056     else:

/local/data/huss/software/sage-4.1.1/local/lib/python2.6/site-packages/sage/functions/prime_pi.so in sage.functions.prime_pi.PrimePi.plot (sage/functions/prime_pi.c:2395)()

/local/data/huss/software/sage-4.1.1/local/lib/python2.6/site-packages/sage/functions/prime_pi.so in sage.functions.prime_pi.PrimePi.__call__ (sage/functions/prime_pi.c:1038)()

TypeError: an integer is required
```


For *nth_prime*


```
sage: plot(nth_prime(x), (x, 1, 100))
```


also gives an error, but


```
sage: plot(nth_prime, (1, 100))
```


works.


---

Comment by jason created at 2010-01-05 01:05:43

This is because it implements its own variable handling, instead of using the standard sage.plot.misc.setup_for_eval_on_grid function (which, to be fair, probably wasn't around when prime_pi was written).

There are plenty of examples of how to use setup_for_eval_on_grid in the plotting code.  Possibly, the variable-handling code should be factored out of that function as well.


---

Comment by kcrisman created at 2012-05-26 20:43:32

Here is what _did already_ work.

```
sage: plot(prime_pi,1,1000)
```

because

```
Definition:	prime_pi.plot(self, xmin, xmax=0, vertical_lines=100, **kwds=True)
Docstring:
```

So really we want to make prime_pi symbolic.  Same with nth_prime, presumably.

And it so happens that #11475 has done so, though unfortunately keeping a custom plotting method intact.

```
sage: plot(prime_pi(x), (x, 1, 100)) # works with #11475
sage: plot(prime_pi, (x, 1, 100)) # gives empty plot with #11475 since it is the same as doing sage: prime_pi.plot((x,1,100))
sage: plot(prime_pi,(1,100)) # same
sage: plot(prime_pi, x, 1, 100) # error about floats
sage: plot(prime_pi(x), x, 1, 100) # works with #11475
```

So we would want to someone modify that work to make the other things work that should.  And same for `nth_prime`.


---

Comment by was created at 2012-05-26 21:19:08

> though unfortunately keeping a custom plotting method intact.

Prime_pi should have a custom plotting method since it is a *step function* so plotting via sampling will be very misleading.


---

Comment by kcrisman created at 2012-05-26 21:45:15

> > though unfortunately keeping a custom plotting method intact.
> 
> Prime_pi should have a custom plotting method since it is a *step function* so plotting via sampling will be very misleading. 
Oh, duh, yes you're right.  So this means the plot at #11475 I just added is bad (actually, it's fine, because we sample plenty, but for larger regions it won't be), so I'm removing it.

Hmm, that means we need to not only make them symbolic, but try to figure out what to do so that we _don't_ get that bad behavior in fixing this.  At least a good error message would be helpful...


---

Comment by kedlaya created at 2016-08-17 00:56:07

Just tried this in 7.3 and it no longer returns an error:

```
sage: sage: plot(prime_pi(x), (x, 1, 100))
Launched png viewer for Graphics object consisting of 1 graphics primitive
```

(and then a picture pops up). Does that mean this ticket can be closed?


---

Comment by paulmasson created at 2016-08-20 19:50:21

Plotting of `prime_pi` now works as expected, but another part of the ticket is making `nth_prime` symbolic. Is that still useful?


---

Comment by kedlaya created at 2016-08-20 21:11:15

I don't know whether any of it is useful, but it is indeed the case that the issue raised still exists for `nth_prime`, so this ticket can't be closed as fixed.

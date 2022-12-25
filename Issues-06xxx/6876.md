# Issue 6876: plotting prime_pi and nth_prime fails

archive/issues_006876.json:
```json
{
    "body": "Assignee: @williamstein\n\nCC:  @kcrisman\n\nPlotting **prime_pi** gives the following error:\n\n```\nsage: plot(prime_pi(x), (x, 1, 100))\n---------------------------------------------------------------------------\nTypeError                                 Traceback (most recent call last)\n\n/home/huss/.sage/temp/bernoulli/12905/_home_huss__sage_init_sage_0.py in <module>()\n\n/local/data/huss/software/sage-4.1.1/local/lib/python2.6/site-packages/sage/functions/prime_pi.so in sage.functions.prime_pi.PrimePi.__call__ (sage/functions/prime_pi.c:1038)()\n\n/local/data/huss/software/sage-4.1.1/local/lib/python2.6/site-packages/sage/symbolic/expression.so in sage.symbolic.expression.Expression.__int__ (sage/symbolic/expression.cpp:4389)()\n\n/local/data/huss/software/sage-4.1.1/local/lib/python2.6/site-packages/sage/symbolic/expression.so in sage.symbolic.expression.Expression.__float__ (sage/symbolic/expression.cpp:5526)()\n\nTypeError: float() argument must be a string or a number\n```\n\nIt also does not work without the variable:\n\n```\nsage: plot(prime_pi, (1, 100))\nERROR: An unexpected error occurred while tokenizing input\nThe following traceback may be corrupted or invalid\nThe error message is: ('EOF in multi-line statement', (35, 0))\n\n---------------------------------------------------------------------------\nTypeError                                 Traceback (most recent call last)\n\n/home/huss/.sage/temp/bernoulli/12905/_home_huss__sage_init_sage_0.py in <module>()\n\n/local/data/huss/software/sage-4.1.1/local/lib/python2.6/site-packages/sage/plot/misc.pyc in wrapper(*args, **kwds)\n    238                     kwds[new_name] = kwds[old_name]\n    239                     del kwds[old_name]\n--> 240             return func(*args, **kwds)\n    241\n    242         from sage.misc.sageinspect import sage_getsource\n\n/local/data/huss/software/sage-4.1.1/local/lib/python2.6/site-packages/sage/plot/misc.pyc in wrapper(*args, **kwds)\n    133                 options['__original_opts'] = kwds\n    134             options.update(kwds)\n--> 135             return func(*args, **options)\n    136\n    137\n\n/local/data/huss/software/sage-4.1.1/local/lib/python2.6/site-packages/sage/plot/plot.pyc in plot(funcs, *args, **kwds)\n   2052     do_show = kwds.pop('show',False)\n   2053     if hasattr(funcs, 'plot'):\n-> 2054         G = funcs.plot(*args, **original_opts)\n   2055     # if we are using the generic plotting method\n   2056     else:\n\n/local/data/huss/software/sage-4.1.1/local/lib/python2.6/site-packages/sage/functions/prime_pi.so in sage.functions.prime_pi.PrimePi.plot (sage/functions/prime_pi.c:2395)()\n\n/local/data/huss/software/sage-4.1.1/local/lib/python2.6/site-packages/sage/functions/prime_pi.so in sage.functions.prime_pi.PrimePi.__call__ (sage/functions/prime_pi.c:1038)()\n\nTypeError: an integer is required\n```\n\nFor **nth_prime**\n\n```\nsage: plot(nth_prime(x), (x, 1, 100))\n```\n\nalso gives an error, but\n\n```\nsage: plot(nth_prime, (1, 100))\n```\n\nworks.\n\nIssue created by migration from https://trac.sagemath.org/ticket/6876\n\n",
    "created_at": "2009-09-03T11:30:15Z",
    "labels": [
        "component: graphics",
        "minor",
        "bug"
    ],
    "title": "plotting prime_pi and nth_prime fails",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/6876",
    "user": "https://trac.sagemath.org/admin/accounts/users/whuss"
}
```
Assignee: @williamstein

CC:  @kcrisman

Plotting **prime_pi** gives the following error:

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

For **nth_prime**

```
sage: plot(nth_prime(x), (x, 1, 100))
```

also gives an error, but

```
sage: plot(nth_prime, (1, 100))
```

works.

Issue created by migration from https://trac.sagemath.org/ticket/6876





---

archive/issue_comments_056657.json:
```json
{
    "body": "This is because it implements its own variable handling, instead of using the standard sage.plot.misc.setup_for_eval_on_grid function (which, to be fair, probably wasn't around when prime_pi was written).\n\nThere are plenty of examples of how to use setup_for_eval_on_grid in the plotting code.  Possibly, the variable-handling code should be factored out of that function as well.",
    "created_at": "2010-01-05T01:05:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6876",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6876#issuecomment-56657",
    "user": "https://github.com/jasongrout"
}
```

This is because it implements its own variable handling, instead of using the standard sage.plot.misc.setup_for_eval_on_grid function (which, to be fair, probably wasn't around when prime_pi was written).

There are plenty of examples of how to use setup_for_eval_on_grid in the plotting code.  Possibly, the variable-handling code should be factored out of that function as well.



---

archive/issue_comments_056658.json:
```json
{
    "body": "Here is what *did already* work.\n\n```\nsage: plot(prime_pi,1,1000)\n```\nbecause\n\n```\nDefinition:\tprime_pi.plot(self, xmin, xmax=0, vertical_lines=100, **kwds=True)\nDocstring:\n```\nSo really we want to make prime_pi symbolic.  Same with nth_prime, presumably.\n\nAnd it so happens that #11475 has done so, though unfortunately keeping a custom plotting method intact.\n\n```\nsage: plot(prime_pi(x), (x, 1, 100)) # works with #11475\nsage: plot(prime_pi, (x, 1, 100)) # gives empty plot with #11475 since it is the same as doing sage: prime_pi.plot((x,1,100))\nsage: plot(prime_pi,(1,100)) # same\nsage: plot(prime_pi, x, 1, 100) # error about floats\nsage: plot(prime_pi(x), x, 1, 100) # works with #11475\n```\nSo we would want to someone modify that work to make the other things work that should.  And same for `nth_prime`.",
    "created_at": "2012-05-26T20:43:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6876",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6876#issuecomment-56658",
    "user": "https://github.com/kcrisman"
}
```

Here is what *did already* work.

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

archive/issue_comments_056659.json:
```json
{
    "body": "> though unfortunately keeping a custom plotting method intact.\n\n\nPrime_pi should have a custom plotting method since it is a *step function* so plotting via sampling will be very misleading.",
    "created_at": "2012-05-26T21:19:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6876",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6876#issuecomment-56659",
    "user": "https://github.com/williamstein"
}
```

> though unfortunately keeping a custom plotting method intact.


Prime_pi should have a custom plotting method since it is a *step function* so plotting via sampling will be very misleading.



---

archive/issue_comments_056660.json:
```json
{
    "body": "> > though unfortunately keeping a custom plotting method intact.\n\n> \n> Prime_pi should have a custom plotting method since it is a *step function* so plotting via sampling will be very misleading. \n\nOh, duh, yes you're right.  So this means the plot at #11475 I just added is bad (actually, it's fine, because we sample plenty, but for larger regions it won't be), so I'm removing it.\n\nHmm, that means we need to not only make them symbolic, but try to figure out what to do so that we *don't* get that bad behavior in fixing this.  At least a good error message would be helpful...",
    "created_at": "2012-05-26T21:45:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6876",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6876#issuecomment-56660",
    "user": "https://github.com/kcrisman"
}
```

> > though unfortunately keeping a custom plotting method intact.

> 
> Prime_pi should have a custom plotting method since it is a *step function* so plotting via sampling will be very misleading. 

Oh, duh, yes you're right.  So this means the plot at #11475 I just added is bad (actually, it's fine, because we sample plenty, but for larger regions it won't be), so I'm removing it.

Hmm, that means we need to not only make them symbolic, but try to figure out what to do so that we *don't* get that bad behavior in fixing this.  At least a good error message would be helpful...



---

archive/issue_comments_056661.json:
```json
{
    "body": "Just tried this in 7.3 and it no longer returns an error:\n\n```\nsage: sage: plot(prime_pi(x), (x, 1, 100))\nLaunched png viewer for Graphics object consisting of 1 graphics primitive\n```\n(and then a picture pops up). Does that mean this ticket can be closed?",
    "created_at": "2016-08-17T00:56:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6876",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6876#issuecomment-56661",
    "user": "https://github.com/kedlaya"
}
```

Just tried this in 7.3 and it no longer returns an error:

```
sage: sage: plot(prime_pi(x), (x, 1, 100))
Launched png viewer for Graphics object consisting of 1 graphics primitive
```
(and then a picture pops up). Does that mean this ticket can be closed?



---

archive/issue_comments_056662.json:
```json
{
    "body": "Plotting of `prime_pi` now works as expected, but another part of the ticket is making `nth_prime` symbolic. Is that still useful?",
    "created_at": "2016-08-20T19:50:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6876",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6876#issuecomment-56662",
    "user": "https://github.com/paulmasson"
}
```

Plotting of `prime_pi` now works as expected, but another part of the ticket is making `nth_prime` symbolic. Is that still useful?



---

archive/issue_comments_056663.json:
```json
{
    "body": "I don't know whether any of it is useful, but it is indeed the case that the issue raised still exists for `nth_prime`, so this ticket can't be closed as fixed.",
    "created_at": "2016-08-20T21:11:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6876",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6876#issuecomment-56663",
    "user": "https://github.com/kedlaya"
}
```

I don't know whether any of it is useful, but it is indeed the case that the issue raised still exists for `nth_prime`, so this ticket can't be closed as fixed.

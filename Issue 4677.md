# Issue 4677: Plotting lambda functions

Issue created by migration from Trac.

Original creator: kcrisman

Original creation time: 2008-12-02 17:51:07

Assignee: was

This works:

```
sage: f=x^2
sage: plot(lambda x:f(x),(x,-1,1))
```

But this doesn't:

```
sage: f=x^2
sage: plot(lambda x:f,(x,-1,1))
verbose 0 (3633: plot.py, _plot) WARNING: When plotting, failed to evaluate function at 400 points.
verbose 0 (3633: plot.py, _plot) Last error message: 'float() argument must be a string or a number'
```

The behavior is the same for f(x)=x^2.

This is because in the second example "evaluating" the lambda function yields a SymbolicCallableExpression, which needs to be called again to actually yield a numerical value.  


---

Comment by jason created at 2008-12-02 23:07:04

Sure, it probably shouldn't work:


```
sage: f=x^2
sage: a=lambda x: f
sage: a(2)
x^2
```


plot expects that when it feeds "a" a number (like a(2)), a number should be returned.  Instead, a function is returned.


---

Comment by kcrisman created at 2008-12-03 00:52:37

Replying to [comment:1 jason]:
> Sure, it probably shouldn't work: 
> plot expects that when it feeds "a" a number (like a(2)), a number should be returned.  Instead, a function is returned.

I guess my point was that I think one can catch this and use it.  Unless for some reason this is not desired, like some MS Word "guesses" at fixing mistakes, it is the sort of thing that one can do

```
sage: f=x^2
sage: a=lambda x: f
sage: a(2)
x^2
sage: a=a(x)
sage: a(2)
4
```

so that in principle upon a TypeError, one could try letting func=func(x) and then do float(func(point)).  

But I don't have time to try that for a few more days.  And maybe there is some internal reason not to do this... but I don't think so, because the result of plotting these is the empty plot otherwise, and one would reraise the exception if this still caused a TypeError.  Can you think of anything where this would not raise an exception but still lead to bad behavior?  I've seen weirder things...


---

Comment by jason created at 2008-12-03 01:15:13

I think this is enough of a change in design that the issue ought to be raised on sage-devel to get more input.  Would you like to post a message?


---

Comment by kcrisman created at 2009-01-24 19:38:57

Changing assignee from was to kcrisman.


---

Comment by kcrisman created at 2009-01-24 19:38:57

Replying to [comment:3 jason]:
> I think this is enough of a change in design that the issue ought to be raised on sage-devel to get more input.  Would you like to post a message?

This was done, but the issue generated no interest on sage-devel, so I will go ahead and try to implement and document this as detailed above.


---

Comment by jason created at 2010-03-17 05:25:06

Changing type from defect to enhancement.


---

Comment by kcrisman created at 2012-07-07 03:24:57

Remove assignee kcrisman.

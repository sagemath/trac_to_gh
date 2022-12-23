# Issue 9630: Python ints should have a conversion to Maxima

Issue created by migration from https://trac.sagemath.org/ticket/9630

Original creator: kcrisman

Original creation time: 2010-07-29 01:36:07

Assignee: burcin

CC:  mjo

I don't know how this might be done, but 

```
for n in range(1,10): 
    sum(k, k, 1, n) 
```

doesn't work, while 

```
for n in [1..10]:
    sum(k,k,1,n)
```

does.  We need to fix

```
int(3)._maxima_()
AttributeError: 'int' object has no attribute '_maxima_'
```



---

Comment by nbruin created at 2010-07-29 06:31:11

the particular error that arises here is raised in sage/calculus/calculus.pyc line 501:

```
sum  = "'sum(%s, %s, %s, %s)" % tuple([repr(expr._maxima_()) for expr in (expression, v, a, b)])
```

One could fix this one by first coercing a,b into SR. As an example:

```
sage: SR(int(1))._maxima_()
1
```

This code looks rather convoluted to me anyway: Convert to maxima, take string representative, paste together and then simplify? Shouldn't the whole sum first be turned into a pynac sum expression, the whole thing converted to maxima, simplified, and then cast back?

```
sage: var("x,a,b")                       # this is just because I don't know
sage: SUM=sum(sin(x^2),x,a,b).operator() # where this is defined
sage: SR(SUM(x,x,1,int(10))._maxima_().simplify_sum())
55
```



---

Comment by kcrisman created at 2010-07-29 13:23:47

Sure, if Pynac sum expressions had been known to exist (or how to use them) when this code went in.  There was also some weird bug that this originally took care of that had to do with held expressions in Maxima, if I recall correctly, though that had ceased to be an issue.

This just goes to show that we need some sort of Pynac tutorial so that more people can be effective on this!


---

Comment by mjo created at 2012-01-16 05:29:30

I don't think it's possible to monkey-patch methods onto int, but the symbolic sum issue has been fixed and I have a patch with a doctest (needs review!) at #9393.


---

Comment by burcin created at 2012-01-16 09:39:42

This is a duplicate of #9393. There is a patch with a doctest attached to that ticket.


---

Comment by burcin created at 2012-01-16 09:39:42

Changing status from new to needs_review.


---

Comment by burcin created at 2012-01-16 09:39:49

Changing status from needs_review to positive_review.


---

Comment by jdemeyer created at 2012-01-16 10:07:05

Resolution: duplicate

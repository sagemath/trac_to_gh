# Issue 8603: Partial sums are off for Fourier series of piecewise functions

Issue created by migration from Trac.

Original creator: novoselt

Original creation time: 2010-03-25 04:06:02

Assignee: burcin

CC:  wdj jason jondo kcrisman vbraun slelievre mkoeppe eviatarbach rws novoselt

Doing

```
f = Piecewise([This is the Trac macro ** that was inherited from the migration called with arguments (-pi, pi), x)](https://trac.sagemath.org/wiki/WikiMacros#-macro))
print f.fourier_series_partial_sum(2, pi)
print f.fourier_series_partial_sum(3, pi)
```

we get

```
2*sin(x)
-sin(2*x) + 2*sin(x)
```

while according to the documentation we should get the second output with the first command.


---

Comment by kcrisman created at 2011-03-14 20:25:10

Changing priority from major to minor.


---

Comment by kcrisman created at 2011-03-14 20:25:10

This is still true, and syntax is also deprecated.

```

sage: f = Piecewise([This is the Trac macro ** that was inherited from the migration called with arguments (-pi, pi), x)](https://trac.sagemath.org/wiki/WikiMacros#-macro))
sage: print f.fourier_series_partial_sum(2, pi)
/Applications/MathApps/sage/local/lib/python2.6/site-packages/sage/functions/piecewise.py:1095: DeprecationWarning: Substitution using function-call syntax and unnamed arguments is deprecated and will be removed from a future release of Sage; you can use named arguments instead, like EXPR(x=..., y=...)
  a0 = self.fourier_series_cosine_coefficient(0,L)
/Applications/MathApps/sage/local/lib/python2.6/site-packages/sage/functions/piecewise.py:1099: DeprecationWarning: Substitution using function-call syntax and unnamed arguments is deprecated and will be removed from a future release of Sage; you can use named arguments instead, like EXPR(x=..., y=...)
  for n in srange(1,N)])
2*sin(x)
sage: print f.fourier_series_partial_sum(3, pi)
-sin(2*x) + 2*sin(x)
```



---

Comment by novoselt created at 2011-06-18 00:31:32

Changing keywords from "" to "sd31".


---

Comment by novoselt created at 2011-06-18 00:31:32

On a related note: what is the purpose of `plot` methods for Fourier partial sums? They don't do anything except for passing arguments to the usual global `plot` function, so they seem redundant to me and perhaps can be removed (after deprecation period).


---

Comment by kcrisman created at 2011-06-18 00:41:27

You may be right.  I'd have to look at it.  Remember, these are all _really_ old, so they probably at the time bypassed the non-existent 'plot' function, and then were subsequently changed, perhaps.


---

Comment by wdj created at 2011-06-18 10:44:59

one line change in docstring


---

Comment by wdj created at 2011-06-18 10:46:16

Changing status from new to needs_review.


---

Attachment

This fixes the documentation of fourier_series_partial_sum, replacing

```
 f(x) \sim \frac{a_0}{2} + \sum_{n=1}^N [a_n\cos(\frac{n\pi x}{L}) +
b_n\sin(\frac{n\pi x}{L})],
```

by

```
 f(x) \sim \frac{a_0}{2} + \sum_{n=1}^{N-1} [a_n\cos(\frac{n\pi x}{L})
+ b_n\sin(\frac{n\pi x}{L})],
```



---

Comment by kcrisman created at 2011-06-19 01:23:35

Thanks, David; I don't have time to review this now, but appreciate it.  

Andrey and I were discussing this at Sage Days 31, and thought that maybe changing the behavior instead to match Taylor series would be good, but if this was in fact what you had intended all along, then this solution is better.


---

Comment by burcin created at 2011-06-19 02:42:25

Replying to [comment:5 kcrisman]:
> Thanks, David; I don't have time to review this now, but appreciate it.  
> 
> Andrey and I were discussing this at Sage Days 31, and thought that maybe changing the behavior instead to match Taylor series would be good, but if this was in fact what you had intended all along, then this solution is better. 

The `.series()` method of symbolic expressions cut off in a pythonic way, like David's change here. If `.taylor()` does something different we should change it.

This is a trivial change. I'd be happy to give a positive review if it passes all tests but the patch bot doesn't seem to be working for some reason.


---

Comment by novoselt created at 2011-06-21 17:48:20

Changing status from needs_review to needs_work.


---

Comment by novoselt created at 2011-06-21 17:48:20

There are more instances of the same typo in other functions of this module, let's fix them all at once!-)

David, do you agree that plot methods can be eliminated as they are not really doing anything?


---

Comment by kcrisman created at 2011-08-15 14:30:07

Replying to [comment:7 novoselt]:
> There are more instances of the same typo in other functions of this module, let's fix them all at once!-)
Can you be more specific?
> David, do you agree that plot methods can be eliminated as they are not really doing anything?
I think I looked at this at Sage Days 31, but now I forgot whether that statement is true.


---

Comment by mkoeppe created at 2016-06-27 03:31:36

Updated with information regarding the new `piecewise` implementation from #14801.


---

Comment by mkoeppe created at 2016-06-27 03:31:36

Changing status from needs_work to needs_info.


---

Comment by egourgoulhon created at 2017-09-07 12:01:47

This is fixed by #23672.

Regarding the example in the ticket description, in Sage 8.1.beta4, we have now

```
sage: f = piecewise([This is the Trac macro ** that was inherited from the migration called with arguments (-pi, pi), x)](https://trac.sagemath.org/wiki/WikiMacros#-macro))
sage: f.fourier_series_partial_sum(2, pi)
-sin(2*x) + 2*sin(x)
```

We even have, since the half-period is now a default argument,

```
sage: f.fourier_series_partial_sum(2)
-sin(2*x) + 2*sin(x)
```



---

Comment by egourgoulhon created at 2017-09-07 12:01:47

Changing status from needs_info to positive_review.


---

Comment by kcrisman created at 2017-09-07 14:33:16

Excellent.  Is this documented via a test?


---

Comment by kcrisman created at 2017-09-07 14:33:38

Changing status from positive_review to needs_info.


---

Comment by egourgoulhon created at 2017-09-07 14:41:41

Replying to [comment:16 kcrisman]:
> Excellent.  Is this documented via a test?

Yes this is documented, both in [Sage Reference Manual](http://doc.sagemath.org/html/en/reference/) and in [Sage Constructions](http://doc.sagemath.org/html/en/constructions/), see [here](https://git.sagemath.org/sage.git/commit?id=ddeef52c783ef2f87c21b4b26e4410ace5007f02).


---

Comment by kcrisman created at 2017-09-07 17:30:44

Sweet.  Strange that it didn't cause any doctest errors then?  If it didn't, we should make sure to include at least two of the examples on the ticket in the doc _somewhere_.


---

Comment by kcrisman created at 2017-09-07 17:30:44

Changing status from needs_info to positive_review.


---

Comment by egourgoulhon created at 2017-09-07 19:30:33

Replying to [comment:19 kcrisman]:
> Sweet.  Strange that it didn't cause any doctest errors then?  If it didn't, we should make sure to include at least two of the examples on the ticket in the doc _somewhere_.

I am not sure to understand what you mean. In the current version, as integrated in Sage 8.1.beta4, there are doctests like

```
sage: f = piecewise([((-1,0), -1), ((0,1), 1)])
sage: f.fourier_series_partial_sum(5)
4/5*sin(5*pi*x)/pi + 4/3*sin(3*pi*x)/pi + 4*sin(pi*x)/pi
```

In Sage <= 8.0, this would have returned (*)

```
4/3*sin(3*pi*x)/pi + 4*sin(pi*x)/pi
```


(*) with the half-period added as the second argument, i.e. `f.fourier_series_partial_sum(5, 1)`)


---

Comment by kcrisman created at 2017-09-07 21:34:42

My concern was just that the _correct_ nature was doctested, not the wrong one, and that we really did have that to test against regression at some point.  Good!


---

Comment by embray created at 2017-12-12 08:23:33

Resolution: wontfix


---

Comment by zimmerma created at 2017-12-12 13:27:06

I wonder why "wontfix" since the issue is fixed in 8.1.beta4.
Paul


---

Comment by egourgoulhon created at 2017-12-12 13:41:20

Replying to [comment:23 zimmerma]:
> I wonder why "wontfix" since the issue is fixed in 8.1.beta4.
> Paul
Actually, as said in comment:15, the issue is fixed in another ticket: #23672, hence the "sage-duplicate/invalid/wontfix" milestone for the current one and the "wonfix" resolution.


---

Comment by kcrisman created at 2017-12-12 15:18:01

Hey, do non-release managers get to mark "closed"?  That would be a change in protocol.

Also, maybe the resolution should be "fixed" or "duplicate" if it is indeed fixed in another ticket?


---

Comment by kcrisman created at 2017-12-12 15:18:01

Resolution changed from wontfix to duplicate


---

Comment by egourgoulhon created at 2017-12-12 15:27:29

Replying to [comment:26 kcrisman]:
> Hey, do non-release managers get to mark "closed"?  That would be a change in protocol.
> 

This was announced in https://groups.google.com/d/msg/sage-release/4bIUu1NECwY/we3BMdkeAAAJ with apparently the approval of the release manager.

> Also, maybe the resolution should be "fixed" or "duplicate" if it is indeed fixed in another ticket?

Ah yes, you are right (I thought this was automatically set to "wontfix"  while closing "sage-duplicate/invalid/wontfix" tickets).


---

Comment by kcrisman created at 2017-12-12 19:15:37

Replying to [comment:27 egourgoulhon]:
> Replying to [comment:26 kcrisman]:
> > Hey, do non-release managers get to mark "closed"?  That would be a change in protocol.
> > 
> 
> This was announced in https://groups.google.com/d/msg/sage-release/4bIUu1NECwY/we3BMdkeAAAJ with apparently the approval of the release manager.
> 

10 hours ago :-) but this will be welcome for obvious dupes etc.

> > Also, maybe the resolution should be "fixed" or "duplicate" if it is indeed fixed in another ticket?
> 
> Ah yes, you are right (I thought this was automatically set to "wontfix"  while closing "sage-duplicate/invalid/wontfix" tickets).

Yeah, that might be the default, but typically we try to be precise on this. Nice.

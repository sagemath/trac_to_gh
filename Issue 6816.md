# Issue 6816: sage/maxima hang when doing an indefinite integral

Issue created by migration from https://trac.sagemath.org/ticket/6816

Original creator: was

Original creation time: 2009-08-24 00:07:01

Assignee: burcin

CC:  mhansen

Integration sometimes hangs in sage-4.1.1.


```
flat:~ wstein$ sage
----------------------------------------------------------------------
----------------------------------------------------------------------
sage: var('t,theta')
(t, theta)
sage: integrate(t * cos(-theta*t), (t,-oo,oo))
[.. and it hangs forever ..]
```

| Sage Version 4.1.1, Release Date: 2009-08-14                       |
| Type notebook() for the GUI, and license() for information.        |
In fact, in Maxima what is happening is the following:

```
(%i6) integrate(t*cos(-theta*t),t,-inf,inf);
Is  theta  positive, negative, or zero?

positive       <--- i type this.

;
(%o6)                                  0
(%i7) 
```


For some reason the question "Is  theta  positive, negative, or zero?" is not getting seen by pexpect as it should.  Argh!

This works in Maxima:

```
(%i1) assume(theta>0);
(%o1)                             [theta > 0]
(%i2) integrate(t*cos(-theta*t),t,-inf,inf);
(%o2)                                  0
```


The same doesn't work in Sage though, which is very weird:

```
sage: var('t,theta')
(t, theta)
sage: assume(theta>0)
sage: integrate(t * cos(-theta*t), (t,-oo,oo))
```



---

Comment by kcrisman created at 2009-09-24 13:49:10

Just an update; in Maxima 5.19.1 (in Sage, in fact from maxima_console() ) this particular example does not even ask a question but returns zero.

But it still hangs in Sage.  That is really strange.  Note that the indefinite integral works fine in Sage.


---

Comment by kcrisman created at 2009-10-05 15:45:51

This ticket is invalid.  


```
sage: var('t,theta')
(t, theta)
sage: integrate(t*cos(-theta*t),t,-oo,oo)
0
```


In fact, ANY sage integration attempted with the syntax provided by the originator of the ticket will fail!!!  That's because (for better or for worse) we don't have #1221 or #2787 in Sage.  But those tickets already exist.


---

Comment by was created at 2009-10-05 15:52:51

I don't consider this ticket invalid. The fact that Sage totally hangs without an error is bad.  Independent of implementing #1221 and #2787, we could easily and quickly improve the type checking of the input to integrate.


---

Comment by kcrisman created at 2009-10-05 15:55:41

Good point.


---

Comment by kcrisman created at 2009-10-05 16:19:30

I am fixing the error, but not actually adding documentation (other than in testing) that this works, because I view that as the proper place of the afore-mentioned tickets, which still need to resolve how backwards-incompatibility will be dealt with and probably have much better ways of dealing with it than my hackish solution.  I'm also not accepting lists, just tuples, which I think is reasonable given the syntax of all the other calculus functions.


---

Comment by was created at 2009-10-05 16:28:56

I read it and it looks good. If it passes tests I would give it a positive review....  I don't have time right now.


---

Comment by kcrisman created at 2009-10-20 06:23:09

Based on 4.2.alpha0


---

Attachment

Rebased, otherwise should be fine.


---

Comment by kcrisman created at 2009-10-28 01:13:05

Now that #7327 has been opened, one of these two is a duplicate.


---

Comment by jason created at 2009-10-28 01:28:40

Hmm...that code looks pretty long.  Why not just:


```
if 1<=len(v)<=3:
    return integral(expression,*v)
```


and take care of all three cases in one swoop?

Also, it completely ignores the rest of the parameters in the function call, like algorithm, etc.


---

Comment by jason created at 2009-10-28 01:28:40

Changing status from needs_review to needs_work.


---

Comment by kcrisman created at 2009-11-05 17:45:26

To release manager: please close this as a duplicate of #7327, where a patch including the doctests for the specific bug above resides.


---

Comment by mhansen created at 2009-11-06 05:53:32

Resolution: duplicate


---

Comment by kcrisman created at 2009-12-22 16:30:25

Just an update - it turns out the original integral reported here is not, in fact, convergent - it is an odd function, so the limit of the indefinite integral evaluated at N and -N is 0, though.  Fixing this doctest so something mathematically correct happens will be done in #7745, since Maxima 5.20.1 simply returns that integral now, as opposed to giving 0.

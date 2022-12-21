# Issue 5338: Sage 3.2.2: speed regression/infite loop for "K.<b> = QQ[a]"

Issue created by migration from Trac.

Original creator: mabshoff

Original creation time: 2009-02-22 18:50:31

Assignee: tbd

CC:  robertwb

The code below works instantly in Sage 3.2.1, but starting with Sage 3.2.2 it doesn't even finish the last command in 30 minutes CPU time:

```
----------------------------------------------------------------------
----------------------------------------------------------------------
sage:     sage: x = var('x')
sage:     sage: eqn =  x^3 + sqrt(2)*x + 5 == 0
sage:     sage: a = solve(eqn, x)[0].rhs()
sage:     sage: K.<b> = QQ[a]
```

Carl Witty suggests:

```
[10:23am] mabs: So far it has eaten *4 minutes* of CPU time.
[10:23am] cwitty: It looks like somebody changed the embedding 
system to use QQbar instead of wstein's algdep-of-numerical-value.
```

This is likely related to the new embedding code in Sage 3.2.2, so I am CCing RobertWB.
| Sage Version 3.2.2, Release Date: 2008-12-18                       |
| Type notebook() for the GUI, and license() for information.        |
Cheers,

Michael


---

Comment by robertwb created at 2009-02-23 20:27:12

You can still access my old (numeric) minpoly code via


```
sage: x = var('x')
sage: eqn =  x^3 + sqrt(2)*x + 5 == 0
sage: a = solve(eqn, x)[0].rhs()
sage: a.minpoly(algorithm='numeric')
x^6 + 10*x^3 - 2*x^2 + 25
```


However, for many cases this is much slower or fails completely.


---

Comment by robertwb created at 2009-02-23 21:06:47

Hmm, this is insanely slow (i.e. never finishes for me)


```
sage: b = (sqrt(sqrt(2) + 1)/(sqrt(3)) - 1)^(1/3)
sage: time QQbar(b).minpoly()
```



---

Comment by mabshoff created at 2009-02-24 19:31:32

Note that for now the doctest has been disabled to get the doctests to pass.

Cheers,

Michael


---

Comment by AlexGhitza created at 2009-06-02 08:05:50

Replying to [comment:2 robertwb]:
> Hmm, this is insanely slow (i.e. never finishes for me)
> 
> {{{
> sage: b = (sqrt(sqrt(2) + 1)/(sqrt(3)) - 1)^(1/3)
> sage: time QQbar(b).minpoly()
> }}}

The problem seems to be here:


```
sage: b = (sqrt(sqrt(2) + 1)/(sqrt(3)) - 1)^(1/3)
sage: c = QQbar(b)
sage: od = c._descr
sage: od.exactify()    # doesn't seem to finish
```



---

Comment by cremona created at 2009-09-06 21:10:18

Replying to [comment:5 AlexGhitza]:
> Replying to [comment:2 robertwb]:
> > Hmm, this is insanely slow (i.e. never finishes for me)
> > 
> > {{{
> > sage: b = (sqrt(sqrt(2) + 1)/(sqrt(3)) - 1)^(1/3)
> > sage: time QQbar(b).minpoly()
> > }}}
> 
> The problem seems to be here:
> 
> {{{
> sage: b = (sqrt(sqrt(2) + 1)/(sqrt(3)) - 1)^(1/3)
> sage: c = QQbar(b)
> sage: od = c._descr
> sage: od.exactify()    # doesn't seem to finish
> }}}

As far as I can see, the latter is getting into an infinite loop.  If that is right, it's real bug and not just a new inefficiency.


---

Comment by AlexGhitza created at 2009-11-10 20:59:58

It seems that `exactify` is not the culprit, it's just a bit slow:


```
----------------------------------------------------------------------
----------------------------------------------------------------------
sage: b = (sqrt(sqrt(2) + 1)/(sqrt(3)) - 1)^(1/3)
sage: c = QQbar(b)
sage: od = c._descr
sage: time od.exactify()
CPU times: user 102.89 s, sys: 0.17 s, total: 103.06 s
Wall time: 117.04 s
-13576/8180757*a^23 + 833411/13634595*a^20 - 6092092/13634595*a^17 + 2402147/4544865*a^14 + 16778234/4544865*a^11 - 5085581/504985*a^8 + 2414627/302991*a^5 - 1318781/504985*a^2 where a^24 - 36*a^21 + 240*a^18 - 144*a^15 - 2214*a^12 + 4320*a^9 - 2484*a^6 + 648*a^3 - 162 = 0 and a in -0.4328720060607604? + 0.7497563076715000?*I
```



---

Comment by was created at 2009-11-19 21:15:40

Changing status from new to needs_review.


---

Comment by was created at 2009-11-19 21:15:40

I've attached a patch that reverses the order: it first tries the numerical algorithm, and if that fails, it then tries the algebraic algorithm.  This makes vastly more sense to me, since the numerical algorithm -- if it will fail -- is likely to fail in a reasonable amount of time, but the algebraic algorithm can succeed and take a huge amount of time.


---

Comment by robertwb created at 2009-11-20 02:53:16


```
sage: b = sin(pi/5)
sage: time sage.calculus.calculus.minpoly(b, algorithm='algebraic')
CPU times: user 0.05 s, sys: 0.00 s, total: 0.05 s
Wall time: 0.05 s
x^4 - 5/4*x^2 + 5/16
sage: time sage.calculus.calculus.minpoly(b)
Traceback (most recent call last):
...
NotImplementedError: Could not prove minimal polynomial x^4 - 5/4*x^2 + 5/16 (epsilon 0.00000000000000e-1)
```


We need to wrap raising this error to not be raised if the algorithm is numeric... 

I remember doing it in this order because there were cases where the numeric algorithm was way slower, but at least the numeric one finishes in constant bounded time. 

I really feel there should be a quicker way of computing compositums than using QQbar.


---

Comment by robertwb created at 2009-11-20 02:53:16

Changing status from needs_review to needs_work.


---

Comment by robertwb created at 2009-12-02 04:02:32

Changing status from needs_work to needs_review.


---

Attachment


---

Comment by robertwb created at 2009-12-02 04:02:39

Changing status from needs_review to positive_review.


---

Comment by mhansen created at 2009-12-02 08:44:27

Resolution: fixed

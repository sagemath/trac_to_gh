# Issue 8857: lcm over QQ[x] broken

Issue created by migration from https://trac.sagemath.org/ticket/8857

Original creator: burcin

Original creation time: 2010-05-03 14:40:18

Assignee: AlexGhitza

CC:  mjo

Reported by Manuel Kauers:


```
sage: R.<x> = QQ[x]
sage: R(1/2).lcm(R(1))
<boom>
sage: R(2^31).lcm(R(1))
<boom>
```


The backtrace indicates that we call Singular for this, which is completely unnecessary.

We should check if this persists with #4000 as well.


---

Comment by mjo created at 2012-01-09 02:27:04

We're halfway there:


```
sage: R.<x> = QQ[x]
sage: R(1/2).lcm(R(1))
1
sage: R(2^31).lcm(R(1))
1
```


but the second result is clearly wrong.


---

Comment by mmezzarobba created at 2013-12-12 14:07:34

Replying to [comment:1 mjo]:
> but the second result is clearly wrong.

Sorry if this is a stupid question, but why is it wrong? what result would you expect?


---

Comment by mjo created at 2013-12-12 14:31:46

Replying to [comment:3 mmezzarobba]:
> 
> Sorry if this is a stupid question, but why is it wrong?

It isn't, after I read the documentation *facepalm*. Sorry.


---

Comment by mmezzarobba created at 2013-12-12 14:41:47

Changing status from new to needs_review.


---

Comment by mjo created at 2013-12-12 14:55:15

This should get a doctest, since it is a bug that was fixed, albeit not in this ticket.


---

Comment by mmezzarobba created at 2013-12-12 17:07:22

Replying to [comment:6 mjo]:
> This should get a doctest, since it is a bug that was fixed, albeit not in this ticket.

You are right.


---

Comment by mmezzarobba created at 2013-12-12 17:10:12

New commits:


---

Comment by tscrim created at 2013-12-12 17:10:30

I think that this is very counter-intuitive behavior and is inconsistent. Compare:

```
sage: R.<x> = ZZ['x']
sage: R(2^31).lcm(2*x + 1)
4294967296*x + 2147483648
sage: R(2^31).lcm(1)
2147483648

sage: QQ(2^31).lcm(QQ(1))
2147483648

sage: R.<x,y> = QQ['x,y']
sage: R(2^31).lcm(2*x + 1)
4294967296*x + 2147483648
sage: R(2^31).lcm(1)
2147483648
```

with

```
sage: R.<x> = QQ['x']
sage: R(2^31).lcm(2*x + 1)
x + 1/2
```


However, I do think that this should have a doctest nevertheless.


---

Comment by tscrim created at 2013-12-12 17:10:30

Changing status from needs_review to needs_work.


---

Comment by tscrim created at 2013-12-12 17:11:06

Ack, I deleted the branch due to race conditions.
----
New commits:


---

Comment by mmezzarobba created at 2014-01-27 12:48:39

Replying to [comment:9 tscrim]:
> I think that this is very counter-intuitive behavior and is inconsistent.

What part do you find counter-intuitive? That `p.lcm(q)`� for `p, q ∈ QQ[x]` returns the monic lcm of `p` and `q` is clearly what I would expect, even though it might make sense to ask that `gcd·lcm = p·q`. However, I do find the definition of `gcd` and `lcm` over `QQ` counter-intuitive.


---

Comment by tscrim created at 2014-01-27 15:52:45

It's just not what my naive/non-number-theorist self expects, but I can see why `lcm` would be counter-intuitive. However you do agree that this behavior is inconsistent? Also, a similar problem with using `RR` (and other like fields) as in the this ticket:

```
sage: R.<x,y> = RR[]
sage: R(2^31).lcm(R(2*x+1)) # Boom
```

and `R.<x,y> = FractionField(QQ['t'])[]`. So should we use this ticket as one to fix this as well since it essentially is the same bug?


---

Comment by mmezzarobba created at 2014-01-27 16:36:11

Replying to [comment:12 tscrim]:
> However you do agree that this behavior is inconsistent?

From a user interface point of view, yes, I do. From a mathematical (or programming) point of view I am not sure.

> Also, a similar problem with using `RR` (and other like fields) as in the this ticket:
> {{{
> sage: R.<x,y> = RR[]
> sage: R(2^31).lcm(R(2*x+1)) # Boom
> }}}
> and `R.<x,y> = FractionField(QQ['t'])[]`. So should we use this ticket as one to fix this as well since it essentially is the same bug?

Yes, why not.

# Issue 8166: Expose max_weight_matching from NetworkX

Issue created by migration from Trac.

Original creator: ncohen

Original creation time: 2010-02-03 08:45:32

Assignee: rlm

CC:  ylchapuy jason mvngu

Since the new version of NetworkX is being merged into Sage, we could use their max matching algorithm. We already have one, though it uses Linear Programming and is optional :

The efficiency of these two algorithms have to be compared !

Based upon this, the default behaviour could be :
    * To always use NetworkX
    * Only use it if there is no LP available
    * Not to use it if not asked explicitely

Nathann


---

Comment by jason created at 2010-03-17 05:27:31

Changing type from defect to enhancement.


---

Comment by ncohen created at 2010-05-15 19:03:56

Changing status from new to needs_review.


---

Comment by ncohen created at 2010-05-15 19:03:56

As max_weight_matching had been exposed while I wasn't looking, this ticket now merges the two function into only one, for the better I hope ! :-)

From now on, maximum matching are not optional anymore, and are way faster !


```
sage: g = graphs.RandomGNP(50,.3)
sage: %timeit g.matching(algorithm="LP",solver="GLPK")
5 loops, best of 3: 248 ms per loop
sage: %timeit g.matching()
25 loops, best of 3: 16.9 ms per loop
```


The two different ways to solve matchings are kept, just in case.... But network'x version is now the default one, obviously :-)

Requires #8364

Nathann


---

Attachment

I have attached a rebase of ncohen's patch, rebased on top of #8364. Based upon that, I did some clean-ups of the changes proposed by ncohen. My changes are mainly cosmetic clean-ups along the lines of PEP 008. Both ncohen's patch and my changes are folded into one patch to make it easier for anyone to give a final review.


---

Comment by ncohen created at 2010-05-21 17:50:25

Oh, but then it means I can not review it myself ? :-)

Nathann


---

Comment by mvngu created at 2010-05-21 18:15:14

[reviewer.diff](http://trac.sagemath.org/sage_trac/attachment/ticket/8166/reviewer.diff) contains the changes I folded into ncohen's patch. This should make it easier to review [trac_8166-rebase.patch](http://trac.sagemath.org/sage_trac/attachment/ticket/8166/trac_8166-rebase.patch).


---

Attachment


---

Attachment

diff patch showing changes proposed by reviewer


---

Comment by ncohen created at 2010-05-21 18:49:56

Nice, perfect, no error anywhere and many spelling/syntax mistakes fixed... Thank you again Minh ! :-)

Nathann


---

Comment by ncohen created at 2010-05-21 18:49:56

Changing status from needs_review to positive_review.


---

Comment by mhansen created at 2010-06-06 00:41:55

Resolution: fixed

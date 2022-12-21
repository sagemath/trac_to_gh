# Issue 6959: modular forms -- add aplist and anlist for newforms

Issue created by migration from Trac.

Original creator: was

Original creation time: 2009-09-19 05:01:49

Assignee: craigcitro




---

Attachment


---

Comment by cremona created at 2009-10-29 21:19:53

Changing status from needs_review to needs_work.


---

Comment by cremona created at 2009-10-29 21:19:53

Looks mainly good to me -- patch applies and tests (in sage/modular/modform) pass.  One glitch:

```
        if not all_embeddings: 
 	            return A 
 	return A 
```

looks like a typo.

It does not seem very efficient to factor all the n in the range, and that is not the way I have always done this.  The result is pretty slow -- for example, if you wanted to compute all a_n for n<10^6, this is not good enough:

```
sage: f = CuspForms(11,2).newforms()[0]; f
q - 2*q^2 - q^3 + 2*q^4 + q^5 + O(q^6)
sage: time an = f.anlist(1000)
CPU times: user 0.40 s, sys: 0.00 s, total: 0.40 s
Wall time: 0.40 s
sage: time an = f.anlist(10000)
CPU times: user 13.84 s, sys: 0.79 s, total: 14.63 s
Wall time: 14.65 s
sage: time an = f.anlist(100000)
#(gave up waiting after a few minutes)
```

On second thoughts it is probably computing the a_p which is slow here.  But are they even cached?

```
sage: time an = f.aplist(10000)
CPU times: user 11.09 s, sys: 0.65 s, total: 11.74 s
Wall time: 11.81 s
sage: time an = f.anlist(10000)
CPU times: user 13.71 s, sys: 0.69 s, total: 14.40 s
Wall time: 14.53 s
```

-- it seems not.


---

Comment by chapoton created at 2013-09-01 12:13:50

Changing keywords from "" to "newform".


---

Comment by chapoton created at 2013-09-01 12:13:50

there are three failing doctest (sage 5.12.beta4)


---

Comment by chapoton created at 2014-06-19 20:23:18

New commits:


---

Comment by chapoton created at 2014-06-19 20:25:50

The 3 failing doctests looks to me like a problem with galois ambiguity (i.e. an algebraic number a1 is replaced by its conjugate -a1). Maybe one can just replace them by the results ?


---

Comment by git created at 2016-03-01 11:14:32

Branch pushed to git repo; I updated commit sha1. New commits:


---

Comment by git created at 2017-06-08 19:42:21

Branch pushed to git repo; I updated commit sha1. New commits:


---

Comment by git created at 2018-03-11 19:57:31

Branch pushed to git repo; I updated commit sha1. New commits:

# Issue 6265: fix toy_d_basis.py

Issue created by migration from Trac.

Original creator: ncalexan

Original creation time: 2009-06-12 08:01:59

Assignee: malb

CC:  malb tscrim kedlaya simonking

As discussed at #6051.  Line 91 of sage/rings/polynomial/toy_d_basis.py needs to be unrandomed when this is fixed.


```
However, when we compute the Groebner basis of I (defined over `\ZZ`), we note that there is a certain integer in the ideal which is not 1.::

    sage: d_basis(I) # random -- waiting on upstream singular fixes at #6051
    [x + 170269749119, y + 2149906854, z + ..., 282687803443]                                
```



---

Comment by chapoton created at 2017-03-30 20:29:44

New commits:


---

Comment by chapoton created at 2017-03-30 20:29:44

Changing status from new to needs_review.


---

Comment by chapoton created at 2017-03-30 20:31:20

Changing status from needs_review to needs_work.


---

Comment by git created at 2017-03-30 20:40:40

Branch pushed to git repo; I updated commit sha1. New commits:


---

Comment by chapoton created at 2017-03-30 20:41:55

Changing status from needs_work to needs_review.


---

Comment by tscrim created at 2017-03-30 22:41:11

It doesn't seem like the problem is fixed if you have to use `...` in the doctest. So I'm not sure we should remove the comment, but I haven't looked to deep into this.


---

Comment by chapoton created at 2017-03-31 06:56:53

Changing status from needs_review to needs_info.


---

Comment by chapoton created at 2017-03-31 06:56:53

Indeed, I also have some doubts. Let us check "needs_info"

The `...` are there to replace *huge* numbers. Maybe we should keep the top few digits ?


---

Comment by git created at 2017-04-01 16:45:57

Branch pushed to git repo; I updated commit sha1. New commits:


---

Comment by chapoton created at 2017-04-01 19:31:41

Here is another try, with green bot. I changed the term order so that the Groebner basis has much smaller coefficients. Maybe this should be tested on diverse machines.


---

Comment by chapoton created at 2017-04-01 19:31:50

Changing status from needs_info to needs_review.


---

Comment by chapoton created at 2017-04-04 19:13:50

maybe this is good enough, I don't know..


---

Comment by tscrim created at 2017-04-04 19:23:51

Hmm...I'm now not so sure what the point of the doctest is. From the description above it looks more like the minimal integer that is in the ideal is the important point rather than the integers that are part of the binomial generators. I'm cc-ing Simon to see if he has a thought on this. Yet, this was last touched in 2009, so maybe we can just `...` the binomial term integers and be done with it.


---

Comment by SimonKing created at 2017-04-04 19:43:31

Replying to [comment:15 tscrim]:
> Hmm...I'm now not so sure what the point of the doctest is. From the description above it looks more like the minimal integer that is in the ideal is the important point rather than the integers that are part of the binomial generators. I'm cc-ing Simon to see if he has a thought on this.

I don't know anything about the theory of d-Gröbner bases. However, from the explanation in the doctest, it seems to me that the integers in the binomial generators do not matter (at least not for the test). It seems to me that the point of the example is to show that
- there is an integer in the d_basis, and
- the prime factors of that integer have the property that the original system has solutions modulo that prime.


---

Comment by tscrim created at 2017-04-05 16:33:17

Thanks Simon.

So shall we revert back to 716ac65?


---

Comment by chapoton created at 2017-04-05 18:29:48

IMHO, the current branch should be just as good. I would rather try to let this in and see if the buildbots of Volker report any failure on apples and oranges.


---

Comment by tscrim created at 2017-04-05 21:31:24

Okay, then if you break the long line into each of the generators, you can set a positive review on my behalf.


---

Comment by git created at 2017-04-06 06:19:32

Branch pushed to git repo; I updated commit sha1. New commits:


---

Comment by chapoton created at 2017-04-06 06:20:20

ok, done. Thanks. Setting to positive


---

Comment by chapoton created at 2017-04-06 06:20:20

Changing status from needs_review to positive_review.


---

Comment by vbraun created at 2017-04-07 22:24:09

Resolution: fixed

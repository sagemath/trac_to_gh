# Issue 8238: heegner_index_bound may be incorrect for curves with rational torsion

Issue created by migration from https://trac.sagemath.org/ticket/8238

Original creator: rlm

Original creation time: 2010-02-11 19:10:09

Assignee: cremona

CC:  was

Result of a recent conversation with William Stein.


---

Comment by rlm created at 2010-02-12 09:14:59

I need to fix this to use `two_torsion_rank` instead of `torsion_order`... tomorrow!


---

Comment by rlm created at 2010-02-14 20:29:45

Changing status from new to needs_review.


---

Comment by wuthrich created at 2010-02-15 12:50:18

I wouldn't mind reviewing this, but I am probably not the right person to do so, since I don't really understand what it changes. Would it be good to have a test example included to illustrate the change.

Also in 4.3.3.alpha0 I get a test error in heegner.py, which wuld make my review useless.Sorry.


---

Comment by was created at 2010-04-19 06:38:13

Changing status from needs_review to needs_work.


---

Comment by was created at 2010-04-19 06:38:13

Robert,

I think the point of this patch is to change the function so it is no longer off by factors of 2 by default. 
Note that the documentation, even after applying your patch, says:

```
    r"""
    Return an interval that contains the index of the Heegner
    point `y_K` in the group of `K`-rational points modulo torsion
    on this elliptic curve, computed using the Gross-Zagier
    formula and/or a point search, or the index divided by `2`.

    .. note::

       If ``min_p`` is bigger than 2 then the index can be off by
       any prime less than ``min_p``. This function returns the
       index divided by `2` exactly when the rank of `E(K)` is
       greater than 1 and `E(\QQ)_{/tor} \oplus E^D(\QQ)_{/tor}`
       has index `2` in `E(K)_{/tor}`, where the second factor
       undergoes a twist.
```


If you've really fixed the "factor of 2" issue, as it seems you have, then the documentation should be changed to reflect this.  Moreover, this is an enhancement, rather than a bug fix.


---

Comment by rlm created at 2010-04-19 14:07:42

I was able to fix the output for rank 0 and 1 curves, but not in general. Note it says
"This function returns the index divided by `2` exactly when the rank of `E(K)` is greater than 1 and ..."


---

Comment by rlm created at 2010-04-19 14:07:42

Changing type from defect to enhancement.


---

Comment by rlm created at 2010-05-25 23:24:16

Ping! This ticket still needs a review...


---

Comment by rlm created at 2010-05-25 23:24:16

Changing status from needs_work to needs_review.


---

Comment by cremona created at 2010-06-05 15:06:48

I applied the patch to 4.4.3 and it worked fine (patch applies cleanly, all long tests in heegner.py pass, 

Some minor quibbles:
   1. on line 6365:  instead of "an interval that contains the index, or the index over 2" say "... or half the index".
   2. line 6454++:  this code is reached whe then rank is 0 (or it appears to be) but then F.gens()[0] would fail.  If it is the case that the rank would never be 0 here. I would prefer a comment to that effect and change the test to if F.rank() == 1.  (I assume that in this context calling F.rank() and F.gens() is not expensive?)
   3. After setting a=2 in line 6460 the loop should break.  (OK, so there will not be that many torsion points o nEK, but still.)  Even better would be to first compute EK.torsion_points() and only run the loop at all if it has even length?  (But still test if z itself can be divided by 2).  I'm sure I once wrote a function which returned a list of points generating torsion modulo 2*torsion....if you did

```
sage: for T in EK.torsion_subgroup().gens():
....:     if T.order()%2==0:
```

you would have at most 2 points to check.

I'll give this a positive review once these have been fixed.


---

Comment by cremona created at 2010-06-05 15:06:48

Changing status from needs_review to needs_work.


---

Comment by rlm created at 2010-06-05 15:56:41

Changing status from needs_work to needs_review.


---

Comment by rlm created at 2010-06-05 15:56:41

I think I've addressed each of the above concerns. Thank you for the review!


---

Comment by cremona created at 2010-06-05 21:41:46

Great -- positive review now.


---

Comment by cremona created at 2010-06-05 21:41:46

Changing status from needs_review to positive_review.


---

Comment by cremona created at 2010-06-05 21:45:53

very sorry, my mistake -- if there are 2 torsion gens of even order you still needs to also trying adding their sum (i.e. if T/2T has order 4 there should be 4 tests).


---

Comment by cremona created at 2010-06-05 21:45:53

Changing status from positive_review to needs_work.


---

Attachment


---

Comment by rlm created at 2010-06-05 22:08:54

Changing status from needs_work to needs_review.


---

Comment by cremona created at 2010-06-06 10:27:32

OK!


---

Comment by cremona created at 2010-06-06 10:27:32

Changing status from needs_review to positive_review.


---

Comment by mhansen created at 2010-06-07 05:24:25

Resolution: fixed

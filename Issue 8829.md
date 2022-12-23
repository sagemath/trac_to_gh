# Issue 8829: Saturation for curves over number fields.

Issue created by migration from https://trac.sagemath.org/ticket/8829

Original creator: robertwb

Original creation time: 2010-04-30 06:49:16

Assignee: cremona

CC:  pbruin kedlaya

I also implemented the simple case of E.gens() for E(K) when E/Q and [K:Q] = 2.


---

Comment by robertwb created at 2010-04-30 06:50:28

Some dependance on #8828.


---

Comment by robertwb created at 2010-04-30 06:50:28

Changing status from new to needs_review.


---

Comment by cremona created at 2010-04-30 08:29:35

I have had a quick look and will go through this in more detail later (after #8828 is completed, probably).  I spent a long time on my C++ implementation of this (over QQ but the algorithm is general) so am quite familiar with the details.

Here are two references you should give:  [1] S. Siksek "Infinite descent on elliptic curves", Rocky Mountain J of M, Vol 25 No. 4 (1995), 1501-1538.  [2] M. Prickett, "Saturation of Mordell-Weil groups of elliptic curves over number fields", U of Nottingham PhD thesis (2004), http://etheses.nottingham.ac.uk/52/.

Martin Prickett implemented this in Magma, but the code was very slow and hard to read so it never got incorporated into Magma releases.

Incidentally, it was for this that I implemented group structure for curves over GF(q) in the first place!  In my C++ implementation I cache a lot of the information of this group structure so that when you do p-saturation for larger and larger p, the structures are already there.  A good example is to take one of those curves of very high rank:  I think I once successfully p-saturated the rank 24 curve at all p < `10^6`  (the bound was totally out of reach, something like `10^100`).

Another point which might be useful over number fields:  it suffices to use degree one primes to reduce modulo.


---

Attachment


---

Comment by robertwb created at 2010-04-30 08:46:39

Replying to [comment:2 cremona]:
> I have had a quick look and will go through this in more detail later (after #8828 is completed, probably).  I spent a long time on my C++ implementation of this (over QQ but the algorithm is general) so am quite familiar with the details.
> 
> Here are two references you should give:  [1] S. Siksek "Infinite descent on elliptic curves", Rocky Mountain J of M, Vol 25 No. 4 (1995), 1501-1538.  [2] M. Prickett, "Saturation of Mordell-Weil groups of elliptic curves over number fields", U of Nottingham PhD thesis (2004), http://etheses.nottingham.ac.uk/52/.

Ah, those look like good references to read too :). 

> Martin Prickett implemented this in Magma, but the code was very slow and hard to read so it never got incorporated into Magma releases.
> 
> Incidentally, it was for this that I implemented group structure for curves over GF(q) in the first place!  In my C++ implementation I cache a lot of the information of this group structure so that when you do p-saturation for larger and larger p, the structures are already there.  

The way I do it is consider many p at once, and for each curve over GF(q) I see which primes in my set it could help with, though this won't scale as far. I'm sure there's still lots of room for improvement. 

> A good example is to take one of those curves of very high rank:  I think I once successfully p-saturated the rank 24 curve at all p < `10^6`  (the bound was totally out of reach, something like `10^100`).

That reminds me--I was wondering if there's any way to go from min(h(P)) to a bound on the regulator for rank > 1. 

> Another point which might be useful over number fields:  it suffices to use degree one primes to reduce modulo.

Good point. Those get pretty rare for large degree number fields though, right?


---

Comment by cremona created at 2010-04-30 11:41:49

You might also like to look at my C++ code which is in eclib, in src/qcurves.  I can point to the right files if it is not clear.  In case you wonder, "TLSS" stands for "Tate-Lichtenbaum-Samir_Siksek" since I use the TL map when the p-torsion in E(GF(q)) is not cyclic and Samir's original method when it is.  Samir only used reduction modulo primes where p exactly divided the order, and in particular for which the reduction had cyclic p-part.  But Martin and I discovered that this can fail when there is a p-isogeny.  Here, fail means in the sense that there can exist points which are not multiples of p in E(QQ) but which map to zero in E(GF(q))/p for all q.

In MP's thesis he proves that this cannot happen if you use all q, or all but a finite number, or all but a finite number of degree 1 primes, .... some of these  results we then found had been proved elsewhere (3 or 4 times, independently, within 3 or 4 years!).  But it can happen if you leave out the q for which the quotient has non-cyclic p-part.


---

Comment by cremona created at 2010-05-09 17:49:06

Changing status from needs_review to needs_work.


---

Comment by cremona created at 2010-05-09 17:49:06

Patch applies fine to 4.4.1 and tests pass.

This functionality is badly needed!

We now have heights for points on curves defined over number_fields
but no associated regulator function.  I suggest that the function
regulator_of_points() be moved up from ell_rational_field to
ell_number_field.  This tcan then be called instead of the code in
lines 424-432 [line numbers are from the patched file, not the patch].

Line 439 uses a function self.height_function() which does not exist.
This block needs to be replaced by something sensible.  If one has a lower bound on the height of non-torsion
points, then a bound on the index can be deduced from standard
geometry of numbers estimates.   To get such a lower bound, see papers
of Cremona & Siksek (over Q) and Thongjunthug (over number fields) for
an algorithm which would need to be implemented.  (Not hard over Q,
not much harder for totally real fields, quite a lot worse over fields
with a complex embedding).  Until this is done, I don't think this
saturation function can allow maxprime==0.

In the rank one code:   when large primes p (say, over 20!) are being
tested then the division_points code will be expensive since it
involves constructing the multiplication-by-p map.  I would recommend
using a reduction strategy here just as in the general case.  To check
p-saturation just find primes q such that #E(Fq) is divisible by p and
then see if the reduction of P mod q is a multiple of p.  This will
almost always prove saturation very quickly.  If it fails for several
(say 5) q then try to divide P by p;  else use more q, and so on.
There is one theoretical drawback here:  this strategy might fail if
there is a rational p-isogeny.  Over Q,  we know which p this might
happen for and I would first test for the existence of isogenies of
primes degree, and use the division test (as here) for any primes that
show up.  Over number fields that's harder to deal with, but again we
can fall back on the division test to rpove that P cannot be divided
by p.

The function list_of_multiples(P,n) duplicated the generic function
multiples() which I wrote for just this sort of purpose!

I don't like the loop through all linear combinations for small
primes.  Even with p=2 there are curves with 24 independent points out
there and `2^24` divisions is not nice to contemplate.  If you want this
short cut, do it based on the size of `p^r`.

The main code with reduction etc looks fine to me (but I did not check
the logic rigorously).

The gens function for E(K) when E is defined over Q and [K:Q]=2 looks
fine.  For a more general case we could always try using
simon_two_descent (followed by saturation).  Trying such an examples
led me to:

```
sage: K.<a> = NumberField(x^2-2)
sage: E = EllipticCurve([a,0])
sage: P = E(0,0)
sage: P.has_finite_order()
True
sage: P.order()
2
sage: P.height()
0
sage: E.saturation([P], verbose=True, max_prime=5)
## infinite loop
```

This is caused as follows:   The height matrix is [0] with det=0 but
reg / min(heights) is NaN so reg / min(heights) < 1e-6 is False!.
This will need fixing.  At the very least, I would discard any points
of finite order before doing anything else with them.  Then
min(heights) will never be 0.

Most of the above is easy to deal with.  The hard part is computing a
suitable max_prime form a lower height bound on points.  I suggest
that for now you make it compulsory to have a positive max_prime and
add a TODO.


---

Comment by robertwb created at 2010-05-11 18:17:49

Thank you for all your input. `self.height_function` comes from #8828, though as you suggest we could make max_prime mandatory for now (and for rank > 1 once that goes in). That's a good point about large primes in the rank one case. I found the loop through all linear combinations to be much faster in practice for small primes, but the hard coded `p == 2` case was left by accident, I meant to cap that on `p^r` as I did the others. 

I probably won't fix and polish this up before finishing my thesis, but at the latest we should be able to get it done during the workshop at MSRI next month.


---

Comment by cremona created at 2010-05-11 20:48:47

Replying to [comment:6 robertwb]:
> Thank you for all your input. `self.height_function` comes from #8828, though as you suggest we could make max_prime mandatory for now (and for rank > 1 once that goes in). That's a good point about large primes in the rank one case. I found the loop through all linear combinations to be much faster in practice for small primes, but the hard coded `p == 2` case was left by accident, I meant to cap that on `p^r` as I did the others. 
> 
> I probably won't fix and polish this up before finishing my thesis, but at the latest we should be able to get it done during the workshop at MSRI next month. 

OK -- looking forward to it!  I'll take a look at #8828 by then as well.


---

Comment by cremona created at 2010-06-29 04:54:59

Since rwb is now busy at Google, and I want this functionality, I am now implementing the changes I suggested above!


---

Comment by cremona created at 2010-06-29 04:59:02

I made a separate ticket for the regulator functions.  See #9372.


---

Comment by roed created at 2012-10-15 09:36:35

How is this going John?  It seems to have been awhile....


---

Comment by cremona created at 2013-01-08 09:28:53

See #12509: until we can fix the height computation, saturation cannot be carried out properly.  It's still on my to-do list though.


---

Comment by cremona created at 2013-01-10 09:30:38

Replying to [comment:11 cremona]:
> See #12509: until we can fix the height computation, saturation cannot be carried out properly.  It's still on my to-do list though.

#12509 is now up for review.


---

Comment by cremona created at 2015-08-13 16:05:47

I do not know why this was left drifting, but I really need it myself now so will look at it again, rebase on 6.8 and see what we can do.  But I only have one day before a week off, so...


---

Comment by cremona created at 2015-09-11 16:16:06

Changing keywords from "" to "saturation".


---

Comment by cremona created at 2015-09-11 16:16:06

New commits:


---

Comment by cremona created at 2015-09-11 16:18:50

Current branch works but more doctests and testing are needed; so not ready for review yet.

I did a lot of rewriting of the main saturation routine, separating off p-saturation and also allowing saturation to be done at just one prime.  This is a useful special case, since if you take the images of some saturated points under a p-isogeny the images may not be p-saturated but will still be saturated at all other primes.

The code for computing E(K) when K is quadratic and E is a base change has been completely rewritten and will now work in many more cases (not just when the coefficients of E are in Q).


---

Comment by git created at 2015-09-14 16:09:59

Branch pushed to git repo; I updated commit sha1. New commits:


---

Comment by cremona created at 2015-09-14 16:16:53

The latest commit involves more than adding more doctests to the new functions, since bugs were revealed which led to a rewrite of the sieving code for the two cases where the p-rank of the reduction is 1 or 2; the former uses discrete log in the reduction, the latter uses Weil pairing and discrte log in the multiplicative group.  In the sieve I restrict to primes of degree 1.  It is a Theorem (see http://eprints.nottingham.ac.uk/10052/) that this will suffice to prove p-saturation, provided that one does use reductions with p-rank 2 and not just those of p-rank 1 as originally suggested by Siksek in https://ore.exeter.ac.uk/repository/handle/10871/8323 .

I will mark this as ready for review so the bots get to work on it, and of course humans are welcome to look at the new code, but I will now test it thoroughly on the LMFDB curves and report back.


---

Comment by cremona created at 2015-09-14 16:17:16

Changing status from needs_work to needs_review.


---

Comment by chapoton created at 2015-09-14 17:52:14

Hello,

1) indent correctly the INPUT and OUTPUT fields:

```
INPUT:

- first thing
  goes one there (note the shift of 2 characters)
```


2) use the new syntax for raise:

```
raise MyError("is rich")
```


Point 1 may be the source of the doc build failure found by the bot:

OSError: [plane_cur] /home/patchbot/sage-patchbot/local/lib/python2.7/site-packages/sage/schemes/elliptic_curves/ell_number_field.py:docstring of sage.schemes.elliptic_curves.ell_number_field.EllipticCurve_number_field.saturation:9: WARNING: Bullet list ends without a blank line; unexpected unindent.


---

Comment by cremona created at 2015-09-14 18:34:30

Replying to [comment:26 chapoton]:
> Hello,
> 
> 1) indent correctly the INPUT and OUTPUT fields:
> {{{
> INPUT:
> 
> - first thing
>   goes one there (note the shift of 2 characters)
> }}}
> 
> 2) use the new syntax for raise:
> {{{
> raise MyError("is rich")
> }}}
> 
> Point 1 may be the source of the doc build failure found by the bot:
> 
> OSError: [plane_cur] /home/patchbot/sage-patchbot/local/lib/python2.7/site-packages/sage/schemes/elliptic_curves/ell_number_field.py:docstring of sage.schemes.elliptic_curves.ell_number_field.EllipticCurve_number_field.saturation:9: WARNING: Bullet list ends without a blank line; unexpected unindent.

Thanks, I will fix those.


---

Comment by git created at 2015-09-14 19:01:14

Branch pushed to git repo; I updated commit sha1. New commits:


---

Comment by chapoton created at 2015-09-15 09:57:24

Changing status from needs_review to needs_work.


---

Comment by chapoton created at 2015-09-15 09:57:24

many failing doctests, see bot report


---

Comment by cremona created at 2015-09-15 10:33:37

Apologies, it was a mistake to set this to needs_review prematurely.  Next time I do, I will mean it.


---

Comment by git created at 2015-09-15 11:09:14

Branch pushed to git repo; I updated commit sha1. New commits:


---

Comment by cremona created at 2015-09-16 11:38:42

Progress report:  I am currently running the p-saturation (for single primes) on lots of LMFDB curves and all is well so far.  This is almost always for very small p (mainly 2 and 3) though, since I am starting with some saturated points on one curve (provided by Magma) and using p-isogenies to map to other curves in the isogeny class.  Higher degree isogenies are not so common.

I did start to veryify that the points from Magma were fully saturated, but ran into problems computing the saturation index, using (line 3717) the lower bound on the height of all non-torsion points -- previously implemented and merged i n6.3 (see #8828).  For example, I had a curve where the value of 5 in that line was insufficient *and led to an infinite loop in the call to min()*, while 10 worked fine, but now I have a curve where I have not yet found a value which gives anything.  For the record I will give that example here:

```
K.<phi> = NumberField(x^2-x-1) # Q(sqrt(5))
E = EllipticCurve([phi + 1, -phi + 1, 1, 20*phi - 39, 196*phi + 237])
H = E.height_function()
H.min(.1,10,verbose=True) #  does not appear to terminate
```


Strictly this is about the code merged in #8828, but it will need fixing here before we can let this (useful!) function out into the world.


---

Comment by git created at 2015-09-17 13:55:22

Branch pushed to git repo; I updated commit sha1. New commits:


---

Comment by cremona created at 2015-09-17 14:06:04

The latest branch I just pushed has some merges in it which were not intended but I hope that will not cause any problems -- as well as merging 6.9.beta6 I also merged by branch 'isogs' which has been merged into beta7.

One bug fix addresses the previous comment -- after re-reading my own 2006 paper I found that the original implementer from #8828 had missed one point (when mu is halved one must increment n_max in order to guarantee termination).   A small additional improvement in the same place (the method min_gr() in height.py) now gives a small improvement in the bound, which is why one doctest there has been changed.

The second bug was to do with mutability of lists giving unwanted side effects, and is commented at the point in the source which has changed.

It is likely that users who call the saturation() method will also want to lll_reduce() the output but I have not made that automatic.

I will set this to needs_review once my own full test has completed.


---

Comment by cremona created at 2015-09-17 14:13:55

Changing status from needs_work to needs_review.


---

Comment by cremona created at 2015-09-19 09:00:54

Changing status from needs_review to needs_work.


---

Comment by cremona created at 2015-09-19 09:00:54

After further testing (on many thousands of curves but only p-saturating for small p) I saw that it was bad to use discrete_log_lambda() for the dlog in the multiplcative group (in the rarer case where the p-rank of the reduction is 2 and the Weil pairing is used), both unnecessary and less efficient than simply w.log(zeta).
One additional commit coming up...


---

Comment by git created at 2015-09-19 10:35:24

Branch pushed to git repo; I updated commit sha1. New commits:


---

Comment by cremona created at 2015-09-19 10:37:31

Changing status from needs_work to needs_review.


---

Comment by cremona created at 2015-09-25 17:09:18

Changing status from needs_review to needs_work.


---

Comment by cremona created at 2015-09-25 17:09:18

There's some bug in the Weil pairing section which I don't have time to fix now, and this has missed 6.9 anyway.


---

Comment by cremona created at 2015-12-10 16:43:54

I did do more work on that but did not get to the bottom of it.  Just keeping the ticket alive!


---

Comment by git created at 2015-12-28 13:53:25

Branch pushed to git repo; I updated commit sha1. New commits:


---

Comment by git created at 2016-01-04 15:25:50

Branch pushed to git repo; I updated commit sha1. New commits:


---

Comment by cremona created at 2016-02-17 13:20:31

Merging with 7.1.beta3....


---

Comment by git created at 2016-02-17 16:49:24

Branch pushed to git repo; I updated commit sha1. New commits:


---

Comment by chapoton created at 2016-11-20 08:23:25

just rebased on 7.5.b3
----
New commits:


---

Comment by git created at 2016-12-11 11:36:34

Branch pushed to git repo; I updated commit sha1. New commits:


---

Comment by git created at 2017-08-06 15:58:17

Branch pushed to git repo; I updated commit sha1. New commits:


---

Comment by cremona created at 2017-08-06 15:59:08

I just merged 8,0 into the branch prior to looking at it again.


---

Comment by git created at 2017-08-06 20:05:33

Branch pushed to git repo; I updated commit sha1. New commits:


---

Comment by cremona created at 2017-08-06 20:08:19

Changing status from needs_work to needs_review.


---

Comment by cremona created at 2017-08-06 20:08:19

After merging into 8.0 I fixed some newly failing doctests (trivial things caused by the usual pari number field changes).  I moved the two p-saturation functions to a new file saturation.py, and added that to the reference manual.
Ready for review.  I intend to use this a lot soon over number fields of degree up to 6 for the LMFDB and it would be most helpful to have it merged into 8.1.


---

Comment by chapoton created at 2017-08-06 20:13:14

Quick comments :

* dot not use $ but backticks

* every function must be doctested


---

Comment by cremona created at 2017-08-06 20:16:38

!!! New docstrings use backticks, and new functions are doctested. !!!  The file ell_number_field is 3800 lines  long.  Both the files I just worked on have 100% coverage.


---

Comment by chapoton created at 2017-08-07 06:16:25

Hello ! some dollars there :

```
+        For rank 1 subgroups, simply do trial divison up to the maximal
+        prime divisor. For higher rank subgroups, perform trial divison
+        on all linear combinations for small primes, and look for
+        projections $E(K) \rightarrow \oplus E(k) \otimes \FF_p$ which
+        are either full rank or provide p-divisble linear combinations,
+        where the $k$ here are residue fields of $K$.
```

and no doc for

```
+    def projections(Q, p):
```

which is indeed an inner function, but quite a complicated one. Maybe just explain its input and output ?


---

Comment by cremona created at 2017-08-07 08:18:42

I stand corrected and will see to this.


---

Comment by cremona created at 2017-08-07 08:39:49

For the inner function projections(Q, p) there is already a docstring:

```
        Project points onto (E mod Q)(K mod Q) \otimes \F_p.

        Returns a list of 0, 1 or 2 vectors in \F_p^n
```

which explains what it does.  I'll make sure that all the other inner functions are explained.


---

Comment by git created at 2017-08-07 11:33:12

Branch pushed to git repo; I updated commit sha1. New commits:


---

Comment by cremona created at 2017-08-07 11:34:49

I hope the latest commits do what was wanted for docstrings.  I did remove some rather unnecessary one-liner internal functions.
In the course of doing this I found at least 2 bugs ;)  which is good because the reason this was not finished with 18 months ago was the existence of a bug.

Please review!


---

Comment by chapoton created at 2017-08-07 11:47:35

a typo here:

```
trial divison
```

and also a missing line break here after `r"""`:

```
+        r""" Given a list of rational points on `E` over `K`, compute the
```

same here:

```
        """Return generators for the Mordell-Weil group modulo torsion, for a
```

same there:

```
+    r""" Checks whether the list of points is `p`-saturated.
```

and

```
+    r""" Full `p`-saturation of ``Plist``.
```


another typo:

```
divisble
```

This :

```
+        if len(EE)==0:
```

can be replaced by `if not EE`

another typo:

```
algirithm
```



---

Comment by git created at 2017-08-07 12:15:37

Branch pushed to git repo; I updated commit sha1. New commits:


---

Comment by cremona created at 2017-08-07 12:16:13

I fixed those, and at least one more.  Thanks


---

Comment by chapoton created at 2017-08-07 20:21:24

"trial divison" is still there


---

Comment by git created at 2017-08-08 16:46:07

Branch pushed to git repo; I updated commit sha1. New commits:


---

Comment by cremona created at 2017-08-08 16:47:06

Not now it isn't.  I also used "grep -r" to catch 3 more (not mine).

One day I might get a review of the __code__!


---

Comment by roed created at 2017-08-22 22:23:30

Some comments on code:

* There's something weird with the indentation at `for Q in K.primes_above(q, degree=1):` in `p_saturation` (it looks only indented one space).
* There are various points where you don't have spaces around `==` and `+=`.  If you feel like fixing it, I think that spaces are the Python coding standard.
* At various points you add commented out code (either verbose print statements or the definition of `pair_max`).  I'm fine with what you have, but I could also see just deleting it.  I just wanted to make sure that the decision to include it, commented out, was conscious.

There are also test failures.

Other than these comments, the code looks good to me and I'm happy to give it a positive review once they're addressed.


---

Comment by kedlaya created at 2017-08-23 00:42:18

Also, the example from comment 5 still seems to go into an infinite loop.


---

Comment by cremona created at 2017-08-23 08:21:00

Changing status from needs_review to needs_work.


---

Comment by cremona created at 2017-08-23 08:21:00

Thanks to both for the reviews.  I'll look into the spacing issues and the example.  I really really want to get finished with this!


---

Comment by cremona created at 2017-08-23 08:59:01

I first merged in the current develop (and fixed one small conflict).  this required a rebuild (i.e. 'make' not just './sage -b' which failed).

I fixed that indentation issue -- logically correct but of course non-standard to have just one space of indentation.  I hope the result is OK, that indented block was very long and had a lot of subsidiary indented parts.

I have fixed all (I hope) the == and += spacing.

I changed some commented-out debugging print statements into comments.  I like having lots of comments since the logic is quite complicated (and if further bugs are found it may well be me who has to fix them so I might as well be helpful).

I'll test the example from comment 5 once the rebuild has finished.


---

Comment by cremona created at 2017-08-23 11:38:36

Dammit, I always use trac branch names of the form u/cremona/nnnnn where nnnnn is the ticket number, but at some point the branch here became public/8829, so I have just been fixing the wrong version.  What a waste of time.  Back soon.


---

Comment by cremona created at 2017-08-23 11:43:18

New commits:


---

Comment by cremona created at 2017-08-23 11:43:18

Changing status from needs_work to needs_review.


---

Comment by cremona created at 2017-08-23 11:47:56

OK, back to review.  Note that the branch is now u/cremona/8829.


---

Comment by chapoton created at 2017-08-23 11:51:00

"trial divison" is back, and probably all the other fixes went away.... Sorry for nitpicking, really..


---

Comment by cremona created at 2017-08-23 12:19:20

Changing status from needs_review to needs_work.


---

Comment by cremona created at 2017-08-23 12:19:20

!`@`$#!.  OK, I will check out commit d242123 by hash to be sure that is what was most recently reviewed, and redo the work I did before.  It's the only way to be certain.


---

Comment by cremona created at 2017-08-23 14:05:29

I hope I got it right this time.  The correct branch is public/8829 and I basically redid the edits I had already done this morning on the wrong branch.
----
Last 10 new commits:


---

Comment by cremona created at 2017-08-23 14:05:29

Changing status from needs_work to needs_review.


---

Comment by roed created at 2017-08-23 15:28:19

It looks like you've addressed everything.  I ran all tests and checked that the loop in comment 5 is no longer a problem.


---

Comment by roed created at 2017-08-23 15:28:19

Changing status from needs_review to positive_review.


---

Comment by cremona created at 2017-08-23 15:38:00

Thanks a lot!  This ticket was opened in 2010, so I'll be celebrating.  Now, if any of you would like to head on over to #22345...


---

Comment by chapoton created at 2017-08-23 18:07:09

Very well, and I share your joy, but you introduced a .next(), which is not compatible with python3 (see patchbot plugin report). To be fixed in a later ticket, please.


---

Comment by cremona created at 2017-08-23 18:39:25

That's a pity I thought the next () was rather neat. You can fix it here if you want.


---

Comment by chapoton created at 2017-08-23 18:40:05

no, no, let us wait and do that later


---

Comment by chapoton created at 2017-08-23 18:51:30

By the way, John, could you tell LMFDB people about #23671, please ?


---

Comment by git created at 2017-08-23 20:45:59

Changing status from positive_review to needs_review.


---

Comment by git created at 2017-08-23 20:45:59

Branch pushed to git repo; I updated commit sha1 and set ticket back to needs_review. New commits:


---

Comment by kedlaya created at 2017-08-23 20:46:53

Replying to [comment:80 chapoton]:
> no, no, let us wait and do that later

Isn't it just this one-line change? If so, no reason to postpone it...


---

Comment by roed created at 2017-08-23 22:58:11

Looks good to me!


---

Comment by roed created at 2017-08-23 22:58:11

Changing status from needs_review to positive_review.


---

Comment by vbraun created at 2017-08-29 19:51:22

Resolution: fixed


---

Comment by jdemeyer created at 2017-09-12 14:03:36

This is causing doctest failures: #23840.


---

Comment by cremona created at 2017-09-12 14:40:17

I'm pretty certain it will be the usual nonsense of mathematically equivalent outputs.  I'll look at #23840 and judge properly.

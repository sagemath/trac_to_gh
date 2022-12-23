# Issue 8723: Change to return type of E.multiplcation_by_m(m,True)

Issue created by migration from https://trac.sagemath.org/ticket/8723

Original creator: cremona

Original creation time: 2010-04-20 10:53:54

Assignee: cremona

As reported to sage-nt:

If E is an elliptic curve over K and m is a nonzero integer, then E.multiplication_by_m(m) returns a tuple (X,Y) where X and Y are both in K(x,y) and give the "formula" for the multiplcation-by-m map on E.  Of course, mathematically, X is in K(x), but it is returned with the same parent as Y, namely K(x,y) (i.e. the fraction field of the 2-variable polynomial ring over K).

There is an optional parameter x_only which by default is False, but if True the return value is just X as above, an element of K(x,y) which happens not to involve y.

I propose to change the function so that there is no change when x_only is False (the default), but when it is True the rational function returned would be in K(x) and not in K(x,y);  in this case one would not need to construct any bivariate polynomial rings or fields at all.

Would anyone be unhappy about this?  The only issue which I can see is that if you construct phi to be the multiplcation-by-m isogeny, then phi.rational_maps() is currently of the form (X,Y) as above, so now one can check that

phi.rational_maps()[0] == E.multiplication_by_m(m,True)

while after my proposed change this would be False (I think, unless coercion would magically embed K(x) into K(x,y), which I have not checked).  

Implementation and checking would be very easy.



---

Comment by chapoton created at 2013-08-20 14:30:40

here is a proposal, if this is still wanted after so many years


---

Comment by chapoton created at 2013-08-20 14:30:40

Changing status from new to needs_review.


---

Comment by cremona created at 2013-08-20 14:42:48

So now I really am going to have to learn how to use the new git system!


---

Comment by chapoton created at 2013-08-20 14:50:48

well, sooner or later...  =)

there are some explanations here  :

http://sagemath.github.io/git-developer-guide/walk_through.html#section-walkthrough-review


---

Comment by cremona created at 2013-08-21 19:43:01

Replying to [comment:5 chapoton]:
> well, sooner or later...  =)
> 
> there are some explanations here  :
> 
> http://sagemath.github.io/git-developer-guide/walk_through.html#section-walkthrough-review
> 

I have a clone of the git repository and pulled in all the commits on trac (using git pull trac master followed by make), and have a working version (./sage runs ok and shows 5.12.beta2 in the banner).  But ./sage -dev fails (unknown option).  Does that mean that I should do the "manual git" as in Git the Hard Way, using git fetch trac ...?  I can do that, of course, but thought that the scripts made it unnecessary.

Meanwhile I looked at the diff for your commit and looks reasonable, though I would of course want to check it.


---

Comment by chapoton created at 2013-08-21 19:51:24

well, I must admit that I have never done a review for a git branch. 

If I would try, I would go for the "hard way".

But I would really like to know how to use the dev script manner too.


---

Comment by chapoton created at 2013-08-30 19:26:06

I have made a second commit, trying to improve the documentation


---

Comment by git created at 2013-12-02 20:58:00

Branch pushed to git repo; I updated commit sha1. New commits:


---

Comment by git created at 2013-12-02 21:08:19

Branch pushed to git repo; I updated commit sha1. New commits:


---

Comment by cremona created at 2013-12-17 11:41:44

I am attempting to review this as my first real venture into the new world of reviewing using the git model...


---

Comment by cremona created at 2013-12-17 15:19:16

See the discussion on sage-git here: https://groups.google.com/d/topic/sage-git/mbAH7xAia3Y/discussion

My plan now is to merge this branch with the current master, which I think will make it easier to see what has now changed with this ticket.  There are some problems caused by the fact that this branch was forked off the master branch rather along time ago.  An alternative to merging would be to use git's cherry-pick or rebase procedure to apply the changes made by the commits in this branch to the current master branch.  I think that would be better: it would be like pretending that the work on this ticket all happened right now.

Would you like to do that or shall I try?


---

Comment by chapoton created at 2013-12-17 15:39:01

Well, I am rather busy right now, and I am really not enough git-confident and knowledgeable to do that. Please do it yourself if you can.

Frederic


---

Comment by cremona created at 2013-12-17 16:10:42

Replying to [comment:14 chapoton]:
> Well, I am rather busy right now, and I am really not enough git-confident and knowledgeable to do that. Please do it yourself if you can.
> 
> Frederic

It turns out that I am not allowed to (see further discussion on sage-git).  I cannot rebase, since that is rewriting history and not allowed (by convention) on commits that have been made public (as on this ticket) since there might be people who have taken those commits as a base for something else.  (Clearly not likeliy in this case.)  And whle I can merge the current master, as a way of seeing what changes you have made (by comparing the merged current-master + your changes to the current-master by itself), which helps me see the cumulative effect of what you did, I am not supposed to upload that merged commit back to this ticket.

This makes it rather complicated for me to something which used to be so simple, i.e. to make some small "reviewer patch" additional changes.  I have to first unmerge the current master, then make my edits and a new commit whose parent is the one downloaded from this ticket and push that back up to the ticket.

Of course, that will not be necessary if I find your changes perfect ;)


---

Comment by cremona created at 2013-12-17 17:19:26

Very sorry, but checking that this works revealed a problem.  The function `multiplication_by_m` calls  `_multiple_x_numerator(m,x)` and the latter caches its results with a cache whose key is just m and not the tuple (m,x), which means that the x in the returned value of `E.multiplication_by_m` is not necessarily the x you defined in the function.  For example:

```
sage: E = EllipticCurve([0,0,0,0,1])
sage: x2,y2 = E.multiplication_by_m(2)
sage: x2.parent(), y2.parent()
(Fraction Field of Multivariate Polynomial Ring in x, y over Rational Field,
 Fraction Field of Multivariate Polynomial Ring in x, y over Rational Field)
sage: X2 = E.multiplication_by_m(2, x_only=True)
sage: X2.parent()
Fraction Field of Multivariate Polynomial Ring in x, y over Rational Field
```

where the last parent is wrong, and in the other direction

```
sage: E = EllipticCurve([0,0,0,0,1])
sage: X2 = E.multiplication_by_m(2, x_only=True)
sage: X2.parent()
Fraction Field of Univariate Polynomial Ring in x over Rational Field
sage: x2,y2 = E.multiplication_by_m(2)
sage: x2.parent(), y2.parent()
(Fraction Field of Univariate Polynomial Ring in x over Rational Field,
 Univariate Polynomial Ring in y over Fraction Field of Univariate Polynomial Ring in x over Rational Field)
```

which is worse!

I will fix this by changing the caching behaviour of the subsidiary function, and see if I can push the new commit onto this ticket.


---

Comment by cremona created at 2013-12-17 17:33:40

Replying to [comment:16 cremona]:

> 
> I will fix this by changing the caching behaviour of the subsidiary function, 

Done.  Now the output of that example is

```
sage: E = EllipticCurve([0,0,0,0,1])
sage: X2 = E.multiplication_by_m(2, x_only=True)
sage: X2.parent()
Fraction Field of Univariate Polynomial Ring in x over Rational Field
sage: x2,y2 = E.multiplication_by_m(2)
sage: x2.parent()
Fraction Field of Multivariate Polynomial Ring in x, y over Rational Field
sage: y2.parent()
Fraction Field of Multivariate Polynomial Ring in x, y over Rational Field
sage: E = EllipticCurve([0,0,0,0,1])
sage: x2,y2 = E.multiplication_by_m(2)
sage: x2.parent()
Fraction Field of Multivariate Polynomial Ring in x, y over Rational Field
sage: y2.parent()
Fraction Field of Multivariate Polynomial Ring in x, y over Rational Field
sage: X2 = E.multiplication_by_m(2, x_only=True)
sage: X2.parent()
Fraction Field of Univariate Polynomial Ring in x over Rational Field
```


> and see if I can push the new commit onto this ticket.

This failed with

```
Counting objects: 136, done.
Delta compression using up to 64 threads.
Compressing objects: 100% (26/26), done.
Writing objects: 100% (30/30), 4.47 KiB, done.
Total 30 (delta 20), reused 4 (delta 4)
remote: FATAL: W refs/heads/master sage cremona DENIED by fallthru
remote: error: hook declined to update refs/heads/master
To ssh://git@trac.sagemath.org:2222/sage.git
 ! [remote rejected] master -> master (hook declined)
error: failed to push some refs to 'ssh://git@trac.sagemath.org:2222/sage.git'
```


for which I am seeking help on sage-git.


---

Comment by cremona created at 2013-12-17 17:38:17

I have pushed my new commit now:

```
 * [new branch]      HEAD -> u/cremona/8723
```

though I cannot see any sign of it here on trac.


---

Comment by cremona created at 2013-12-17 19:30:10

New commits:


---

Comment by cremona created at 2013-12-17 19:44:41

For info:  I added some edits to Frederic's and pushed the resulting commit to a branch owned by me called u/cremona/8723, using the command

```
git push trac HEAD:u/cremona/8723 
```

Then I manually changed the Branch field on this ticket;  saving that updated the commit hash as well.

To see just my additional changes, pull the branch and do `git diff HEAD^ HEAD`.  It should be possible to see the changes since the parent's of Frederic's first commit, but I have not yet managed to do so.


---

Comment by cremona created at 2014-01-02 15:50:44

Frederic, if you approve of my additional changes (see previous comment) then we can jointly give this a positive review.  It would be very nice to rebase this into one simple commit on top of the current develop branch, but we are not allowed to do that, simply because of the remote possibility that someone else has based a new branch on what we already have here.  So the sooner we can get this merged the better!


---

Comment by chapoton created at 2014-01-02 17:08:20

There is a [x,0] to be replaced by [x] in sage/schemes/elliptic_curves/isogeny_small_degree.py

Because now the parent has only one variable

Otherwise, the tests do not pass.


---

Comment by cremona created at 2014-01-02 17:08:50

Patience... I grabbed the top commit and after remaking Sage find doctest errors (in `ell_field.py` and {{{isogeny_small_degree.py}}) so this needs more work.  Since git is perfect I must have not done enough testing.


---

Comment by cremona created at 2014-01-02 17:08:50

Changing status from needs_review to needs_work.


---

Comment by cremona created at 2014-01-02 17:25:28

Replying to [comment:23 chapoton]:
> There is a [x,0] to be replaced by [x] in sage/schemes/elliptic_curves/isogeny_small_degree.py
> 
> Because now the parent has only one variable
> 
> Otherwise, the tests do not pass.

You are quite right, and by chance you were editing your comment at the same time as I was.  I have fixed that and will push a new commit in a few minutes.  Apologies.  I wrote the original patch on this ticket before that code existed, I think.


---

Comment by cremona created at 2014-01-02 17:40:42

Note that the branch name has changed (it was non-standard, my fault).

I have checked that from this branch, "git merge develop" works ok -- since this branched off the tree at around 5.13.beta4 I thought that would be helpful to know, since it means (I think) that merging this branch into develop will also work!  And for good measure I will also rebuild and test everything.
----
New commits:


---

Comment by cremona created at 2014-01-02 18:01:03

I can confirm that after merging the develop branch and rebuilding, all (long) test pass.

Now the only question is, who gives this a positive review?


---

Comment by chapoton created at 2014-01-02 19:06:52

Well, I am happy with your changes, so you can set a positive review if you want.


---

Comment by chapoton created at 2014-01-02 19:12:31

Changing status from needs_work to needs_review.


---

Comment by cremona created at 2014-01-02 22:43:26

Changing status from needs_review to positive_review.


---

Comment by vbraun created at 2014-01-05 06:54:07

Resolution: fixed


---

Comment by saraedum created at 2014-04-11 12:38:27

I just stumbled upon this while working on #16129.

Replying to [comment:20 cremona]:
> New commits:
> ||[1fec983](http://git.sagemath.org/sage.git/commit/?id=1fec983)||reviewer's patch, makes sure that the parents are correct even with caching||

If I understand correctly, this is to make sure that the returned elements live in the correct rings. Does this really work the way it is meant to? The `x` in a univariate/bivariate ring can not be distinguished in the cache:

```
sage: R.<x,y> = QQ[]
sage: S.<x> = QQ[]
sage: R(x) == S(x)
True
sage: hash(R(x))==hash(S(x))
True
```


So what actually makes the patch work is this explicit conversion back to the right ring:

```
- mx = self._multiple_x_numerator(m.abs(), x) / self._multiple_x_denominator(m.abs(), x)
+ mx = (x.parent()(self._multiple_x_numerator(m.abs(), x))
+ / x.parent()(self._multiple_x_denominator(m.abs(), x)))
```


In other words, `_multiple_x_numerator/denominator` still return elements in the wrong ring. This is probably acceptable since they are marked as internal methods anyway:

```
sage: E = EllipticCurve([0,0,0,0,1])
sage: R.<x,y> = QQ[]
sage: E._multiple_x_numerator(2, x).parent()
Univariate Polynomial Ring in x, y over Rational Field
sage: E._multiple_x_numerator(2).parent()
Univariate Polynomial Ring in x, y over Rational Field
```


Should I fix this in #16129?

What causes actual trouble for me is that `x` has been added to the cache key in `division_polynomial_0`. Why is it necessary there? Is `division_polynomial_0` ever called with a different `x` but the same `cache`?


---

Comment by cremona created at 2014-04-11 15:10:59

I think the quick answer to the last question is "yes".  Apart from wanting to call the division poly functions with x's from different polynomial rings, which is frequently needed, there are places where instead of getting the polynomial and then substituting a value for x, one can compute the polynomials already evaluated, using the same recursion.  So there has to be a different cache for different values of x.

If your fix at #16129 does a better job while respecting this -- good!


---

Comment by saraedum created at 2014-04-11 20:16:03

Replying to [comment:34 cremona]:
> I think the quick answer to the last question is "yes".  Apart from wanting to call the division poly functions with x's from different polynomial rings, which is frequently needed,
But this does not seem to work if you pass in the same `cache` dictionary. An `x` from different polynomial rings has the same hash value, i.e., you get a result in the wrong ring.

```
sage: E = EllipticCurve([0,0,0,0,1])
sage: R.<x,y> = QQ[]
sage: cache = {}
sage: E.division_polynomial_0(1, cache=cache).parent()
Univariate Polynomial Ring in x over Rational Field
sage: E.division_polynomial_0(1, x, cache=cache).parent()
Univariate Polynomial Ring in x over Rational Field
```


> there are places where instead of getting the polynomial and then substituting a value for x, one can compute the polynomials already evaluated, using the same recursion.
I see. But would you really want to store these in the same `cache` dictionary?

If I understand correctly, the `cache` parameter is needed because you want to compute things for multiple values of `n`. Would it be acceptable if the method accepted a list for `n`? Or is the `cache` keyword used heavily by code outside the sage library?


---

Comment by cremona created at 2014-04-11 20:22:07

Replying to [comment:35 saraedum]:
> Replying to [comment:34 cremona]:
> > I think the quick answer to the last question is "yes".  Apart from wanting to call the division poly functions with x's from different polynomial rings, which is frequently needed,
> But this does not seem to work if you pass in the same `cache` dictionary. An `x` from different polynomial rings has the same hash value, i.e., you get a result in the wrong ring.
> {{{
> sage: E = EllipticCurve([0,0,0,0,1])
> sage: R.<x,y> = QQ[]
> sage: cache = {}
> sage: E.division_polynomial_0(1, cache=cache).parent()
> Univariate Polynomial Ring in x over Rational Field
> sage: E.division_polynomial_0(1, x, cache=cache).parent()
> Univariate Polynomial Ring in x over Rational Field
> }}}
> 
> > there are places where instead of getting the polynomial and then substituting a value for x, one can compute the polynomials already evaluated, using the same recursion.
> I see. But would you really want to store these in the same `cache` dictionary?
> 
> If I understand correctly, the `cache` parameter is needed because you want to compute things for multiple values of `n`. Would it be acceptable if the method accepted a list for `n`? Or is the `cache` keyword used heavily by code outside the sage library?

No, absolutely not.  The cache variable is not intended for use by users at all.  (I did not design this!).  It is for internal use so that the function for one value of n can re-use its values for smaller n and the same x.  I'm sure there are are other (and possibly better) ways to do it.


---

Comment by saraedum created at 2014-04-11 20:26:31

Replying to [comment:36 cremona]:
> Replying to [comment:35 saraedum]:
> > Replying to [comment:34 cremona]:
> > > I think the quick answer to the last question is "yes".  Apart from wanting to call the division poly functions with x's from different polynomial rings, which is frequently needed,
> > But this does not seem to work if you pass in the same `cache` dictionary. An `x` from different polynomial rings has the same hash value, i.e., you get a result in the wrong ring.
> > {{{
> > sage: E = EllipticCurve([0,0,0,0,1])
> > sage: R.<x,y> = QQ[]
> > sage: cache = {}
> > sage: E.division_polynomial_0(1, cache=cache).parent()
> > Univariate Polynomial Ring in x over Rational Field
> > sage: E.division_polynomial_0(1, x, cache=cache).parent()
> > Univariate Polynomial Ring in x over Rational Field
> > }}}
> > 
> > > there are places where instead of getting the polynomial and then substituting a value for x, one can compute the polynomials already evaluated, using the same recursion.
> > I see. But would you really want to store these in the same `cache` dictionary?
> > 
> > If I understand correctly, the `cache` parameter is needed because you want to compute things for multiple values of `n`. Would it be acceptable if the method accepted a list for `n`? Or is the `cache` keyword used heavily by code outside the sage library?
> 
> No, absolutely not.  The cache variable is not intended for use by users at all.  (I did not design this!).  It is for internal use so that the function for one value of n can re-use its values for smaller n and the same x.  I'm sure there are are other (and possibly better) ways to do it.

Great. Thanks for your answers. I will try to implement this in a different way at #16129 then.

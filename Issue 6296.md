# Issue 6296: linbox minpoly over small finite fields is TOTALLY BROKEN

Issue created by migration from Trac.

Original creator: was

Original creation time: 2009-06-15 10:51:54

Assignee: was


```


On Wed, Jun 10, 2009 at 6:03 PM, Yann<yannlaiglechapuy`@`gmail.com> wrote:
>
> ----------------------------------------------------------------------
> | Sage Version 4.0.1, Release Date: 2009-06-06                       |
> | Type notebook() for the GUI, and license() for information.        |
> ----------------------------------------------------------------------
> sage: A=matrix(GF(3),2,[0,0,1,2])
> sage: R.<x>=GF(3)[]
> sage: D={ x:0 , x+1:0 , x^2+x:0 }
> sage: for i in range(100000):
> ....:         D[A._minpoly_linbox()]+=1
> ....:
> sage: D
> {x: 38266, x + 1: 29397, x^2 + x: 32337}
>


You're absolutely right!  This *sucks* -- it seems like nothing we have ever wrapped in Linbox is right at first.  Hopefully the issue is that somehow the algorithm is only supposed to be probabilistic, and we're just misusing it in sage (quite possible). 
```



---

Comment by was created at 2009-06-15 14:49:38

from a linbox devel:

```
Well, I think this was corrected in linbox-1.1.6:

The minpoly algorithm used depends on which method you are using from
LinBox of course but,
If you use the solution "minpoly" you will get the blackbox algorithm
(just like if you specify "minpoly(pol, mat, Method::Blackbox())")
then (since sept 2008 and 1.1.6) we will end up using an extension field
to compute the minpoly (on my machine it will be GF(3^10)) and then
I e.g. got the following result for one try (the algorithm is still
probabilistic, but has a much larger success rate, roughly around 1/3^10):

 > 99993 minimal Polynomials are x^2 +x, 3 minimal polynomial are x+1, 4
minimal polynomials are x

Now for a so small matrix it could be better to use a dense version,
which can be called by "minpoly(pol,mat,Method::Elimination())".
If i am correct this dense version is also probabilistic (choice of the
Krylov non-zero vector) and therefore should also pick vectors from an
extension.
This is not the case in 1.1.6.
Clément can you confirm this ? If so it should be easy to fix, the same
way we fixed Wiedemann.

For your example matrix in some of the cases, when vectors [1,1], and
[2,2] are chosen the Krylov space has rank 1, whereas for other non zero
vectors  it has rank 2 and
thus the dense minbpoly will be x^2+x or x+1 ...

btw, the returned polynomial is always a factor of the true polynomial,
therefore to get a 1/3^{10k} probability  of success it will be
sufficient to perform the lcm of k runs.

Best,

--
                                       Jean-Guillaume Dumas.
```


My remarks

```
Hi Yann (and sage-support),

This is from a linbox developer (see below).   This will be fixed by:

 (1) upgrading -- actually, we *already* use linbox-1.1.6 in sage, so ...

 (2) making it so minpoly by default just raises a NotImplementedError, however
   minpoly(proof=False) will call minpoly a bunch of times and return
the lcm of the
   results.

It turns out that maybe linbox doesn't seem to have a proof=True
minpoly algorithm yet (they are hard to write), so our wrapping of
linbox is wrong, given that in Sage the default is proof=True
everywhere.

Yann -- if you want to work on improving the situation wrt any of the
above, please do.

William
```



---

Comment by was created at 2010-01-17 13:14:14

Changing status from new to needs_review.


---

Attachment


---

Comment by ylchapuy created at 2010-02-02 16:54:45

We should at least take the lcm of the results so far:

line 974:  g = g.lcm(self._minpoly_linbox(var)

otherwise, it seems ok.

Yann


---

Attachment

this is part 2


---

Comment by ylchapuy created at 2010-02-07 12:24:52

Ok positive review.

As an aside, is their any reason the result is cached but never fetched?

Yann


---

Comment by ylchapuy created at 2010-02-07 12:24:52

Changing status from needs_review to positive_review.


---

Comment by mpatel created at 2010-02-11 14:37:52

Please remember to update the relevant ticket fields --- the release
managers use an automated script to generate lists of merged tickets.


---

Comment by mpatel created at 2010-02-11 14:37:52

Resolution: fixed

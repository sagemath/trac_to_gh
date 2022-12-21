# Issue 4735: Make e^X try calling X.exp() before trying to coerce X to the symbolic ring

Issue created by migration from Trac.

Original creator: jason

Original creation time: 2008-12-07 04:53:37

Assignee: burcin

CC:  kcrisman

From sage-devel:

> I'd like to add an exponential function to RDF/CDF matrices (and  
> > enhance
> > the existing exp function for SR matrices) so that:
> >
> > sage: A = matrix(SR, [[1,2],[3,4]])
> > sage: e^A
> >
> > gives the same as
> >
> > sage: A.exp()
> >
> > (I'd also like this to work for other matrices, like over RDF or CDF,
> > where the returned matrix would be another RDF/CDF matrix---scipy has
> > functions that do this).
> >
> > However, currently for constants (in sage/functions/constants.py), the
> > __pow__ function automatically converts the exponent to an SR object,
> > which fails for a matrix.
> >
> > I have not worked with the constants code before.  Would there be a
> > problem with, for the E constant, overriding __pow__ so that if the
> > object had an "_exp" method, that was called instead of the default
> > conversion to SR objects?

+1, this was my first though when I started reading your email. I  
don't think it makes sense for other constants, but for E it  
certainly does. Also, I'd just call exp (not _exp), making sure that  
it doesn't introduce a recursive call...

> > Would that be the proper way to get the above functionality?  The goal
> > is also to get exp(A) to work as well; would I get that for free?

Yes. When you do exp(A) it attempts to return A.exp() before doing  
anything symbolic.


---

Comment by mhansen created at 2009-06-05 02:07:25

To do this, you'd have to add a check before every __pow__ operation with elements of SR, which may or may not be too much overhead.


---

Comment by kcrisman created at 2011-03-16 15:38:42

Changing priority from major to minor.


---

Comment by mhansen created at 2012-03-29 05:23:28

I don't think that this is necessarily a good idea to implement due to the reason I gave before.


---

Comment by kcrisman created at 2012-03-29 14:11:10

I'm changing the title to address the actual problem reported.

Can you think of a solution to the problem that this doesn't work, though?

```
sage: A = matrix(SR, [[1,2],[3,4]])
sage: exp(A)
[-1/22*((sqrt(33) - 11)*e^sqrt(33) - sqrt(33) - 11)*e^(-1/2*sqrt(33) + 5/2)              2/33*(sqrt(33)*e^sqrt(33) - sqrt(33))*e^(-1/2*sqrt(33) + 5/2)]
[             1/11*(sqrt(33)*e^sqrt(33) - sqrt(33))*e^(-1/2*sqrt(33) + 5/2)  1/22*((sqrt(33) + 11)*e^sqrt(33) - sqrt(33) + 11)*e^(-1/2*sqrt(33) + 5/2)]
sage: A.exp()
[-1/22*((sqrt(33) - 11)*e^sqrt(33) - sqrt(33) - 11)*e^(-1/2*sqrt(33) + 5/2)              2/33*(sqrt(33)*e^sqrt(33) - sqrt(33))*e^(-1/2*sqrt(33) + 5/2)]
[             1/11*(sqrt(33)*e^sqrt(33) - sqrt(33))*e^(-1/2*sqrt(33) + 5/2)  1/22*((sqrt(33) + 11)*e^sqrt(33) - sqrt(33) + 11)*e^(-1/2*sqrt(33) + 5/2)]
sage: e^A
---------------------------------------------------------------------------
TypeError: mutable matrices are unhashable
```

I get the same problem with entries in `RR`, and the original post noted `RDF` is also a problem.

I wonder if this is more calculus or more linear algebra... maybe a different component?


---

Comment by burcin created at 2012-03-29 14:29:24

Wouldn't changing `e.__pow__()` to be smarter work?

The error message above is raised when you try convert a matrix to a symbolic ring element. In the new symbolics, the constant E (defined in `sage/symbolic/constants.py` has a `__pow__` method that essentially does `e^x -> SR(x).exp()`. (This was probably written by Mike.)

If you change that to call `x.exp()` first, you might get what you want.


---

Comment by kcrisman created at 2012-03-29 14:38:56

Ah.  And the original posts apparently do refer only to changing for `E`.  Mike, are you saying this could cause a problem in this specific case, or only if we did it more widely?  It would be interesting to compare timings for making this change; naturally, one could potentially have a _lot_ of `e^foo` in a given computation, so even microseconds spent checking whether `foo` had a `exp()` method could add up, which I think is his point... maybe?


---

Comment by mhansen created at 2012-03-29 16:47:46

Actually, I was confused -- I was under the impression that `e` was of type `Expression`.  I'll post a patch soon.


---

Attachment


---

Comment by mhansen created at 2012-05-28 07:08:46

Changing status from new to needs_review.


---

Comment by mhansen created at 2012-05-28 07:08:46

Changing keywords from "" to "sd40.5".


---

Comment by kcrisman created at 2012-05-28 15:39:22

Adds lots of examples


---

Attachment

This is a *heavily* requested feature, so I've added a number of examples, as well as added the original file in question to the reference manual (though the new doc there from the first patch doesn't show up since it's in a double-underscore method).  The complex matrices were in particular demand, so thank you so much for fixing this.

I've added enough that, though it passes tests, I'd appreciate a further review to make sure I didn't do something silly.  Positive review for Mike's patch.


---

Comment by mhansen created at 2012-05-28 17:47:39

Changing status from needs_review to positive_review.


---

Comment by mhansen created at 2012-05-28 17:47:39

Karl-Dieter's patch looks good to me.


---

Comment by jdemeyer created at 2012-06-18 10:21:31

Resolution: fixed

# Issue 9547: x * Infinity assumes that x is positive

Issue created by migration from https://trac.sagemath.org/ticket/9547

Original creator: fredrik.johansson

Original creation time: 2010-07-19 08:25:53

Assignee: AlexGhitza

CC:  kcrisman


```
sage: var('x') * Infinity
+Infinity
```


This is not right; x could represent something non-positive.


---

Comment by tscrim created at 2012-05-11 13:32:58

Likely the solution will be related with #11506.


---

Comment by burcin created at 2012-05-15 22:23:58

Changing component from algebra to symbolics.


---

Comment by burcin created at 2012-05-15 22:23:58

Changing assignee from AlexGhitza to burcin.


---

Comment by burcin created at 2012-05-15 22:23:58

This is fixed by #12950. There is a doctest on line 2429 of `sage/symbolic/expression.pyx`. We should close this ticket when that is merged.


---

Comment by burcin created at 2012-06-29 10:48:58

Changing status from new to needs_review.


---

Comment by burcin created at 2012-06-29 10:49:28

Changing status from needs_review to positive_review.


---

Comment by kcrisman created at 2012-06-29 13:09:20

Patch is at #12950, but still a valid ticket; that was a meta-ticket for the Pynac upgrade.


---

Comment by jdemeyer created at 2012-06-29 14:03:13

Replying to [comment:6 kcrisman]:
> Patch is at #12950, but still a valid ticket; that was a meta-ticket for the Pynac upgrade.
Same question as #1861: why doesn't this count as duplicate/invalid/wontfix?


---

Comment by kcrisman created at 2012-06-29 15:00:04

> > Patch is at #12950, but still a valid ticket; that was a meta-ticket for the Pynac upgrade.
> Same question as #1861: why doesn't this count as duplicate/invalid/wontfix?
In my opinion (only?), tickets that are closed by metatickets are not duplicates.  It seems better to me (only?) to make it clear that work went into all of the issues we close, instead of making it seem like we have hundreds of duplicates that people open.  We already _do_ have enough duplicates as it is :) 

And we certainly fixed it, so it's not "wontfix", and it's not invalid either, or at least wasn't before #12950, which however, explicitly refers to this ticket - it's not like some other change in #12950 made this invalid, which does sometimes happen.


---

Comment by jdemeyer created at 2012-06-29 15:30:26

If the issue is fixed by a _different_ ticket, then this ticket should be either a "duplicate" or a "worksforme".

Has a doctest been added for this?  If not, one could consider needs_work.


---

Comment by kcrisman created at 2012-06-29 15:42:40

> If the issue is fixed by a _different_ ticket, then this ticket should be either a "duplicate" or a "worksforme".
I simply disagree.  So you are saying that, hypothetically, a gigantic metaticket for foo.spkg that bundles fifty changes, all of which are doctested by some huge patch at that ticket, means all the others are duplicates?  That seems to denigrate the hard work that went into each of those other tickets.  Although the people currently working on these particular tickets are not counting on this material for promotion, that is certainly a future possibility, as standards evolve, especially at less research-focused institutions.
> Has a doctest been added for this?  If not, one could consider needs_work.
Yes, it is at #12950.


---

Comment by jdemeyer created at 2012-06-29 16:25:04

Replying to [comment:10 kcrisman]:
> > If the issue is fixed by a _different_ ticket, then this ticket should be either a "duplicate" or a "worksforme".
> I simply disagree.  So you are saying that, hypothetically, a gigantic metaticket for foo.spkg that bundles fifty changes, all of which are doctested by some huge patch at that ticket, means all the others are duplicates?  That seems to denigrate the hard work that went into each of those other tickets.  Although the people currently working on these particular tickets are not counting on this material for promotion, that is certainly a future possibility, as standards evolve, especially at less research-focused institutions.
You could give credit to those people on the other gigantic metaticket.

On this particular ticket here, I don't see any work done, so I would simply close it as duplicate.


---

Comment by kcrisman created at 2012-06-29 16:30:05

> You could give credit to those people on the other gigantic metaticket.
Which Burcin did.  The point was that although a ticket isn't a great measure of work, we don't have to make it an even worse measure.
> On this particular ticket here, I don't see any work done, so I would simply close it as duplicate.
Well, I was going by the fact that someone else filled in author and reviewer fields and the work "just happened" to be there; see also the discussion at #12950.  But if you insist, I suppose I've engaged in enough bikeshedding for one day.


---

Comment by jdemeyer created at 2012-07-04 07:23:50

Resolution: duplicate

# Issue 9712: Make building PolyBoRi depend on GD

Issue created by migration from Trac.

Original creator: leif

Original creation time: 2010-08-09 22:35:52

Assignee: tbd

CC:  leif malb

From #9472:

 "Since PolyBoRi also uses GD, `$SAGE_ROOT/spkg/standard/deps` should be updated (but there seem to have been no issues with that in the past)."



---

Attachment

Updated `spkg/standard/deps`.  Based on 4.5.2 + #8316.


---

Attachment

Diff of `spkg/standard/deps` vs. 4.5.2 + #8316.


---

Comment by mpatel created at 2010-08-09 23:17:01

I've attached a new `deps` and `deps.diff`.

I'm not sure whether to put Leif or Martin as the author, or both Leif and Martin.  Can someone please update the field?


---

Comment by mpatel created at 2010-08-09 23:17:01

Changing status from new to needs_review.


---

Comment by leif created at 2010-08-10 00:46:58

Replying to [comment:1 mpatel]:
> I'm not sure whether to put Leif or Martin as the author, or both Leif and Martin.  Can someone please update the field?

Can you update the _"Reported by:"_ field? ;-)

From PolyBoRi's `SPKG.txt`:

```
...

## Dependencies

 * Python
 * Scons
 * Boost
 * gd (FIXME/TODO: should be added to deps, I think. Leif, 2010-07-10)
 * M4RI/libm4ri (already included in deps)
 * png/libpng12 (accomplished because Python and gd depend on it, too)
 * libz         (accomplished because e.g. libpng depends on it)

...
```


I must admit I did not check _all_ transitive dependencies, i.e. if some package that PolyBoRi (indirectly) depends on pulls in the GD dependency. Anyway, I think it's always better to add an explicit, perhaps "redundant" dependency rather than to omit it, (not only) since the deps of other packages might change over the time. (Same for explicitly linking against libraries directly used despite other used libraries - _currently_ - already doing so.)

The only package in `standard/deps` that's listed to *directly* depend on GD is `gdmodule`, which in turn is only listed as a (direct) dependency of MatPlotLib (and the Sage library).


---

Comment by leif created at 2010-08-10 00:54:30

I've only "reviewed" `deps.diff` though... :)


---

Comment by leif created at 2010-08-10 00:54:30

Changing status from needs_review to positive_review.


---

Comment by leif created at 2010-08-10 13:18:15

I'm pretty sure it's just good luck this ever worked. GD is one of the "early" packages, and all of these take little time to build.

I'll perhaps verify that later by forcing GD to be built very late.


---

Comment by leif created at 2010-08-10 13:22:16

P.S.: The suggestion to change the "Reported by:" field was just a joke.


---

Comment by mpatel created at 2010-08-15 06:57:32

Resolution: fixed

# Issue 9802: Generalize and document the random_matrix constructor

Issue created by migration from Trac.

Original creator: rbeezer

Original creation time: 2010-08-26 00:27:48

Assignee: jason, was

CC:  bwonderly mhansen wdj jason

This will vastly improve the documentation of the `random_matrix` command in common use cases (integers, rationals,...).

It will also allow for new, more specialized constructions, such as Billy Wonderly's work at #9720, #9754, #9820.

See #9720 for motivating discussion.


---

Attachment


---

Comment by rbeezer created at 2010-08-26 22:19:57

Patch expands the functionality of the `random_matrix` routine.  A matrix space is used to accumulate the base ring, dimensions and representation (sparse/dense).  This can then be passed to the new `random_*_matrix` routines where a matrix can actually be constructed and returned.

Documentation for previous behavior greatly expanded, notably for integer and rational matrices.  New routines are demonstrated, with clear directions (links, imports) to expanded documentation.

Had to handle density and sparse keywords in a backwards-compatible fashion, so they are "popped" out of the `kwds` dictionary and passed as before to the matrix randomize() routine.  The keywords are now required and won't work as positional arguments.  Had to adjust code in the group theory isomorphism code in a couple of modules as a result.  Also the `random_matrix` command was employed coincidentally in a doctest in the lazy import routine.  I think the new version works just as well as a test, so I changed the output.

This code below looks like some artifact of the switch to allowing/disallowing zero entries.  I've left it in, though it *never* gets called in any of the tests (I checked).  Before my changes, `density` had a default value of 1, so you would have to consciously pass in `None` to make this happen.  It was not documented.


```
        if density is None:
            A.randomize(density=float(1), nonzero=False, *args, **kwds)
        else:
            A.randomize(density=density, nonzero=True, *args, **kwds)
```


One fix in mod n dense matrix code.  Could not figure out how `range(25)` was doing anything useful, and it was ending up in the algorithm argument, so in the end I just removed it and the affected test passes.


---

Comment by rbeezer created at 2010-08-26 22:19:57

Changing status from new to needs_review.


---

Attachment

Standalone patch


---

Comment by rbeezer created at 2010-08-27 01:45:46

First patch contained:


```
columns = parent.nrows()
```


which is just plain wrong, but also `columns` was never referenced (which is why the doctests were unaffected).  Its gone now.  Use just the v2 patch.


---

Comment by wdj created at 2010-08-27 17:16:46

Does this patch depend on any other patches?


---

Comment by rbeezer created at 2010-08-27 17:40:25

Replying to [comment:3 wdj]:
> Does this patch depend on any other patches?

Ah, yes, totally forgot.  It needs to have #9720 (just the v4 patch) applied first.  Thanks.


---

Comment by wdj created at 2010-08-28 19:56:14

Applied (with #9720) to 4.5.1 and passed sage -testall. Positive review as far as I see, but maybe Mike Hansen should weight in.


---

Comment by mhansen created at 2010-08-30 03:45:39

This looks good to me.


---

Comment by rbeezer created at 2010-08-30 03:55:13

Replying to [comment:6 mhansen]:
> This looks good to me.

Thanks for your input.  I think this is much improved organized this way, and I finally did something about the documentation for the `random_matrix()` command.  ;-)

Looks like this can go to positive review along with the rest of Billy's work.


---

Comment by rbeezer created at 2010-08-30 03:55:13

Changing status from needs_review to positive_review.


---

Comment by bwonderly created at 2010-09-03 06:27:29

## Release Manager

#9720, #9803, #9802, #9754 is each dependent on the predecessor, merge in this
order.


---

Comment by mpatel created at 2010-09-15 09:52:57

Resolution: fixed

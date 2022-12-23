# Issue 8746: Equality of posets element is very slow

Issue created by migration from https://trac.sagemath.org/ticket/8746

Original creator: hivert

Original creation time: 2010-04-22 19:45:56

Assignee: sage-combinat

CC:  sage-combinat

Keywords: Comparison posets elements

This is due to comparing the parent which can indeed be very slow. However most of the time when comparing `x` and `y`, the two parent are identical and are better compared with `is`. Here is the results:

Before the patch:


```
sage: P = Posets.ChainPoset(30)
sage: %time len([x == y for x in P for y in P])
CPU times: user 18.05 s, sys: 0.04 s, total: 18.09 s
Wall time: 18.25 s
900
```

After the patch:

```
sage: P = Posets.ChainPoset(30)
sage: %time len([x == y for x in P for y in P])
CPU times: user 0.03 s, sys: 0.00 s, total: 0.03 s
Wall time: 0.02 s
900
```


Cheers,

Florent



---

Comment by hivert created at 2010-04-22 19:49:57

Changing status from new to needs_review.


---

Attachment

Looks good to me and passes all doctests.


---

Comment by novoselt created at 2010-04-22 22:05:05

Changing status from needs_review to positive_review.


---

Comment by hivert created at 2010-04-22 22:13:22

Replying to [comment:2 novoselt]:
> Looks good to me and passes all doctests.

Thanks a lot for the very quick review !


---

Comment by hivert created at 2010-04-26 12:34:14

Changing priority from major to blocker.


---

Comment by hivert created at 2010-04-26 12:34:14

Remove assignee sage-combinat.


---

Comment by hivert created at 2010-04-26 12:39:24

I've sent the following message to sage-release and sage-devel but it doesn't seems to pass through

```
> This release candidate for Sage 4.4 closed 19 tickets (on top of
> 4.4.alpha1). On trac, these tickets were labeled as "merged into
> 4.4.alpha2", but then I decided that alpha2 should be the same as rc0.

Cool ! So there is a good chance that we'll have 4.4 for sage 20.5 next week
at Toronto ! This is perfect...

I'm however embarrassed to have the following question/request:
 - how do we decide to make some ticket blocker for a release. Is it possible
at this stage to make #8746 blocker for 4.4. Here is the rationale:

The Posets library (by Franco Saliola) allows to deals with small Partially
Ordered SETS. This kind of structure is extremely useful an common in
combinatorics. Usually we play with one poset at a time, seeking for
particular property of one of them. For my research I had to play with many of
them and I discovered that the equality was (very fast) but completely broken,
preventing them to be used eg. as key in dict. This was fixed in #7438. We
solved this together with Nicolas Borie (which is a student of Nicolas Thiéry)
and this was merged in alpha0. However we didn't realize that doing this we
slowed of the most common usage that is comparing element in a single poset by
several order of magnitude. I take the full blame for this mistake which I
consider as an important regression. #8746 solve this common use issue.

So is there still possible to merge #8746 while having 4.4 out before sage
days 20.5 ? I realize that I should have marked this ticket as critical or
blocker at its creation but I don't know how this is decided so that I never
change this field... Many Apologies for this late request.
```



---

Comment by was created at 2010-04-29 05:22:27

Resolution: fixed

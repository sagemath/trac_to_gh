# Issue 9696: Add methods to AdditiveAbelianGroup

Issue created by migration from Trac.

Original creator: rbeezer

Original creation time: 2010-08-06 06:22:59

Assignee: joyner

CC:  davidloeffler cremona

Patch adds `is_cyclic()` and `_latex_()` methods to the `AdditiveAbelianGroup`s.


---

Attachment


---

Comment by rbeezer created at 2010-08-06 06:28:00

Changing status from new to needs_review.


---

Comment by cremona created at 2010-08-22 13:28:39

Changing status from needs_review to positive_review.


---

Comment by cremona created at 2010-08-22 13:28:39

Applies fine to 4.5.3.alpha1.   Perhaps it would be good to have a doctest showing this:

```
sage: AdditiveAbelianGroup([1])._latex_()
'\\frac{\\ZZ}{1\\ZZ}'
```

which is not what a mathematician would write (perhaps change it to '0'). 

I have given a positive review anyway, but would be happy to re-review with this changed and/or doctested.


---

Comment by rbeezer created at 2010-08-22 18:53:24

Changing status from positive_review to needs_work.


---

Comment by rbeezer created at 2010-08-22 18:53:24

Replying to [comment:2 cremona]:
> which is not what a mathematician would write (perhaps change it to '0'). 

Yes, I like the '0' suggestion, I'll make that change and post an updated patch shortly.  Thanks for the suggestion.

> I have given a positive review anyway, but would be happy to re-review with this changed and/or doctested.


---

Attachment

Stand-alone patch, apply just this one


---

Comment by rbeezer created at 2010-08-22 20:00:44

Changing status from needs_work to needs_review.


---

Comment by rbeezer created at 2010-08-22 20:00:44

v2 patch adds a stanza to the latex representation code to detect trivial factor(s) and format as '0'.  This probably only happens when the invariant list passed in is empty, but there shouldn't be much penalty in burying this inside the construction of all the other possible terms.

A doctest is added for this situation, and the affected file passes all tests.  I built the documentation, but it would appear this section is not being included in the documentation?  I could rectify that with another patch and a look at the resulting output.

Thanks,
Rob


---

Comment by cremona created at 2010-08-22 21:09:27

Second patch looks good.  (I was just thinking of testing for the trivial group, but this is more general.)

Abelian groups are in the reference manual:  doc/en/reference/groups.rst has

```
   sage/groups/abelian_gps/abelian_group
   sage/groups/abelian_gps/abelian_group_element
   sage/groups/abelian_gps/abelian_group_morphism
   sage/groups/abelian_gps/dual_abelian_group
```


There are some formatting issues with those but not caused by this patch.


---

Comment by cremona created at 2010-08-22 21:09:27

Changing status from needs_review to positive_review.


---

Comment by cremona created at 2010-08-22 21:11:16

Replying to [comment:5 cremona]:
> Second patch looks good.  (I was just thinking of testing for the trivial group, but this is more general.)
> 
> Abelian groups are in the reference manual:  doc/en/reference/groups.rst has
> {{{
>    sage/groups/abelian_gps/abelian_group
>    sage/groups/abelian_gps/abelian_group_element
>    sage/groups/abelian_gps/abelian_group_morphism
>    sage/groups/abelian_gps/dual_abelian_group
> }}}
> 
> There are some formatting issues with those but not caused by this patch.

Sorry, my mistake -- abelian_groups are not additive_abelian_groups, and the latter are not included.  Something for another ticket!


---

Comment by rbeezer created at 2010-08-22 23:28:03

Replying to [comment:6 cremona]:
> Sorry, my mistake -- abelian_groups are not additive_abelian_groups, and the latter are not included.  Something for another ticket!

New ticket at #9783 which I will try to make some progress on.

Release manager:  Only apply the v2 patch.


---

Comment by mpatel created at 2010-09-15 10:40:03

Resolution: fixed

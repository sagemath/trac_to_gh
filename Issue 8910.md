# Issue 8910: Have CombinatorialClass inherits from Parent

Issue created by migration from Trac.

Original creator: hivert

Original creation time: 2010-05-07 12:02:11

Assignee: hivert

CC:  sage-combinat

This is the first step of the cleanup of the combinatorial classes see 
  http://trac.sagemath.org/sage_trac/wiki/SageCombinatRoadMap


---

Comment by hivert created at 2010-05-12 17:47:11

Changing status from new to needs_work.


---

Attachment

The patch has been reviewed by Nicolas on the patch queue. I folded the review patches:

```
$ hg qgoto trac_8910-subsets_an_element-fh.patch
$ hg qfold trac_8910-subsets_an_element-review-nt.patch
$ hg qfold trac_8910-subsets_an_element-review-review-fh.patch
```

And Nicolas said by e-mail

```
> Dès que j'ai ton feu vert, je folde tout, et met la positive review sur trac.

Feu vert!
```

Meaning: (FH) as soon as I have your green light I fold the whole bunch, and set positive review on trac. (Answer from Nicolas) Green Light.

Therefore I allowed myself to put the positive review.


---

Comment by hivert created at 2010-05-31 15:37:21

Changing keywords from "" to "CombinatorialClass Parent".


---

Comment by hivert created at 2010-05-31 15:37:21

Changing status from needs_work to needs_review.


---

Comment by hivert created at 2010-05-31 15:38:17

Changing status from needs_review to positive_review.


---

Comment by hivert created at 2010-05-31 15:38:17

> Meaning: (FH) as soon as I have your green light I fold the whole bunch, and set positive review on trac. (Answer from Nicolas) Green Light.

> Therefore I allowed myself to put the positive review.

Done


---

Comment by hivert created at 2010-05-31 15:40:40

I forgot to tell: depend on #8881 (review in progress. Should be done soon).


---

Attachment


---

Comment by mhansen created at 2010-06-05 22:19:15

Note that this depends on #8902.


---

Comment by mhansen created at 2010-06-05 22:21:59

Resolution: fixed

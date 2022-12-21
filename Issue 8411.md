# Issue 8411: Branching rule fix and doc revision

Issue created by migration from Trac.

Original creator: bump

Original creation time: 2010-03-01 19:42:24

Assignee: sage-combinat

CC:  sage-combinat brant@math.ucdavis.edu

This corrects a minor problem with branching rules in weyl_characters.py.

Previously branching rules SO(m+n)->SO(m)xSO(n) were implemented using
rule="extended", and similarly for symplectic groups. However there is one
case where this does not meet the definition of the extended rule, namely
SO(2n+2m+2)->SO(2n+1)xSO(2m+1). Indeed, the extended rule checks
to see if the ranks are equal, which they are not in this case.

I thought the cleanest fix was to implement a new rule called "orthogonal_sum"
for such cases.

I also took the chance to revise the documentation since what was said
before about rule="symmetric" was misleading.


---

Comment by bump created at 2010-03-01 19:45:46

Changing status from new to needs_review.


---

Comment by nthiery created at 2010-04-18 15:30:43

All test pass on 4.3.4 and, from a technical point of view, the patch
looks good.

So it is good to go as soon as someone more knowledgeable with
branching rules will have double check the mathematics? Well, of
course, the expert is Dan :-) Maybe Brant?


---

Comment by nthiery created at 2010-04-18 15:34:59

Changing keywords from "" to "Branching rules".


---

Comment by bump created at 2010-04-18 17:32:03

jhpalmieri objected in #8414 to the fact that the patch there did not contain
mercurial headers information.

I therefore remade this patch. There is no change to the content of the patch.


---

Comment by nthiery created at 2010-04-18 17:44:56

Please also include the ticket number in the patch title!

#8411: Branching rule fix and doc revision

Sorry for the extra bother ...


---

Comment by bump created at 2010-04-19 01:29:10

Branching rule fix and revised doc in weyl_characters.py


---

Attachment

> Please also include the ticket number in the patch title!
>
> #8411: Branching rule fix and doc revision
>
> Sorry for the extra bother ...

OK, I changed the patch description to begin #8411.


---

Comment by brant.c.jones created at 2010-04-20 16:32:48

Changing status from needs_review to positive_review.


---

Comment by brant.c.jones created at 2010-04-20 16:32:48

This is a positive review for trac_8411.

Prior to this patch, sage would not branch e.g. SO(3) x SO(3) -> SO(6) because this would embed a rank 2 group in a rank 3 group, and the get_branching_rule() code required the ranks to be equal.  After applying this patch, the "orthogonal_sum" rule will allow such branching (as the identity map) between types B/D, and within type C (only).

This patch correctly implements useful mathematics.

-- Brant Jones


---

Comment by jhpalmieri created at 2010-04-23 17:10:54

Resolution: fixed


---

Comment by jhpalmieri created at 2010-04-23 17:10:54

Merged into 4.4.alpha2.

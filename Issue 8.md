# Issue 8: py3: Make doctest pass in combinat/rigged_configurations module

CC:  chapoton



Issue created by migration from https://trac.sagemath.org/ticket/26805




---

Changing status from new to needs_review.


---

ok, good to go. But would you please first fix the pyflakes warnings ?


---

Sure, i will do it this morning.


---

Branch pushed to git repo; I updated commit sha1. New commits:


---

`@`chapoton I commented `vct` rather than deleting the line to keep consistency with
the comments below in the code. 
Do you think the comments 

```
        # vct = self.parent()._folded_ct
        # sigma = vct.folding_orbit()
        # gammatilde = list(vct.scaling_factors())
        # gammatilde[-1] = 2
}}} 
are helpful or do you think we should delete them?


---

oh, we can keep them.

green bot => positive review.

Do you have a patchbot at your disposal that you could launch on this ticket ? Mines are already busy right now.


---

Not right now (some computing in progress). I will try this afternoon.


---

Changing status from needs_review to positive_review.


---

Resolution: fixed


---

This tickets were closed as fixed after the Sage 8.5 release.

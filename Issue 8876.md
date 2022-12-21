# Issue 8876: Allows triangular morphisms to have domain and codomain with different index sets

Issue created by migration from Trac.

Original creator: hivert

Original creation time: 2010-05-04 22:37:22

Assignee: hivert

Keywords: Triangular Morphisms

Patch in progress on sage-combinat queue.


---

Attachment


---

Comment by hivert created at 2010-06-02 10:15:19

Changing status from new to needs_review.


---

Attachment

Hi Florent, I found some issues with the file as I was going through it, which I've fixed in the attached reviewer patch. (Many were probably my fault to begin with.)  Everything else looks good to me.  If you approve my reviewer patch and verify that all tests pass on massena without prereqs, you can set a positive review.  (I will post my reviewer patch on the combinat queue immediately below yours right now.)


---

Comment by hivert created at 2010-06-04 08:19:40

Everything was ok with the following patch applied:

```
trac_8881-functorial_constructions-nt.patch
trac_8742-lazy_format-fh.patch
trac_8742-lazy_format-review-nt.patch
trac_8876-triangular_morphisms_improve-fh.patch
trac_8876-reviewer_patch-jb.patch
```


Thanks for the review and the corrections. Your patch is good. Positive review


---

Comment by hivert created at 2010-06-04 08:19:40

Changing status from needs_review to positive_review.


---

Comment by mhansen created at 2010-06-05 21:51:42

Resolution: fixed

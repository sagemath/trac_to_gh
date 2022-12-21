# Issue 9075: sage.structure.sage_object.unpickle_all improvements

Issue created by migration from Trac.

Original creator: nthiery

Original creation time: 2010-05-28 17:38:25

Assignee: was

CC:  sage-combinat




---

Comment by nthiery created at 2010-05-28 17:41:17

Changing status from new to needs_review.


---

Comment by nthiery created at 2010-05-28 17:41:17

Changing keywords from "" to "pickling, testsuite".


---

Comment by mhansen created at 2010-09-17 00:47:33

Changing status from needs_review to positive_review.


---

Comment by mhansen created at 2010-09-17 00:47:33

Looks good to me.


---

Comment by nthiery created at 2010-09-17 09:15:10

Hi Mike!

Replying to [comment:2 mhansen]:
> Looks good to me.

Thanks for the review!


---

Comment by mpatel created at 2010-09-28 09:11:23

Resolution: fixed


---

Comment by mpatel created at 2010-09-28 09:28:16

Actually, I get a docbuild error:

```
docstring of sage.structure.sage_object.unpickle_all:39: (ERROR/3) Unknown interpreted text role "cls".
```

I've unmerged the patch.


---

Comment by mpatel created at 2010-09-28 09:28:16

Changing status from closed to needs_work.


---

Attachment


---

Comment by nthiery created at 2010-10-13 20:10:06

Replying to [comment:5 mpatel]:
> Actually, I get a docbuild error:
> {{{
> docstring of sage.structure.sage_object.unpickle_all:39: (ERROR/3) Unknown interpreted text role "cls".
> }}}
> I've unmerged the patch.

Argl; Florent had actually already fixed this, but I forgot to upload the updated version of the patch. Since the only difference between the two patches is the cls -> class change, I am allowing myself to revert back the status to positive review.


---

Comment by nthiery created at 2010-10-13 20:10:06

Changing status from needs_work to positive_review.

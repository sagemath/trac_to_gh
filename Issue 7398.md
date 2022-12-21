# Issue 7398: Improved mantra to find whether an object is iterable (and get an iterator out it)

Issue created by migration from Trac.

Original creator: nthiery

Original creation time: 2009-11-05 18:15:27

Assignee: hivert

CC:  sage-combinat was

Keywords: iterators

The following mantra occurs at three places in Sage's code to test whether v is an iterator:

     if hasattr(v, 'next'):

This patches replaces them with:

     if hasattr(v, '__iter__')

which is safer (some sage objects have a next method without being iterable, or with a different semantic)

if not just, when appropriate:

     v = iter(v)


---

Comment by hivert created at 2009-11-05 22:47:31

Changing status from new to needs_review.


---

Attachment


---

Attachment

Updated patch after review by Nicolas (uses itertools to simplify further  sage.server.interact.list_of_first_n)


---

Comment by nthiery created at 2009-11-06 14:00:14

William: this makes a small edit to sage.server.notebook.interact.list_of_first_n

You may want to check/backport to the notebook code


---

Comment by nthiery created at 2009-11-06 14:00:14

Changing keywords from "iterators" to "iterators, itertools".


---

Comment by nthiery created at 2009-11-06 14:00:14

Changing status from needs_review to positive_review.


---

Comment by hivert created at 2009-11-06 21:10:46

The given patch actually breaks somme code... I'm uploading a new one.


---

Comment by hivert created at 2009-11-06 21:10:46

Changing status from positive_review to needs_work.


---

Comment by hivert created at 2009-11-06 21:15:51

Changing status from needs_work to needs_review.


---

Attachment

Nicolas : can you re-review this patch...
I commented out some line saying that it was never user and actually is was quite a lot... I don't understand why we didn't caught it by the tests. Anyway, Massena did.

Sorry for the mess,

Florent


---

Attachment


---

Comment by hivert created at 2009-11-09 16:35:43

The patch trac_7398_iter_detect-fh.3.patch broke something in graph_generators. 
the patch trac_7398_combclass_set_compat-fh.patch should fix it. 

Apply those two patches in that order.

Cheers,

Florent


---

Comment by nthiery created at 2009-11-09 17:19:57

Changing status from needs_review to positive_review.


---

Comment by mhansen created at 2009-11-12 06:21:27

Resolution: fixed

# Issue 9651: Addition on CombinatorialFreeModule directly on dictionaries

Issue created by migration from Trac.

Original creator: stumpc5

Original creation time: 2010-07-31 18:23:15

Assignee: sage-combinat

Keywords: addition of dictionaries, CombinatorialFreeModule

At the moment, adding (and taking negative, substracting,...) for CombinatorialFreeModule is not done in a very efficient way.

This patch

- provides a cythonized version of a pointwise addition of dictionaries, together with multiple options

- uses this addition of dictionaries to provide fast methods for CombinatorialFreeModule

- is (indirectly) based on the patch in Ticket #9648


---

Attachment

The patch still needs some doctesting (I have not yet done much, but will do more these days) - in particular, I modified CombinatorialFreeModule._apply_module_morphism and .apply_module_endomorphism. The first method is used in the code for symmetric functions: powersum.py, sfa.py and macdonald.py. Would be nice if someone could check if everything there still works well.

Thx, Christian


---

Comment by stumpc5 created at 2010-07-31 18:40:02

Changing status from new to needs_review.


---

Comment by bump created at 2010-09-06 17:02:20

The patch doesn't apply cleanly to sage-4.5.3.rc0. Applying #9648 first doesn't help.


---

Attachment


---

Comment by bump created at 2010-09-22 00:14:43

The revised patch trac_9651_CombinatorialFreeModule_Addition-cs.patch
applies cleanly to sage 4.6.alpha1 and passes all tests.

But I haven't been able to confirm that it is a speedup. The results
of some testing are here:

http://groups.google.com/group/sage-combinat-devel/msg/4869cc885ca42bc1


---

Attachment


---

Comment by stumpc5 created at 2010-10-20 13:25:39

includes referees suggestions


---

Attachment

includes more referees suggestions


---

Comment by bump created at 2010-10-20 23:42:19

Changing status from needs_review to positive_review.


---

Comment by bump created at 2010-10-20 23:42:19

Positive review!

There is a thread about this patch in sage-combinat-devel
resulting in the latest version.

I tested this with sage-4.6.alpha3. After applying

```
trac_9648_modulemorphism_codomain_extension.2.patch 
trac_9651_CombinatorialFreeModule_Addition-cs.4.patch
```

all tests pass. I also confirmed that the test is a speedup.


---

Comment by jdemeyer created at 2010-10-23 12:23:58

Changing status from positive_review to needs_work.


---

Comment by jdemeyer created at 2010-10-23 12:23:58

Please remove * * * from the commit message


---

Attachment

Replying to [comment:6 jdemeyer]:
> Please remove * * * from the commit message

done!


---

Comment by stumpc5 created at 2010-10-23 17:04:22

Changing status from needs_work to positive_review.


---

Comment by jdemeyer created at 2010-11-01 10:09:06

Resolution: fixed

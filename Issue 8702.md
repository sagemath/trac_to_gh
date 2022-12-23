# Issue 8702: Datastructure for objects with prototype (clone) design pattern.

Issue created by migration from https://trac.sagemath.org/ticket/8702

Original creator: hivert

Original creation time: 2010-04-17 09:32:15

Assignee: hivert

CC:  novoselt mhansen sage-combinat

This is the future Cython replacement for CombinatorialObject. 

Patch in preparation in sage-combinat queue


---

Comment by hivert created at 2010-06-10 17:26:45

Changing status from new to needs_review.


---

Comment by novoselt created at 2010-06-10 19:04:53

Changing type from defect to enhancement.


---

Comment by hivert created at 2010-10-24 09:33:56

Hi mike,

I adressed your comment:

> 2. Is there a good use case for allowing None to be passed in to
> ClonableArray, ClonableList, and ConableIntArray.  There is a bit of
> mental overhead in always having to remember to check that self._list
> is always an actual list.

and updated a new patch... Please review.


---

Comment by hivert created at 2010-10-24 09:36:14

> and updated a new patch... Please review.

Sorry: I should have said that I also folded your review patch... Thanks for it.


---

Comment by mhansen created at 2010-11-04 04:53:02

Looks good to me.


---

Comment by mhansen created at 2010-11-04 04:53:02

Changing status from needs_review to positive_review.


---

Comment by hivert created at 2010-11-04 19:47:03

Replying to [comment:6 mhansen]:
> Looks good to me.

Thanks for the review !


---

Comment by jdemeyer created at 2010-11-06 07:23:05

I get doctest errors:

```
**********************************************************************
File "/mnt/usb1/scratch/jdemeyer/merger/sage-4.6.1.alpha1/devel/sage-main/sage/structure/list_clone_timings.py", line 8:
    sage: from sage.structure.list_clone_timmings import *
Exception raised:
    Traceback (most recent call last):
      File "/mnt/usb1/scratch/jdemeyer/merger/sage-4.6.1.alpha1/local/bin/ncadoctest.py", line 1231, in run_one_test
        self.run_one_example(test, example, filename, compileflags)
      File "/mnt/usb1/scratch/jdemeyer/merger/sage-4.6.1.alpha1/local/bin/sagedoctest.py", line 38, in run_one_example
        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)
      File "/mnt/usb1/scratch/jdemeyer/merger/sage-4.6.1.alpha1/local/bin/ncadoctest.py", line 1172, in run_one_example
        compileflags, 1) in test.globs
      File "<doctest __main__.example_0[2]>", line 1, in <module>
        from sage.structure.list_clone_timmings import *###line 8:
    sage: from sage.structure.list_clone_timmings import *
    ImportError: No module named list_clone_timmings
**********************************************************************
```



---

Comment by jdemeyer created at 2010-11-06 07:23:05

Changing status from positive_review to needs_work.


---

Attachment


---

Comment by hivert created at 2010-11-19 08:59:16

Changing status from needs_work to needs_review.


---

Comment by hivert created at 2010-11-19 08:59:16

Replying to [comment:8 jdemeyer]:
> I get doctest errors:

```
**********************************************************************
File "/mnt/usb1/scratch/jdemeyer/merger/sage-4.6.1.alpha1/devel/sage-main/sage/structure/list_clone_timings.py", line 8:
    sage: from sage.structure.list_clone_timmings import *
[...]
```


Oups ! I forgot to fold some corrective patches. I just resubmitted the corrected version. To ease the review I also uploaded the [diff](http://trac.sagemath.org/sage_trac/attachment/ticket/8702/diff-8702) between the older version and the new one. Do not apply this chunk of code.

Only apply [trac_8702-list_clone-fh.patch](http://trac.sagemath.org/sage_trac/attachment/ticket/8702/trac_8702-list_clone-fh.patch)


---

Attachment


---

Comment by hivert created at 2010-11-19 09:58:24

Added a missing utf8 tag on the file `list_clone_timings.py`... 

Apply only [trac_8702-list_clone-fh.2.patch](http://trac.sagemath.org/sage_trac/attachment/ticket/8702/trac_8702-list_clone-fh.2.patch)


---

Attachment

Oops ! I forgot to add Copyright notices... Sorry for the mess.

Apply only [trac_8702-list_clone-fh.patch](http://trac.sagemath.org/sage_trac/attachment/ticket/8702/trac_8702-list_clone-fh.patch)


---

Comment by nthiery created at 2010-11-19 10:13:28

Changing status from needs_review to positive_review.


---

Comment by jdemeyer created at 2011-01-12 06:31:33

Resolution: fixed

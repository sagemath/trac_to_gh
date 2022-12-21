# Issue 9599: re-merge #1396 and insure that Sage starts on t2.math

Issue created by migration from Trac.

Original creator: ddrake

Original creation time: 2010-07-26 08:14:06

Assignee: drkirkby

CC:  wjp simonking malb jhpalmieri

A patch at #1396 was merged in 4.5.2.alpha0, but that caused Sage to segfault when starting on t2.math. That ticket was backed out in 4.5.2.alpha1, and should be re-merged. See #9583 for discussion.


---

Comment by wjp created at 2010-07-26 08:33:15

To summarize the lengthy discussion on #9583:

#1396 exposed a symbol clash between Singular and Pari with some linkers.

To fix this, we rename Singular's `mu` to `Kstd1_mu`. This could be done either with the SPKG at #9583 which changes only this, or with the SPKG at #8059 which upgrades Singular to a new version that includes the renamed `mu`.


---

Comment by malb created at 2010-07-28 12:17:25

See

 http://groups.google.com/group/libsingular-devel/browse_thread/thread/e49fe19e034ec774

for upstream's reaction.


---

Comment by malb created at 2011-01-08 15:19:05

Changing status from new to needs_review.


---

Comment by malb created at 2011-01-08 15:19:35

The rebased patch passes doctests for me. It still needs testing on t2.


---

Comment by malb created at 2011-01-13 09:34:56

Changing status from needs_review to positive_review.


---

Comment by malb created at 2011-01-13 09:34:56

The patch applies fine to 4.6.1.rc1 and doctests pass on t2, except:


```
sage -t  -long -force_lib devel/sage/sage/tests/cmdline.py # 19 doctests failed, timeouts
sage -t  -long -force_lib devel/sage/sage/parallel/decorate.py # 1 doctests failed, OSError: [Errno 12] Not enough space
sage -t  -long -force_lib devel/sage/sage/misc/trace.py # 2 doctests failed, 
```


These don't seem related to this patch.

The patch did have a positive review before and the only issue was a SIGSEGV on startup on t2. I'll thus set this patch to a positive review.


---

Comment by jdemeyer created at 2011-01-23 20:31:54

Is there a reason the milestone is sage-5.0?


---

Comment by malb created at 2011-01-23 21:27:24

No :)


---

Comment by jdemeyer created at 2011-01-26 18:39:40

The commit message will have to be changed to reflect number, also you should split it over multiple lines if it's that long (but make sure the first line makes sense by itself).


---

Attachment


---

Comment by malb created at 2011-01-26 20:24:33

done


---

Comment by jdemeyer created at 2011-01-27 13:14:39

Resolution: fixed

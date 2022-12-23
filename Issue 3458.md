# Issue 3458: parallel -- a very simple reference api for @parallel and parallel_eval

Issue created by migration from https://trac.sagemath.org/ticket/3458

Original creator: was

Original creation time: 2008-06-18 03:14:08

Assignee: yi




---

Attachment

This depends on #3453.


---

Attachment


---

Attachment


---

Comment by was created at 2008-06-19 00:53:50

first three patches have positive review


---

Attachment


---

Comment by was created at 2008-06-19 01:35:27

Example test function:


```
def MS1(N,k):
    return ModularSymbols(N,k,sign=1).decomposition(10)[0]
```


Typical inputs:

```
time v = MS1([(250,2), (11,2), (37,2)])
```



---

Attachment


---

Comment by yi created at 2008-06-19 21:12:24

patch 3 should not be used anymore since the p_iter implementation is in 

```
sage.dsage.interface.parallel_iter
```



---

Comment by gfurnish created at 2008-06-19 23:20:34

patch 3 should still be applied since it changes things other then dsage.


---

Attachment


---

Comment by yi created at 2008-06-20 20:25:39

Patch 6 does not apply for me after having applied the first 5 patches. Specifically, decorate.py, ncpus.py and multiprocessing.py result in .rej's. Can you post plain copies of those files?


---

Comment by was created at 2008-06-21 23:53:08

This is a clean bundle that one can apply instead of all the patches.


---

Attachment

Yi: bundle posted.


---

Comment by yi created at 2008-06-23 20:04:34

Updated bundle which uses sage.dsage.interface.dsage_interface.BlockingDSage's parallel_iter instead of the one supplied in the bundle. This will only work after #3467 gets merged in.


---

Attachment


---

Comment by was created at 2008-06-24 03:04:45

Changing keywords from "" to "editor_wstein".


---

Comment by yi created at 2008-06-26 02:48:37

Patch looks great. Doctests pass on 3.0.3 OS X 10.5.


---

Comment by mabshoff created at 2008-06-26 04:22:19

Merged sage-3458-fixed.hg in Sage 3.0.4.alpha1


---

Comment by mabshoff created at 2008-06-26 04:22:19

Resolution: fixed

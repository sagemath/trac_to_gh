# Issue 6599: hidden markov models are completely broken on OS X 64-bit

Issue created by migration from Trac.

Original creator: was

Original creation time: 2009-07-23 10:12:26

Assignee: tbd


```
was`@`bsd:~/build/64bit/sage-4.1.rc1$ ./sage
----------------------------------------------------------------------
----------------------------------------------------------------------
sage: A  = [[0.5,0.5],[0.5,0.5]]
sage: B  = [[(0.5,(0.0,1.0)), (0.1,(1,10000))],[(1,(1,1)), (0,(0,0.1))]]
sage: pi = [1,0]
sage: hmm.GaussianMixtureHiddenMarkovModel(A, B, pi)
| Sage Version 4.1, Release Date: 2009-07-09                         |
| Type notebook() for the GUI, and license() for information.        |
------------------------------------------------------------
Unhandled SIGSEGV: A segmentation fault occured in SAGE.
This probably occured because a *compiled* component
of SAGE has a bug in it (typically accessing invalid memory)
or is not properly wrapped with _sig_on, _sig_off.
You might want to run SAGE under gdb with 'sage -gdb' to debug this.
SAGE will now terminate (sorry).
------------------------------------------------------------

```


Note that a long time ago we stupidly turned off doctesting of HMM's so that tests would pass on itanium.  We were lazy and never turned them back on, which is why this never got caught before. 


---

Comment by chapoton created at 2018-04-30 12:29:27

Changing status from new to needs_review.


---

Comment by chapoton created at 2018-04-30 12:29:27

There are plenty of tests in sage/stats/hmm/hmm.pyx.

Let us close that old one.


---

Comment by mmezzarobba created at 2018-06-01 12:36:42

Changing status from needs_review to positive_review.


---

Comment by embray created at 2019-02-26 13:58:00

Resolution: invalid


---

Comment by embray created at 2019-02-26 13:58:00

Presuming these are all correctly reviewed as either duplicate, invalid, or wontfix.

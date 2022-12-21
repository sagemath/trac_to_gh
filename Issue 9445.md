# Issue 9445: GalRep.non_surjective_primes() returns unexpected errors

Issue created by migration from Trac.

Original creator: justin

Original creation time: 2010-07-07 05:43:03

Assignee: cremona

It's possible these are related.  In tests of 4.5.a4, the following doctests fail:

1)       File "wrapper.pyx", line 171, in sage.libs.galrep.wrapper.GalRep.non_surjective_primes (sage/libs/galrep/wrapper.c:2602)
    ValueError: min and max must be <= 59

2) File "/Users/Sage/sage-4.5.alpha4/devel/sage/sage/libs/galrep/wrapper.pyx", line 163:
    sage: galrep.GalRep().non_surjective_primes(-432,8208,7,59)
Expected:
    []
Got:
    [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59]

Seems to be a failure on Mac OS X, 10.5.8, and has not been reported elsewhere.




---

Comment by drkirkby created at 2010-07-13 14:54:00

I did not notice this ticket, but this is giving a different error on a Solaris 10 system (t2.math). See #9490. It's basically crashing:


```
sage -t -long "devel/sage/sage/libs/galrep/wrapper.pyx"     


------------------------------------------------------------
Unhandled SIGBUS: A bus error occurred in Sage.
This probably occurred because a *compiled* component
of Sage has a bug in it (typically accessing invalid memory)
or is not properly wrapped with _sig_on, _sig_off.
You might want to run Sage under gdb with 'sage -gdb' to debug this.
Sage will now terminate (sorry).
------------------------------------------------------------


	 [18.0 s]
 
----------------------------------------------------------------------
The following tests failed:


	sage -t -long "devel/sage/sage/libs/galrep/wrapper.pyx"
Total time for all tests: 18.0 seconds
```


I guess this was tested on Linux!

Dave


---

Comment by rlm created at 2010-07-14 18:32:33

Changing priority from blocker to major.


---

Comment by rlm created at 2010-07-14 18:32:33

Remove blocker status since galrep was reverted.


---

Comment by rlm created at 2010-11-10 14:01:53

In fact, I'm closing the ticket since galrep was never added to Sage. This ticket will still be here to demonstrate the current problems...


---

Comment by rlm created at 2010-11-10 14:01:53

Resolution: fixed

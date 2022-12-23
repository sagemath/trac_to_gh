# Issue 9127: BSD.py doctest failure due to timeout of Heegner index computation.

Issue created by migration from https://trac.sagemath.org/ticket/9127

Original creator: drkirkby

Original creation time: 2010-06-03 12:39:49

Assignee: cremona

CC:  robertwb rlm was jhpalmieri

This failure seems remarkably close to #8749, which is closed as fixed, but this is the same sort of problem on the same doctest. Note, changing SAGE_TIMOUT will not change this, as it appears (to me at least), Sage is switching from one algorithm to another in a time which is independent of the processor speed or settings of any timeout variables. 

## Hardware & associated software

 * Sun Blade 1000
 * 2 x 900 MHz UltraSPARC III+ CPUs
 * 2 GB RAM
 * Solaris 10 03/2005 (first release of Solaris 10)
 * gcc 4.4.3 (uses Sun linker and assembler)

 == Sage version ==
 * 4.4.3.alpha0 and 4.4.3.alpha1
 
 == The test failure ==
A full log of all tests can be found at

http://boxen.math.washington.edu/home/kirkby/sage-4.4.3.alpha0-Sun-Blade-1000-900MHz-Solaris-10-ptestlong.log.gz

(There are 3 failures, but I believe the other two are common to more than one platform and work is progressing on them)

I would expect to see this fail the same way on 't2' as 't2' is slower on single threaded tasks than the Blade 1000. 


```
sage -t  -long devel/sage/sage/schemes/elliptic_curves/BSD.py
**********************************************************************
File "/export/home/drkirkby/sage-4.4.3.alpha1/devel/sage-main/sage/schemes/elliptic_curves/BSD.py", line 377:
    sage: E.prove_BSD(verbosity=2)               # long time
Expected:
    p = 2: True by 2-descent...
    True for p not in {2, 3} by Kolyvagin.
    ALERT: p = 3 left in Kolyvagin bound
        0 <= ord_p(#Sha) <= 2
        ord_p(#Sha_an) = 2
    Remaining primes:
    p = 3: irreducible, surjective, non-split multiplicative
        (0 <= ord_p <= 2)
    [3]
Got:
    p = 2: True by 2-descent
    Timeout stopped Heegner index computation...
    Proceeding to use heegner_index_bound instead.
    True for p not in {2, 3} by Kolyvagin.
    p = 3 may divide the Heegner index, for which only a bound was computed.
    ALERT: p = 3 left in Kolyvagin bound
        0 <= ord_p(#Sha) <= 2
        ord_p(#Sha_an) = 2
    Remaining primes:
    p = 3: irreducible, surjective, non-split multiplicative
        (0 <= ord_p <= 2)
    [3]
**********************************************************************
1 items had failures:
   1 of  35 in __main__.example_6
***Test Failed*** 1 failures.
For whitespace errors, see the file /export/home/drkirkby/.sage//tmp/.doctest_BSD.py
         [132.1 s]
```





---

Comment by rlm created at 2010-06-03 17:33:32

Changing status from new to needs_review.


---

Comment by cremona created at 2010-06-05 14:47:56

Changing status from needs_review to needs_work.


---

Comment by cremona created at 2010-06-05 14:47:56

This one confuses me.  Before I apply the patch, the file passes long tests for me (ubuntu 64-bit, on 4.4.3).  But after the patch it does not:

```
sage -t -long "sage/schemes/elliptic_curves/BSD.py"         
**********************************************************************
File "/storage/jec/sage-4.4.3/devel/sage-tests/sage/schemes/elliptic_curves/BSD.py", line 377:
    sage: E.prove_BSD(verbosity=2)               # long time
Expected:
    p = 2: True by 2-descent
    ...
    True for p not in {2, 3} by Kolyvagin.
    ...
    ALERT: p = 3 left in Kolyvagin bound
        0 <= ord_p(#Sha) <= 2
        ord_p(#Sha_an) = 2
    Remaining primes:
    p = 3: irreducible, surjective, non-split multiplicative
        (0 <= ord_p <= 2)
    [3]
Got:
    p = 2: True by 2-descent
    True for p not in {2, 3} by Kolyvagin.
    ALERT: p = 3 left in Kolyvagin bound
        0 <= ord_p(#Sha) <= 2
        ord_p(#Sha_an) = 2
    Remaining primes:
    p = 3: irreducible, surjective, non-split multiplicative
        (0 <= ord_p <= 2)
    [3]
**********************************************************************
```


So whether or not the patch fixes things on some systems, it breaks others, so cannot be included.


---

Attachment


---

Comment by rlm created at 2010-06-05 15:02:44

Changing status from needs_work to needs_review.


---

Comment by drkirkby created at 2010-06-05 17:06:38

The patch results in the test passing on the Sun Blade 1000 where the test originally failed. 


```
drkirkby@redstart:~/sage-4.4.3.alpha3$ ./sage -t  -long devel/sage/sage/schemes/elliptic_curves/BSD.py
sage -t -long "devel/sage/sage/schemes/elliptic_curves/BSD.py"
         [135.0 s]
 
----------------------------------------------------------------------
All tests passed!
Total time for all tests: 135.0 seconds
```


I would be tempted to give it a positive review, though the fact John had a problem, it would be wise to wait and see if he has any further comments. But the changes look OK to me and it solves the problem. 

Dave


---

Comment by drkirkby created at 2010-06-05 17:06:38

Changing assignee from cremona to drkirkby.


---

Comment by drkirkby created at 2010-06-05 17:07:06

Changing assignee from drkirkby to cremona.


---

Comment by drkirkby created at 2010-06-05 19:34:48

Once this issue is resolved (and it looks like it will be very soon), #8409 can be closed. 

Dave


---

Comment by rlm created at 2010-06-07 12:09:06

Replying to [comment:6 drkirkby]:
> I would be tempted to give it a positive review, though the fact John had a problem, it would be wise to wait and see if he has any further comments. But the changes look OK to me and it solves the problem. 
> 
> Dave 

I think all of the issues with this ticket have been resolved.


---

Comment by drkirkby created at 2010-06-07 12:46:11

In which case, positive review. I'm happy with it.


---

Comment by drkirkby created at 2010-06-07 12:46:11

Changing status from needs_review to positive_review.


---

Comment by cremona created at 2010-06-07 13:34:49

I am happy.  (I thought I had reviewed the new patch, but maybe I was dreaming!)


---

Comment by mhansen created at 2010-06-09 02:28:08

Resolution: fixed

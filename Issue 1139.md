# Issue 1139: nintegral fails for large precision (version 2.8.12)

Issue created by migration from https://trac.sagemath.org/ticket/1139

Original creator: zimmerma

Original creation time: 2007-11-10 15:39:07

Assignee: jkantor


```
sage: f=x
sage: f.nintegral(x,0,1,1e-14)
Maxima ERROR:
         ***MESSAGE FROM ROUTINE DQAGS IN LIBRARY SLATEC.
 ***POTENTIALLY RECOVERABLE ERROR, PROG ABORTED, TRACEBACK REQUESTED
 *  ABNORMAL RETURN
 *  ERROR NUMBER = 6
 *   
 ***END OF MESSAGE
 
 ***JOB ABORT DUE TO UNRECOVERED ERROR.
0          ERROR MESSAGE SUMMARY
 LIBRARY    SUBROUTINE MESSAGE START             NERR     LEVEL     COUNT
 SLATEC     DQAGS      ABNORMAL RETURN              6         1         2
```



---

Comment by mhansen created at 2007-12-06 21:00:14

This is due to a restriction in QUADPACK (which Maxima is using).


```
c                     and epsrel.lt.max(50*rel.mach.acc.,0.5d-28),
c                     the routine will end with ier = 6.
```


The exception should be caught, and a more helpful error should be raised.


---

Comment by mhansen created at 2007-12-06 21:00:14

Changing assignee from jkantor to mhansen.


---

Comment by mhansen created at 2007-12-06 21:00:14

Changing status from new to assigned.


---

Attachment


---

Comment by mhansen created at 2007-12-06 22:00:40

Patch attached.  Apply after #553 .


---

Comment by was created at 2007-12-15 10:32:23

p


---

Comment by rlm created at 2007-12-17 22:14:03

Merged in 2.9.1.alpha1


---

Comment by rlm created at 2007-12-17 22:14:03

Resolution: fixed

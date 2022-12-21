# Issue 4181: Mysterious error somewhat related to 16-Bit signed integers on Mac OS X

Issue created by migration from Trac.

Original creator: GeorgSWeber

Original creation time: 2008-09-23 22:25:28

Assignee: somebody

On both my Mac OS X 10.4 / Xcode 25 boxes, one Intel and one PPC, the following Sage code runs through fine (hit return twice):

sage: for p in prime_range(32768, 100000):  EllipticCurve(GF(p),[0,1,1,10,13]) 

Please note that the length of the interval is almost 70000, so quite some primes are involved.
But if the startpoint of the range is lower the 32768, then Sage crashes, e.g. for:

sage: for p in prime_range(31300, 32600):  EllipticCurve(GF(p),[0,1,1,10,13]) 

(note that the length of the interval is only 1300) one gets the following message with sage crashed:


error: no more memory
System 8672k:8672k Appl 8233k/438k Malloc 4030k/33k Valloc 4608k/404k Pages 1071/81 Regions 9:9

halt 14


The problem/bug can't be due to low physical RAM, or due to not enough virtual RAM for processes, since then the first line of code would have to crash, too. Which is not the case.

It is not related to the mathematical code, since if the length of the interval of primes is only 100 or less, the code runs fine for startpoints above and (!) below 32768.

The bug is triggered also if consecutively several small intervals (below 32768) are calculated, so it seems to be some caching / stack / heap / whatsoever related issue.
It does not seem to occur on platforms other than Mac (OS X 10.4 only?), so I put this under the "porting" issues.


---

Comment by mabshoff created at 2008-09-23 22:42:52

As expected nothing bad happen under valgrind on 64 bit, but I will take a closer look with valgrind running on a 32 bit Linux box. It seems too much of a coincidence to not be related to something close to `2^15-1` or thereabout.

Cheers,

Michael


---

Comment by GeorgSWeber created at 2008-11-15 22:03:38

Just for the record: once tis ticket is fixed, most probably #3760 will be resolved, too.


---

Comment by GeorgSWeber created at 2009-02-22 22:06:58

relies on #5344, apply after this patch after the patch there (to Singular spkg)


---

Comment by GeorgSWeber created at 2009-02-22 22:13:25

Changing priority from major to blocker.


---

Attachment

Well, what shall I say: apply the two patches (the one from #5344 and this one), and the long standing "long" doctest for "ell_finite_field.py" now succeeds on sage 3.3, finally:

```
sage -t -long "local/lib/python/site-packages/sage/schemes/elliptic_curves/ell_finite_field.py"
         [53.9 s]
 
----------------------------------------------------------------------
All tests passed!
Total time for all tests: 53.9 seconds
```


I'll test 666 rings (#3760) in a minute.

Cheers, gsw


---

Comment by mabshoff created at 2009-02-22 22:26:27

Changing priority from blocker to major.


---

Comment by mabshoff created at 2009-02-22 22:26:27

This will not work and has been tried before. Please do not repurpose tickets since this is not what this ticket is about, but open a new one in case the Singular.spkg needs to be changed. You did that at #5344, but then why change the subject of this ticket?

In general this is a dupe of #3760, so I am closing this as one :)

If you want a less messy ticket to switch to using 

Cheers,

Michael


---

Comment by mabshoff created at 2009-02-22 22:26:27

Resolution: duplicate


---

Comment by GeorgSWeber created at 2009-02-23 08:15:20

Sure, let's close dupes.


---

Comment by mabshoff created at 2009-02-23 08:46:58

Replying to [comment:6 GeorgSWeber]:
> Sure, let's close dupes.

Absolutely.

For the record: It only became clear two or maybe three days ago that all these problems on OSX were related to libSingular+mmap, so back in the day when this ticket was opened it was the correct way to do so.

Too bad this path series is being held up by the minpoly bug, but I am hoping someone will fix that issue soon, too.

Cheers,

Michael


---

Comment by mabshoff created at 2009-02-23 14:50:26

Hmm, we might need this patch after all, so we can either attach it to another ticket, i.e. #3760, or close that one as a dupe and reopen this one. I will test this patch now on a 32 bit OSX box, so let's wait and see for now.

The whole issue is spread out over too many tickets and has gotten pretty messy, so let's try to get this resolved :)

Cheers,

Michale


---

Comment by mabshoff created at 2009-02-23 18:46:17

Changing component from porting to packages.


---

Comment by mabshoff created at 2009-02-23 18:46:17

Changing priority from major to blocker.


---

Comment by mabshoff created at 2009-02-23 18:46:17

Ok, reopened and made a blocker against 3.4 again. I am now quite confident we will merge this :)

Cheers,

Michael


---

Comment by mabshoff created at 2009-02-23 22:47:57

Changing status from closed to reopened.


---

Comment by mabshoff created at 2009-02-23 22:47:57

Positive review. Build on OSX 32 bit, OSX 64 bit, FC 10 and also sage.math. I did valgrind the *entire* test suite on sage.math.

George's patch is integrated into 

http://sage.math.washington.edu/home/mabshoff/SPKG/singular-3-0-4-4-20080711.p4.spkg

Cheers,

Michael


---

Comment by mabshoff created at 2009-02-23 22:47:57

Resolution changed from duplicate to 


---

Comment by mabshoff created at 2009-02-24 19:38:08

Resolution: fixed


---

Comment by mabshoff created at 2009-02-24 19:38:08

Merged in Sage 3.4.alpha0.

Cheers,

Michael

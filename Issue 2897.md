# Issue 2897: [with new spkg] GAP: replace guava 3.4 by new and improved guava 3.4

Issue created by migration from Trac.

Original creator: wdj

Original creation time: 2008-04-12 14:42:49

Assignee: rlm

There was a small bug in the previous version of guava 3.4 which caused it to fail the (GAP) guava.tst file. This version is fixed. Also, some file permissions were "wrong" and those are fixed. The SPKG.txt file was updated. Other than these, the spkg is the same. It has been copied to 
http://sage.math.washington.edu/home/wdj/patches/gap-4.4.10.p6.spkg and was
tested using sage -f. Seems to work fine.


---

Comment by mabshoff created at 2008-04-12 16:00:17

Two issue: Somebody is moving back in time. 

```
### gap-4.4.10.p3 (David Joyner, March 30th, 2008)
 * replace guava 3.4 by guava 3.4 with fixed Makefile.in

### gap-4.4.10.p5 (Michael Abshoff, April 1st, 2008)
 * Debianize GAP spkg (Tim Abbott, #2756)
```

David, are you a terminator? ;)

The other thing is that the changes to SPKG.txt were not checked into the main spkg repo. The slightly updated spkg builds fine and passes doctests for me. Positive review.

Cheers,

Michael


---

Comment by mabshoff created at 2008-04-12 16:10:37

Resolution: fixed


---

Comment by mabshoff created at 2008-04-12 16:10:37

Merged in Sage 3.0.alpha4

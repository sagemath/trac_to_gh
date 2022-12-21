# Issue 7209: Make `sage -coverage` aware of TestSuite

Issue created by migration from Trac.

Original creator: nthiery

Original creation time: 2009-10-14 13:50:22

Assignee: nthiery

CC:  sage-combinat

With the attached patch, sage -coverage looks for either a loads/dumps test or TestSuite, and suggests using the later.


---

Comment by nthiery created at 2009-10-14 13:55:04

Changing status from new to needs_review.


---

Attachment


---

Comment by hivert created at 2009-10-19 19:50:54

With the new category framework there will be a lot of parent which will be tested by the testsuite machinery. It is very useful that sage-coverage stop complaining about missing `s == loads(dumps(s))` because it is done during
`TestSuite(s).run()`. The patch looks good and works. Positive review. 

Cheers,

Florent


---

Comment by hivert created at 2009-10-19 19:50:54

Changing keywords from "" to "TestSuite, coverage".


---

Comment by hivert created at 2009-10-19 19:50:54

Changing status from needs_review to positive_review.


---

Comment by jhpalmieri created at 2009-10-19 20:20:57

Notice that #5819 is somewhat related to this. It would be nice to fix that issue eventually...


---

Comment by hivert created at 2009-10-19 20:57:50

Replying to [comment:5 jhpalmieri]:
> Notice that #5819 is somewhat related to this. It would be nice to fix that issue eventually...

Sure. But right now our primary goal is to finish the category stuff ASAP...
I'm sorry for this but we really have to take the straight line :-)

Cheers,

Florent


---

Comment by mhansen created at 2009-10-21 04:01:53

Resolution: fixed

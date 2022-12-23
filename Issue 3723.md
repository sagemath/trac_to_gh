# Issue 3723: alarm doesn't work with the factor command on os x (but control c does)

Issue created by migration from https://trac.sagemath.org/ticket/3723

Original creator: was

Original creation time: 2008-07-25 10:45:37

Assignee: cwitty


```
teragon-2:~ was$ sage
----------------------------------------------------------------------
----------------------------------------------------------------------
Loading SAGE library. Current Mercurial branch is: review
sage: alarm(3); factor(2^997-1) 
| SAGE Version 3.0.5, Release Date: 2008-07-11                       |
| Type notebook() for the GUI, and license() for information.        |
#
# and I wait 10 seconds then hit control c
#

^C---------------------------------------------------------------------------
KeyboardInterrupt                         Traceback (most recent call last)

/Users/was/s/local/lib/python2.5/site-packages/sage/misc/misc.py in __mysig(a, b)
   1343 __alarm_time=0
   1344 def __mysig(a,b):
-> 1345     raise KeyboardInterrupt, "computation timed out because alarm was set for %s seconds"%__alarm_time
   1346 
   1347 def alarm(seconds):

KeyboardInterrupt: computation timed out because alarm was set for 3 seconds
sage: 
```



---

Comment by jdemeyer created at 2013-05-15 13:37:50

Changing status from new to needs_review.


---

Comment by jdemeyer created at 2013-05-15 13:37:50

Clearly duplicate of #13311.


---

Comment by jdemeyer created at 2013-05-15 13:37:58

Changing status from needs_review to positive_review.


---

Comment by jdemeyer created at 2013-05-16 07:33:38

Resolution: duplicate

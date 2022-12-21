# Issue 5237: qsieve hangs on some machines when doctesting book_stein_ent.py

Issue created by migration from Trac.

Original creator: mabshoff

Original creation time: 2009-02-11 22:56:54

Assignee: tbd

CC:  alexghitza

Reported in http://groups.google.com/group/sage-devel/browse_thread/thread/894d29e0bde4550c as well as once by Alex Ghitza:

```
Trying: 
    qsieve(n)###line 289:_sage_    : qsieve(n) 
Expecting: 
    ([6340271405786663791648052309, 
      46102313108592180286398757159], '') 
*** *** Error: TIMED OUT! PROCESS KILLED! *** *** 
*** *** Error: TIMED OUT! *** *** 
         [360.3 s] 
exit code: 1024 
```


This is Bill Hart's quadratic sieve, but an ancient version from 2007. We should really get rid of that code and use the current code in FLINT 1.1.x.

Cheers,

Michael


---

Comment by jdemeyer created at 2016-01-22 10:57:12

Changing status from new to needs_review.


---

Comment by jdemeyer created at 2016-01-22 10:57:12

I assume this very old ticket is no longer relevant.


---

Comment by jdemeyer created at 2016-01-22 10:57:16

Changing status from needs_review to positive_review.


---

Comment by vbraun created at 2016-02-23 22:52:58

Resolution: wontfix

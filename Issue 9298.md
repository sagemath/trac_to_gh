# Issue 9298: Memory leak in libsingular polynomial evaluation

Issue created by migration from https://trac.sagemath.org/ticket/9298

Original creator: robertwb

Original creation time: 2010-06-21 17:50:56

Assignee: tbd

CC:  polybori alexanderdreyer jpflori


```
sage: R.<A,B,C>=QQ[]
sage: print get_memory_usage()
180.0390625
sage: for i in xrange(10000): v = A(1,8,9) # leaks
....: 
sage: print get_memory_usage()
181.5390625
sage: for i in xrange(10000): v = A(1,8,9.0) # good
....: 
sage: print get_memory_usage()
181.5390625
sage: for i in xrange(10000): v = A(1/2,1/3,1/4) # leaks
....: 
sage: print get_memory_usage()
183.5390625
```



---

Comment by drkirkby created at 2010-08-10 18:40:26

There's a new version of Singular likely to be merged soon (#8059). I'd retest then.

Dave


---

Comment by Bouillaguet created at 2013-01-02 14:57:51

Indeed, the leak seems fixed. This ticket can be closed.


---

Comment by Bouillaguet created at 2013-01-02 14:57:51

Changing assignee from tbd to malb.


---

Comment by Bouillaguet created at 2013-01-02 14:58:09

Changing status from new to needs_review.


---

Comment by Bouillaguet created at 2013-01-04 13:42:26

Since the ticker cannot easily be doctested, and I cannot reproduce the leak, I suggest we close it.


---

Comment by Bouillaguet created at 2013-01-04 13:42:26

Changing status from needs_review to positive_review.


---

Comment by jdemeyer created at 2013-01-10 09:27:12

Resolution: worksforme

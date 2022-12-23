# Issue 7493: Implement sage -t --time

Issue created by migration from https://trac.sagemath.org/ticket/7493

Original creator: nthiery

Original creation time: 2009-11-19 11:22:25

Assignee: tbd

When a test file takes time to execute, it would be handy to have a quick overview of which specific tests take long. 

Something like:

```
    sage -t --verbose --time bla.py
    Trying: 
        1+1
    Expecting:
        2
    ok [0.1ms]
    Trying: 
        factor(....)
    Expecting:
        ...
    ok [10s] warning: please use # long time
    Trying: 
        factor(.....) # long time
    Expecting:
        ...
    ok [10s]
    Trying: 
        factor(........)
    Expecting:
        ...
    ok [300s] warning: this is too long!
```


And in non verbose mode:


```
    sage -t --time bla.py
    Warning: factor(....) line 30 takes 10s: please use # long time
    Warning: factor(........) line 50 takes 300s: this is too long!
```




---

Comment by nthiery created at 2010-01-20 10:30:42

Here is a patch which sorts of do the job. It is not intended to be merged, but to make you crave enough for the feature to actually implement it right:

```
zephyr-~s/categories>sage -t -time coxeter_groups.py    
sage -t -time "4.3/devel/sage-combinat/sage/categories/coxeter_groups.py"
...
File "/opt/sage-4.3/devel/sage-combinat/sage/categories/coxeter_groups.py", line 1010:
    sage: for u in P4:
          for v in P4:
              assert u.bruhat_lequal(v) == P4toW(u).bruhat_le(P4toW(v))
Expected nothing
Got:
    Warning: test took 8.1s > 1s. Please use # long time
Total time for all tests: 24.0 seconds
```



---

Comment by AlexGhitza created at 2010-01-23 22:50:50

Nicolas, can you actually attach your toy patch to this ticket?  I've now been in a few situations where I'm staring at the output of sage -t -verbose, and having *anything* automated for this would be a great help to my sanity.


---

Attachment


---

Comment by nthiery created at 2010-01-23 23:01:01

Replying to [comment:2 AlexGhitza]:
> Nicolas, can you actually attach your toy patch to this ticket?  I've now been in a few situations where I'm staring at the output of sage -t -verbose, and having *anything* automated for this would be a great help to my sanity.

Oops, there it is.

Eh eh, maybe my strategy is going to work :-)


---

Comment by jdemeyer created at 2013-02-22 21:35:59

Resolution: duplicate


---

Comment by jdemeyer created at 2013-02-22 21:35:59

This is essentially all implemented in #12415.

# Issue 6652: should not have algebra structure on streams

Issue created by migration from Trac.

Original creator: hemmecke

Original creation time: 2009-07-28 22:35:30

Assignee: mhansen

CC:  sage-combinat

combinat/species/stream.py has its origin in

```
svn cat svn://svn.risc.uni-linz.ac.at/hemmecke/combinat/trunk/combinat/src/stream.as.nw
```

I designed the original Aldor domain `DataStream` as a container being an equivalent of an infinite array. Since the Stream can contain any objects, it makes no sense for the stream to provide a `__mul__` and `__add__` method. Any algebraic operations should be defined in a derived class.

Suggestion: Remove `__add__`, `__mul__`, `_times_naive`, `stretch` and `_stretch_gen` from stream.py and put them into a more appropriate place in the class hierarchy.


---

Comment by hemmecke created at 2009-07-29 11:44:35

Changing assignee from mhansen to hemmecke.


---

Comment by hemmecke created at 2009-07-29 11:44:35

Changing status from new to assigned.


---

Attachment


---

Comment by hivert created at 2009-07-29 12:26:40

Changing keywords from "" to "stream".


---

Comment by hivert created at 2009-09-11 15:33:06

The deleted code is completely redundant with some code in `generating_series.py`. 
It is never used, and the design says that it must go in generating series. Therefore, 
I agree with Ralf that it should be deleted !

Positive review. 

Florent


---

Comment by mvngu created at 2009-09-11 16:52:15

Resolution: fixed

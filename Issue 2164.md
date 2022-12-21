# Issue 2164: add fast iterator for partitions

Issue created by migration from Trac.

Original creator: mhansen

Original creation time: 2008-02-14 23:15:56

Assignee: mhansen

CC:  sage-combinat

which only returns lists rather than Partition_class objects.


This is also useful where you don't necessarily need the Partition_class object, you just need the values.


Before the patch:

```
sage: timeit a = Partitions(40).list()
10 loops, best of 3: 1.4 s per loop
```


After the patch:

```
sage: timeit a = Partitions(40).list()
10 loops, best of 3: 280 ms per loop
```



---

Attachment


---

Comment by mhansen created at 2008-02-14 23:19:07

Changing status from new to assigned.


---

Attachment


---

Comment by mhansen created at 2008-02-14 23:53:23

Apply both patches.


---

Comment by ncalexan created at 2008-02-15 03:39:38

Looks fine to me.


---

Comment by ncalexan created at 2008-02-15 03:39:38

Changing type from defect to enhancement.


---

Comment by mabshoff created at 2008-02-15 05:00:45

Resolution: fixed


---

Comment by mabshoff created at 2008-02-15 05:00:45

Merged in Sage 2.10.2.alpha0

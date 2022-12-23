# Issue 907: [with patch] fix small memory leak in modn_sparse_lift

Issue created by migration from https://trac.sagemath.org/ticket/907

Original creator: mabshoff

Original creation time: 2007-10-16 04:55:03

Assignee: mabshoff

Running

```
for n in range(10,100):
   a=ModularSymbols(n,sign=1).decomposition(); print n, get_memory_usage()
```

Before (with the other memleak patches tagged for 2.8.8):

```
==15147== LEAK SUMMARY:
==15147==    definitely lost: 1,072,216 bytes in 96,412 blocks.
==15147==    indirectly lost: 419,120 bytes in 7,205 blocks.
==15147==      possibly lost: 376,558 bytes in 1,194 blocks.
==15147==    still reachable: 92,977,412 bytes in 1,342,343 blocks.
==15147==         suppressed: 0 bytes in 0 blocks.
```

With the patch:

```
==22935== LEAK SUMMARY:
==22935==    definitely lost: 1,071,084 bytes in 88,923 blocks.
==22935==    indirectly lost: 408,752 bytes in 7,166 blocks.
==22935==      possibly lost: 379,454 bytes in 1,197 blocks.
==22935==    still reachable: 92,968,751 bytes in 1,342,412 blocks.
==22935==         suppressed: 0 bytes in 0 blocks.
```


Every byte counts!

Cheers,

Michael


---

Comment by mabshoff created at 2007-10-16 04:55:10

Changing status from new to assigned.


---

Attachment


---

Comment by was created at 2007-10-20 19:18:48

Resolution: fixed

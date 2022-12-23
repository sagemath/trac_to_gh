# Issue 3150: Memory leak in combinat/matrices/dancing_links.pyx

Issue created by migration from https://trac.sagemath.org/ticket/3150

Original creator: carlohamalainen

Original creation time: 2008-05-10 19:10:02

Assignee: carlohamalainen

CC:  sage-combinat

The wrapper for the C++ class dancing_links in dancing_links.pyx does not deallocate all memory resulting in a leak.


Running valgrind on dlxcpp.py:


```
==23234== LEAK SUMMARY:
==23234==    definitely lost: 64 bytes in 2 blocks.
==23234==    indirectly lost: 368 bytes in 12 blocks.
==23234==      possibly lost: 201,979 bytes in 708 blocks.
==23234==    still reachable: 28,370,716 bytes in 19,122 blocks.
==23234==         suppressed: 0 bytes in 0 blocks.
```


After applying the patch:


```
==26826== LEAK SUMMARY:
==26826==    definitely lost: 0 bytes in 0 blocks.
==26826==      possibly lost: 202,323 bytes in 709 blocks.
==26826==    still reachable: 28,370,372 bytes in 19,121 blocks.
==26826==         suppressed: 0 bytes in 0 blocks.
```


As another test I ran the following Sage program and watched the memory usage in top. Before the memory usage of the python process would grow rapidly, with the patch it seems to stabilise quickly (about 10% memory on my 2Gb laptop).


```
from sage.combinat.matrices.dancing_links import dlx_solver

rows = [[0,1,2]]
rows+= [[0,2]]
rows+= [[1]]
rows+= [[3]]

for _ in range(10000000):
    x = sage.combinat.matrices.dancing_links.dlx_solver(rows) 
    x.search()
```




---

Attachment


---

Comment by rlm created at 2008-05-10 21:48:35

I haven't done doctests with this patch, but I'm familiar with this file, and it looks right. Tom Boothby should probably confirm.


---

Comment by mabshoff created at 2008-05-11 10:30:53

The patch is good and valgrinds clean to me. I am doctesting with only that patch applied to make sure everything still works, so if nothing pops up it will be merged :)

Cheers,

Michael


---

Comment by mabshoff created at 2008-05-11 10:44:47

Resolution: fixed


---

Comment by mabshoff created at 2008-05-11 10:44:47

Merged in Sage 3.0.2.alpha0

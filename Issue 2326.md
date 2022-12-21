# Issue 2326: compiled sparse and dense graph datastructures

Issue created by migration from Trac.

Original creator: rlm

Original creation time: 2008-02-27 00:00:40

Assignee: rlm

CC:  jason

Implement compiled base classes for graphs, which will be faster than Python based NetworkX classes (especially when accessed from Cython).


---

Comment by rlm created at 2008-02-27 00:01:12

The patches on this ticket will depend on those in #2307.


---

Comment by rlm created at 2008-02-27 01:59:12

Don't know what's up with the HTML preview on the second patch, but...


---

Comment by rlm created at 2008-02-28 19:29:04

For the results of `sage -t -valgrind` on the new code, see

sparse_graph:

http://sage.math.washington.edu/home/rlmill/.sage/valgrind/sage-memcheck.12219

dense_graph:

http://sage.math.washington.edu/home/rlmill/.sage/valgrind/sage-memcheck.18970

They certainly look clean to me :)


---

Comment by rlm created at 2008-02-28 20:01:18

Alternatively,

sparse_graph:

http://sage.math.washington.edu/home/rlmill/sage-memcheck.12219

dense_graph:

http://sage.math.washington.edu/home/rlmill/sage-memcheck.18970


---

Attachment

Sorry for the caps, but I just wanted to make sure mabshoff saw it :)  It looks good to me.


---

Comment by mabshoff created at 2008-03-01 23:55:21

Merged 2326-final.patch in Sage 2.10.3.rc1


---

Comment by mabshoff created at 2008-03-01 23:55:21

Resolution: fixed

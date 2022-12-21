# Issue 1295: butterfly graph

Issue created by migration from Trac.

Original creator: jason

Original creation time: 2007-11-28 00:08:49

Assignee: mhansen

Keywords: graphs

Added code to make the butterfly graph:

[http://mathworld.wolfram.com/ButterflyGraph.html](http://mathworld.wolfram.com/ButterflyGraph.html)




---

Attachment


---

Comment by jason created at 2007-11-28 06:42:56

apply this instead of butterfly-graph.patch


---

Attachment

butterfly-graph-2.patch adds a very fast bit-fiddling method from Robert Miller which works nicely when n<=30.


---

Comment by rlm created at 2007-11-28 20:02:23

looks good to me


---

Comment by mabshoff created at 2007-12-01 11:19:51

Merged butterfly-graph-2.patch in 2.8.15.alpha0.


---

Comment by mabshoff created at 2007-12-01 11:19:51

Resolution: fixed

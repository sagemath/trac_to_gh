# Issue 5623: 5x speedup in all_graph_colorings

Issue created by migration from Trac.

Original creator: carlohamalainen

Original creation time: 2009-03-28 13:13:25

Assignee: boothby

This patch changes all_graph_colorings to use the C++ dancing links implementation instead of the Cython implementation.

* sage -testall is all ok
* valgrind is ok
* Roughly 5x speedup on some random graphs (see test.sage):

Sage 3.4 timing:
carlo`@`ka37:~/work/code/graphdlx$ sage test.sage 
5 loops, best of 3: 158 ms per loop
carlo`@`ka37:~/work/code/graphdlx$ sage test.sage 
5 loops, best of 3: 158 ms per loop
carlo`@`ka37:~/work/code/graphdlx$ sage test.sage 
5 loops, best of 3: 157 ms per loop

Sage 3.4 with patch timing:

5 loops, best of 3: 33.5 ms per loop
carlo`@`ka37:~/work/code/graphdlx$ sage test.sage 
5 loops, best of 3: 33.1 ms per loop
carlo`@`ka37:~/work/code/graphdlx$ sage test.sage 
5 loops, best of 3: 33.3 ms per loop


---

Attachment

Works for me.  I'd like to see the test.sage file be reworked into a Test class for randomized testing.  search_src('class Test') for examples.


---

Comment by boothby created at 2009-03-30 06:04:39

OOps.


```
sage: g = Graph()
sage: c = 0
sage: for h in graph_coloring.all_graph_colorings(g,0,False): c+=1
------------------------------------------------------------
Unhandled SIGSEGV: A segmentation fault occured in SAGE.
This probably occured because a *compiled* component
of SAGE has a bug in it (typically accessing invalid memory)
or is not properly wrapped with _sig_on, _sig_off.
You might want to run SAGE under gdb with 'sage -gdb' to debug this.
SAGE will now terminate (sorry).
------------------------------------------------------------
```



---

Attachment

The attachment 'graphcoloring_5623_test.patch' implements a Test class that does randomized testing.  Fix the segfault, and I'll be happy with it.


---

Attachment


---

Attachment


---

Comment by carlohamalainen created at 2009-03-30 08:03:26

I updated graphcolouring.patch:

 * returns immediately when n == 0
 * raises a ValueError if n < 0

The patch dlxcpp.patch fixes the segfault on an empty graph.


---

Comment by mabshoff created at 2009-03-31 03:19:03

Could you please specify exactly which patches need to be applied and reviewed?

Cheers,

Michael


---

Comment by mabshoff created at 2009-03-31 03:19:19

Could you please specify exactly which patches need to be applied and reviewed?

Cheers,

Michael


---

Comment by carlohamalainen created at 2009-03-31 06:31:02

All three patches should be applied:

 * graphcoloring_5623_test.patch
 * graphcolouring.patch
 * dlxcpp.patch

The final patch is new and I guess should be reviewed (it's just a one-liner).


---

Attachment


---

Comment by boothby created at 2009-03-31 18:22:21

I've added one more patch which tests for the previous segfault, and negative entries.  The patches work when applied in the order:

    * graphcolouring.patch
    * dlxcpp.patch 
    * graphcoloring_5623_test.patch
    * graphcoloring_5623_doctests.patch


---

Comment by mabshoff created at 2009-04-01 02:24:39

Merged

 * graphcolouring.patch
 * dlxcpp.patch
 * graphcoloring_5623_test.patch
 * graphcoloring_5623_doctests.patch 

in Sage 3.4.1.rc0.

Cheers,

Michael


---

Comment by mabshoff created at 2009-04-01 02:24:39

Resolution: fixed

# Issue 3541: graph multiedge plotting

Issue created by migration from Trac.

Original creator: ekirkman

Original creation time: 2008-07-01 21:57:08

Assignee: rlm

CC:  rlm mabshoff

Wanted:  New code to make a pretty plot of graphs with multiedges.  I'm working on a patch now and will post it soon.


---

Comment by mhansen created at 2008-07-01 22:13:12

Awesome!


---

Comment by robertwb created at 2008-07-02 05:08:05

Some code from Ashley Saunders up at http://wiki.wstein.org/2008/480a/theprojects


---

Comment by rlm created at 2008-08-10 03:24:53

Changing assignee from rlm to ekirkman.


---

Comment by rlm created at 2009-02-07 02:22:58

This depends on #4774, and implements multiple edges for graphs only.


---

Attachment

This set of patches should fix #5248.


---

Attachment


---

Comment by rlm created at 2009-02-14 01:59:35

This is still a little quirky, due to issues with #4774, but it will be great to get this merged. The only problems left are on a different ticket.

+ exp[(10!)^(10!)]


---

Comment by rlm created at 2009-02-14 01:59:52

Apply both patches in order.


---

Comment by mabshoff created at 2009-02-14 02:59:53

This is going into 3.3.

Cheers,

Michael


---

Comment by ekirkman created at 2009-02-14 03:44:43

Just fixes edge_color and adds a doctest


---

Attachment

I caught some things while looking at the plots.  It should be a pretty quick review-- hopefully I got it in fast enough.


---

Comment by mabshoff created at 2009-02-14 13:13:56

What is the credit situation here? I assume Emily as author, Robert for review?

Cheers,

Michael


---

Comment by mabshoff created at 2009-02-14 13:16:41

There is one doctest failure:

```
mabshoff`@`sage:/scratch/mabshoff/sage-3.3.rc1$ ./sage -t -long devel/sage/sage/combinat/crystals/crystals.py
sage -t -long "devel/sage/sage/combinat/crystals/crystals.py"
**********************************************************************
File "/scratch/mabshoff/sage-3.3.rc1/devel/sage/sage/combinat/crystals/crystals.py", line 553:
    sage: C.plot()
Expected:
    Graphics object consisting of 11 graphics primitives
Got:
    Graphics object consisting of 17 graphics primitives
**********************************************************************
```

I assume this is becase previously the graph was incorrect.

Cheers,

Michael


---

Comment by mabshoff created at 2009-02-14 13:22:03

After checking with Mike Hansen he gave me the thumbs up for the change, so I will post a tiny reviewer patch in a second. Note that trac_3541_tinyfixes.patch is a diff, but I committed in Emily's name :)

Cheers,

Michael


---

Attachment


---

Comment by mabshoff created at 2009-02-14 13:31:16

Merged 

 * trac_3541-multiedge-1.patch
 * trac_3541_beezy.patch
 * trac_3541_tinyfixes.patch
 * trac_3541-reviewer-doctest.patch

in Sage 3.3.rc1. :)

Cheers,

Michael


---

Comment by mabshoff created at 2009-02-14 13:31:16

Resolution: fixed


---

Comment by rlm created at 2009-02-14 18:38:16

Emily wrote all that by herself. I only reviewed and helped her with matplotlib.


---

Attachment

sample plot of a multi-edge graph


---

Comment by mvngu created at 2009-02-20 03:18:57

Uploaded an image of a sample plot of a multi-edge graph. The graph was produced using the following code from the docstring of `sage.graphs.graph.GenericGraph.plot`:

```
sage: g = Graph({}, loops=True, multiedges=True)
sage: g.add_edges([(0,0,'a'),(0,0,'b'),(0,1,'c'),(0,1,'d'), 
...     (0,1,'e'),(0,1,'f'),(0,1,'f'),(2,1,'g'),(2,2,'h')]) 
sage: g.plot(edge_labels=True, color_by_label=True, edge_style='dashed')
```

I uploaded the image here, so it can be referred to in the release tour of 3.3.

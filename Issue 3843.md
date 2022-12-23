# Issue 3843: typo in graphs: "edge_labels -- whether to print edgeedge labels. By default, False,                 but"

Issue created by migration from https://trac.sagemath.org/ticket/3843

Original creator: was

Original creation time: 2008-08-13 21:41:36

Assignee: rlm

Notice the edgeedge.

Also a complaint - I tried for 15 minutes and couldn't figure out how to label the edges!


---

Comment by rlm created at 2008-08-13 21:47:36


```
sage: G = graphs.PetersenGraph()
sage: G.set_edge_label(0,1,'spam')
sage: G.plot(edge_labels=True)
```


I don't see how to make it easier to figure out...


---

Attachment


---

Attachment


---

Comment by rlm created at 2008-08-13 23:35:10

Depends on patches at #3801.

One note- many doctests are deleted in this patch, since I have probably spent a sum of about five days cutting and pasting the same tests from plot to show or vice versa. Now there is one simple test in show and it suggests to look at plot for good documentation.


---

Attachment


---

Comment by saliola created at 2008-08-14 17:51:22

One suggested change (I'll attach a diff file):

tree_root takes a tuple as an argument (v, str), where v is a vertex and str is either "top" or "bottom". This isn't intuitive: I first tried a vertex only, which forced me to look at the documentation to understand why I got an unpacking error message.

I suggest splitting this option into two: tree_root (takes a vertex) and tree_orientation (takes "up" or "down").


---

Comment by saliola created at 2008-08-14 17:52:17

diff file with my suggested changes


---

Attachment

+1 to saliola's patch. I haven't tested it, but I completely agree with the idea.


---

Comment by rlm created at 2008-08-14 19:52:04

There is a little more work needing to be done here. I ignored William when he was trying to tell me that the tree options aren't available to G.show(). In fact, I'm going to rewrite both plot and show's argument handling to use keywords instead. This will improve usability and code.

Sorry, was. You were right. :-)


---

Attachment


---

Comment by mabshoff created at 2008-08-27 02:15:05

Against my current 3.1.2.alpha1 merge tree there is one doctest failure with all five patches applied:

```
sage -t -long devel/sage/sage/graphs/graph.py               
**********************************************************************
File "/scratch/mabshoff/release-cycle/sage-3.1.2.alpha1/tmp/graph.py", line 7632:
    sage: ((graphs.ChvatalGraph()).cliques_get_clique_bipartite()).show(figsize=[2,2], vertex_size=20, vertex_labels=False)
Exception raised:
    Traceback (most recent call last):
      File "/scratch/mabshoff/release-cycle/sage-3.1.2.alpha1/local/lib/python2.5/doctest.py", line 1228, in __run
        compileflags, 1) in test.globs
      File "<doctest __main__.example_161[3]>", line 1, in <module>
        ((graphs.ChvatalGraph()).cliques_get_clique_bipartite()).show(figsize=[Integer(2),Integer(2)], vertex_size=Integer(20), vertex_labels=False)###line 7632:
    sage: ((graphs.ChvatalGraph()).cliques_get_clique_bipartite()).show(figsize=[2,2], vertex_size=20, vertex_labels=False)
      File "/scratch/mabshoff/release-cycle/sage-3.1.2.alpha1/local/lib/python2.5/site-packages/sage/graphs/graph.py", line 5439, in show
        self.plot(**plot_kwds).show(**kwds)
    TypeError: show() got an unexpected keyword argument 'vertex_size'
**********************************************************************
```



---

Comment by rlm created at 2008-08-30 19:43:03

With the new flat patch:

```
rank4:sage-3843 rlmill$ ../../sage -tp 2 -long sage/graphs
...
All tests passed!
Total time for all tests: 300.7 seconds
```



---

Attachment


---

Comment by mabshoff created at 2008-08-30 20:05:44

Positive review. rlm explained the last fix to me and I am satisfied.

Cheers,

Michael


---

Comment by mabshoff created at 2008-08-30 22:16:47

Merged trac_3843-flat-and-fixed.2.patch in Sage 3.1.2.alpha3


---

Comment by mabshoff created at 2008-08-30 22:16:47

Resolution: fixed

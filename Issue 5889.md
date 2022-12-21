# Issue 5889: [with patch, needs review] random simplicial complexes

Issue created by migration from Trac.

Original creator: jhpalmieri

Original creation time: 2009-04-24 17:14:45

Assignee: jhpalmieri

Add random simplicial complexes to the class of examples of simplicial complexes, so you can do

```
sage: simplicial_complexes.RandomComplex(6, 2)
```

to get a random simplicial complex with 6 vertices, all possible edges, and the possible 2-dimensional simplices (triangles) randomly included (or not).



---

Comment by AlexGhitza created at 2009-04-30 12:24:52

This looks good.

There is one little issue: as far as I know, you do not need to label the doctest with #random.  Sage doctests work in such a way that the same random seed is set before testing, so you will get the same results.  So the #random should be removed from line 712.

Apart from that, positive review.


Michael, should we have a new trac component labeled "algebraic topology"?  It's a bit weird to have this under "misc", and it will probably come in handy at the next Sage Days in Seattle.


---

Comment by jhpalmieri created at 2009-04-30 20:51:51

Okay, this patch is identical to the first one, but without "#random".  It passes all tests for me on sage.math, although I would like someone else to double-check that.


---

Attachment


---

Comment by AlexGhitza created at 2009-04-30 21:12:15

It also passes doctests for me.


---

Comment by mabshoff created at 2009-04-30 21:40:35

Alex,

"Algebraic Topology" - here we come. I have made John default owner for now :)

If you want any other component please let me know and I will add them.

Cheers,

Michael


---

Comment by mabshoff created at 2009-04-30 21:40:35

Changing component from misc to algebraic topology.


---

Comment by jhpalmieri created at 2009-04-30 21:54:02

Excellent!


---

Comment by mabshoff created at 2009-05-11 13:19:38

Merged in Sage 4.0.alpha0.

Cheers,

Michael


---

Comment by mabshoff created at 2009-05-11 13:19:38

Resolution: fixed

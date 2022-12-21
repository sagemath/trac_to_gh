# Issue 5003: [with patch, needs review] equality testing in graphs should check "weighted" property

Issue created by migration from Trac.

Original creator: rlm

Original creation time: 2009-01-17 19:53:07

Assignee: rlm

See:

http://groups.google.com/group/sage-support/browse_thread/thread/d01dd8082da28d52?hl=en


---

Attachment


---

Comment by shumow created at 2009-01-24 11:25:31

Hey, I ran into some doctest failures w/ your new change.

Specifically, around line 839 (in the docstring for weighted_ajacency_matrix(...)):



```
        EXAMPLES:
            sage: G = Graph(sparse=True)
            sage: G.add_edges([(0,1,1),(1,2,2),(0,2,3),(0,3,4)])
            sage: M = G.weighted_adjacency_matrix(); M
            [0 1 3 4]
            [1 0 2 0]
            [3 2 0 0]
            [4 0 0 0]
            sage: H = Graph(data=M, format='weighted_adjacency_matrix', sparse=True)
            sage: H == G
            True
```


This fails.  Specifically, G.weighted() returns false (which seems like its own bug.)

And Also, the example starting at line 1180 (in the docstring for weighted(...):


```
        EXAMPLE:
        Here we have two graphs with different labels, but weighted is False
        for both, so we just check for the presence of edges:
            sage: G = Graph({0:{1:'a'}}, implementation='networkx')
            sage: H = Graph({0:{1:'b'}}, implementation='networkx')
            sage: G == H
            True

        Now one is weighted and the other is not, so the comparison is done as
        if neither is weighted:
            sage: G.weighted(True)
            sage: H.weighted()
            False
            sage: G == H
            True

```


Fails.  Because of the change.

The first of these issues, is a bug and should be fixed IMHO.  The second issue is more subtle and disturbing.  Particularly because it indicates that a valid example used to work, you will be breaking compatibility with code that works this way, and you should think about what the previous assumptions were, and if you can work around them with a fix.


---

Comment by rlm created at 2009-01-24 12:57:12

Replying to [comment:1 shumow]:
> This fails.  Specifically, G.weighted() returns false (which seems like its own bug.)

Not so much a bug, as a typo in the doctest. If you don't say G is weighted, then just adding edges with weights shouldn't change that. In fact, that's the point of the other doctest.

> And Also, the example starting at line 1180 (in the docstring for weighted(...):
> 
...
> 
> Fails.  Because of the change.
> 
> The second issue is more subtle and disturbing.  Particularly because it indicates that a valid example used to work, you will be breaking compatibility with code that works this way, and you should think about what the previous assumptions were, and if you can work around them with a fix.

Well, it's more like we're updating things to actually do it correctly. Before, weighted wasn't a property of graphs, and that test was kind of a warning about that. I don't know of any code that would be affected by this, but I think this is the right way to do things.


---

Comment by rlm created at 2009-01-24 12:57:30

Apply this patch second.


---

Attachment

Looks good to me.


---

Comment by mabshoff created at 2009-01-24 23:00:55

Resolution: fixed


---

Comment by mabshoff created at 2009-01-24 23:00:55

Merged in Sage 3.3.alpha2.

Cheers,

Michael

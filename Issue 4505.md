# Issue 4505: Boyer's planarity code mishandles graphs with no edges

Issue created by migration from Trac.

Original creator: jason

Original creation time: 2008-11-13 00:47:11

Assignee: rlm

CC:  ekirkman bober

We get random segfaults from the planarity code because it doesn't seem to handle graphs with no edges properly.

The segfaults occur in these lines from sage/graphs/planarity/graphEmbed.c


```
        Jfirst = theGraph->G[I].link[1];

        if (theGraph->G[Jfirst].type == EDGE_FORWARD)
        {

            /* Find the end of the forward edge list */

            Jnext = Jfirst;
            while (theGraph->G[Jnext].type == EDGE_FORWARD)
```


The problem is that when there are no edges, theGraph->G[I].link[1] is -1, Jfirst is -1.  If the random value at theGraph->G[-1].type is 2 (EDGE_FORWARD), then the code in the if block is executed and we get a segfault when trying to access fields inside the if block.

For now, this patch skirts the issue by checking for the case of no edges explicitly before Boyer's code is called.

I am emailing John Boyer about this as well.


---

Attachment


---

Comment by jason created at 2008-11-13 03:22:46

Changing priority from major to blocker.


---

Comment by mabshoff created at 2008-11-13 03:30:42

Positive review assuming this passes doctests:

```
[7:24pm] mabshoff|afk: Is a graph without edges planar?
[7:24pm] jason--: yep!
[7:24pm] mabshoff|afk: In that case you would get a positive review 
[7:24pm] jason--: you can easily draw it with no edges crossing
[7:24pm] jason--: thanks, that was fast too.
```

Cheers,

Michael


---

Comment by mabshoff created at 2008-11-13 04:50:08

Merged in Sage 3.2.rc1


---

Comment by mabshoff created at 2008-11-13 04:50:08

Resolution: fixed

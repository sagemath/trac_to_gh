# Issue 6632: Bug in blocks_and_cut_vertices() of a graph that occurs when vertex 0 is a cut vertex

archive/issues_006632.json:
```json
{
    "body": "Assignee: rlm\n\nCC:  rlm\n\nThere is a bug in the blocks_and_cut_vertices() function for graphs such that an incorrect result is returned if the vertex 0 is a cut vertex.\n\n\n```\nsage: G=Graph()\nsage: G.add_vertices(range(5))\nsage: G.add_edges([(0,1),(0,2),(1,2),(2,3),(2,4),(3,4)])\nsage: print G.blocks_and_cut_vertices()\n([[0, 1, 2]], [])\n```\n\n\nThe bug arises because the algorithm as presented in the referenced book uses 0 to indicate a vertex not in the graph.  However, in Sage, we number the vertices of a graph starting at 0.\n\nA patch will be attached below.\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/6632\n\n",
    "created_at": "2009-07-26T22:10:42Z",
    "labels": [
        "graph theory",
        "minor",
        "bug"
    ],
    "title": "Bug in blocks_and_cut_vertices() of a graph that occurs when vertex 0 is a cut vertex",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/6632",
    "user": "hartke"
}
```
Assignee: rlm

CC:  rlm

There is a bug in the blocks_and_cut_vertices() function for graphs such that an incorrect result is returned if the vertex 0 is a cut vertex.


```
sage: G=Graph()
sage: G.add_vertices(range(5))
sage: G.add_edges([(0,1),(0,2),(1,2),(2,3),(2,4),(3,4)])
sage: print G.blocks_and_cut_vertices()
([[0, 1, 2]], [])
```


The bug arises because the algorithm as presented in the referenced book uses 0 to indicate a vertex not in the graph.  However, in Sage, we number the vertices of a graph starting at 0.

A patch will be attached below.


Issue created by migration from https://trac.sagemath.org/ticket/6632





---

archive/issue_comments_054350.json:
```json
{
    "body": "Attachment\n\nPatch to fix bug in blocks_and_cut_vertices() in graph.py",
    "created_at": "2009-07-26T22:13:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6632",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6632#issuecomment-54350",
    "user": "hartke"
}
```

Attachment

Patch to fix bug in blocks_and_cut_vertices() in graph.py



---

archive/issue_comments_054351.json:
```json
{
    "body": "Stephen: If you want people to review your patch, you should mark the subject of the ticket with \"needs review\". That way, the ticket would be picked up by the relevant trac report and people can easily identify those tickets that need review.",
    "created_at": "2009-07-26T22:38:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6632",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6632#issuecomment-54351",
    "user": "mvngu"
}
```

Stephen: If you want people to review your patch, you should mark the subject of the ticket with "needs review". That way, the ticket would be picked up by the relevant trac report and people can easily identify those tickets that need review.



---

archive/issue_comments_054352.json:
```json
{
    "body": "Minh:  Thanks for fixing the summary!  This was my first submitted patch, so I'm trying to learn the ropes.",
    "created_at": "2009-07-27T15:28:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6632",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6632#issuecomment-54352",
    "user": "hartke"
}
```

Minh:  Thanks for fixing the summary!  This was my first submitted patch, so I'm trying to learn the ropes.



---

archive/issue_comments_054353.json:
```json
{
    "body": "Replying to [comment:3 hartke]:\n> Minh:  Thanks for fixing the summary!  This was my first submitted patch, so I'm trying to learn the ropes.\nNo worries. We all have to start somewhere :-)",
    "created_at": "2009-07-28T03:19:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6632",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6632#issuecomment-54353",
    "user": "mvngu"
}
```

Replying to [comment:3 hartke]:
> Minh:  Thanks for fixing the summary!  This was my first submitted patch, so I'm trying to learn the ropes.
No worries. We all have to start somewhere :-)



---

archive/issue_comments_054354.json:
```json
{
    "body": "Thanks for looking at this!\n\nHow about we trade reviews?  I'd like to get #6659 reviewed and in 4.1.1 :).\n\nCould you also just initialize p to [None]*G.num_verts()?  Then the check at the bottom becomes `p[v] is None`.\n\nI'm a little concerned about you taking out the last B.append(S) statement.  Can you comment on it?  I don't have Jungnickel handy, so forgive me if the answer is easy.\n\nI noticed a few other things with this function, but I'll open up another ticket to address these.  For one, it totally ignores the original vertex labeling in the answer.  For example, you can't make sense of the following output.\n\n```\nsage: g=graphs.CubeGraph(2)\nsage: g.blocks_and_cut_vertices()\n([[2, 3, 1, 0]], [])\nsage: g\n2-Cube: Graph on 4 vertices\nsage: g.vertices()\n['00', '01', '10', '11']\n```\n\n\nSecond: there seems to be a serious error (in the old implementation too) in the case of a star graph.  Look at the cut vertices returned here.\n\n\n```\nsage: g=graphs.StarGraph(8)      \nsage: g.blocks_and_cut_vertices() # current implementation\n\n([[1, 0], [2, 0], [3, 0], [4, 0], [5, 0], [6, 0], [7, 0], [8, 0], [0]],\n [0, 0, 0, 0, 0, 0, 0])\n```\n\n\nYour implementation corrects at least one problem: the last [0] is gone (probably as an effect of you taking out that last append() statement, right?):\n\n\n```\nsage: g=graphs.StarGraph(8)      \nsage: g.blocks_and_cut_vertices() # your implementation\n\n([[1, 0], [2, 0], [3, 0], [4, 0], [5, 0], [6, 0], [7, 0], [8, 0]],\n [0, 0, 0, 0, 0, 0, 0])\n```\n",
    "created_at": "2009-07-31T06:54:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6632",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6632#issuecomment-54354",
    "user": "jason"
}
```

Thanks for looking at this!

How about we trade reviews?  I'd like to get #6659 reviewed and in 4.1.1 :).

Could you also just initialize p to [None]*G.num_verts()?  Then the check at the bottom becomes `p[v] is None`.

I'm a little concerned about you taking out the last B.append(S) statement.  Can you comment on it?  I don't have Jungnickel handy, so forgive me if the answer is easy.

I noticed a few other things with this function, but I'll open up another ticket to address these.  For one, it totally ignores the original vertex labeling in the answer.  For example, you can't make sense of the following output.

```
sage: g=graphs.CubeGraph(2)
sage: g.blocks_and_cut_vertices()
([[2, 3, 1, 0]], [])
sage: g
2-Cube: Graph on 4 vertices
sage: g.vertices()
['00', '01', '10', '11']
```


Second: there seems to be a serious error (in the old implementation too) in the case of a star graph.  Look at the cut vertices returned here.


```
sage: g=graphs.StarGraph(8)      
sage: g.blocks_and_cut_vertices() # current implementation

([[1, 0], [2, 0], [3, 0], [4, 0], [5, 0], [6, 0], [7, 0], [8, 0], [0]],
 [0, 0, 0, 0, 0, 0, 0])
```


Your implementation corrects at least one problem: the last [0] is gone (probably as an effect of you taking out that last append() statement, right?):


```
sage: g=graphs.StarGraph(8)      
sage: g.blocks_and_cut_vertices() # your implementation

([[1, 0], [2, 0], [3, 0], [4, 0], [5, 0], [6, 0], [7, 0], [8, 0]],
 [0, 0, 0, 0, 0, 0, 0])
```




---

archive/issue_comments_054355.json:
```json
{
    "body": "Attachment\n\nApply both patches.",
    "created_at": "2009-08-03T01:14:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6632",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6632#issuecomment-54355",
    "user": "rlm"
}
```

Attachment

Apply both patches.



---

archive/issue_comments_054356.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-08-03T02:02:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6632",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6632#issuecomment-54356",
    "user": "mvngu"
}
```

Resolution: fixed

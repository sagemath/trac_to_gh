# Issue 5620: Digraph plotting bug

archive/issues_005620.json:
```json
{
    "body": "Assignee: ekirkman\n\nPointed out by rlm-- digraphs can have two paths between a pair of vertices without being multiple edged graphs.  So the graph\n\n```\nsage: G = DiGraph({1:{2: 'h'}, 2:{1:'g'}})\n```\n\nis drawn with only one straight-line arrow even though there are two edges.  Basically, this will just require a quick check for this case and then treating such a graph the same as a multidigraph.\n\nAlso, need to update multiple_edges and loops function calls in graph_plot.py to match the new function definitions has_multiple_edges and has_loops in graph.py\n\nPretty straightforward stuff... I should have a patch up in 3, 2, 1...\n\nIssue created by migration from https://trac.sagemath.org/ticket/5620\n\n",
    "created_at": "2009-03-27T22:34:49Z",
    "labels": [
        "graph theory",
        "major",
        "bug"
    ],
    "title": "Digraph plotting bug",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/5620",
    "user": "ekirkman"
}
```
Assignee: ekirkman

Pointed out by rlm-- digraphs can have two paths between a pair of vertices without being multiple edged graphs.  So the graph

```
sage: G = DiGraph({1:{2: 'h'}, 2:{1:'g'}})
```

is drawn with only one straight-line arrow even though there are two edges.  Basically, this will just require a quick check for this case and then treating such a graph the same as a multidigraph.

Also, need to update multiple_edges and loops function calls in graph_plot.py to match the new function definitions has_multiple_edges and has_loops in graph.py

Pretty straightforward stuff... I should have a patch up in 3, 2, 1...

Issue created by migration from https://trac.sagemath.org/ticket/5620





---

archive/issue_comments_043885.json:
```json
{
    "body": "I am also working on a straight-line alternative...  I'll put that one up shortly.",
    "created_at": "2009-03-27T23:05:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5620",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5620#issuecomment-43885",
    "user": "ekirkman"
}
```

I am also working on a straight-line alternative...  I'll put that one up shortly.



---

archive/issue_comments_043886.json:
```json
{
    "body": "So the straight line version turned out to be kind of hokey-looking, which is what I was afraid of.  But I was able to clean up the original fix so it's not so costly to run for large directed graphs.  So the patch that should be reviewed is trac5620_digraph_plotting.patch and the alternative option can be ignored.  I am leaving the alt patch up for now, to see if there's any feedback about whether it should be a non-default display option.  Also, I'm attaching pictures from executing\n\n```\nsage: G = DiGraph({1:{2: 'h', 4:'j'}, 2:{1:'g'}, 3:{1:'a', 2:'b'}, 4:{1:'f'}})\nsage: G.show(color_by_label=True, edge_labels=True)\n```\n\nin each version.",
    "created_at": "2009-03-28T02:16:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5620",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5620#issuecomment-43886",
    "user": "ekirkman"
}
```

So the straight line version turned out to be kind of hokey-looking, which is what I was afraid of.  But I was able to clean up the original fix so it's not so costly to run for large directed graphs.  So the patch that should be reviewed is trac5620_digraph_plotting.patch and the alternative option can be ignored.  I am leaving the alt patch up for now, to see if there's any feedback about whether it should be a non-default display option.  Also, I'm attaching pictures from executing

```
sage: G = DiGraph({1:{2: 'h', 4:'j'}, 2:{1:'g'}, 3:{1:'a', 2:'b'}, 4:{1:'f'}})
sage: G.show(color_by_label=True, edge_labels=True)
```

in each version.



---

archive/issue_comments_043887.json:
```json
{
    "body": "Changing assignee from ekirkman to rlm.",
    "created_at": "2009-03-28T02:34:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5620",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5620#issuecomment-43887",
    "user": "ekirkman"
}
```

Changing assignee from ekirkman to rlm.



---

archive/issue_comments_043888.json:
```json
{
    "body": "Reviewer patch to original",
    "created_at": "2009-03-31T23:14:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5620",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5620#issuecomment-43888",
    "user": "rlm"
}
```

Reviewer patch to original



---

archive/issue_comments_043889.json:
```json
{
    "body": "Attachment",
    "created_at": "2009-03-31T23:15:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5620",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5620#issuecomment-43889",
    "user": "rlm"
}
```

Attachment



---

archive/issue_comments_043890.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-04-01T00:46:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5620",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5620#issuecomment-43890",
    "user": "mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_043891.json:
```json
{
    "body": "Merged in Sage 3.4.1.rc0.\n\nCheers,\n\nMichael",
    "created_at": "2009-04-01T00:46:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5620",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5620#issuecomment-43891",
    "user": "mabshoff"
}
```

Merged in Sage 3.4.1.rc0.

Cheers,

Michael

# Issue 3843: typo in graphs: "edge_labels -- whether to print edgeedge labels. By default, False,                 but"

archive/issues_003843.json:
```json
{
    "body": "Assignee: rlm\n\nNotice the edgeedge.\n\nAlso a complaint - I tried for 15 minutes and couldn't figure out how to label the edges!\n\nIssue created by migration from https://trac.sagemath.org/ticket/3843\n\n",
    "created_at": "2008-08-13T21:41:36Z",
    "labels": [
        "graph theory",
        "major",
        "bug"
    ],
    "title": "typo in graphs: \"edge_labels -- whether to print edgeedge labels. By default, False,                 but\"",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/3843",
    "user": "was"
}
```
Assignee: rlm

Notice the edgeedge.

Also a complaint - I tried for 15 minutes and couldn't figure out how to label the edges!

Issue created by migration from https://trac.sagemath.org/ticket/3843





---

archive/issue_comments_027329.json:
```json
{
    "body": "\n```\nsage: G = graphs.PetersenGraph()\nsage: G.set_edge_label(0,1,'spam')\nsage: G.plot(edge_labels=True)\n```\n\n\nI don't see how to make it easier to figure out...",
    "created_at": "2008-08-13T21:47:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3843",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3843#issuecomment-27329",
    "user": "rlm"
}
```


```
sage: G = graphs.PetersenGraph()
sage: G.set_edge_label(0,1,'spam')
sage: G.plot(edge_labels=True)
```


I don't see how to make it easier to figure out...



---

archive/issue_comments_027330.json:
```json
{
    "body": "Attachment [trac_3843-come_on.patch](tarball://root/attachments/some-uuid/ticket3843/trac_3843-come_on.patch) by rlm created at 2008-08-13 22:18:56",
    "created_at": "2008-08-13T22:18:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3843",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3843#issuecomment-27330",
    "user": "rlm"
}
```

Attachment [trac_3843-come_on.patch](tarball://root/attachments/some-uuid/ticket3843/trac_3843-come_on.patch) by rlm created at 2008-08-13 22:18:56



---

archive/issue_comments_027331.json:
```json
{
    "body": "Attachment [trac_3843-plot-trees.patch](tarball://root/attachments/some-uuid/ticket3843/trac_3843-plot-trees.patch) by rlm created at 2008-08-13 23:32:49",
    "created_at": "2008-08-13T23:32:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3843",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3843#issuecomment-27331",
    "user": "rlm"
}
```

Attachment [trac_3843-plot-trees.patch](tarball://root/attachments/some-uuid/ticket3843/trac_3843-plot-trees.patch) by rlm created at 2008-08-13 23:32:49



---

archive/issue_comments_027332.json:
```json
{
    "body": "Depends on patches at #3801.\n\nOne note- many doctests are deleted in this patch, since I have probably spent a sum of about five days cutting and pasting the same tests from plot to show or vice versa. Now there is one simple test in show and it suggests to look at plot for good documentation.",
    "created_at": "2008-08-13T23:35:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3843",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3843#issuecomment-27332",
    "user": "rlm"
}
```

Depends on patches at #3801.

One note- many doctests are deleted in this patch, since I have probably spent a sum of about five days cutting and pasting the same tests from plot to show or vice versa. Now there is one simple test in show and it suggests to look at plot for good documentation.



---

archive/issue_comments_027333.json:
```json
{
    "body": "Attachment [trac_3843-docs.patch](tarball://root/attachments/some-uuid/ticket3843/trac_3843-docs.patch) by ekirkman created at 2008-08-14 01:08:35",
    "created_at": "2008-08-14T01:08:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3843",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3843#issuecomment-27333",
    "user": "ekirkman"
}
```

Attachment [trac_3843-docs.patch](tarball://root/attachments/some-uuid/ticket3843/trac_3843-docs.patch) by ekirkman created at 2008-08-14 01:08:35



---

archive/issue_comments_027334.json:
```json
{
    "body": "One suggested change (I'll attach a diff file):\n\ntree_root takes a tuple as an argument (v, str), where v is a vertex and str is either \"top\" or \"bottom\". This isn't intuitive: I first tried a vertex only, which forced me to look at the documentation to understand why I got an unpacking error message.\n\nI suggest splitting this option into two: tree_root (takes a vertex) and tree_orientation (takes \"up\" or \"down\").",
    "created_at": "2008-08-14T17:51:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3843",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3843#issuecomment-27334",
    "user": "saliola"
}
```

One suggested change (I'll attach a diff file):

tree_root takes a tuple as an argument (v, str), where v is a vertex and str is either "top" or "bottom". This isn't intuitive: I first tried a vertex only, which forced me to look at the documentation to understand why I got an unpacking error message.

I suggest splitting this option into two: tree_root (takes a vertex) and tree_orientation (takes "up" or "down").



---

archive/issue_comments_027335.json:
```json
{
    "body": "diff file with my suggested changes",
    "created_at": "2008-08-14T17:52:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3843",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3843#issuecomment-27335",
    "user": "saliola"
}
```

diff file with my suggested changes



---

archive/issue_comments_027336.json:
```json
{
    "body": "Attachment [trac_3843-reviewer-suggestions.patch](tarball://root/attachments/some-uuid/ticket3843/trac_3843-reviewer-suggestions.patch) by rlm created at 2008-08-14 17:53:50\n\n+1 to saliola's patch. I haven't tested it, but I completely agree with the idea.",
    "created_at": "2008-08-14T17:53:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3843",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3843#issuecomment-27336",
    "user": "rlm"
}
```

Attachment [trac_3843-reviewer-suggestions.patch](tarball://root/attachments/some-uuid/ticket3843/trac_3843-reviewer-suggestions.patch) by rlm created at 2008-08-14 17:53:50

+1 to saliola's patch. I haven't tested it, but I completely agree with the idea.



---

archive/issue_comments_027337.json:
```json
{
    "body": "There is a little more work needing to be done here. I ignored William when he was trying to tell me that the tree options aren't available to G.show(). In fact, I'm going to rewrite both plot and show's argument handling to use keywords instead. This will improve usability and code.\n\nSorry, was. You were right. :-)",
    "created_at": "2008-08-14T19:52:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3843",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3843#issuecomment-27337",
    "user": "rlm"
}
```

There is a little more work needing to be done here. I ignored William when he was trying to tell me that the tree options aren't available to G.show(). In fact, I'm going to rewrite both plot and show's argument handling to use keywords instead. This will improve usability and code.

Sorry, was. You were right. :-)



---

archive/issue_comments_027338.json:
```json
{
    "body": "Attachment [trac_3843-plot-options.patch](tarball://root/attachments/some-uuid/ticket3843/trac_3843-plot-options.patch) by rlm created at 2008-08-16 21:06:20",
    "created_at": "2008-08-16T21:06:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3843",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3843#issuecomment-27338",
    "user": "rlm"
}
```

Attachment [trac_3843-plot-options.patch](tarball://root/attachments/some-uuid/ticket3843/trac_3843-plot-options.patch) by rlm created at 2008-08-16 21:06:20



---

archive/issue_comments_027339.json:
```json
{
    "body": "Against my current 3.1.2.alpha1 merge tree there is one doctest failure with all five patches applied:\n\n```\nsage -t -long devel/sage/sage/graphs/graph.py               \n**********************************************************************\nFile \"/scratch/mabshoff/release-cycle/sage-3.1.2.alpha1/tmp/graph.py\", line 7632:\n    sage: ((graphs.ChvatalGraph()).cliques_get_clique_bipartite()).show(figsize=[2,2], vertex_size=20, vertex_labels=False)\nException raised:\n    Traceback (most recent call last):\n      File \"/scratch/mabshoff/release-cycle/sage-3.1.2.alpha1/local/lib/python2.5/doctest.py\", line 1228, in __run\n        compileflags, 1) in test.globs\n      File \"<doctest __main__.example_161[3]>\", line 1, in <module>\n        ((graphs.ChvatalGraph()).cliques_get_clique_bipartite()).show(figsize=[Integer(2),Integer(2)], vertex_size=Integer(20), vertex_labels=False)###line 7632:\n    sage: ((graphs.ChvatalGraph()).cliques_get_clique_bipartite()).show(figsize=[2,2], vertex_size=20, vertex_labels=False)\n      File \"/scratch/mabshoff/release-cycle/sage-3.1.2.alpha1/local/lib/python2.5/site-packages/sage/graphs/graph.py\", line 5439, in show\n        self.plot(**plot_kwds).show(**kwds)\n    TypeError: show() got an unexpected keyword argument 'vertex_size'\n**********************************************************************\n```\n",
    "created_at": "2008-08-27T02:15:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3843",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3843#issuecomment-27339",
    "user": "mabshoff"
}
```

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

archive/issue_comments_027340.json:
```json
{
    "body": "With the new flat patch:\n\n```\nrank4:sage-3843 rlmill$ ../../sage -tp 2 -long sage/graphs\n...\nAll tests passed!\nTotal time for all tests: 300.7 seconds\n```\n",
    "created_at": "2008-08-30T19:43:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3843",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3843#issuecomment-27340",
    "user": "rlm"
}
```

With the new flat patch:

```
rank4:sage-3843 rlmill$ ../../sage -tp 2 -long sage/graphs
...
All tests passed!
Total time for all tests: 300.7 seconds
```




---

archive/issue_comments_027341.json:
```json
{
    "body": "Attachment [trac_3843-flat-and-fixed.2.patch](tarball://root/attachments/some-uuid/ticket3843/trac_3843-flat-and-fixed.2.patch) by rlm created at 2008-08-30 19:58:50",
    "created_at": "2008-08-30T19:58:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3843",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3843#issuecomment-27341",
    "user": "rlm"
}
```

Attachment [trac_3843-flat-and-fixed.2.patch](tarball://root/attachments/some-uuid/ticket3843/trac_3843-flat-and-fixed.2.patch) by rlm created at 2008-08-30 19:58:50



---

archive/issue_comments_027342.json:
```json
{
    "body": "Positive review. rlm explained the last fix to me and I am satisfied.\n\nCheers,\n\nMichael",
    "created_at": "2008-08-30T20:05:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3843",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3843#issuecomment-27342",
    "user": "mabshoff"
}
```

Positive review. rlm explained the last fix to me and I am satisfied.

Cheers,

Michael



---

archive/issue_comments_027343.json:
```json
{
    "body": "Merged trac_3843-flat-and-fixed.2.patch in Sage 3.1.2.alpha3",
    "created_at": "2008-08-30T22:16:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3843",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3843#issuecomment-27343",
    "user": "mabshoff"
}
```

Merged trac_3843-flat-and-fixed.2.patch in Sage 3.1.2.alpha3



---

archive/issue_comments_027344.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-08-30T22:16:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3843",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3843#issuecomment-27344",
    "user": "mabshoff"
}
```

Resolution: fixed

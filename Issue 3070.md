# Issue 3070: bug in SymmetricGroup(1).cayley_graph()

archive/issues_003070.json:
```json
{
    "body": "Assignee: boothby\n\nIn https://groups.google.com/group/sage-support/browse_thread/thread/443ce49730b43396 M. Fix reported:\n\n```\nHello-\nI input the following:\n\nsage: s1 = SymmetricGroup(1)\nsage: s = s1.cayley_graph()\nsage: s.vertices()\n[]\n\nShouldn't the set of vertices have one element in it for the\nidentity?  s1 reports this element, but as shown the graph does not.\nI suppose this is trivial, but it seems like it should be fixed at\nsome point.  I am, however, still fairly new to SAGE, and could easily\nbe missing something.  Any thoughts on this? \n```\n\n\nCheers,\n\nMichael\n\nIssue created by migration from https://trac.sagemath.org/ticket/3070\n\n",
    "created_at": "2008-05-01T05:20:47Z",
    "labels": [
        "graph theory",
        "major",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.0.1",
    "title": "bug in SymmetricGroup(1).cayley_graph()",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/3070",
    "user": "mabshoff"
}
```
Assignee: boothby

In https://groups.google.com/group/sage-support/browse_thread/thread/443ce49730b43396 M. Fix reported:

```
Hello-
I input the following:

sage: s1 = SymmetricGroup(1)
sage: s = s1.cayley_graph()
sage: s.vertices()
[]

Shouldn't the set of vertices have one element in it for the
identity?  s1 reports this element, but as shown the graph does not.
I suppose this is trivial, but it seems like it should be fixed at
some point.  I am, however, still fairly new to SAGE, and could easily
be missing something.  Any thoughts on this? 
```


Cheers,

Michael

Issue created by migration from https://trac.sagemath.org/ticket/3070





---

archive/issue_comments_021191.json:
```json
{
    "body": "Attachment [trac3070-cayley_graph_constructor.patch](tarball://root/attachments/some-uuid/ticket3070/trac3070-cayley_graph_constructor.patch) by @rlmill created at 2008-05-01 18:11:13",
    "created_at": "2008-05-01T18:11:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3070",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3070#issuecomment-21191",
    "user": "@rlmill"
}
```

Attachment [trac3070-cayley_graph_constructor.patch](tarball://root/attachments/some-uuid/ticket3070/trac3070-cayley_graph_constructor.patch) by @rlmill created at 2008-05-01 18:11:13



---

archive/issue_comments_021192.json:
```json
{
    "body": "Applied to sage-3.0 on my macbook:\n\n\n```\n$ ./sage -t devel/sage/sage/groups/\n... \n----------------------------------------------------------------------\nAll tests passed!\nTotal time for all tests: 178.3 seconds\n$ ./sage -t devel/sage/sage/graphs\n...\n----------------------------------------------------------------------\nAll tests passed!\nTotal time for all tests: 217.6 seconds\n```\n",
    "created_at": "2008-05-01T18:13:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3070",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3070#issuecomment-21192",
    "user": "@rlmill"
}
```

Applied to sage-3.0 on my macbook:


```
$ ./sage -t devel/sage/sage/groups/
... 
----------------------------------------------------------------------
All tests passed!
Total time for all tests: 178.3 seconds
$ ./sage -t devel/sage/sage/graphs
...
----------------------------------------------------------------------
All tests passed!
Total time for all tests: 217.6 seconds
```




---

archive/issue_comments_021193.json:
```json
{
    "body": "Conclusion:\n\nThe function `cayley_graph` was unnecessarily complicated.",
    "created_at": "2008-05-01T18:14:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3070",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3070#issuecomment-21193",
    "user": "@rlmill"
}
```

Conclusion:

The function `cayley_graph` was unnecessarily complicated.



---

archive/issue_comments_021194.json:
```json
{
    "body": "the patch looks good to me.  I didn't apply or doctest it, though.",
    "created_at": "2008-05-02T16:07:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3070",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3070#issuecomment-21194",
    "user": "@jasongrout"
}
```

the patch looks good to me.  I didn't apply or doctest it, though.



---

archive/issue_comments_021195.json:
```json
{
    "body": "Doctests pass with the patch applied.\n\nCheers,\n\nMichael",
    "created_at": "2008-05-02T17:07:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3070",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3070#issuecomment-21195",
    "user": "mabshoff"
}
```

Doctests pass with the patch applied.

Cheers,

Michael



---

archive/issue_comments_021196.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-05-02T17:07:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3070",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3070#issuecomment-21196",
    "user": "mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_021197.json:
```json
{
    "body": "Merged in Sage 3.0.1.rc0",
    "created_at": "2008-05-02T17:07:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3070",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3070#issuecomment-21197",
    "user": "mabshoff"
}
```

Merged in Sage 3.0.1.rc0

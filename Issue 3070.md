# Issue 3070: bug in SymmetricGroup(1).cayley_graph()

archive/issues_003070.json:
```json
{
    "body": "Assignee: boothby\n\nIn https://groups.google.com/group/sage-support/browse_thread/thread/443ce49730b43396 M. Fix reported:\n\n```\nHello-\nI input the following:\n\nsage: s1 = SymmetricGroup(1)\nsage: s = s1.cayley_graph()\nsage: s.vertices()\n[]\n\nShouldn't the set of vertices have one element in it for the\nidentity?  s1 reports this element, but as shown the graph does not.\nI suppose this is trivial, but it seems like it should be fixed at\nsome point.  I am, however, still fairly new to SAGE, and could easily\nbe missing something.  Any thoughts on this? \n```\n\n\nCheers,\n\nMichael\n\nIssue created by migration from https://trac.sagemath.org/ticket/3070\n\n",
    "created_at": "2008-05-01T05:20:47Z",
    "labels": [
        "component: graph theory",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.0.1",
    "title": "bug in SymmetricGroup(1).cayley_graph()",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/3070",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
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

archive/issue_comments_021147.json:
```json
{
    "body": "Attachment [trac3070-cayley_graph_constructor.patch](tarball://root/attachments/some-uuid/ticket3070/trac3070-cayley_graph_constructor.patch) by @rlmill created at 2008-05-01 18:11:13",
    "created_at": "2008-05-01T18:11:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3070",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3070#issuecomment-21147",
    "user": "https://github.com/rlmill"
}
```

Attachment [trac3070-cayley_graph_constructor.patch](tarball://root/attachments/some-uuid/ticket3070/trac3070-cayley_graph_constructor.patch) by @rlmill created at 2008-05-01 18:11:13



---

archive/issue_comments_021148.json:
```json
{
    "body": "Applied to sage-3.0 on my macbook:\n\n\n```\n$ ./sage -t devel/sage/sage/groups/\n... \n----------------------------------------------------------------------\nAll tests passed!\nTotal time for all tests: 178.3 seconds\n$ ./sage -t devel/sage/sage/graphs\n...\n----------------------------------------------------------------------\nAll tests passed!\nTotal time for all tests: 217.6 seconds\n```\n",
    "created_at": "2008-05-01T18:13:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3070",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3070#issuecomment-21148",
    "user": "https://github.com/rlmill"
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

archive/issue_comments_021149.json:
```json
{
    "body": "Conclusion:\n\nThe function `cayley_graph` was unnecessarily complicated.",
    "created_at": "2008-05-01T18:14:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3070",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3070#issuecomment-21149",
    "user": "https://github.com/rlmill"
}
```

Conclusion:

The function `cayley_graph` was unnecessarily complicated.



---

archive/issue_comments_021150.json:
```json
{
    "body": "the patch looks good to me.  I didn't apply or doctest it, though.",
    "created_at": "2008-05-02T16:07:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3070",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3070#issuecomment-21150",
    "user": "https://github.com/jasongrout"
}
```

the patch looks good to me.  I didn't apply or doctest it, though.



---

archive/issue_comments_021151.json:
```json
{
    "body": "Doctests pass with the patch applied.\n\nCheers,\n\nMichael",
    "created_at": "2008-05-02T17:07:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3070",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3070#issuecomment-21151",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Doctests pass with the patch applied.

Cheers,

Michael



---

archive/issue_comments_021152.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-05-02T17:07:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3070",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3070#issuecomment-21152",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_021153.json:
```json
{
    "body": "Merged in Sage 3.0.1.rc0",
    "created_at": "2008-05-02T17:07:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3070",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3070#issuecomment-21153",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged in Sage 3.0.1.rc0



---

archive/issue_events_003284.json:
```json
{
    "actor": "mabshoff",
    "created_at": "2008-05-02T17:07:53Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/3070",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/3070#event-3284"
}
```

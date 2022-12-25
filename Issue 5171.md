# Issue 5171: Bugs in the Graph constructor when input an adjacency matrix.

archive/issues_005171.json:
```json
{
    "body": "Assignee: @rlmill\n\n1. The adjacency matrix of a graph constructed from an adjacency matrix should either be the same or one should get an error when constructing the graph:\n\n```\nsage: a = matrix(2,2,[1,0,0,1])\nsage: Graph(a)\nGraph on 2 vertices\nsage: Graph(a).adjacency_matrix()  # I think Graph(a) should work or given an error\n[0 0]\n[0 0]\nsage: Graph(a, loops=True).adjacency_matrix()\n[1 0]\n[0 1]\n```\n\n\nAnother example -- this is WRONG, since multiple loops should not be ignored.\n\n```\nsage: a = matrix(2,2,[2,0,0,1])\nsage: Graph(a,loops=True).adjacency_matrix()\n[1 0]\n[0 1]\n```\n\n\nWhy not just make a graph with loops and multiple edges (or at least weighted edges) if and only if the adjacency matrix has diagonal entries or non-1 entries?  I'm guessing the Graph constructor just grew from a time when these constructions weren't allowed or that networkx is just poorly designed.  Either way, this needs to be fixed for Sage. \n\n2. When the input matrix is non-square, the error message is wrong in multiple ways:\n\n```\nsage: a = matrix([1,0,0,1])\nsage: Graph(a)\nTraceback (most recent call last):\n...\nAttributeError: Incidence Matrix must have one 1 and one -1 per column.\n```\n\n\n* it should be \"adjacency matrix\". \n\n* The exception should be ValueError, not AttributeError\n\n* The Graph constructor doesn't take only 1's or -1's as input (but see above)\n\n* The Graph constructor is perfectly fine with having multiple 1's per column!\n\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/5171\n\n",
    "created_at": "2009-02-04T02:53:08Z",
    "labels": [
        "component: graph theory",
        "critical",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.3",
    "title": "Bugs in the Graph constructor when input an adjacency matrix.",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/5171",
    "user": "https://github.com/williamstein"
}
```
Assignee: @rlmill

1. The adjacency matrix of a graph constructed from an adjacency matrix should either be the same or one should get an error when constructing the graph:

```
sage: a = matrix(2,2,[1,0,0,1])
sage: Graph(a)
Graph on 2 vertices
sage: Graph(a).adjacency_matrix()  # I think Graph(a) should work or given an error
[0 0]
[0 0]
sage: Graph(a, loops=True).adjacency_matrix()
[1 0]
[0 1]
```


Another example -- this is WRONG, since multiple loops should not be ignored.

```
sage: a = matrix(2,2,[2,0,0,1])
sage: Graph(a,loops=True).adjacency_matrix()
[1 0]
[0 1]
```


Why not just make a graph with loops and multiple edges (or at least weighted edges) if and only if the adjacency matrix has diagonal entries or non-1 entries?  I'm guessing the Graph constructor just grew from a time when these constructions weren't allowed or that networkx is just poorly designed.  Either way, this needs to be fixed for Sage. 

2. When the input matrix is non-square, the error message is wrong in multiple ways:

```
sage: a = matrix([1,0,0,1])
sage: Graph(a)
Traceback (most recent call last):
...
AttributeError: Incidence Matrix must have one 1 and one -1 per column.
```


* it should be "adjacency matrix". 

* The exception should be ValueError, not AttributeError

* The Graph constructor doesn't take only 1's or -1's as input (but see above)

* The Graph constructor is perfectly fine with having multiple 1's per column!



Issue created by migration from https://trac.sagemath.org/ticket/5171





---

archive/issue_comments_039533.json:
```json
{
    "body": "William: when the matrix is non-square, we are assuming it is an incidence matrix; the error message is perfect.  See http://en.wikipedia.org/wiki/Incidence_matrix.\n\nHowever, it's not the first time that I've been frustrated with the behavior completely being different when a small change in input happens.  In fact, I remember complaining about the adjacency matrix/incidence matrix assumptions a long time ago.  I think it was part of one of my grand re-architecting schemes, though, so it got abandoned eventually :).",
    "created_at": "2009-02-04T03:28:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5171",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5171#issuecomment-39533",
    "user": "https://github.com/jasongrout"
}
```

William: when the matrix is non-square, we are assuming it is an incidence matrix; the error message is perfect.  See http://en.wikipedia.org/wiki/Incidence_matrix.

However, it's not the first time that I've been frustrated with the behavior completely being different when a small change in input happens.  In fact, I remember complaining about the adjacency matrix/incidence matrix assumptions a long time ago.  I think it was part of one of my grand re-architecting schemes, though, so it got abandoned eventually :).



---

archive/issue_comments_039534.json:
```json
{
    "body": "Patches here will depend on #3541 and its dependencies.",
    "created_at": "2009-02-14T23:16:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5171",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5171#issuecomment-39534",
    "user": "https://github.com/rlmill"
}
```

Patches here will depend on #3541 and its dependencies.



---

archive/issue_comments_039535.json:
```json
{
    "body": "This patch implements fixes for `Graph.__init__` but not `DiGraph.__init__`. It is not ready for review. It passes tests in `sage/graphs`.",
    "created_at": "2009-02-14T23:19:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5171",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5171#issuecomment-39535",
    "user": "https://github.com/rlmill"
}
```

This patch implements fixes for `Graph.__init__` but not `DiGraph.__init__`. It is not ready for review. It passes tests in `sage/graphs`.



---

archive/issue_comments_039536.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2009-02-17T18:40:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5171",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5171#issuecomment-39536",
    "user": "https://github.com/rlmill"
}
```

Changing status from new to assigned.



---

archive/issue_comments_039537.json:
```json
{
    "body": "This will allow us to close #5046 as well.",
    "created_at": "2009-02-17T18:40:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5171",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5171#issuecomment-39537",
    "user": "https://github.com/rlmill"
}
```

This will allow us to close #5046 as well.



---

archive/issue_comments_039538.json:
```json
{
    "body": "With only the first patch some trouble:\n\n```\n\tsage -t -long devel/sage/sage/graphs/graph.py # 1 doctests failed\n\tsage -t -long devel/sage/sage/combinat/crystals/crystals.py # 94 doctests failed\n\tsage -t -long devel/sage/sage/combinat/posets/posets.py # 2 doctests failed\n\tsage -t -long devel/sage/sage/combinat/crystals/fast_crystals.py # 64 doctests failed\n\tsage -t -long devel/sage/sage/combinat/crystals/tensor_product.py # 110 doctests failed\n\tsage -t -long devel/sage/sage/combinat/crystals/letters.py # 68 doctests failed\n\tsage -t -long devel/sage/sage/combinat/crystals/spins.py # 64 doctests failed\n```\n\n\nCheers,\n\nMichael",
    "created_at": "2009-02-17T19:01:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5171",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5171#issuecomment-39538",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

With only the first patch some trouble:

```
	sage -t -long devel/sage/sage/graphs/graph.py # 1 doctests failed
	sage -t -long devel/sage/sage/combinat/crystals/crystals.py # 94 doctests failed
	sage -t -long devel/sage/sage/combinat/posets/posets.py # 2 doctests failed
	sage -t -long devel/sage/sage/combinat/crystals/fast_crystals.py # 64 doctests failed
	sage -t -long devel/sage/sage/combinat/crystals/tensor_product.py # 110 doctests failed
	sage -t -long devel/sage/sage/combinat/crystals/letters.py # 68 doctests failed
	sage -t -long devel/sage/sage/combinat/crystals/spins.py # 64 doctests failed
```


Cheers,

Michael



---

archive/issue_comments_039539.json:
```json
{
    "body": "I believe this new patch addresses the issues above.",
    "created_at": "2009-02-17T21:11:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5171",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5171#issuecomment-39539",
    "user": "https://github.com/rlmill"
}
```

I believe this new patch addresses the issues above.



---

archive/issue_comments_039540.json:
```json
{
    "body": "The new version of the patch makes all doctests pass on sage.math.\n\nCheers,\n\nMichael",
    "created_at": "2009-02-17T21:25:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5171",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5171#issuecomment-39540",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

The new version of the patch makes all doctests pass on sage.math.

Cheers,

Michael



---

archive/issue_comments_039541.json:
```json
{
    "body": "REPORT:\n\n* All doctests pass in the graphs directory\n\n* old doctests don't fail in too disturbing a way\n\n* I definitely do not like at all the new multiple_edges function.  It should be split into two functions: has_multiple_edges() and allows_multiple_edges() and the current multiple_edges should be deprecated.  I personally would expect a function named \"multiple_edges\" to return a list of all multiple edges, which no variant of the current function does!  Having a check parameter that determines the functionality is particularly bad, given that check is used elsewhere all over in sage in a way that never changes the meaning of the output (it is always for speed).\n\n \nOtherwise I'm good with this patch.",
    "created_at": "2009-02-17T22:21:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5171",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5171#issuecomment-39541",
    "user": "https://github.com/williamstein"
}
```

REPORT:

* All doctests pass in the graphs directory

* old doctests don't fail in too disturbing a way

* I definitely do not like at all the new multiple_edges function.  It should be split into two functions: has_multiple_edges() and allows_multiple_edges() and the current multiple_edges should be deprecated.  I personally would expect a function named "multiple_edges" to return a list of all multiple edges, which no variant of the current function does!  Having a check parameter that determines the functionality is particularly bad, given that check is used elsewhere all over in sage in a way that never changes the meaning of the output (it is always for speed).

 
Otherwise I'm good with this patch.



---

archive/issue_comments_039542.json:
```json
{
    "body": "Attachment [trac_5171.patch](tarball://root/attachments/some-uuid/ticket5171/trac_5171.patch) by @rlmill created at 2009-02-17 23:28:40",
    "created_at": "2009-02-17T23:28:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5171",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5171#issuecomment-39542",
    "user": "https://github.com/rlmill"
}
```

Attachment [trac_5171.patch](tarball://root/attachments/some-uuid/ticket5171/trac_5171.patch) by @rlmill created at 2009-02-17 23:28:40



---

archive/issue_comments_039543.json:
```json
{
    "body": "This looks good. Excellent!",
    "created_at": "2009-02-17T23:33:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5171",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5171#issuecomment-39543",
    "user": "https://github.com/williamstein"
}
```

This looks good. Excellent!



---

archive/issue_comments_039544.json:
```json
{
    "body": "This latest patch requires one trivial doctest fix:\n\n```\nsage -t -long devel/sage/sage/groups/perm_gps/partn_ref/refinement_graphs.pyx\n**********************************************************************\nFile \"/scratch/mabshoff/sage-3.3.rc2/devel/sage-main/sage/groups/perm_gps/partn_ref/refinement_graphs.pyx\", line 808:\n    sage: sage.groups.perm_gps.partn_ref.refinement_graphs.random_tests()\nExpected:\n    All passed: ... random tests on ... graphs.\nGot:\n    doctest:1: DeprecationWarning: The function loops is replaced by allow_loops and allows_loops.\n    All passed: 560 random tests on 28 graphs.\n**********************************************************************\n```\n\nI am posting a reviewer patch shortly.\n\nCheers,\n\nMichael",
    "created_at": "2009-02-17T23:45:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5171",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5171#issuecomment-39544",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

This latest patch requires one trivial doctest fix:

```
sage -t -long devel/sage/sage/groups/perm_gps/partn_ref/refinement_graphs.pyx
**********************************************************************
File "/scratch/mabshoff/sage-3.3.rc2/devel/sage-main/sage/groups/perm_gps/partn_ref/refinement_graphs.pyx", line 808:
    sage: sage.groups.perm_gps.partn_ref.refinement_graphs.random_tests()
Expected:
    All passed: ... random tests on ... graphs.
Got:
    doctest:1: DeprecationWarning: The function loops is replaced by allow_loops and allows_loops.
    All passed: 560 random tests on 28 graphs.
**********************************************************************
```

I am posting a reviewer patch shortly.

Cheers,

Michael



---

archive/issue_comments_039545.json:
```json
{
    "body": "Attachment [trac_5171-reviewer.patch](tarball://root/attachments/some-uuid/ticket5171/trac_5171-reviewer.patch) by mabshoff created at 2009-02-18 00:07:51\n\nMike suggested the reviewer fix.\n\nCheers,\n\nMichael",
    "created_at": "2009-02-18T00:07:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5171",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5171#issuecomment-39545",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Attachment [trac_5171-reviewer.patch](tarball://root/attachments/some-uuid/ticket5171/trac_5171-reviewer.patch) by mabshoff created at 2009-02-18 00:07:51

Mike suggested the reviewer fix.

Cheers,

Michael



---

archive/issue_comments_039546.json:
```json
{
    "body": "Merged both patches in Sage 3.3.rc2.\n\nCheers,\n\nMichael",
    "created_at": "2009-02-18T00:08:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5171",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5171#issuecomment-39546",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged both patches in Sage 3.3.rc2.

Cheers,

Michael



---

archive/issue_events_005421.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2009-02-18T00:08:15Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/5171",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/5171#event-5421"
}
```



---

archive/issue_comments_039547.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-02-18T00:08:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5171",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5171#issuecomment-39547",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_039548.json:
```json
{
    "body": "Replying to [comment:12 mabshoff]:\n> Mike suggested the reviewer fix.\n\n+1",
    "created_at": "2009-02-18T00:16:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5171",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5171#issuecomment-39548",
    "user": "https://github.com/rlmill"
}
```

Replying to [comment:12 mabshoff]:
> Mike suggested the reviewer fix.

+1

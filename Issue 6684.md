# Issue 6684: [with patch, positive review] warnings when building reference manual in Sage 4.1.1.rc2

archive/issues_006684.json:
```json
{
    "body": "Assignee: tba\n\nCC:  @jhpalmieri\n\nI received the following warning messages when building the reference manual under Sage 4.1.1.rc2:\n\n```\nWARNING: /scratch/mvngu/sandbox-2/sage-4.1.1.rc2/local/lib/python2.6/site-packages/sage/graphs/graph.py:docstring of sage.graphs.graph.GenericGraph.kirchhoff_matrix:56: (WARNING/2) Literal block ends without a blank line; unexpected unindent.\nWARNING: /scratch/mvngu/sandbox-2/sage-4.1.1.rc2/local/lib/python2.6/site-packages/sage/graphs/graph.py:docstring of sage.graphs.graph.GenericGraph.laplacian_matrix:56: (WARNING/2) Literal block ends without a blank line; unexpected unindent.\nWARNING: /scratch/mvngu/sandbox-2/sage-4.1.1.rc2/local/lib/python2.6/site-packages/sage/graphs/graph.py:docstring of sage.graphs.graph.Graph.clique_number:19: (WARNING/2) Inline literal start-string without end-string.\n```\n\nIssue created by migration from https://trac.sagemath.org/ticket/6684\n\n",
    "closed_at": "2009-08-11T23:20:04Z",
    "created_at": "2009-08-07T10:39:55Z",
    "labels": [
        "component: documentation",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.1.1",
    "title": "[with patch, positive review] warnings when building reference manual in Sage 4.1.1.rc2",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/6684",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```
Assignee: tba

CC:  @jhpalmieri

I received the following warning messages when building the reference manual under Sage 4.1.1.rc2:

```
WARNING: /scratch/mvngu/sandbox-2/sage-4.1.1.rc2/local/lib/python2.6/site-packages/sage/graphs/graph.py:docstring of sage.graphs.graph.GenericGraph.kirchhoff_matrix:56: (WARNING/2) Literal block ends without a blank line; unexpected unindent.
WARNING: /scratch/mvngu/sandbox-2/sage-4.1.1.rc2/local/lib/python2.6/site-packages/sage/graphs/graph.py:docstring of sage.graphs.graph.GenericGraph.laplacian_matrix:56: (WARNING/2) Literal block ends without a blank line; unexpected unindent.
WARNING: /scratch/mvngu/sandbox-2/sage-4.1.1.rc2/local/lib/python2.6/site-packages/sage/graphs/graph.py:docstring of sage.graphs.graph.Graph.clique_number:19: (WARNING/2) Inline literal start-string without end-string.
```

Issue created by migration from https://trac.sagemath.org/ticket/6684





---

archive/issue_comments_054855.json:
```json
{
    "body": "Attachment [trac_6684-docbuild.patch](tarball://root/attachments/some-uuid/ticket6684/trac_6684-docbuild.patch) by mvngu created at 2009-08-07 10:59:02\n\nbased on Sage 4.1.1.rc2",
    "created_at": "2009-08-07T10:59:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6684",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6684#issuecomment-54855",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

Attachment [trac_6684-docbuild.patch](tarball://root/attachments/some-uuid/ticket6684/trac_6684-docbuild.patch) by mvngu created at 2009-08-07 10:59:02

based on Sage 4.1.1.rc2



---

archive/issue_comments_054856.json:
```json
{
    "body": "This fixes the warnings and the rendering of this page of the reference manual.  All tests pass.",
    "created_at": "2009-08-07T16:15:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6684",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6684#issuecomment-54856",
    "user": "https://github.com/jhpalmieri"
}
```

This fixes the warnings and the rendering of this page of the reference manual.  All tests pass.



---

archive/issue_comments_054857.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-08-11T23:20:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6684",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6684#issuecomment-54857",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

Resolution: fixed



---

archive/issue_events_015773.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mvngu",
    "created_at": "2009-08-11T23:20:04Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/6684",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/6684#event-15773"
}
```

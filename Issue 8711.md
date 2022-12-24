# Issue 8711: fix warnings when building the ref manual (4.4.alpha0)

archive/issues_008711.json:
```json
{
    "body": "Assignee: mvngu\n\nHere is a patch to fix the warnings...\n\nIssue created by migration from https://trac.sagemath.org/ticket/8711\n\n",
    "created_at": "2010-04-18T04:45:17Z",
    "labels": [
        "documentation",
        "major",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.4",
    "title": "fix warnings when building the ref manual (4.4.alpha0)",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/8711",
    "user": "@jhpalmieri"
}
```
Assignee: mvngu

Here is a patch to fix the warnings...

Issue created by migration from https://trac.sagemath.org/ticket/8711





---

archive/issue_comments_079485.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-04-18T07:06:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8711",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8711#issuecomment-79485",
    "user": "mvngu"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_079486.json:
```json
{
    "body": "Attachment [trac_8711-reference44alpha0.patch](tarball://root/attachments/some-uuid/ticket8711/trac_8711-reference44alpha0.patch) by mvngu created at 2010-04-18 07:06:56",
    "created_at": "2010-04-18T07:06:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8711",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8711#issuecomment-79486",
    "user": "mvngu"
}
```

Attachment [trac_8711-reference44alpha0.patch](tarball://root/attachments/some-uuid/ticket8711/trac_8711-reference44alpha0.patch) by mvngu created at 2010-04-18 07:06:56



---

archive/issue_comments_079487.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-04-18T07:07:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8711",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8711#issuecomment-79487",
    "user": "mvngu"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_079488.json:
```json
{
    "body": "Building the reference manual of Sage 4.4.alpha0 results in the following warnings:\n\n```\n/dev/shm/mvngu/sandbox/sage-4.4.alpha0-8711-ref/local/lib/python2.6/site-packages/sage/graphs/generic_graph.py:docstring of sage.graphs.generic_graph.GenericGraph.add_cycle:5: (ERROR/3) Unexpected indentation.\n/dev/shm/mvngu/sandbox/sage-4.4.alpha0-8711-ref/local/lib/python2.6/site-packages/sage/graphs/generic_graph.py:docstring of sage.graphs.generic_graph.GenericGraph.vertex_cover:26: (WARNING/2) Block quote ends without a blank line; unexpected unindent.\n/dev/shm/mvngu/sandbox/sage-4.4.alpha0-8711-ref/local/lib/python2.6/site-packages/sage/symbolic/units.py:docstring of sage.symbolic.units.unitdocs:15: (WARNING/2) Block quote ends without a blank line; unexpected unindent.\n/dev/shm/mvngu/sandbox/sage-4.4.alpha0-8711-ref/local/lib/python2.6/site-packages/sage/symbolic/units.py:docstring of sage.symbolic.units.unitdocs:18: (WARNING/2) Definition list ends without a blank line; unexpected unindent.\n```\n\nThe attached patch resolves those warnings as claimed.",
    "created_at": "2010-04-18T07:07:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8711",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8711#issuecomment-79488",
    "user": "mvngu"
}
```

Building the reference manual of Sage 4.4.alpha0 results in the following warnings:

```
/dev/shm/mvngu/sandbox/sage-4.4.alpha0-8711-ref/local/lib/python2.6/site-packages/sage/graphs/generic_graph.py:docstring of sage.graphs.generic_graph.GenericGraph.add_cycle:5: (ERROR/3) Unexpected indentation.
/dev/shm/mvngu/sandbox/sage-4.4.alpha0-8711-ref/local/lib/python2.6/site-packages/sage/graphs/generic_graph.py:docstring of sage.graphs.generic_graph.GenericGraph.vertex_cover:26: (WARNING/2) Block quote ends without a blank line; unexpected unindent.
/dev/shm/mvngu/sandbox/sage-4.4.alpha0-8711-ref/local/lib/python2.6/site-packages/sage/symbolic/units.py:docstring of sage.symbolic.units.unitdocs:15: (WARNING/2) Block quote ends without a blank line; unexpected unindent.
/dev/shm/mvngu/sandbox/sage-4.4.alpha0-8711-ref/local/lib/python2.6/site-packages/sage/symbolic/units.py:docstring of sage.symbolic.units.unitdocs:18: (WARNING/2) Definition list ends without a blank line; unexpected unindent.
```

The attached patch resolves those warnings as claimed.



---

archive/issue_comments_079489.json:
```json
{
    "body": "Merged \"trac_8711-reference44alpha0.patch\" into 4.4.alpha1.",
    "created_at": "2010-04-19T05:18:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8711",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8711#issuecomment-79489",
    "user": "@jhpalmieri"
}
```

Merged "trac_8711-reference44alpha0.patch" into 4.4.alpha1.



---

archive/issue_comments_079490.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-04-19T05:18:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8711",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8711#issuecomment-79490",
    "user": "@jhpalmieri"
}
```

Resolution: fixed

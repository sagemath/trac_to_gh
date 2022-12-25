# Issue 7853: block_and_cut_vertices is inconsistent when graph has one vertex

archive/issues_007853.json:
```json
{
    "body": "Assignee: @rlmill\n\nCC:  hartke @rlmill @nathanncohen\n\nCurrently, block_and_cut_vertices says that the vertex in a single-vertex graph is a cut vertex:\n\n\n```\nsage: Graph(1).blocks_and_cut_vertices()\n([0], [0])\n```\n\n\nAccording to the definition of cut vertices given in the documentation of the function, a cut vertex, when removed, increases the connected components of the graph.  Either that documentation should be changed to mention a corner case, or (preferably), the above computation should look like:\n\n\n```\nsage: Graph(1).blocks_and_cut_vertices()\n([0], [])\n```\n\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/7853\n\n",
    "created_at": "2010-01-06T06:06:06Z",
    "labels": [
        "component: graph theory",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.3.1",
    "title": "block_and_cut_vertices is inconsistent when graph has one vertex",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/7853",
    "user": "https://github.com/jasongrout"
}
```
Assignee: @rlmill

CC:  hartke @rlmill @nathanncohen

Currently, block_and_cut_vertices says that the vertex in a single-vertex graph is a cut vertex:


```
sage: Graph(1).blocks_and_cut_vertices()
([0], [0])
```


According to the definition of cut vertices given in the documentation of the function, a cut vertex, when removed, increases the connected components of the graph.  Either that documentation should be changed to mention a corner case, or (preferably), the above computation should look like:


```
sage: Graph(1).blocks_and_cut_vertices()
([0], [])
```



Issue created by migration from https://trac.sagemath.org/ticket/7853





---

archive/issue_comments_067924.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-01-06T10:24:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7853",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7853#issuecomment-67924",
    "user": "https://github.com/nathanncohen"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_067925.json:
```json
{
    "body": "Here it is ! Actually the answer [0],[0] seemed deliberate in the code, but my tests with the patch applied did not show any error coming from the fix :-)\n\n( Apply on top of patches from #7634 )\n\nNathann",
    "created_at": "2010-01-06T10:24:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7853",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7853#issuecomment-67925",
    "user": "https://github.com/nathanncohen"
}
```

Here it is ! Actually the answer [0],[0] seemed deliberate in the code, but my tests with the patch applied did not show any error coming from the fix :-)

( Apply on top of patches from #7634 )

Nathann



---

archive/issue_comments_067926.json:
```json
{
    "body": "Apply on top of patches from #7634",
    "created_at": "2010-01-06T10:24:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7853",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7853#issuecomment-67926",
    "user": "https://github.com/nathanncohen"
}
```

Apply on top of patches from #7634



---

archive/issue_comments_067927.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-01-06T16:26:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7853",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7853#issuecomment-67927",
    "user": "https://github.com/rlmill"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_067928.json:
```json
{
    "body": "Attachment [trac_7853.patch](tarball://root/attachments/some-uuid/ticket7853/trac_7853.patch) by @rlmill created at 2010-01-06 16:26:20\n\nLooks good to me.",
    "created_at": "2010-01-06T16:26:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7853",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7853#issuecomment-67928",
    "user": "https://github.com/rlmill"
}
```

Attachment [trac_7853.patch](tarball://root/attachments/some-uuid/ticket7853/trac_7853.patch) by @rlmill created at 2010-01-06 16:26:20

Looks good to me.



---

archive/issue_events_008068.json:
```json
{
    "actor": "@rlmill",
    "created_at": "2010-01-13T04:51:06Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/7853",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/7853#event-8068"
}
```



---

archive/issue_comments_067929.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-01-13T04:51:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7853",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7853#issuecomment-67929",
    "user": "https://github.com/rlmill"
}
```

Resolution: fixed

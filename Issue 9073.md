# Issue 9073: Handle multigraphs better in planarity

archive/issues_009073.json:
```json
{
    "body": "Assignee: @aghitza\n\nCC:  @rlmill\n\n\n```\nsage: G = Graph({0:[1,1]}, multiedges=True)\nsage: G.is_planar()\n---------------------------------------------------------------------------\nKeyError                                  Traceback (most recent call last)\n\n/mnt/usb1/scratch/boothby/sage-4.4.2/<ipython console> in <module>()\n\n/mnt/usb1/scratch/boothby/sage-4.4.2/local/lib/python2.6/site-packages/sage/graphs/generic_graph.pyc in is_planar(self, on_embedding, kuratowski, set_embedding, set_pos)\n   2217             from sage.graphs.planarity import is_planar\n   2218             G = self.to_undirected()\n-> 2219             planar = is_planar(G,kuratowski=kuratowski,set_pos=set_pos,set_embedding=set_embedding)\n   2220             if kuratowski:\n   2221                 bool_result = planar[0]\n\n/mnt/usb1/scratch/boothby/sage-4.4.2/local/lib/python2.6/site-packages/sage/graphs/planarity.so in sage.graphs.planarity.is_planar (sage/graphs/planarity.c:1327)()\n\nKeyError: -1\nsage: G = Graph({0:[1,1,1,1,1,1,1,1,1,1,1,1,1]}, multiedges=True)\nsage: G.is_planar()\nFalse\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/9073\n\n",
    "created_at": "2010-05-28T03:57:01Z",
    "labels": [
        "component: algebra",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.5",
    "title": "Handle multigraphs better in planarity",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/9073",
    "user": "https://trac.sagemath.org/admin/accounts/users/boothby"
}
```
Assignee: @aghitza

CC:  @rlmill


```
sage: G = Graph({0:[1,1]}, multiedges=True)
sage: G.is_planar()
---------------------------------------------------------------------------
KeyError                                  Traceback (most recent call last)

/mnt/usb1/scratch/boothby/sage-4.4.2/<ipython console> in <module>()

/mnt/usb1/scratch/boothby/sage-4.4.2/local/lib/python2.6/site-packages/sage/graphs/generic_graph.pyc in is_planar(self, on_embedding, kuratowski, set_embedding, set_pos)
   2217             from sage.graphs.planarity import is_planar
   2218             G = self.to_undirected()
-> 2219             planar = is_planar(G,kuratowski=kuratowski,set_pos=set_pos,set_embedding=set_embedding)
   2220             if kuratowski:
   2221                 bool_result = planar[0]

/mnt/usb1/scratch/boothby/sage-4.4.2/local/lib/python2.6/site-packages/sage/graphs/planarity.so in sage.graphs.planarity.is_planar (sage/graphs/planarity.c:1327)()

KeyError: -1
sage: G = Graph({0:[1,1,1,1,1,1,1,1,1,1,1,1,1]}, multiedges=True)
sage: G.is_planar()
False
```


Issue created by migration from https://trac.sagemath.org/ticket/9073





---

archive/issue_comments_084040.json:
```json
{
    "body": "Changing priority from major to minor.",
    "created_at": "2010-05-28T04:00:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9073",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9073#issuecomment-84040",
    "user": "https://trac.sagemath.org/admin/accounts/users/boothby"
}
```

Changing priority from major to minor.



---

archive/issue_comments_084041.json:
```json
{
    "body": "Changing component from algebra to graph theory.",
    "created_at": "2010-05-28T04:00:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9073",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9073#issuecomment-84041",
    "user": "https://trac.sagemath.org/admin/accounts/users/boothby"
}
```

Changing component from algebra to graph theory.



---

archive/issue_comments_084042.json:
```json
{
    "body": "Changing assignee from @aghitza to jason, ncohen, rlm.",
    "created_at": "2010-05-28T04:00:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9073",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9073#issuecomment-84042",
    "user": "https://trac.sagemath.org/admin/accounts/users/boothby"
}
```

Changing assignee from @aghitza to jason, ncohen, rlm.



---

archive/issue_comments_084043.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-06-15T19:43:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9073",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9073#issuecomment-84043",
    "user": "https://github.com/rlmill"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_084044.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-06-17T19:49:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9073",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9073#issuecomment-84044",
    "user": "https://trac.sagemath.org/admin/accounts/users/boothby"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_084045.json:
```json
{
    "body": "works!",
    "created_at": "2010-06-17T19:49:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9073",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9073#issuecomment-84045",
    "user": "https://trac.sagemath.org/admin/accounts/users/boothby"
}
```

works!



---

archive/issue_comments_084046.json:
```json
{
    "body": "Changing status from positive_review to needs_work.",
    "created_at": "2010-06-17T19:52:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9073",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9073#issuecomment-84046",
    "user": "https://trac.sagemath.org/admin/accounts/users/boothby"
}
```

Changing status from positive_review to needs_work.



---

archive/issue_comments_084047.json:
```json
{
    "body": "oops, jumped the gun.  we need to check for loops, too.\n\n\n```\nsage: G = Graph(loops=True)\nsage: G.add_edge(0,0)\nsage: G.add_edge(1,0)\nsage: G.is_planar(set_embedding=True)\nsage: G.get_embedding()\nTraceback (click to the left of this block for traceback)\n...\nException: Looped graph on 2 vertices has been modified and the\nembedding is no longer valid.\n```\n",
    "created_at": "2010-06-17T19:52:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9073",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9073#issuecomment-84047",
    "user": "https://trac.sagemath.org/admin/accounts/users/boothby"
}
```

oops, jumped the gun.  we need to check for loops, too.


```
sage: G = Graph(loops=True)
sage: G.add_edge(0,0)
sage: G.add_edge(1,0)
sage: G.is_planar(set_embedding=True)
sage: G.get_embedding()
Traceback (click to the left of this block for traceback)
...
Exception: Looped graph on 2 vertices has been modified and the
embedding is no longer valid.
```




---

archive/issue_comments_084048.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2010-06-17T20:00:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9073",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9073#issuecomment-84048",
    "user": "https://trac.sagemath.org/admin/accounts/users/boothby"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_084049.json:
```json
{
    "body": "Attachment [trac_9073.patch](tarball://root/attachments/some-uuid/ticket9073/trac_9073.patch) by boothby created at 2010-06-17 20:00:44",
    "created_at": "2010-06-17T20:00:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9073",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9073#issuecomment-84049",
    "user": "https://trac.sagemath.org/admin/accounts/users/boothby"
}
```

Attachment [trac_9073.patch](tarball://root/attachments/some-uuid/ticket9073/trac_9073.patch) by boothby created at 2010-06-17 20:00:44



---

archive/issue_comments_084050.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-06-17T20:01:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9073",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9073#issuecomment-84050",
    "user": "https://trac.sagemath.org/admin/accounts/users/boothby"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_084051.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-06-29T16:48:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9073",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9073#issuecomment-84051",
    "user": "https://github.com/rlmill"
}
```

Resolution: fixed

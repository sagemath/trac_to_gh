# Issue 4445: is_isomorphic throws an error when the graph is compared to itself

archive/issues_004445.json:
```json
{
    "body": "Assignee: @rlmill\n\nConsider:\n\n\n```\nsage: g=graphs.HeawoodGraph()\nsage: g.is_isomorphic(g)\n---------------------------------------------------------------------------\nTypeError                                 Traceback (most recent call last)\n\n/home/jason/<ipython console> in <module>()\n\n/home/jason/sage/local/lib/python2.5/site-packages/sage/graphs/graph.pyc in is_isomorphic(self, other, certify, verbosity, edge_labels)\n   6540             G2 = other; partition2 = [other.vertices()]\n   6541         from sage.misc.flatten import flatten\n-> 6542         isom = isomorphic(G, G2, partition, flatten(partition2, max_level=1), (self._directed or self.loops()), 1)\n   6543         if not isom and certify:\n   6544             return False, None\n\n/home/jason/sage/local/lib/python2.5/site-packages/sage/groups/perm_gps/partn_ref/refinement_graphs.so in sage.groups.perm_gps.partn_ref.refinement_graphs.isomorphic (sage/groups/perm_gps/partn_ref/refinement_graphs.c:9946)()\n\nTypeError: 'NoneType' object is unsubscriptable\n```\n\n\nHowever, \n\n```\nsage: g.is_isomorphic(graphs.HeawoodGraph())\nTrue\n```\n\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/4445\n\n",
    "created_at": "2008-11-05T15:04:17Z",
    "labels": [
        "component: graph theory",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.2",
    "title": "is_isomorphic throws an error when the graph is compared to itself",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/4445",
    "user": "https://github.com/jasongrout"
}
```
Assignee: @rlmill

Consider:


```
sage: g=graphs.HeawoodGraph()
sage: g.is_isomorphic(g)
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)

/home/jason/<ipython console> in <module>()

/home/jason/sage/local/lib/python2.5/site-packages/sage/graphs/graph.pyc in is_isomorphic(self, other, certify, verbosity, edge_labels)
   6540             G2 = other; partition2 = [other.vertices()]
   6541         from sage.misc.flatten import flatten
-> 6542         isom = isomorphic(G, G2, partition, flatten(partition2, max_level=1), (self._directed or self.loops()), 1)
   6543         if not isom and certify:
   6544             return False, None

/home/jason/sage/local/lib/python2.5/site-packages/sage/groups/perm_gps/partn_ref/refinement_graphs.so in sage.groups.perm_gps.partn_ref.refinement_graphs.isomorphic (sage/groups/perm_gps/partn_ref/refinement_graphs.c:9946)()

TypeError: 'NoneType' object is unsubscriptable
```


However, 

```
sage: g.is_isomorphic(graphs.HeawoodGraph())
True
```



Issue created by migration from https://trac.sagemath.org/ticket/4445





---

archive/issue_comments_032639.json:
```json
{
    "body": "Attachment [trac_4445-is_isom_fail.patch](tarball://root/attachments/some-uuid/ticket4445/trac_4445-is_isom_fail.patch) by @jasongrout created at 2008-11-05 20:31:35\n\nThis does indeed seem to fix the problem.  Thanks for the speedy work!  doctests in graph.py pass.\n\nPositive review.",
    "created_at": "2008-11-05T20:31:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4445",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4445#issuecomment-32639",
    "user": "https://github.com/jasongrout"
}
```

Attachment [trac_4445-is_isom_fail.patch](tarball://root/attachments/some-uuid/ticket4445/trac_4445-is_isom_fail.patch) by @jasongrout created at 2008-11-05 20:31:35

This does indeed seem to fix the problem.  Thanks for the speedy work!  doctests in graph.py pass.

Positive review.



---

archive/issue_comments_032640.json:
```json
{
    "body": "Merged in Sage 3.2.alpha3",
    "created_at": "2008-11-05T21:25:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4445",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4445#issuecomment-32640",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged in Sage 3.2.alpha3



---

archive/issue_comments_032641.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-11-05T21:25:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4445",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4445#issuecomment-32641",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed



---

archive/issue_events_004691.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2008-11-05T21:25:37Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/4445",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/4445#event-4691"
}
```

# Issue 2676: [with patch, needs easy review] is_equitable: flatten flattens too much!

archive/issues_002676.json:
```json
{
    "body": "Assignee: rlm\n\nThis is the problem, which is now a doctest:\n\n```\nsage: ss = (graphs.WheelGraph(5)).line_graph(labels=False)\nsage: prt = [[(0, 1)], [(0, 2), (0, 3), (0, 4), (1, 2), (1, 4)], [(2, 3), (3, 4)]]\nsage: ss.is_equitable(prt)\n---------------------------------------------------------------------------\n<type 'exceptions.TypeError'>             Traceback (most recent call last)\n\n/Users/rlmill/sage-2.11.alpha1/<ipython console> in <module>()\n\n/Users/rlmill/sage-2.11.alpha1/local/lib/python2.5/site-packages/sage/graphs/graph.py in is_equitable(self, partition, quotient_matrix)\n   5477         from sage.misc.misc import uniq\n   5478         if sorted(flatten(partition)) != self.vertices() or any(len(cell)==0 for cell in partition):\n-> 5479             raise TypeError(\"Partition (%s) is not valid for this graph.\"%partition)\n   5480         if quotient_matrix:\n   5481             from sage.matrix.constructor import Matrix\n\n<type 'exceptions.TypeError'>: Partition ([[(0, 1)], [(0, 2), (0, 3), (0, 4), (1, 2), (1, 4)], [(2, 3), (3, 4)]]) is not valid for this graph.\n```\n\n\nReported by Chris Godsil.\n\nIssue created by migration from https://trac.sagemath.org/ticket/2676\n\n",
    "created_at": "2008-03-26T17:41:40Z",
    "labels": [
        "graph theory",
        "major",
        "bug"
    ],
    "title": "[with patch, needs easy review] is_equitable: flatten flattens too much!",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/2676",
    "user": "rlm"
}
```
Assignee: rlm

This is the problem, which is now a doctest:

```
sage: ss = (graphs.WheelGraph(5)).line_graph(labels=False)
sage: prt = [[(0, 1)], [(0, 2), (0, 3), (0, 4), (1, 2), (1, 4)], [(2, 3), (3, 4)]]
sage: ss.is_equitable(prt)
---------------------------------------------------------------------------
<type 'exceptions.TypeError'>             Traceback (most recent call last)

/Users/rlmill/sage-2.11.alpha1/<ipython console> in <module>()

/Users/rlmill/sage-2.11.alpha1/local/lib/python2.5/site-packages/sage/graphs/graph.py in is_equitable(self, partition, quotient_matrix)
   5477         from sage.misc.misc import uniq
   5478         if sorted(flatten(partition)) != self.vertices() or any(len(cell)==0 for cell in partition):
-> 5479             raise TypeError("Partition (%s) is not valid for this graph."%partition)
   5480         if quotient_matrix:
   5481             from sage.matrix.constructor import Matrix

<type 'exceptions.TypeError'>: Partition ([[(0, 1)], [(0, 2), (0, 3), (0, 4), (1, 2), (1, 4)], [(2, 3), (3, 4)]]) is not valid for this graph.
```


Reported by Chris Godsil.

Issue created by migration from https://trac.sagemath.org/ticket/2676





---

archive/issue_comments_018411.json:
```json
{
    "body": "Attachment [2676-equitable-flatten.patch](tarball://root/attachments/some-uuid/ticket2676/2676-equitable-flatten.patch) by rlm created at 2008-03-26 17:43:42",
    "created_at": "2008-03-26T17:43:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2676",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2676#issuecomment-18411",
    "user": "rlm"
}
```

Attachment [2676-equitable-flatten.patch](tarball://root/attachments/some-uuid/ticket2676/2676-equitable-flatten.patch) by rlm created at 2008-03-26 17:43:42



---

archive/issue_comments_018412.json:
```json
{
    "body": "Attachment [2676-equitable-refinement.patch](tarball://root/attachments/some-uuid/ticket2676/2676-equitable-refinement.patch) by rlm created at 2008-03-26 19:57:47\n\nApply this as well. Fixes a related problem in the next function down. Also reported by Chris Godsil.",
    "created_at": "2008-03-26T19:57:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2676",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2676#issuecomment-18412",
    "user": "rlm"
}
```

Attachment [2676-equitable-refinement.patch](tarball://root/attachments/some-uuid/ticket2676/2676-equitable-refinement.patch) by rlm created at 2008-03-26 19:57:47

Apply this as well. Fixes a related problem in the next function down. Also reported by Chris Godsil.



---

archive/issue_comments_018413.json:
```json
{
    "body": "Attachment [2676-equitable-refinement-flatten.patch](tarball://root/attachments/some-uuid/ticket2676/2676-equitable-refinement-flatten.patch) by rlm created at 2008-03-26 20:08:14\n\nOops. Apply this one too. Fixes the original problem in the other function.",
    "created_at": "2008-03-26T20:08:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2676",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2676#issuecomment-18413",
    "user": "rlm"
}
```

Attachment [2676-equitable-refinement-flatten.patch](tarball://root/attachments/some-uuid/ticket2676/2676-equitable-refinement-flatten.patch) by rlm created at 2008-03-26 20:08:14

Oops. Apply this one too. Fixes the original problem in the other function.



---

archive/issue_comments_018414.json:
```json
{
    "body": "These 3 patches fix the bug, are documented and pass the doctests.  Ready for inclusion.",
    "created_at": "2008-03-27T21:34:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2676",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2676#issuecomment-18414",
    "user": "ekirkman"
}
```

These 3 patches fix the bug, are documented and pass the doctests.  Ready for inclusion.



---

archive/issue_comments_018415.json:
```json
{
    "body": "Well, not that I am paranoid, but applying all three patches works for me, too.\n\nCheers,\n\nMichael",
    "created_at": "2008-03-28T07:21:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2676",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2676#issuecomment-18415",
    "user": "mabshoff"
}
```

Well, not that I am paranoid, but applying all three patches works for me, too.

Cheers,

Michael



---

archive/issue_comments_018416.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-03-28T07:21:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2676",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2676#issuecomment-18416",
    "user": "mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_018417.json:
```json
{
    "body": "Merged in Sage 2.11.alpha2",
    "created_at": "2008-03-28T07:21:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2676",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2676#issuecomment-18417",
    "user": "mabshoff"
}
```

Merged in Sage 2.11.alpha2

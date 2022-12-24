# Issue 1961: graph_isom bug

archive/issues_001961.json:
```json
{
    "body": "Assignee: rlm\n\n\n```\ng1 = graphs.EmptyGraph()\ng2 = graphs.EmptyGraph()\n\ng1.add_edges([(1, 17, None), (1, 21, None), (1, 25, None), (2, 17,\nNone), (2, 22, None), (2, 26, None), (3, 17, None), (3, 23, None), (3,\n27, None), (4, 17, None), (4, 24, None), (4, 28, None), (5, 18, None),\n(5, 21, None), (5, 26, None), (6, 18, None), (6, 22, None), (6, 27,\nNone), (7, 18, None), (7, 23, None), (7, 28, None), (8, 18, None), (8,\n24, None), (8, 25, None), (9, 19, None), (9, 21, None), (9, 27, None),\n(10, 19, None), (10, 22, None), (10, 28, None), (11, 19, None), (11,\n23, None), (11, 25, None), (12, 19, None), (12, 24, None), (12, 26,\nNone), (13, 20, None), (13, 21, None), (13, 28, None), (14, 20, None),\n(14, 22, None), (14, 25, None), (15, 20, None), (15, 23, None), (15,\n26, None), (16, 20, None), (16, 24, None), (16, 27, None), (17, 29,\nNone), (18, 29, None), (19, 29, None), (20, 29, None), (21, 30, None),\n(22, 30, None), (23, 30, None), (24, 30, None), (25, 31, None), (26,\n31, None), (27, 31, None), (28, 31, None)])\n\ng2.add_edges([(1, 17, None), (1, 21, None), (1, 28, None), (2, 17,\nNone), (2, 22, None), (2, 25, None), (3, 17, None), (3, 23, None), (3,\n26, None), (4, 17, None), (4, 24, None), (4, 27, None), (5, 18, None),\n(5, 21, None), (5, 26, None), (6, 18, None), (6, 22, None), (6, 27,\nNone), (7, 18, None), (7, 23, None), (7, 28, None), (8, 18, None), (8,\n24, None), (8, 25, None), (9, 19, None), (9, 21, None), (9, 27, None),\n(10, 19, None), (10, 22, None), (10, 28, None), (11, 19, None), (11,\n23, None), (11, 25, None), (12, 19, None), (12, 24, None), (12, 26,\nNone), (13, 20, None), (13, 21, None), (13, 25, None), (14, 20, None),\n(14, 22, None), (14, 26, None), (15, 20, None), (15, 23, None), (15,\n27, None), (16, 20, None), (16, 24, None), (16, 28, None), (17, 29,\nNone), (18, 29, None), (19, 29, None), (20, 29, None), (21, 30, None),\n(22, 30, None), (23, 30, None), (24, 30, None), (25, 31, None), (26,\n31, None), (27, 31, None), (28, 31, None)])\n\nperm = {0:0, 1: 13, 2: 14, 3: 15, 4: 16, 5: 5, 6: 6, 7: 7, 8: 8, 9: 9,\n10: 10, 11: 11, 12: 12, 13: 1, 14: 2, 15: 3, 16: 4, 17: 20, 18: 18,\n19: 19, 20: 17, 21: 21, 22: 22, 23: 23, 24: 24, 25: 25, 26: 26, 27:\n27, 28: 28, 29: 29, 30: 30, 31: 31}\n\n# This says no:\nprint g1.is_isomorphic(g2)\n\n# But I can find a vertex relabelling...\ng1.relabel(perm)\n# ... and this says yes:\nprint g1.is_isomorphic(g2)\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/1961\n\n",
    "created_at": "2008-01-28T18:24:35Z",
    "labels": [
        "graph theory",
        "major",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-2.10.2",
    "title": "graph_isom bug",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/1961",
    "user": "rlm"
}
```
Assignee: rlm


```
g1 = graphs.EmptyGraph()
g2 = graphs.EmptyGraph()

g1.add_edges([(1, 17, None), (1, 21, None), (1, 25, None), (2, 17,
None), (2, 22, None), (2, 26, None), (3, 17, None), (3, 23, None), (3,
27, None), (4, 17, None), (4, 24, None), (4, 28, None), (5, 18, None),
(5, 21, None), (5, 26, None), (6, 18, None), (6, 22, None), (6, 27,
None), (7, 18, None), (7, 23, None), (7, 28, None), (8, 18, None), (8,
24, None), (8, 25, None), (9, 19, None), (9, 21, None), (9, 27, None),
(10, 19, None), (10, 22, None), (10, 28, None), (11, 19, None), (11,
23, None), (11, 25, None), (12, 19, None), (12, 24, None), (12, 26,
None), (13, 20, None), (13, 21, None), (13, 28, None), (14, 20, None),
(14, 22, None), (14, 25, None), (15, 20, None), (15, 23, None), (15,
26, None), (16, 20, None), (16, 24, None), (16, 27, None), (17, 29,
None), (18, 29, None), (19, 29, None), (20, 29, None), (21, 30, None),
(22, 30, None), (23, 30, None), (24, 30, None), (25, 31, None), (26,
31, None), (27, 31, None), (28, 31, None)])

g2.add_edges([(1, 17, None), (1, 21, None), (1, 28, None), (2, 17,
None), (2, 22, None), (2, 25, None), (3, 17, None), (3, 23, None), (3,
26, None), (4, 17, None), (4, 24, None), (4, 27, None), (5, 18, None),
(5, 21, None), (5, 26, None), (6, 18, None), (6, 22, None), (6, 27,
None), (7, 18, None), (7, 23, None), (7, 28, None), (8, 18, None), (8,
24, None), (8, 25, None), (9, 19, None), (9, 21, None), (9, 27, None),
(10, 19, None), (10, 22, None), (10, 28, None), (11, 19, None), (11,
23, None), (11, 25, None), (12, 19, None), (12, 24, None), (12, 26,
None), (13, 20, None), (13, 21, None), (13, 25, None), (14, 20, None),
(14, 22, None), (14, 26, None), (15, 20, None), (15, 23, None), (15,
27, None), (16, 20, None), (16, 24, None), (16, 28, None), (17, 29,
None), (18, 29, None), (19, 29, None), (20, 29, None), (21, 30, None),
(22, 30, None), (23, 30, None), (24, 30, None), (25, 31, None), (26,
31, None), (27, 31, None), (28, 31, None)])

perm = {0:0, 1: 13, 2: 14, 3: 15, 4: 16, 5: 5, 6: 6, 7: 7, 8: 8, 9: 9,
10: 10, 11: 11, 12: 12, 13: 1, 14: 2, 15: 3, 16: 4, 17: 20, 18: 18,
19: 19, 20: 17, 21: 21, 22: 22, 23: 23, 24: 24, 25: 25, 26: 26, 27:
27, 28: 28, 29: 29, 30: 30, 31: 31}

# This says no:
print g1.is_isomorphic(g2)

# But I can find a vertex relabelling...
g1.relabel(perm)
# ... and this says yes:
print g1.is_isomorphic(g2)
```


Issue created by migration from https://trac.sagemath.org/ticket/1961





---

archive/issue_comments_012660.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2008-01-28T19:11:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1961",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1961#issuecomment-12660",
    "user": "rlm"
}
```

Changing status from new to assigned.



---

archive/issue_comments_012661.json:
```json
{
    "body": "The real problem can be boiled down a little:\n\n```\nsage: G = Graph('^????????????????????{??N??@w??FaGa?PCO@CP?AGa?_QO?Q@G?CcA??cc????Bo????{????F_')\nsage: G.relabel([i+1 for i in xrange(31)])\nsage: perm = {4:16, 16:4}\nsage: A = G.canonical_label()\nsage: B = G.relabel(perm, inplace=False).canonical_label()\nsage: A == B\nFalse\n```\n",
    "created_at": "2008-02-06T19:08:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1961",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1961#issuecomment-12661",
    "user": "rlm"
}
```

The real problem can be boiled down a little:

```
sage: G = Graph('^????????????????????{??N??@w??FaGa?PCO@CP?AGa?_QO?Q@G?CcA??cc????Bo????{????F_')
sage: G.relabel([i+1 for i in xrange(31)])
sage: perm = {4:16, 16:4}
sage: A = G.canonical_label()
sage: B = G.relabel(perm, inplace=False).canonical_label()
sage: A == B
False
```




---

archive/issue_comments_012662.json:
```json
{
    "body": "Slightly easier to digest still:\n\n```\nsage: G = Graph('^????????????????????{??N??@w??FaGa?PCO@CP?AGa?_QO?Q@G?CcA??cc????Bo????{????F_')\nsage: perm = {3:15, 15:3}\nsage: H = G.relabel(perm, inplace=False)\nsage: G.canonical_label() == H.canonical_label()\nFalse\n```\n",
    "created_at": "2008-02-06T19:54:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1961",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1961#issuecomment-12662",
    "user": "rlm"
}
```

Slightly easier to digest still:

```
sage: G = Graph('^????????????????????{??N??@w??FaGa?PCO@CP?AGa?_QO?Q@G?CcA??cc????Bo????{????F_')
sage: perm = {3:15, 15:3}
sage: H = G.relabel(perm, inplace=False)
sage: G.canonical_label() == H.canonical_label()
False
```




---

archive/issue_comments_012663.json:
```json
{
    "body": "After applying the patches at #2085, and setting use_indicator_function to False, the example returns True! This is our first clue...",
    "created_at": "2008-02-16T21:06:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1961",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1961#issuecomment-12663",
    "user": "rlm"
}
```

After applying the patches at #2085, and setting use_indicator_function to False, the example returns True! This is our first clue...



---

archive/issue_comments_012664.json:
```json
{
    "body": "Attachment [1961-only_update_qzb_if_zero.patch](tarball://root/attachments/some-uuid/ticket1961/1961-only_update_qzb_if_zero.patch) by rlm created at 2008-02-17 02:41:22\n\nAfter three weeks, the problem is solved. The patch should apply on top of #2186, which depends on a few things...",
    "created_at": "2008-02-17T02:41:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1961",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1961#issuecomment-12664",
    "user": "rlm"
}
```

Attachment [1961-only_update_qzb_if_zero.patch](tarball://root/attachments/some-uuid/ticket1961/1961-only_update_qzb_if_zero.patch) by rlm created at 2008-02-17 02:41:22

After three weeks, the problem is solved. The patch should apply on top of #2186, which depends on a few things...



---

archive/issue_comments_012665.json:
```json
{
    "body": "The patch for this problem also fixes #1360, so make sure to close that ticket once this patch is applied.\n\nCheers,\n\nMichael",
    "created_at": "2008-02-18T21:04:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1961",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1961#issuecomment-12665",
    "user": "mabshoff"
}
```

The patch for this problem also fixes #1360, so make sure to close that ticket once this patch is applied.

Cheers,

Michael



---

archive/issue_comments_012666.json:
```json
{
    "body": "After applying this patch, the patch from #2211 should also be applied.",
    "created_at": "2008-02-19T19:45:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1961",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1961#issuecomment-12666",
    "user": "rlm"
}
```

After applying this patch, the patch from #2211 should also be applied.



---

archive/issue_comments_012667.json:
```json
{
    "body": "looks good.",
    "created_at": "2008-02-19T21:17:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1961",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1961#issuecomment-12667",
    "user": "jason"
}
```

looks good.



---

archive/issue_comments_012668.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-02-19T22:18:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1961",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1961#issuecomment-12668",
    "user": "mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_012669.json:
```json
{
    "body": "Merged in Sage 2.10.2.alpha2",
    "created_at": "2008-02-19T22:18:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1961",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1961#issuecomment-12669",
    "user": "mabshoff"
}
```

Merged in Sage 2.10.2.alpha2

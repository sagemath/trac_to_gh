# Issue 6839: [with patch, positive review] Implementation of crystal of letters for type E7

archive/issues_006839.json:
```json
{
    "body": "Assignee: @anneschilling\n\nCC:  sage-combinat\n\nKeywords: combinat, crystals\n\n- Implemented crystal of letters for type E7\n\n- Added the method that goes to the highest weight element from any crystal element (living in a highest weight crystal)\n\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/6839\n\n",
    "closed_at": "2009-09-07T17:25:36Z",
    "created_at": "2009-08-29T06:34:56Z",
    "labels": [
        "component: combinatorics"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.1.2",
    "title": "[with patch, positive review] Implementation of crystal of letters for type E7",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/6839",
    "user": "https://github.com/anneschilling"
}
```
Assignee: @anneschilling

CC:  sage-combinat

Keywords: combinat, crystals

- Implemented crystal of letters for type E7

- Added the method that goes to the highest weight element from any crystal element (living in a highest weight crystal)



Issue created by migration from https://trac.sagemath.org/ticket/6839





---

archive/issue_comments_056302.json:
```json
{
    "body": "Attachment [trac_6839-crystal-E7-as.patch](tarball://root/attachments/some-uuid/ticket6839/trac_6839-crystal-E7-as.patch) by @anneschilling created at 2009-08-29 06:48:41",
    "created_at": "2009-08-29T06:48:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6839",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6839#issuecomment-56302",
    "user": "https://github.com/anneschilling"
}
```

Attachment [trac_6839-crystal-E7-as.patch](tarball://root/attachments/some-uuid/ticket6839/trac_6839-crystal-E7-as.patch) by @anneschilling created at 2009-08-29 06:48:41



---

archive/issue_comments_056303.json:
```json
{
    "body": "Changing assignee from @mwhansen to @anneschilling.",
    "created_at": "2009-08-29T06:49:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6839",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6839#issuecomment-56303",
    "user": "https://github.com/anneschilling"
}
```

Changing assignee from @mwhansen to @anneschilling.



---

archive/issue_comments_056304.json:
```json
{
    "body": "This patch creates the E7 crystal with highest weight\nvector the last fundamental weight. This is the 56-dimensional\none. As usual, once the crystal of letters is implemented,\nothers follow using CrystalOfTableaux, though for such a\nlarge group this will be computationally intensive.\n\nThe patch applies without change to sage 4.1.1.\n\nIt passes `sage --testall`.\n\nI convinced myself that the crystal created is correct. For\nexample, it branches correctly to E6, A6 and D6.\n\nThe new method to_highest_weight() is very useful. You\ncan specify a subset of the index set and partition the\ncrystal into subcrystals for any Levi subgroup.",
    "created_at": "2009-09-04T18:04:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6839",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6839#issuecomment-56304",
    "user": "https://github.com/dwbump"
}
```

This patch creates the E7 crystal with highest weight
vector the last fundamental weight. This is the 56-dimensional
one. As usual, once the crystal of letters is implemented,
others follow using CrystalOfTableaux, though for such a
large group this will be computationally intensive.

The patch applies without change to sage 4.1.1.

It passes `sage --testall`.

I convinced myself that the crystal created is correct. For
example, it branches correctly to E6, A6 and D6.

The new method to_highest_weight() is very useful. You
can specify a subset of the index set and partition the
crystal into subcrystals for any Levi subgroup.



---

archive/issue_events_016103.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mvngu",
    "created_at": "2009-09-07T17:25:36Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/6839",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/6839#event-16103"
}
```



---

archive/issue_comments_056305.json:
```json
{
    "body": "The following docstring causes warnings when building the reference manual:\n\n```\n1287\t    TESTS:: \n1288\t \n1289\t    sage: C = CrystalOfLetters(['E',7]) \n1290\t    sage: C.module_generators \n1291\t    [[7]] \n1292\t    sage: C.list() \n1293\t    [[7], [-7, 6], [-6, 5], [-5, 4], [-4, 2, 3], [-2, 3], [-3, 1, 2], [-1, \n1294\t    2], [-3, -2, 1, 4], [-1, -2, 4], [-4, 1, 5], [-4, -1, 3, 5], [-3, 5], \n1295\t    [-5, 6, 1], [-5, -1, 3, 6], [-5, -3, 4, 6], [-4, 2, 6], [-2, 6], [-6, 7, \n1296\t    1], [-1, -6, 3, 7], [-6, -3, 7, 4], [-6, -4, 2, 7, 5], [-6, -2, 7, 5], \n1297\t    [-5, 7, 2], [-5, -2, 4, 7], [-4, 7, 3], [-3, 1, 7], [-1, 7], [-7, 1], \n1298\t    [-1, -7, 3], [-7, -3, 4], [-4, -7, 2, 5], [-7, -2, 5], [-5, -7, 6, 2], \n1299\t    [-5, -2, -7, 4, 6], [-7, -4, 6, 3], [-3, -7, 1, 6], [-7, -1, 6], [-6, \n1300\t    2], [-2, -6, 4], [-6, -4, 5, 3], [-3, -6, 1, 5], [-6, -1, 5], [-5, 3], \n1301\t    [-3, -5, 4, 1], [-5, -1, 4], [-4, 1, 2], [-1, -4, 3, 2], [-3, 2], [-2, \n1302\t    -3, 4], [-4, 5], [-5, 6], [-6, 7], [-7], [-2, 1], [-2, -1, 3]] \n1303\t    sage: C.check() \n1304\t    True \n1305\t    sage: all(b.f(i).e(i) == b for i in C.index_set() for b in C if b.f(i) is not None) \n1306\t    True \n1307\t    sage: all(b.e(i).f(i) == b for i in C.index_set() for b in C if b.e(i) is not None) \n1308\t    True \n1309\t    sage: G = C.digraph() \n1310\t    sage: G.show(edge_labels=true, figsize=12, vertex_size=1) \n```\nSee #6901 for a follow-up to this ticket.",
    "created_at": "2009-09-07T17:25:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6839",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6839#issuecomment-56305",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

The following docstring causes warnings when building the reference manual:

```
1287	    TESTS:: 
1288	 
1289	    sage: C = CrystalOfLetters(['E',7]) 
1290	    sage: C.module_generators 
1291	    [[7]] 
1292	    sage: C.list() 
1293	    [[7], [-7, 6], [-6, 5], [-5, 4], [-4, 2, 3], [-2, 3], [-3, 1, 2], [-1, 
1294	    2], [-3, -2, 1, 4], [-1, -2, 4], [-4, 1, 5], [-4, -1, 3, 5], [-3, 5], 
1295	    [-5, 6, 1], [-5, -1, 3, 6], [-5, -3, 4, 6], [-4, 2, 6], [-2, 6], [-6, 7, 
1296	    1], [-1, -6, 3, 7], [-6, -3, 7, 4], [-6, -4, 2, 7, 5], [-6, -2, 7, 5], 
1297	    [-5, 7, 2], [-5, -2, 4, 7], [-4, 7, 3], [-3, 1, 7], [-1, 7], [-7, 1], 
1298	    [-1, -7, 3], [-7, -3, 4], [-4, -7, 2, 5], [-7, -2, 5], [-5, -7, 6, 2], 
1299	    [-5, -2, -7, 4, 6], [-7, -4, 6, 3], [-3, -7, 1, 6], [-7, -1, 6], [-6, 
1300	    2], [-2, -6, 4], [-6, -4, 5, 3], [-3, -6, 1, 5], [-6, -1, 5], [-5, 3], 
1301	    [-3, -5, 4, 1], [-5, -1, 4], [-4, 1, 2], [-1, -4, 3, 2], [-3, 2], [-2, 
1302	    -3, 4], [-4, 5], [-5, 6], [-6, 7], [-7], [-2, 1], [-2, -1, 3]] 
1303	    sage: C.check() 
1304	    True 
1305	    sage: all(b.f(i).e(i) == b for i in C.index_set() for b in C if b.f(i) is not None) 
1306	    True 
1307	    sage: all(b.e(i).f(i) == b for i in C.index_set() for b in C if b.e(i) is not None) 
1308	    True 
1309	    sage: G = C.digraph() 
1310	    sage: G.show(edge_labels=true, figsize=12, vertex_size=1) 
```
See #6901 for a follow-up to this ticket.



---

archive/issue_events_016104.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mvngu",
    "created_at": "2009-09-07T17:25:36Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/6839",
    "milestone": "sage-4.1.2",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/6839#event-16104"
}
```



---

archive/issue_comments_056306.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-09-07T17:25:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6839",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6839#issuecomment-56306",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

Resolution: fixed

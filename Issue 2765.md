# Issue 2765: [with patch, needs review] bug in graph_isom, Hoffman-Singleton constructor

archive/issues_002765.json:
```json
{
    "body": "Assignee: rlm\n\nThis fixes a bug in determining the canonical label of different permutations of the Hoffman-Singleton graph. As such, the constructor is included to make for a nice doctest. This bug was discovered by Godsil.\n\nIssue created by migration from https://trac.sagemath.org/ticket/2765\n\n",
    "created_at": "2008-04-01T22:53:37Z",
    "labels": [
        "graph theory",
        "major",
        "bug"
    ],
    "title": "[with patch, needs review] bug in graph_isom, Hoffman-Singleton constructor",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/2765",
    "user": "rlm"
}
```
Assignee: rlm

This fixes a bug in determining the canonical label of different permutations of the Hoffman-Singleton graph. As such, the constructor is included to make for a nice doctest. This bug was discovered by Godsil.

Issue created by migration from https://trac.sagemath.org/ticket/2765





---

archive/issue_comments_018990.json:
```json
{
    "body": "Attachment",
    "created_at": "2008-04-02T07:06:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2765",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2765#issuecomment-18990",
    "user": "rlm"
}
```

Attachment



---

archive/issue_comments_018991.json:
```json
{
    "body": "This ticket patches two problems in the algorithm:\n\n1. In step 11, we have just found an automorphism, which means that the tree descending from where nu and zeta meet in the nu direction is isomorphic to what we have already seen. I was setting k to hb without checking that we are searching for a canonical label. hb keeps track of where nu and rho (the best so far guess at can. label) meet, and h keeps track of where nu and zeta (the first branch) meet. This is a typo in McKay's original paper.\n\n2. In the refinement procedure, I was adding something to the invariant which depended on more than the isomorphism class of the situation, namely `invariant += t + self_col_degs[i-j-1]`. This is before the cell has been split up, so there is some randomness. I moved this instruction to after splitting, and cleaned it up a bit.",
    "created_at": "2008-04-02T19:25:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2765",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2765#issuecomment-18991",
    "user": "rlm"
}
```

This ticket patches two problems in the algorithm:

1. In step 11, we have just found an automorphism, which means that the tree descending from where nu and zeta meet in the nu direction is isomorphic to what we have already seen. I was setting k to hb without checking that we are searching for a canonical label. hb keeps track of where nu and rho (the best so far guess at can. label) meet, and h keeps track of where nu and zeta (the first branch) meet. This is a typo in McKay's original paper.

2. In the refinement procedure, I was adding something to the invariant which depended on more than the isomorphism class of the situation, namely `invariant += t + self_col_degs[i-j-1]`. This is before the cell has been split up, so there is some randomness. I moved this instruction to after splitting, and cleaned it up a bit.



---

archive/issue_comments_018992.json:
```json
{
    "body": "Looks good to me.",
    "created_at": "2008-04-04T03:26:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2765",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2765#issuecomment-18992",
    "user": "mhansen"
}
```

Looks good to me.



---

archive/issue_comments_018993.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-04-04T03:42:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2765",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2765#issuecomment-18993",
    "user": "mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_018994.json:
```json
{
    "body": "Merged in Sage 3.0.alpha0",
    "created_at": "2008-04-04T03:42:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2765",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2765#issuecomment-18994",
    "user": "mabshoff"
}
```

Merged in Sage 3.0.alpha0



---

archive/issue_comments_018995.json:
```json
{
    "body": "Sorry: Merged in Sage *3.0.alpha1* - time to catch some sleep!",
    "created_at": "2008-04-04T03:45:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2765",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2765#issuecomment-18995",
    "user": "mabshoff"
}
```

Sorry: Merged in Sage *3.0.alpha1* - time to catch some sleep!

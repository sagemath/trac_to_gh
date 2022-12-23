# Issue 9967: Stop Dancing Links polluting the global namespace

archive/issues_009967.json:
```json
{
    "body": "Assignee: sage-combinat\n\nKeywords: dancing links\n\nThe Dancing Links class defines a bunch of random integer variables (LEFT, RIGHT, UP, DOWN, ROOTNODE) and exports these to the global namespace. This is kind of sloppy and unprofessional: \n\n\n```\n----------------------------------------------------------------------\n----------------------------------------------------------------------\n**********************************************************************\n*                                                                    *\n* Warning: this is a prerelease version, and it may be unstable.     *\n*                                                                    *\n**********************************************************************\nLoading Sage library. Current Mercurial branch is: hacking\nsage: UP\n2\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/9968\n\n",
    "created_at": "2010-09-22T10:13:36Z",
    "labels": [
        "combinatorics",
        "trivial",
        "bug"
    ],
    "title": "Stop Dancing Links polluting the global namespace",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/9967",
    "user": "davidloeffler"
}
```
Assignee: sage-combinat

Keywords: dancing links

The Dancing Links class defines a bunch of random integer variables (LEFT, RIGHT, UP, DOWN, ROOTNODE) and exports these to the global namespace. This is kind of sloppy and unprofessional: 


```
----------------------------------------------------------------------
----------------------------------------------------------------------
**********************************************************************
*                                                                    *
* Warning: this is a prerelease version, and it may be unstable.     *
*                                                                    *
**********************************************************************
Loading Sage library. Current Mercurial branch is: hacking
sage: UP
2
```


Issue created by migration from https://trac.sagemath.org/ticket/9968





---

archive/issue_comments_099874.json:
```json
{
    "body": "Attachment\n\npatch against 4.6.alpha1",
    "created_at": "2010-09-22T10:17:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9967",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9967#issuecomment-99874",
    "user": "davidloeffler"
}
```

Attachment

patch against 4.6.alpha1



---

archive/issue_comments_099875.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-09-22T10:17:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9967",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9967#issuecomment-99875",
    "user": "davidloeffler"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_099876.json:
```json
{
    "body": "I was a bit worried about the edge_coloring method for graphs which uses this algorithm, but it is still working after this patch is applied : no (related) failure in sage -testall ! \n\nThankssssssssss ! `:-)`\n\nNathann",
    "created_at": "2010-09-22T14:57:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9967",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9967#issuecomment-99876",
    "user": "ncohen"
}
```

I was a bit worried about the edge_coloring method for graphs which uses this algorithm, but it is still working after this patch is applied : no (related) failure in sage -testall ! 

Thankssssssssss ! `:-)`

Nathann



---

archive/issue_comments_099877.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-09-22T14:57:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9967",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9967#issuecomment-99877",
    "user": "ncohen"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_099878.json:
```json
{
    "body": "Perhaps we can get this into 4.6? It's hardly a massive change :-)",
    "created_at": "2010-09-28T11:47:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9967",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9967#issuecomment-99878",
    "user": "davidloeffler"
}
```

Perhaps we can get this into 4.6? It's hardly a massive change :-)



---

archive/issue_comments_099879.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-09-29T04:25:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9967",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9967#issuecomment-99879",
    "user": "mpatel"
}
```

Resolution: fixed

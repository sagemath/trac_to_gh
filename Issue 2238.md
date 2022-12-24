# Issue 2238: [with trivial patch, needs review] doctest failure in sage 2.10.2.alpha1: const.tex

archive/issues_002238.json:
```json
{
    "body": "Assignee: tba\n\nHi,\n\nComputing the points on elliptic curves over finite fields goes through finding the structure of the corresponding abelian group, and the code picks random generators for this.  Therefore the particular generators displayed, and the order in which the set of points is listed, vary from run to run.\n\nThis sometimes causes doctest failures on the examples in const.tex; I added comments containing the word \"random\" so that this doesn't happen.\n\nAlex\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/2238\n\n",
    "created_at": "2008-02-20T23:00:49Z",
    "labels": [
        "documentation",
        "major",
        "bug"
    ],
    "title": "[with trivial patch, needs review] doctest failure in sage 2.10.2.alpha1: const.tex",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/2238",
    "user": "AlexGhitza"
}
```
Assignee: tba

Hi,

Computing the points on elliptic curves over finite fields goes through finding the structure of the corresponding abelian group, and the code picks random generators for this.  Therefore the particular generators displayed, and the order in which the set of points is listed, vary from run to run.

This sometimes causes doctest failures on the examples in const.tex; I added comments containing the word "random" so that this doesn't happen.

Alex


Issue created by migration from https://trac.sagemath.org/ticket/2238





---

archive/issue_comments_014816.json:
```json
{
    "body": "Attachment [const_fails.patch](tarball://root/attachments/some-uuid/ticket2238/const_fails.patch) by AlexGhitza created at 2008-02-20 23:01:01",
    "created_at": "2008-02-20T23:01:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2238",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2238#issuecomment-14816",
    "user": "AlexGhitza"
}
```

Attachment [const_fails.patch](tarball://root/attachments/some-uuid/ticket2238/const_fails.patch) by AlexGhitza created at 2008-02-20 23:01:01



---

archive/issue_comments_014817.json:
```json
{
    "body": "1. The right solution is to always *SORT* the output if possible (which it is), so there is nothing random involved.\n\n2. And 2, my red flag went off when I saw list. Check out this bug!\n\n```\nsage: E = EllipticCurve(GF(5),[0, -1, 1, -10, -20]) \nsage: w = E.points(); w\n[(0 : 1 : 0), (0 : 0 : 1), (1 : 4 : 1), (1 : 0 : 1), (0 : 4 : 1)]\nsage: w[0] = 15\nsage: E.points()\n[15, (0 : 0 : 1), (1 : 4 : 1), (1 : 0 : 1), (0 : 4 : 1)]\n```\n\n\nI'll post a patch to fix both issues.",
    "created_at": "2008-02-20T23:12:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2238",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2238#issuecomment-14817",
    "user": "was"
}
```

1. The right solution is to always *SORT* the output if possible (which it is), so there is nothing random involved.

2. And 2, my red flag went off when I saw list. Check out this bug!

```
sage: E = EllipticCurve(GF(5),[0, -1, 1, -10, -20]) 
sage: w = E.points(); w
[(0 : 1 : 0), (0 : 0 : 1), (1 : 4 : 1), (1 : 0 : 1), (0 : 4 : 1)]
sage: w[0] = 15
sage: E.points()
[15, (0 : 0 : 1), (1 : 4 : 1), (1 : 0 : 1), (0 : 4 : 1)]
```


I'll post a patch to fix both issues.



---

archive/issue_comments_014818.json:
```json
{
    "body": "this and doc-2238.patch should replace the above patch (apply this to sage repo; and doc to doc repo)",
    "created_at": "2008-02-21T00:21:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2238",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2238#issuecomment-14818",
    "user": "was"
}
```

this and doc-2238.patch should replace the above patch (apply this to sage repo; and doc to doc repo)



---

archive/issue_comments_014819.json:
```json
{
    "body": "Attachment [sage-2238.patch](tarball://root/attachments/some-uuid/ticket2238/sage-2238.patch) by was created at 2008-02-21 00:21:36",
    "created_at": "2008-02-21T00:21:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2238",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2238#issuecomment-14819",
    "user": "was"
}
```

Attachment [sage-2238.patch](tarball://root/attachments/some-uuid/ticket2238/sage-2238.patch) by was created at 2008-02-21 00:21:36



---

archive/issue_comments_014820.json:
```json
{
    "body": "Attachment [doc-2238.patch](tarball://root/attachments/some-uuid/ticket2238/doc-2238.patch) by was created at 2008-02-21 00:21:56",
    "created_at": "2008-02-21T00:21:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2238",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2238#issuecomment-14820",
    "user": "was"
}
```

Attachment [doc-2238.patch](tarball://root/attachments/some-uuid/ticket2238/doc-2238.patch) by was created at 2008-02-21 00:21:56



---

archive/issue_comments_014821.json:
```json
{
    "body": "Changing priority from major to blocker.",
    "created_at": "2008-02-21T00:21:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2238",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2238#issuecomment-14821",
    "user": "was"
}
```

Changing priority from major to blocker.



---

archive/issue_comments_014822.json:
```json
{
    "body": "Attachment [sage-2238-new.patch](tarball://root/attachments/some-uuid/ticket2238/sage-2238-new.patch) by AlexGhitza created at 2008-02-21 02:54:37\n\nreplace sage-2238.patch",
    "created_at": "2008-02-21T02:54:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2238",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2238#issuecomment-14822",
    "user": "AlexGhitza"
}
```

Attachment [sage-2238-new.patch](tarball://root/attachments/some-uuid/ticket2238/sage-2238-new.patch) by AlexGhitza created at 2008-02-21 02:54:37

replace sage-2238.patch



---

archive/issue_comments_014823.json:
```json
{
    "body": "Looks great; unfortunately it breaks another doctest (trivial to fix, so I've done it and put in a new patch replacing sage-2238.patch).  The doc-2238.patch looks fine.",
    "created_at": "2008-02-21T02:57:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2238",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2238#issuecomment-14823",
    "user": "AlexGhitza"
}
```

Looks great; unfortunately it breaks another doctest (trivial to fix, so I've done it and put in a new patch replacing sage-2238.patch).  The doc-2238.patch looks fine.



---

archive/issue_comments_014824.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-02-21T03:05:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2238",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2238#issuecomment-14824",
    "user": "mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_014825.json:
```json
{
    "body": "Merged sage-2238.patch and sage-2238-new.patch in Sage 2.10.2.alpah2",
    "created_at": "2008-02-21T03:05:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2238",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2238#issuecomment-14825",
    "user": "mabshoff"
}
```

Merged sage-2238.patch and sage-2238-new.patch in Sage 2.10.2.alpah2



---

archive/issue_comments_014826.json:
```json
{
    "body": "Thanks to Alex and William for fixing these things which were caused by me:  as a relative novice to Python I am not aware as I should be of the critical differences between lists and tuples!  And the need to sort things to be canonical.\n\nI'm not sure what the correct milestone is for this, certainly not 2.10.2, and it's not in 2.10.3.rc0 either, but not for lack of positive reviews.",
    "created_at": "2008-03-02T17:11:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2238",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2238#issuecomment-14826",
    "user": "cremona"
}
```

Thanks to Alex and William for fixing these things which were caused by me:  as a relative novice to Python I am not aware as I should be of the critical differences between lists and tuples!  And the need to sort things to be canonical.

I'm not sure what the correct milestone is for this, certainly not 2.10.2, and it's not in 2.10.3.rc0 either, but not for lack of positive reviews.



---

archive/issue_comments_014827.json:
```json
{
    "body": "Replying to [comment:6 cremona]:\n> Thanks to Alex and William for fixing these things which were caused by me:  as a relative novice to Python I am not aware as I should be of the critical differences between lists and tuples!  And the need to sort things to be canonical.\n> \n> I'm not sure what the correct milestone is for this, certainly not 2.10.2, and it's not in 2.10.3.rc0 either, but not for lack of positive reviews.\n> \n\nI check my 2.10.3.rc1 and:\n\n* sage-2238-new.patch is \"changeset: 8647:97976cb27ad3\" in the sage repo (this is in the 2.10.2 release time frame)\n* doc-2238.patch is \"changeset: 429:3a30bbba6c29\" in the doc repo (this is in the 2.10.2 release time frame)\n\nSo, I am sure both patches have been applied. \n\nCheers,\n\nMichael",
    "created_at": "2008-03-02T17:25:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2238",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2238#issuecomment-14827",
    "user": "mabshoff"
}
```

Replying to [comment:6 cremona]:
> Thanks to Alex and William for fixing these things which were caused by me:  as a relative novice to Python I am not aware as I should be of the critical differences between lists and tuples!  And the need to sort things to be canonical.
> 
> I'm not sure what the correct milestone is for this, certainly not 2.10.2, and it's not in 2.10.3.rc0 either, but not for lack of positive reviews.
> 

I check my 2.10.3.rc1 and:

* sage-2238-new.patch is "changeset: 8647:97976cb27ad3" in the sage repo (this is in the 2.10.2 release time frame)
* doc-2238.patch is "changeset: 429:3a30bbba6c29" in the doc repo (this is in the 2.10.2 release time frame)

So, I am sure both patches have been applied. 

Cheers,

Michael

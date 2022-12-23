# Issue 9206: faster finite field creation with proof=False, done right (via proof architecture)

archive/issues_009206.json:
```json
{
    "body": "Assignee: AlexGhitza\n\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/9206\n\n",
    "created_at": "2010-06-10T19:59:00Z",
    "labels": [
        "basic arithmetic",
        "major",
        "enhancement"
    ],
    "title": "faster finite field creation with proof=False, done right (via proof architecture)",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/9206",
    "user": "was"
}
```
Assignee: AlexGhitza



Issue created by migration from https://trac.sagemath.org/ticket/9206





---

archive/issue_comments_086166.json:
```json
{
    "body": "This example illustrates the effect of this patch:\n\n```\nsage: time GF(next_prime(10^40)^5,'a')\nCPU times: user 0.51 s, sys: 0.00 s, total: 0.52 s\nWall time: 0.52 s\nFinite Field in a of size 10000000000000000000000000000000000000121^5\nsage: proof.arithmetic(False)\nsage: time GF(next_prime(10^40)^5,'a')\nCPU times: user 0.07 s, sys: 0.00 s, total: 0.07 s\nWall time: 0.07 s\nFinite Field in a of size 10000000000000000000000000000000000000121^5\n```\n\n\nUnfortunately, it does *not* address this problem that David Harvey mentioned.  However, it has a similar \"flavor\":\n\n\n```\nsage: R.<x> = PolynomialRing(Integers(16219299585*2^16612 - 1))\n```\n\nDavid Harvey: \"Maybe not literally forever, but I got sick of waiting. Should be instantaneous.\"",
    "created_at": "2010-07-07T20:10:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9206",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9206#issuecomment-86166",
    "user": "was"
}
```

This example illustrates the effect of this patch:

```
sage: time GF(next_prime(10^40)^5,'a')
CPU times: user 0.51 s, sys: 0.00 s, total: 0.52 s
Wall time: 0.52 s
Finite Field in a of size 10000000000000000000000000000000000000121^5
sage: proof.arithmetic(False)
sage: time GF(next_prime(10^40)^5,'a')
CPU times: user 0.07 s, sys: 0.00 s, total: 0.07 s
Wall time: 0.07 s
Finite Field in a of size 10000000000000000000000000000000000000121^5
```


Unfortunately, it does *not* address this problem that David Harvey mentioned.  However, it has a similar "flavor":


```
sage: R.<x> = PolynomialRing(Integers(16219299585*2^16612 - 1))
```

David Harvey: "Maybe not literally forever, but I got sick of waiting. Should be instantaneous."



---

archive/issue_comments_086167.json:
```json
{
    "body": "Attachment\n\nI didn't write the attached patch, but I polished it up, so it would be good if somebody else could sign off on this.  I'm OK with it, as is.",
    "created_at": "2010-07-07T20:12:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9206",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9206#issuecomment-86167",
    "user": "was"
}
```

Attachment

I didn't write the attached patch, but I polished it up, so it would be good if somebody else could sign off on this.  I'm OK with it, as is.



---

archive/issue_comments_086168.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-07-07T20:12:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9206",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9206#issuecomment-86168",
    "user": "was"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_086169.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-07-08T03:18:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9206",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9206#issuecomment-86169",
    "user": "robertwb"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_086170.json:
```json
{
    "body": "Looks good to me.",
    "created_at": "2010-07-08T03:18:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9206",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9206#issuecomment-86170",
    "user": "robertwb"
}
```

Looks good to me.



---

archive/issue_comments_086171.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-07-20T09:20:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9206",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9206#issuecomment-86171",
    "user": "mpatel"
}
```

Resolution: fixed

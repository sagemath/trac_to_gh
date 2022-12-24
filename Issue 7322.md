# Issue 7322: SageNB: Upgrade jsMath to 3.6c

archive/issues_007322.json:
```json
{
    "body": "Assignee: boothby\n\nCC:  jhpalmieri\n\nVersion 3.6c of jsMath works around Firefox 3.5's single-origin policy for local files.  The policy can keep jsMath from loading its external components and functioning properly (cf. #6820).\n\nPlease see the [change log](http://www.math.union.edu/~dpvc/jsMath/changes.html) for other bug fixes. \n\nIssue created by migration from https://trac.sagemath.org/ticket/7322\n\n",
    "created_at": "2009-10-27T17:22:19Z",
    "labels": [
        "notebook",
        "minor",
        "enhancement"
    ],
    "title": "SageNB: Upgrade jsMath to 3.6c",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/7322",
    "user": "mpatel"
}
```
Assignee: boothby

CC:  jhpalmieri

Version 3.6c of jsMath works around Firefox 3.5's single-origin policy for local files.  The policy can keep jsMath from loading its external components and functioning properly (cf. #6820).

Please see the [change log](http://www.math.union.edu/~dpvc/jsMath/changes.html) for other bug fixes. 

Issue created by migration from https://trac.sagemath.org/ticket/7322





---

archive/issue_comments_061184.json:
```json
{
    "body": "Attachment [trac_7322-jsmath_upgrade.patch](tarball://root/attachments/some-uuid/ticket7322/trac_7322-jsmath_upgrade.patch) by mpatel created at 2009-10-29 07:19:11\n\nUpgrade to jsMath 3.6c.",
    "created_at": "2009-10-29T07:19:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7322",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7322#issuecomment-61184",
    "user": "mpatel"
}
```

Attachment [trac_7322-jsmath_upgrade.patch](tarball://root/attachments/some-uuid/ticket7322/trac_7322-jsmath_upgrade.patch) by mpatel created at 2009-10-29 07:19:11

Upgrade to jsMath 3.6c.



---

archive/issue_comments_061185.json:
```json
{
    "body": "I installed it and it seems to work well.  In particular, the patch at #6820 works with Firefox with this.\n\nI skimmed the patch but I'm not going to proofread it carefully; I'm assuming that you just took the new source code for jsMath 3.6c and replaced the old source code for jsMath 3.6b.",
    "created_at": "2009-10-29T20:09:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7322",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7322#issuecomment-61185",
    "user": "jhpalmieri"
}
```

I installed it and it seems to work well.  In particular, the patch at #6820 works with Firefox with this.

I skimmed the patch but I'm not going to proofread it carefully; I'm assuming that you just took the new source code for jsMath 3.6c and replaced the old source code for jsMath 3.6b.



---

archive/issue_comments_061186.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2009-10-29T20:09:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7322",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7322#issuecomment-61186",
    "user": "jhpalmieri"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_061187.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2009-10-29T20:10:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7322",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7322#issuecomment-61187",
    "user": "jhpalmieri"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_061188.json:
```json
{
    "body": "Replying to [comment:1 jhpalmieri]:\n> I skimmed the patch but I'm not going to proofread it carefully; I'm assuming that you just took the new source code for jsMath 3.6c and replaced the old source code for jsMath 3.6b.\n\nIndeed. That's all I did.",
    "created_at": "2009-10-30T14:24:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7322",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7322#issuecomment-61188",
    "user": "mpatel"
}
```

Replying to [comment:1 jhpalmieri]:
> I skimmed the patch but I'm not going to proofread it carefully; I'm assuming that you just took the new source code for jsMath 3.6c and replaced the old source code for jsMath 3.6b.

Indeed. That's all I did.



---

archive/issue_comments_061189.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-11-11T22:14:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7322",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7322#issuecomment-61189",
    "user": "was"
}
```

Resolution: fixed



---

archive/issue_comments_061190.json:
```json
{
    "body": "merged into sagenb-0.4.2 (sage-4.2.1)",
    "created_at": "2009-11-11T22:14:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7322",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7322#issuecomment-61190",
    "user": "was"
}
```

merged into sagenb-0.4.2 (sage-4.2.1)

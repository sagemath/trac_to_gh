# Issue 9178: attrcall: add missing hash function

archive/issues_009178.json:
```json
{
    "body": "Assignee: nthiery\n\nCC:  sage-combinat mhansen\n\nKeywords: attrcall, hash\n\nThis patch implements `attrcall.__hash__`. Its absence caused the\nfollowing misbehavior:\n\n\n```\n    sage: x = attrcall(\"blah\")\n    sage: y = attrcall(\"blah\")\n    sage: x == y\n    True\n    sage: hash(x) == hash(y)\n    False\n```\n\n\nwhich in particular broke unique representation and pickling of some\ncrystals (see #8911).\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/9178\n\n",
    "created_at": "2010-06-07T15:23:23Z",
    "labels": [
        "misc",
        "major",
        "bug"
    ],
    "title": "attrcall: add missing hash function",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/9178",
    "user": "nthiery"
}
```
Assignee: nthiery

CC:  sage-combinat mhansen

Keywords: attrcall, hash

This patch implements `attrcall.__hash__`. Its absence caused the
following misbehavior:


```
    sage: x = attrcall("blah")
    sage: y = attrcall("blah")
    sage: x == y
    True
    sage: hash(x) == hash(y)
    False
```


which in particular broke unique representation and pickling of some
crystals (see #8911).


Issue created by migration from https://trac.sagemath.org/ticket/9178





---

archive/issue_comments_085871.json:
```json
{
    "body": "Attachment [trac_9178-attrcall_hash_fix-nt.patch](tarball://root/attachments/some-uuid/ticket9178/trac_9178-attrcall_hash_fix-nt.patch) by nthiery created at 2010-06-07 15:25:44",
    "created_at": "2010-06-07T15:25:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9178",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9178#issuecomment-85871",
    "user": "nthiery"
}
```

Attachment [trac_9178-attrcall_hash_fix-nt.patch](tarball://root/attachments/some-uuid/ticket9178/trac_9178-attrcall_hash_fix-nt.patch) by nthiery created at 2010-06-07 15:25:44



---

archive/issue_comments_085872.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-06-07T15:26:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9178",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9178#issuecomment-85872",
    "user": "nthiery"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_085873.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-06-07T15:28:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9178",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9178#issuecomment-85873",
    "user": "mhansen"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_085874.json:
```json
{
    "body": "Looks good to me.",
    "created_at": "2010-06-07T15:28:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9178",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9178#issuecomment-85874",
    "user": "mhansen"
}
```

Looks good to me.



---

archive/issue_comments_085875.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-06-09T02:31:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9178",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9178#issuecomment-85875",
    "user": "mhansen"
}
```

Resolution: fixed

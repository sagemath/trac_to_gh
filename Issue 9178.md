# Issue 9178: attrcall: add missing hash function

archive/issues_009178.json:
```json
{
    "body": "Assignee: @nthiery\n\nCC:  sage-combinat @mwhansen\n\nKeywords: attrcall, hash\n\nThis patch implements `attrcall.__hash__`. Its absence caused the\nfollowing misbehavior:\n\n\n```\n    sage: x = attrcall(\"blah\")\n    sage: y = attrcall(\"blah\")\n    sage: x == y\n    True\n    sage: hash(x) == hash(y)\n    False\n```\n\n\nwhich in particular broke unique representation and pickling of some\ncrystals (see #8911).\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/9178\n\n",
    "created_at": "2010-06-07T15:23:23Z",
    "labels": [
        "component: misc",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.4.4",
    "title": "attrcall: add missing hash function",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/9178",
    "user": "https://github.com/nthiery"
}
```
Assignee: @nthiery

CC:  sage-combinat @mwhansen

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

archive/issue_comments_085733.json:
```json
{
    "body": "Attachment [trac_9178-attrcall_hash_fix-nt.patch](tarball://root/attachments/some-uuid/ticket9178/trac_9178-attrcall_hash_fix-nt.patch) by @nthiery created at 2010-06-07 15:25:44",
    "created_at": "2010-06-07T15:25:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9178",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9178#issuecomment-85733",
    "user": "https://github.com/nthiery"
}
```

Attachment [trac_9178-attrcall_hash_fix-nt.patch](tarball://root/attachments/some-uuid/ticket9178/trac_9178-attrcall_hash_fix-nt.patch) by @nthiery created at 2010-06-07 15:25:44



---

archive/issue_comments_085734.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-06-07T15:26:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9178",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9178#issuecomment-85734",
    "user": "https://github.com/nthiery"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_085735.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-06-07T15:28:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9178",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9178#issuecomment-85735",
    "user": "https://github.com/mwhansen"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_085736.json:
```json
{
    "body": "Looks good to me.",
    "created_at": "2010-06-07T15:28:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9178",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9178#issuecomment-85736",
    "user": "https://github.com/mwhansen"
}
```

Looks good to me.



---

archive/issue_events_009335.json:
```json
{
    "actor": "@mwhansen",
    "created_at": "2010-06-09T02:31:14Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/9178",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/9178#event-9335"
}
```



---

archive/issue_comments_085737.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-06-09T02:31:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9178",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9178#issuecomment-85737",
    "user": "https://github.com/mwhansen"
}
```

Resolution: fixed

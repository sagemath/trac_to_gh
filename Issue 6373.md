# Issue 6373: AA and QQbar have no is_square method

archive/issues_006373.json:
```json
{
    "body": "Assignee: @williamstein\n\nCC:  cwitty jcooley\n\nKeywords: algebraic field is square\n\n\n```\nsage: QQbar(5).is_square()\n---------------------------------------------------------------------------\nAttributeError                            Traceback (most recent call last)\n\n...\n\nAttributeError: 'AlgebraicNumber' object has no attribute 'is_square'\n```\n\n\nbut of course:\n\n\n```\nsage: QQbar(5).sqrt()\n2.236067977499790?\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/6373\n\n",
    "created_at": "2009-06-20T19:48:21Z",
    "labels": [
        "component: number theory",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.1.2",
    "title": "AA and QQbar have no is_square method",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/6373",
    "user": "https://github.com/ncalexan"
}
```
Assignee: @williamstein

CC:  cwitty jcooley

Keywords: algebraic field is square


```
sage: QQbar(5).is_square()
---------------------------------------------------------------------------
AttributeError                            Traceback (most recent call last)

...

AttributeError: 'AlgebraicNumber' object has no attribute 'is_square'
```


but of course:


```
sage: QQbar(5).sqrt()
2.236067977499790?
```


Issue created by migration from https://trac.sagemath.org/ticket/6373





---

archive/issue_comments_050914.json:
```json
{
    "body": "Attachment [trac_6373-qqbar.patch](tarball://root/attachments/some-uuid/ticket6373/trac_6373-qqbar.patch) by @JohnCremona created at 2009-09-24 12:18:28",
    "created_at": "2009-09-24T12:18:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6373",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6373#issuecomment-50914",
    "user": "https://github.com/JohnCremona"
}
```

Attachment [trac_6373-qqbar.patch](tarball://root/attachments/some-uuid/ticket6373/trac_6373-qqbar.patch) by @JohnCremona created at 2009-09-24 12:18:28



---

archive/issue_comments_050915.json:
```json
{
    "body": "The attached patch adds this trivial function.  It also corrects a typo which I discovered when testing it (specifically, now that this function exists you can do more with elliptic curves over QQbar;  see also #6879).",
    "created_at": "2009-09-24T12:20:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6373",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6373#issuecomment-50915",
    "user": "https://github.com/JohnCremona"
}
```

The attached patch adds this trivial function.  It also corrects a typo which I discovered when testing it (specifically, now that this function exists you can do more with elliptic curves over QQbar;  see also #6879).



---

archive/issue_comments_050916.json:
```json
{
    "body": "Looks good; positive review.",
    "created_at": "2009-09-25T05:46:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6373",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6373#issuecomment-50916",
    "user": "https://github.com/jasongrout"
}
```

Looks good; positive review.



---

archive/issue_comments_050917.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-09-25T14:35:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6373",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6373#issuecomment-50917",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

Resolution: fixed



---

archive/issue_events_006621.json:
```json
{
    "actor": "mvngu",
    "created_at": "2009-09-25T14:35:32Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/6373",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/6373#event-6621"
}
```



---

archive/issue_comments_050918.json:
```json
{
    "body": "There is no 4.1.2.alpha3. Sage 4.1.2.alpha3 was William Stein's release for working on making the notebook a standalone package.",
    "created_at": "2009-09-27T10:35:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6373",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6373#issuecomment-50918",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

There is no 4.1.2.alpha3. Sage 4.1.2.alpha3 was William Stein's release for working on making the notebook a standalone package.

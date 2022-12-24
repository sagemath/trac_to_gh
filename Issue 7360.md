# Issue 7360: isomorphism_type_info_simple_group returns an exception instead of raising it

archive/issues_007360.json:
```json
{
    "body": "Assignee: joyner\n\nCurrently (sage-4.2):\n\n\n```\nsage: S = KleinFourGroup()\nsage: S.isomorphism_type_info_simple_group()\n(<type 'exceptions.TypeError'>, 'Group must be simple.')\n```\n\n\nThe attached patch fixes this and adds a doctest.\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/7360\n\n",
    "created_at": "2009-10-31T13:04:24Z",
    "labels": [
        "group theory",
        "minor",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.2.1",
    "title": "isomorphism_type_info_simple_group returns an exception instead of raising it",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/7360",
    "user": "@aghitza"
}
```
Assignee: joyner

Currently (sage-4.2):


```
sage: S = KleinFourGroup()
sage: S.isomorphism_type_info_simple_group()
(<type 'exceptions.TypeError'>, 'Group must be simple.')
```


The attached patch fixes this and adds a doctest.


Issue created by migration from https://trac.sagemath.org/ticket/7360





---

archive/issue_comments_061676.json:
```json
{
    "body": "Attachment [trac_7360.patch](tarball://root/attachments/some-uuid/ticket7360/trac_7360.patch) by @aghitza created at 2009-10-31 13:07:29",
    "created_at": "2009-10-31T13:07:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7360",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7360#issuecomment-61676",
    "user": "@aghitza"
}
```

Attachment [trac_7360.patch](tarball://root/attachments/some-uuid/ticket7360/trac_7360.patch) by @aghitza created at 2009-10-31 13:07:29



---

archive/issue_comments_061677.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2009-10-31T13:08:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7360",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7360#issuecomment-61677",
    "user": "@aghitza"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_061678.json:
```json
{
    "body": "Positive review - nice catch.",
    "created_at": "2009-11-10T22:34:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7360",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7360#issuecomment-61678",
    "user": "@kcrisman"
}
```

Positive review - nice catch.



---

archive/issue_comments_061679.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2009-11-10T22:34:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7360",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7360#issuecomment-61679",
    "user": "@kcrisman"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_061680.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-11-12T06:50:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7360",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7360#issuecomment-61680",
    "user": "@mwhansen"
}
```

Resolution: fixed

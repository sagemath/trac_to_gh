# Issue 6188: [with patch, needs review] Add more files in sage/rings/number_field to reference manual

archive/issues_006188.json:
```json
{
    "body": "Assignee: was\n\nKeywords: documentation\n\nThis patch adds the files {{{\norder.py}}}, `number_field_element_quadratic.pyx`, `number_field_rel.py`, `number_field_ideal_rel.py`, and `unit_group.py` to the reference manual, and makes the necessary ReST formatting fixes to get them to build correctly.\n\nIssue created by migration from https://trac.sagemath.org/ticket/6188\n\n",
    "created_at": "2009-06-02T17:22:41Z",
    "labels": [
        "number theory",
        "major",
        "bug"
    ],
    "title": "[with patch, needs review] Add more files in sage/rings/number_field to reference manual",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/6188",
    "user": "davidloeffler"
}
```
Assignee: was

Keywords: documentation

This patch adds the files {{{
order.py}}}, `number_field_element_quadratic.pyx`, `number_field_rel.py`, `number_field_ideal_rel.py`, and `unit_group.py` to the reference manual, and makes the necessary ReST formatting fixes to get them to build correctly.

Issue created by migration from https://trac.sagemath.org/ticket/6188





---

archive/issue_comments_049433.json:
```json
{
    "body": "patch against 4.0.1.alpha0",
    "created_at": "2009-06-02T17:24:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6188",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6188#issuecomment-49433",
    "user": "davidloeffler"
}
```

patch against 4.0.1.alpha0



---

archive/issue_comments_049434.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2009-06-02T17:25:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6188",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6188#issuecomment-49434",
    "user": "davidloeffler"
}
```

Changing status from new to assigned.



---

archive/issue_comments_049435.json:
```json
{
    "body": "Attachment [trac_6188.patch](tarball://root/attachments/some-uuid/ticket6188/trac_6188.patch) by davidloeffler created at 2009-06-02 17:25:51",
    "created_at": "2009-06-02T17:25:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6188",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6188#issuecomment-49435",
    "user": "davidloeffler"
}
```

Attachment [trac_6188.patch](tarball://root/attachments/some-uuid/ticket6188/trac_6188.patch) by davidloeffler created at 2009-06-02 17:25:51



---

archive/issue_comments_049436.json:
```json
{
    "body": "Changing assignee from was to davidloeffler.",
    "created_at": "2009-06-02T17:25:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6188",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6188#issuecomment-49436",
    "user": "davidloeffler"
}
```

Changing assignee from was to davidloeffler.



---

archive/issue_comments_049437.json:
```json
{
    "body": "I am half way through reviewing this and should be able to finish tomorrow.",
    "created_at": "2009-06-03T21:29:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6188",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6188#issuecomment-49437",
    "user": "cremona"
}
```

I am half way through reviewing this and should be able to finish tomorrow.



---

archive/issue_comments_049438.json:
```json
{
    "body": "Attachment [trac_6188_review.patch](tarball://root/attachments/some-uuid/ticket6188/trac_6188_review.patch) by cremona created at 2009-06-04 21:41:35\n\nApply after previous",
    "created_at": "2009-06-04T21:41:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6188",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6188#issuecomment-49438",
    "user": "cremona"
}
```

Attachment [trac_6188_review.patch](tarball://root/attachments/some-uuid/ticket6188/trac_6188_review.patch) by cremona created at 2009-06-04 21:41:35

Apply after previous



---

archive/issue_comments_049439.json:
```json
{
    "body": "I reviewed David's patch by rebuilding the reference manual and looking through the relavant sections.  I found quite a few more things needing tidying up (several in functions I wrote, so my fault), hence the second patch nearly half as large as the first.\n\nI'm happy to OK David's contribution, but someone else (David?) should run mine.  It's all docstring changes, but I did check that all tests in sage/rings/number_field still pass.",
    "created_at": "2009-06-04T21:46:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6188",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6188#issuecomment-49439",
    "user": "cremona"
}
```

I reviewed David's patch by rebuilding the reference manual and looking through the relavant sections.  I found quite a few more things needing tidying up (several in functions I wrote, so my fault), hence the second patch nearly half as large as the first.

I'm happy to OK David's contribution, but someone else (David?) should run mine.  It's all docstring changes, but I did check that all tests in sage/rings/number_field still pass.



---

archive/issue_comments_049440.json:
```json
{
    "body": "Looks fine to me.",
    "created_at": "2009-06-05T08:28:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6188",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6188#issuecomment-49440",
    "user": "davidloeffler"
}
```

Looks fine to me.



---

archive/issue_comments_049441.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-06-13T19:47:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6188",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6188#issuecomment-49441",
    "user": "ncalexan"
}
```

Resolution: fixed

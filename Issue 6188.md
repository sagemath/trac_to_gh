# Issue 6188: [with patch, needs review] Add more files in sage/rings/number_field to reference manual

archive/issues_006188.json:
```json
{
    "body": "Assignee: @williamstein\n\nKeywords: documentation\n\nThis patch adds the files {{{\norder.py}}}, `number_field_element_quadratic.pyx`, `number_field_rel.py`, `number_field_ideal_rel.py`, and `unit_group.py` to the reference manual, and makes the necessary ReST formatting fixes to get them to build correctly.\n\nIssue created by migration from https://trac.sagemath.org/ticket/6188\n\n",
    "created_at": "2009-06-02T17:22:41Z",
    "labels": [
        "component: number theory",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.0.2",
    "title": "[with patch, needs review] Add more files in sage/rings/number_field to reference manual",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/6188",
    "user": "https://github.com/loefflerd"
}
```
Assignee: @williamstein

Keywords: documentation

This patch adds the files {{{
order.py}}}, `number_field_element_quadratic.pyx`, `number_field_rel.py`, `number_field_ideal_rel.py`, and `unit_group.py` to the reference manual, and makes the necessary ReST formatting fixes to get them to build correctly.

Issue created by migration from https://trac.sagemath.org/ticket/6188





---

archive/issue_comments_049338.json:
```json
{
    "body": "patch against 4.0.1.alpha0",
    "created_at": "2009-06-02T17:24:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6188",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6188#issuecomment-49338",
    "user": "https://github.com/loefflerd"
}
```

patch against 4.0.1.alpha0



---

archive/issue_comments_049339.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2009-06-02T17:25:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6188",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6188#issuecomment-49339",
    "user": "https://github.com/loefflerd"
}
```

Changing status from new to assigned.



---

archive/issue_comments_049340.json:
```json
{
    "body": "Attachment [trac_6188.patch](tarball://root/attachments/some-uuid/ticket6188/trac_6188.patch) by @loefflerd created at 2009-06-02 17:25:51",
    "created_at": "2009-06-02T17:25:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6188",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6188#issuecomment-49340",
    "user": "https://github.com/loefflerd"
}
```

Attachment [trac_6188.patch](tarball://root/attachments/some-uuid/ticket6188/trac_6188.patch) by @loefflerd created at 2009-06-02 17:25:51



---

archive/issue_comments_049341.json:
```json
{
    "body": "Changing assignee from @williamstein to @loefflerd.",
    "created_at": "2009-06-02T17:25:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6188",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6188#issuecomment-49341",
    "user": "https://github.com/loefflerd"
}
```

Changing assignee from @williamstein to @loefflerd.



---

archive/issue_comments_049342.json:
```json
{
    "body": "I am half way through reviewing this and should be able to finish tomorrow.",
    "created_at": "2009-06-03T21:29:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6188",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6188#issuecomment-49342",
    "user": "https://github.com/JohnCremona"
}
```

I am half way through reviewing this and should be able to finish tomorrow.



---

archive/issue_comments_049343.json:
```json
{
    "body": "Attachment [trac_6188_review.patch](tarball://root/attachments/some-uuid/ticket6188/trac_6188_review.patch) by @JohnCremona created at 2009-06-04 21:41:35\n\nApply after previous",
    "created_at": "2009-06-04T21:41:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6188",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6188#issuecomment-49343",
    "user": "https://github.com/JohnCremona"
}
```

Attachment [trac_6188_review.patch](tarball://root/attachments/some-uuid/ticket6188/trac_6188_review.patch) by @JohnCremona created at 2009-06-04 21:41:35

Apply after previous



---

archive/issue_comments_049344.json:
```json
{
    "body": "I reviewed David's patch by rebuilding the reference manual and looking through the relavant sections.  I found quite a few more things needing tidying up (several in functions I wrote, so my fault), hence the second patch nearly half as large as the first.\n\nI'm happy to OK David's contribution, but someone else (David?) should run mine.  It's all docstring changes, but I did check that all tests in sage/rings/number_field still pass.",
    "created_at": "2009-06-04T21:46:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6188",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6188#issuecomment-49344",
    "user": "https://github.com/JohnCremona"
}
```

I reviewed David's patch by rebuilding the reference manual and looking through the relavant sections.  I found quite a few more things needing tidying up (several in functions I wrote, so my fault), hence the second patch nearly half as large as the first.

I'm happy to OK David's contribution, but someone else (David?) should run mine.  It's all docstring changes, but I did check that all tests in sage/rings/number_field still pass.



---

archive/issue_comments_049345.json:
```json
{
    "body": "Looks fine to me.",
    "created_at": "2009-06-05T08:28:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6188",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6188#issuecomment-49345",
    "user": "https://github.com/loefflerd"
}
```

Looks fine to me.



---

archive/issue_comments_049346.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-06-13T19:47:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6188",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6188#issuecomment-49346",
    "user": "https://github.com/ncalexan"
}
```

Resolution: fixed

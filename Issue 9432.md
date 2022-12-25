# Issue 9432: remove remaining # optional - GLPK tags on doctests

archive/issues_009432.json:
```json
{
    "body": "Assignee: jason, jkantor\n\nCC:  @nathanncohen @nexttime\n\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/9432\n\n",
    "created_at": "2010-07-05T23:19:19Z",
    "labels": [
        "component: numerical",
        "blocker",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.5",
    "title": "remove remaining # optional - GLPK tags on doctests",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/9432",
    "user": "https://github.com/rlmill"
}
```
Assignee: jason, jkantor

CC:  @nathanncohen @nexttime



Issue created by migration from https://trac.sagemath.org/ticket/9432





---

archive/issue_comments_089898.json:
```json
{
    "body": "The following should also be addressed:\n\n\n```\nage -t -long \"devel/sage-main/sage/numerical/mip.pyx\"\n**********************************************************************\nFile \"/scratch/rlmill/release/sage-4.5.alpha2/devel/sage-main/sage/numerical/mip.pyx\",\nline 1055:\n   sage: p.get_values(x)\nExpected:\n   {0: 0.0, 1: 1.3333333333333333}\nGot:\n   {1: 0.0, 2: 1.3333333333333333}\n*********************************************************************\n```\n",
    "created_at": "2010-07-06T03:49:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9432",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9432#issuecomment-89898",
    "user": "https://github.com/rlmill"
}
```

The following should also be addressed:


```
age -t -long "devel/sage-main/sage/numerical/mip.pyx"
**********************************************************************
File "/scratch/rlmill/release/sage-4.5.alpha2/devel/sage-main/sage/numerical/mip.pyx",
line 1055:
   sage: p.get_values(x)
Expected:
   {0: 0.0, 1: 1.3333333333333333}
Got:
   {1: 0.0, 2: 1.3333333333333333}
*********************************************************************
```




---

archive/issue_comments_089899.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-07-06T09:58:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9432",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9432#issuecomment-89899",
    "user": "https://github.com/nathanncohen"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_089900.json:
```json
{
    "body": "Attachment [trac_9432.patch](tarball://root/attachments/some-uuid/ticket9432/trac_9432.patch) by @nathanncohen created at 2010-07-06 09:58:59\n\nUpdated ! There should not be any other trace of the optional GLPK package in Sage :-)\n\nNathann",
    "created_at": "2010-07-06T09:58:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9432",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9432#issuecomment-89900",
    "user": "https://github.com/nathanncohen"
}
```

Attachment [trac_9432.patch](tarball://root/attachments/some-uuid/ticket9432/trac_9432.patch) by @nathanncohen created at 2010-07-06 09:58:59

Updated ! There should not be any other trace of the optional GLPK package in Sage :-)

Nathann



---

archive/issue_comments_089901.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-07-06T11:48:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9432",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9432#issuecomment-89901",
    "user": "https://github.com/rlmill"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_089902.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-07-06T11:50:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9432",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9432#issuecomment-89902",
    "user": "https://github.com/rlmill"
}
```

Resolution: fixed



---

archive/issue_events_023313.json:
```json
{
    "actor": "https://github.com/rlmill",
    "created_at": "2010-07-06T11:50:11Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/9432",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/9432#event-23313"
}
```

# Issue 3774: __radd__ doesn't work when left hand side is an Element

archive/issues_003774.json:
```json
{
    "body": "Assignee: @robertwb\n\nCC:  alexghitza\n\n\n```\nOn Aug 1, 2008, at 7:05 AM, Nils Skoruppa wrote:\n\n\nIt seems that,  for non elements,  __radd__ is set disfunctional\nby the coercion model. On the other hand, it might be desirable\nto have this enabled for people writing their own classes but having\nreasons to avoid (parts of)  the coercion system (like me :-)\n\n\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/3774\n\n",
    "created_at": "2008-08-05T08:24:46Z",
    "labels": [
        "coercion",
        "major",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.1.3",
    "title": "__radd__ doesn't work when left hand side is an Element",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/3774",
    "user": "@robertwb"
}
```
Assignee: @robertwb

CC:  alexghitza


```
On Aug 1, 2008, at 7:05 AM, Nils Skoruppa wrote:


It seems that,  for non elements,  __radd__ is set disfunctional
by the coercion model. On the other hand, it might be desirable
to have this enabled for people writing their own classes but having
reasons to avoid (parts of)  the coercion system (like me :-)


```


Issue created by migration from https://trac.sagemath.org/ticket/3774





---

archive/issue_comments_026842.json:
```json
{
    "body": "Attachment [3774-radd.patch](tarball://root/attachments/some-uuid/ticket3774/3774-radd.patch) by @robertwb created at 2008-08-05 08:25:54",
    "created_at": "2008-08-05T08:25:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3774",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3774#issuecomment-26842",
    "user": "@robertwb"
}
```

Attachment [3774-radd.patch](tarball://root/attachments/some-uuid/ticket3774/3774-radd.patch) by @robertwb created at 2008-08-05 08:25:54



---

archive/issue_comments_026843.json:
```json
{
    "body": "Might depend on #3738.",
    "created_at": "2008-08-11T16:33:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3774",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3774#issuecomment-26843",
    "user": "@robertwb"
}
```

Might depend on #3738.



---

archive/issue_comments_026844.json:
```json
{
    "body": "This could use a doctest.  robertwb, do you want to write one, if not, I can probably do it a bit later.",
    "created_at": "2008-08-25T00:02:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3774",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3774#issuecomment-26844",
    "user": "@mwhansen"
}
```

This could use a doctest.  robertwb, do you want to write one, if not, I can probably do it a bit later.



---

archive/issue_comments_026845.json:
```json
{
    "body": "Please go ahead and write one, though implementing `__radd__` should not be encouraged.",
    "created_at": "2008-08-25T16:58:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3774",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3774#issuecomment-26845",
    "user": "@robertwb"
}
```

Please go ahead and write one, though implementing `__radd__` should not be encouraged.



---

archive/issue_comments_026846.json:
```json
{
    "body": "Attachment [trac_3774.patch](tarball://root/attachments/some-uuid/ticket3774/trac_3774.patch) by @mwhansen created at 2008-09-24 02:10:59",
    "created_at": "2008-09-24T02:10:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3774",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3774#issuecomment-26846",
    "user": "@mwhansen"
}
```

Attachment [trac_3774.patch](tarball://root/attachments/some-uuid/ticket3774/trac_3774.patch) by @mwhansen created at 2008-09-24 02:10:59



---

archive/issue_comments_026847.json:
```json
{
    "body": "Okay, the new patch should apply.  Positive review.",
    "created_at": "2008-09-24T02:11:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3774",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3774#issuecomment-26847",
    "user": "@mwhansen"
}
```

Okay, the new patch should apply.  Positive review.



---

archive/issue_comments_026848.json:
```json
{
    "body": "Merged trac_3774.patch in Sage 3.1.3.alpha1",
    "created_at": "2008-09-24T04:23:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3774",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3774#issuecomment-26848",
    "user": "mabshoff"
}
```

Merged trac_3774.patch in Sage 3.1.3.alpha1



---

archive/issue_comments_026849.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-09-24T04:23:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3774",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3774#issuecomment-26849",
    "user": "mabshoff"
}
```

Resolution: fixed

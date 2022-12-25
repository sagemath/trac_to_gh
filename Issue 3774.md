# Issue 3774: [with patch, positive review] __radd__ doesn't work when left hand side is an Element

archive/issues_003774.json:
```json
{
    "body": "Assignee: @robertwb\n\nCC:  alexghitza\n\n```\nOn Aug 1, 2008, at 7:05 AM, Nils Skoruppa wrote:\n\n\nIt seems that,  for non elements,  __radd__ is set disfunctional\nby the coercion model. On the other hand, it might be desirable\nto have this enabled for people writing their own classes but having\nreasons to avoid (parts of)  the coercion system (like me :-)\n\n\n```\n\nIssue created by migration from https://trac.sagemath.org/ticket/3774\n\n",
    "closed_at": "2008-09-24T04:23:27Z",
    "created_at": "2008-08-05T08:24:46Z",
    "labels": [
        "component: coercion",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.1.3",
    "title": "[with patch, positive review] __radd__ doesn't work when left hand side is an Element",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/3774",
    "user": "https://github.com/robertwb"
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

archive/issue_comments_026784.json:
```json
{
    "body": "Attachment [3774-radd.patch](tarball://root/attachments/some-uuid/ticket3774/3774-radd.patch) by @robertwb created at 2008-08-05 08:25:54",
    "created_at": "2008-08-05T08:25:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3774",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3774#issuecomment-26784",
    "user": "https://github.com/robertwb"
}
```

Attachment [3774-radd.patch](tarball://root/attachments/some-uuid/ticket3774/3774-radd.patch) by @robertwb created at 2008-08-05 08:25:54



---

archive/issue_comments_026785.json:
```json
{
    "body": "Might depend on #3738.",
    "created_at": "2008-08-11T16:33:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3774",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3774#issuecomment-26785",
    "user": "https://github.com/robertwb"
}
```

Might depend on #3738.



---

archive/issue_comments_026786.json:
```json
{
    "body": "This could use a doctest.  robertwb, do you want to write one, if not, I can probably do it a bit later.",
    "created_at": "2008-08-25T00:02:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3774",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3774#issuecomment-26786",
    "user": "https://github.com/mwhansen"
}
```

This could use a doctest.  robertwb, do you want to write one, if not, I can probably do it a bit later.



---

archive/issue_comments_026787.json:
```json
{
    "body": "Please go ahead and write one, though implementing `__radd__` should not be encouraged.",
    "created_at": "2008-08-25T16:58:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3774",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3774#issuecomment-26787",
    "user": "https://github.com/robertwb"
}
```

Please go ahead and write one, though implementing `__radd__` should not be encouraged.



---

archive/issue_comments_026788.json:
```json
{
    "body": "Attachment [trac_3774.patch](tarball://root/attachments/some-uuid/ticket3774/trac_3774.patch) by @mwhansen created at 2008-09-24 02:10:59",
    "created_at": "2008-09-24T02:10:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3774",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3774#issuecomment-26788",
    "user": "https://github.com/mwhansen"
}
```

Attachment [trac_3774.patch](tarball://root/attachments/some-uuid/ticket3774/trac_3774.patch) by @mwhansen created at 2008-09-24 02:10:59



---

archive/issue_comments_026789.json:
```json
{
    "body": "Okay, the new patch should apply.  Positive review.",
    "created_at": "2008-09-24T02:11:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3774",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3774#issuecomment-26789",
    "user": "https://github.com/mwhansen"
}
```

Okay, the new patch should apply.  Positive review.



---

archive/issue_comments_026790.json:
```json
{
    "body": "Merged trac_3774.patch in Sage 3.1.3.alpha1",
    "created_at": "2008-09-24T04:23:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3774",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3774#issuecomment-26790",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged trac_3774.patch in Sage 3.1.3.alpha1



---

archive/issue_comments_026791.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-09-24T04:23:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3774",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3774#issuecomment-26791",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed



---

archive/issue_events_008651.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2008-09-24T04:23:27Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/3774",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/3774#event-8651"
}
```

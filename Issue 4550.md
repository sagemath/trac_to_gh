# Issue 4550: notebook -- removed unused NotebookSettings and UserSetting related code

archive/issues_004550.json:
```json
{
    "body": "Assignee: boothby\n\nCC:  @wjp\n\nDepends on #4089\n\nIssue created by migration from https://trac.sagemath.org/ticket/4550\n\n",
    "created_at": "2008-11-19T16:59:54Z",
    "labels": [
        "component: notebook",
        "trivial"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-duplicate/invalid/wontfix",
    "title": "notebook -- removed unused NotebookSettings and UserSetting related code",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/4550",
    "user": "https://trac.sagemath.org/admin/accounts/users/TimothyClemans"
}
```
Assignee: boothby

CC:  @wjp

Depends on #4089

Issue created by migration from https://trac.sagemath.org/ticket/4550





---

archive/issue_comments_034031.json:
```json
{
    "body": "Attachment [trac_4550.patch](tarball://root/attachments/some-uuid/ticket4550/trac_4550.patch) by @williamstein created at 2008-12-06 21:16:36\n\nJust out of curiosity, what is the justification for removing this code, besides \"it currently isn't being used\"?  For example, did you (Timothy) write new settings code that will replace this?   I think maybe (?) I wrote this code a long time ago as the framework that user and notebook settings code would go into, but never flushed that out.  So unless there is no code that is going to replace or some new design or *something*, I would like some sort of explanation about what the point of this is.",
    "created_at": "2008-12-06T21:16:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4550",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4550#issuecomment-34031",
    "user": "https://github.com/williamstein"
}
```

Attachment [trac_4550.patch](tarball://root/attachments/some-uuid/ticket4550/trac_4550.patch) by @williamstein created at 2008-12-06 21:16:36

Just out of curiosity, what is the justification for removing this code, besides "it currently isn't being used"?  For example, did you (Timothy) write new settings code that will replace this?   I think maybe (?) I wrote this code a long time ago as the framework that user and notebook settings code would go into, but never flushed that out.  So unless there is no code that is going to replace or some new design or *something*, I would like some sort of explanation about what the point of this is.



---

archive/issue_comments_034032.json:
```json
{
    "body": "I implemented Notebook and User settings without using the pre-existing framework. User Settings is already in Sage and Notebook Settings is #4551",
    "created_at": "2008-12-07T02:04:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4550",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4550#issuecomment-34032",
    "user": "https://trac.sagemath.org/admin/accounts/users/TimothyClemans"
}
```

I implemented Notebook and User settings without using the pre-existing framework. User Settings is already in Sage and Notebook Settings is #4551



---

archive/issue_comments_034033.json:
```json
{
    "body": "Attachment [sage-4550.patch](tarball://root/attachments/some-uuid/ticket4550/sage-4550.patch) by TimothyClemans created at 2008-12-21 20:59:05",
    "created_at": "2008-12-21T20:59:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4550",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4550#issuecomment-34033",
    "user": "https://trac.sagemath.org/admin/accounts/users/TimothyClemans"
}
```

Attachment [sage-4550.patch](tarball://root/attachments/some-uuid/ticket4550/sage-4550.patch) by TimothyClemans created at 2008-12-21 20:59:05



---

archive/issue_comments_034034.json:
```json
{
    "body": "apply sage-4550.patch (rebased)",
    "created_at": "2008-12-21T20:59:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4550",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4550#issuecomment-34034",
    "user": "https://trac.sagemath.org/admin/accounts/users/TimothyClemans"
}
```

apply sage-4550.patch (rebased)



---

archive/issue_comments_034035.json:
```json
{
    "body": "Attachment [trac_4550-2.patch](tarball://root/attachments/some-uuid/ticket4550/trac_4550-2.patch) by @dandrake created at 2009-09-05 01:17:51\n\nrebased on 4.1.2.alpha0",
    "created_at": "2009-09-05T01:17:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4550",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4550#issuecomment-34035",
    "user": "https://github.com/dandrake"
}
```

Attachment [trac_4550-2.patch](tarball://root/attachments/some-uuid/ticket4550/trac_4550-2.patch) by @dandrake created at 2009-09-05 01:17:51

rebased on 4.1.2.alpha0



---

archive/issue_comments_034036.json:
```json
{
    "body": "I'm going to try and go through this group of notebook patches and rebase them so we can at least discuss them.",
    "created_at": "2009-09-05T01:21:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4550",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4550#issuecomment-34036",
    "user": "https://github.com/dandrake"
}
```

I'm going to try and go through this group of notebook patches and rebase them so we can at least discuss them.



---

archive/issue_comments_034037.json:
```json
{
    "body": "See #4551 for a sagenb (cf. #6983) rebase that includes [attachment:trac_4550-2.patch].",
    "created_at": "2009-10-10T07:30:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4550",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4550#issuecomment-34037",
    "user": "https://github.com/qed777"
}
```

See #4551 for a sagenb (cf. #6983) rebase that includes [attachment:trac_4550-2.patch].



---

archive/issue_comments_034038.json:
```json
{
    "body": "Changing status from needs_review to needs_info.",
    "created_at": "2009-10-23T07:17:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4550",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4550#issuecomment-34038",
    "user": "https://github.com/qed777"
}
```

Changing status from needs_review to needs_info.



---

archive/issue_comments_034039.json:
```json
{
    "body": "#4551 subsumes this ticket.  Please close this one.",
    "created_at": "2009-10-23T07:17:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4550",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4550#issuecomment-34039",
    "user": "https://github.com/qed777"
}
```

#4551 subsumes this ticket.  Please close this one.



---

archive/issue_comments_034040.json:
```json
{
    "body": "Resolution: invalid",
    "created_at": "2009-12-09T14:28:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4550",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4550#issuecomment-34040",
    "user": "https://github.com/williamstein"
}
```

Resolution: invalid

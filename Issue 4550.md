# Issue 4550: notebook -- removed unused NotebookSettings and UserSetting related code

archive/issues_004550.json:
```json
{
    "body": "Assignee: boothby\n\nCC:  wjp\n\nDepends on #4089\n\nIssue created by migration from https://trac.sagemath.org/ticket/4550\n\n",
    "created_at": "2008-11-19T16:59:54Z",
    "labels": [
        "notebook",
        "trivial",
        "enhancement"
    ],
    "title": "notebook -- removed unused NotebookSettings and UserSetting related code",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/4550",
    "user": "TimothyClemans"
}
```
Assignee: boothby

CC:  wjp

Depends on #4089

Issue created by migration from https://trac.sagemath.org/ticket/4550





---

archive/issue_comments_034098.json:
```json
{
    "body": "Attachment\n\nJust out of curiosity, what is the justification for removing this code, besides \"it currently isn't being used\"?  For example, did you (Timothy) write new settings code that will replace this?   I think maybe (?) I wrote this code a long time ago as the framework that user and notebook settings code would go into, but never flushed that out.  So unless there is no code that is going to replace or some new design or *something*, I would like some sort of explanation about what the point of this is.",
    "created_at": "2008-12-06T21:16:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4550",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4550#issuecomment-34098",
    "user": "was"
}
```

Attachment

Just out of curiosity, what is the justification for removing this code, besides "it currently isn't being used"?  For example, did you (Timothy) write new settings code that will replace this?   I think maybe (?) I wrote this code a long time ago as the framework that user and notebook settings code would go into, but never flushed that out.  So unless there is no code that is going to replace or some new design or *something*, I would like some sort of explanation about what the point of this is.



---

archive/issue_comments_034099.json:
```json
{
    "body": "I implemented Notebook and User settings without using the pre-existing framework. User Settings is already in Sage and Notebook Settings is #4551",
    "created_at": "2008-12-07T02:04:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4550",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4550#issuecomment-34099",
    "user": "TimothyClemans"
}
```

I implemented Notebook and User settings without using the pre-existing framework. User Settings is already in Sage and Notebook Settings is #4551



---

archive/issue_comments_034100.json:
```json
{
    "body": "Attachment",
    "created_at": "2008-12-21T20:59:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4550",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4550#issuecomment-34100",
    "user": "TimothyClemans"
}
```

Attachment



---

archive/issue_comments_034101.json:
```json
{
    "body": "apply sage-4550.patch (rebased)",
    "created_at": "2008-12-21T20:59:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4550",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4550#issuecomment-34101",
    "user": "TimothyClemans"
}
```

apply sage-4550.patch (rebased)



---

archive/issue_comments_034102.json:
```json
{
    "body": "Attachment\n\nrebased on 4.1.2.alpha0",
    "created_at": "2009-09-05T01:17:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4550",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4550#issuecomment-34102",
    "user": "ddrake"
}
```

Attachment

rebased on 4.1.2.alpha0



---

archive/issue_comments_034103.json:
```json
{
    "body": "I'm going to try and go through this group of notebook patches and rebase them so we can at least discuss them.",
    "created_at": "2009-09-05T01:21:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4550",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4550#issuecomment-34103",
    "user": "ddrake"
}
```

I'm going to try and go through this group of notebook patches and rebase them so we can at least discuss them.



---

archive/issue_comments_034104.json:
```json
{
    "body": "See #4551 for a sagenb (cf. #6983) rebase that includes [attachment:trac_4550-2.patch].",
    "created_at": "2009-10-10T07:30:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4550",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4550#issuecomment-34104",
    "user": "mpatel"
}
```

See #4551 for a sagenb (cf. #6983) rebase that includes [attachment:trac_4550-2.patch].



---

archive/issue_comments_034105.json:
```json
{
    "body": "Changing status from needs_review to needs_info.",
    "created_at": "2009-10-23T07:17:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4550",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4550#issuecomment-34105",
    "user": "mpatel"
}
```

Changing status from needs_review to needs_info.



---

archive/issue_comments_034106.json:
```json
{
    "body": "#4551 subsumes this ticket.  Please close this one.",
    "created_at": "2009-10-23T07:17:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4550",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4550#issuecomment-34106",
    "user": "mpatel"
}
```

#4551 subsumes this ticket.  Please close this one.



---

archive/issue_comments_034107.json:
```json
{
    "body": "Resolution: invalid",
    "created_at": "2009-12-09T14:28:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4550",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4550#issuecomment-34107",
    "user": "was"
}
```

Resolution: invalid

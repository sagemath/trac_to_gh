# Issue 2926: Minilistic change password page for notebook user

archive/issues_002926.json:
```json
{
    "body": "Assignee: TimothyClemans\n\n* Write resource \"passwd\" with inspiration from RegistrationPage\n* Add resource \"passwd\" to UserTopLevel\n* Add link to \"change password\" in the list entries in the function _html_body in notebook.py\n\nIssue created by migration from https://trac.sagemath.org/ticket/2926\n\n",
    "created_at": "2008-04-15T03:46:38Z",
    "labels": [
        "component: notebook"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.0.2",
    "title": "Minilistic change password page for notebook user",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/2926",
    "user": "https://trac.sagemath.org/admin/accounts/users/TimothyClemans"
}
```
Assignee: TimothyClemans

* Write resource "passwd" with inspiration from RegistrationPage
* Add resource "passwd" to UserTopLevel
* Add link to "change password" in the list entries in the function _html_body in notebook.py

Issue created by migration from https://trac.sagemath.org/ticket/2926





---

archive/issue_comments_020102.json:
```json
{
    "body": "Attachment [2926.patch](tarball://root/attachments/some-uuid/ticket2926/2926.patch) by TimothyClemans created at 2008-04-15 18:39:35",
    "created_at": "2008-04-15T18:39:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2926",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2926#issuecomment-20102",
    "user": "https://trac.sagemath.org/admin/accounts/users/TimothyClemans"
}
```

Attachment [2926.patch](tarball://root/attachments/some-uuid/ticket2926/2926.patch) by TimothyClemans created at 2008-04-15 18:39:35



---

archive/issue_comments_020103.json:
```json
{
    "body": "This might be superseded by #2936, but if the functionality is not in there it can probably ported to the new codebase.\n\nCheers,\n\nMichael",
    "created_at": "2008-04-16T01:16:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2926",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2926#issuecomment-20103",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

This might be superseded by #2936, but if the functionality is not in there it can probably ported to the new codebase.

Cheers,

Michael



---

archive/issue_comments_020104.json:
```json
{
    "body": "This just works.  There's no way for a user to actually use it short of explicitly typing\n/passwd in the URL.  But it does work correctly and the underlying code looks good.\n\nI wish it were somehow tested, but I don't know how to test it (yet).\n\nSo it's a preliminary and solid step to this functionality, so it should go in.  \n\nI don't think it overlaps with #2936 which is more backend stuff, whereas this is more UI oriented.",
    "created_at": "2008-05-11T08:49:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2926",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2926#issuecomment-20104",
    "user": "https://github.com/williamstein"
}
```

This just works.  There's no way for a user to actually use it short of explicitly typing
/passwd in the URL.  But it does work correctly and the underlying code looks good.

I wish it were somehow tested, but I don't know how to test it (yet).

So it's a preliminary and solid step to this functionality, so it should go in.  

I don't think it overlaps with #2936 which is more backend stuff, whereas this is more UI oriented.



---

archive/issue_comments_020105.json:
```json
{
    "body": "Merged in Sage 3.0.2.alpha0",
    "created_at": "2008-05-11T10:47:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2926",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2926#issuecomment-20105",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged in Sage 3.0.2.alpha0



---

archive/issue_comments_020106.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-05-11T10:47:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2926",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2926#issuecomment-20106",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed



---

archive/issue_events_003126.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2008-05-11T10:47:42Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/2926",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/2926#event-3126"
}
```

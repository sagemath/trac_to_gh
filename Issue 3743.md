# Issue 3743: notebook -- allow admin user to view any worksheet

archive/issues_003743.json:
```json
{
    "body": "Assignee: boothby\n\nUser \"admin\" will be able to go to hostname/users and click on any listed user and have complete access to that user's worksheets.\n\nIssue created by migration from https://trac.sagemath.org/ticket/3743\n\n",
    "created_at": "2008-07-29T18:09:08Z",
    "labels": [
        "component: notebook"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.1",
    "title": "notebook -- allow admin user to view any worksheet",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/3743",
    "user": "https://trac.sagemath.org/admin/accounts/users/TimothyClemans"
}
```
Assignee: boothby

User "admin" will be able to go to hostname/users and click on any listed user and have complete access to that user's worksheets.

Issue created by migration from https://trac.sagemath.org/ticket/3743





---

archive/issue_comments_026523.json:
```json
{
    "body": "Attachment [sage-3743.patch](tarball://root/attachments/some-uuid/ticket3743/sage-3743.patch) by TimothyClemans created at 2008-07-29 18:19:14",
    "created_at": "2008-07-29T18:19:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3743",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3743#issuecomment-26523",
    "user": "https://trac.sagemath.org/admin/accounts/users/TimothyClemans"
}
```

Attachment [sage-3743.patch](tarball://root/attachments/some-uuid/ticket3743/sage-3743.patch) by TimothyClemans created at 2008-07-29 18:19:14



---

archive/issue_comments_026524.json:
```json
{
    "body": "REFEREE REPORT:\n\nYou determine whether a user is an admin with\n\n```\n           if self.username == 'admin' \n```\n\nIt would be better to determine whether a user is an admin by using the account_type() method of users.  This is because a user with a username other than 'admin' can still be an admin; with the code you've written you would introduce a bug since suddenly certain admin-like things wouldn't work for such a user, but they should.",
    "created_at": "2008-07-29T21:49:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3743",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3743#issuecomment-26524",
    "user": "https://github.com/williamstein"
}
```

REFEREE REPORT:

You determine whether a user is an admin with

```
           if self.username == 'admin' 
```

It would be better to determine whether a user is an admin by using the account_type() method of users.  This is because a user with a username other than 'admin' can still be an admin; with the code you've written you would introduce a bug since suddenly certain admin-like things wouldn't work for such a user, but they should.



---

archive/issue_comments_026525.json:
```json
{
    "body": "I started out using user_type but for whatever reason for user admin it was returning 'user' so to get the functionality working at all I used the current work around.",
    "created_at": "2008-07-30T03:57:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3743",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3743#issuecomment-26525",
    "user": "https://trac.sagemath.org/admin/accounts/users/TimothyClemans"
}
```

I started out using user_type but for whatever reason for user admin it was returning 'user' so to get the functionality working at all I used the current work around.



---

archive/issue_comments_026526.json:
```json
{
    "body": "Attachment [sage-3743_2.patch](tarball://root/attachments/some-uuid/ticket3743/sage-3743_2.patch) by TimothyClemans created at 2008-07-30 04:26:41",
    "created_at": "2008-07-30T04:26:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3743",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3743#issuecomment-26526",
    "user": "https://trac.sagemath.org/admin/accounts/users/TimothyClemans"
}
```

Attachment [sage-3743_2.patch](tarball://root/attachments/some-uuid/ticket3743/sage-3743_2.patch) by TimothyClemans created at 2008-07-30 04:26:41



---

archive/issue_comments_026527.json:
```json
{
    "body": "Positive review",
    "created_at": "2008-08-05T05:44:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3743",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3743#issuecomment-26527",
    "user": "https://github.com/williamstein"
}
```

Positive review



---

archive/issue_comments_026528.json:
```json
{
    "body": "Merged both patches in Sage 3.1.alpha1",
    "created_at": "2008-08-06T01:29:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3743",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3743#issuecomment-26528",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged both patches in Sage 3.1.alpha1



---

archive/issue_comments_026529.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-08-06T01:29:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3743",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3743#issuecomment-26529",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed



---

archive/issue_events_003966.json:
```json
{
    "actor": "mabshoff",
    "created_at": "2008-08-06T01:29:40Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/3743",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/3743#event-3966"
}
```

# Issue 7909: Replace $MKDIR with 'mkdir' in sage-spkg

archive/issues_007909.json:
```json
{
    "body": "Assignee: GeorgSWeber\n\nCC:  @jaapspies\n\nsage-env has $MKDIR in one place, which will cause problems with an updated 'sage-env' which no longer defines MKDIR. \n\nI'm attaching a copy of the revised sage-env, and also a Mercurial patch.\n\nIssue created by migration from https://trac.sagemath.org/ticket/7909\n\n",
    "created_at": "2010-01-12T16:15:32Z",
    "labels": [
        "component: build",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.3.1",
    "title": "Replace $MKDIR with 'mkdir' in sage-spkg",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/7909",
    "user": "https://trac.sagemath.org/admin/accounts/users/drkirkby"
}
```
Assignee: GeorgSWeber

CC:  @jaapspies

sage-env has $MKDIR in one place, which will cause problems with an updated 'sage-env' which no longer defines MKDIR. 

I'm attaching a copy of the revised sage-env, and also a Mercurial patch.

Issue created by migration from https://trac.sagemath.org/ticket/7909





---

archive/issue_comments_068659.json:
```json
{
    "body": "Attachment [sage-spkg](tarball://root/attachments/some-uuid/ticket7909/sage-spkg) by drkirkby created at 2010-01-12 16:21:17\n\nA complete copy of the revised sage-env",
    "created_at": "2010-01-12T16:21:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7909",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7909#issuecomment-68659",
    "user": "https://trac.sagemath.org/admin/accounts/users/drkirkby"
}
```

Attachment [sage-spkg](tarball://root/attachments/some-uuid/ticket7909/sage-spkg) by drkirkby created at 2010-01-12 16:21:17

A complete copy of the revised sage-env



---

archive/issue_comments_068660.json:
```json
{
    "body": "Mercurial patch for sage-env",
    "created_at": "2010-01-12T16:21:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7909",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7909#issuecomment-68660",
    "user": "https://trac.sagemath.org/admin/accounts/users/drkirkby"
}
```

Mercurial patch for sage-env



---

archive/issue_comments_068661.json:
```json
{
    "body": "Attachment [sage-spkg-remove-MKDIR.patch](tarball://root/attachments/some-uuid/ticket7909/sage-spkg-remove-MKDIR.patch) by drkirkby created at 2010-01-12 16:22:15",
    "created_at": "2010-01-12T16:22:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7909",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7909#issuecomment-68661",
    "user": "https://trac.sagemath.org/admin/accounts/users/drkirkby"
}
```

Attachment [sage-spkg-remove-MKDIR.patch](tarball://root/attachments/some-uuid/ticket7909/sage-spkg-remove-MKDIR.patch) by drkirkby created at 2010-01-12 16:22:15



---

archive/issue_comments_068662.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-01-12T16:22:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7909",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7909#issuecomment-68662",
    "user": "https://trac.sagemath.org/admin/accounts/users/drkirkby"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_068663.json:
```json
{
    "body": "Don't know whether the name 'sage-spkg' is any good. Did you mean to attach the new sage-env?\n\nThe patch is simple and looks good.\n\n\nJaap",
    "created_at": "2010-01-12T16:48:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7909",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7909#issuecomment-68663",
    "user": "https://github.com/jaapspies"
}
```

Don't know whether the name 'sage-spkg' is any good. Did you mean to attach the new sage-env?

The patch is simple and looks good.


Jaap



---

archive/issue_comments_068664.json:
```json
{
    "body": "Replying to [comment:2 jsp]:\n> Don't know whether the name 'sage-spkg' is any good. Did you mean to attach the new sage-env?\n> \n> The patch is simple and looks good.\n> \n> \n> Jaap\n> \n\nIt is really in sage-spkg!!  I changed the description.\n\nWaiting for the mercurial patch.\n\nJaap",
    "created_at": "2010-01-12T17:25:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7909",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7909#issuecomment-68664",
    "user": "https://github.com/jaapspies"
}
```

Replying to [comment:2 jsp]:
> Don't know whether the name 'sage-spkg' is any good. Did you mean to attach the new sage-env?
> 
> The patch is simple and looks good.
> 
> 
> Jaap
> 

It is really in sage-spkg!!  I changed the description.

Waiting for the mercurial patch.

Jaap



---

archive/issue_comments_068665.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-01-12T17:30:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7909",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7909#issuecomment-68665",
    "user": "https://github.com/jaapspies"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_068666.json:
```json
{
    "body": "The \"mercurial patch\" is ok. sage-spkg looks good. So positive review.\n\nJaap",
    "created_at": "2010-01-12T17:30:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7909",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7909#issuecomment-68666",
    "user": "https://github.com/jaapspies"
}
```

The "mercurial patch" is ok. sage-spkg looks good. So positive review.

Jaap



---

archive/issue_comments_068667.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-01-14T03:03:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7909",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7909#issuecomment-68667",
    "user": "https://github.com/rlmill"
}
```

Resolution: fixed

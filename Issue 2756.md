# Issue 2756: [with patch; needs review] Debianize GAP spkg

archive/issues_002756.json:
```json
{
    "body": "Assignee: @timabbott\n\nI've attached a patch to add Debian build support to the GAP spkg (it only builds the Guava GAP package).\n\nIssue created by migration from https://trac.sagemath.org/ticket/2756\n\n",
    "created_at": "2008-04-01T18:41:37Z",
    "labels": [
        "component: debian-package"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.0",
    "title": "[with patch; needs review] Debianize GAP spkg",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/2756",
    "user": "https://github.com/timabbott"
}
```
Assignee: @timabbott

I've attached a patch to add Debian build support to the GAP spkg (it only builds the Guava GAP package).

Issue created by migration from https://trac.sagemath.org/ticket/2756





---

archive/issue_comments_018912.json:
```json
{
    "body": "Attachment [guava.patch](tarball://root/attachments/some-uuid/ticket2756/guava.patch) by @timabbott created at 2008-04-01 18:41:49",
    "created_at": "2008-04-01T18:41:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2756",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2756#issuecomment-18912",
    "user": "https://github.com/timabbott"
}
```

Attachment [guava.patch](tarball://root/attachments/some-uuid/ticket2756/guava.patch) by @timabbott created at 2008-04-01 18:41:49



---

archive/issue_comments_018913.json:
```json
{
    "body": "Attachment [gap-spkg-debian.patch](tarball://root/attachments/some-uuid/ticket2756/gap-spkg-debian.patch) by @timabbott created at 2008-04-01 18:42:48",
    "created_at": "2008-04-01T18:42:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2756",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2756#issuecomment-18913",
    "user": "https://github.com/timabbott"
}
```

Attachment [gap-spkg-debian.patch](tarball://root/attachments/some-uuid/ticket2756/gap-spkg-debian.patch) by @timabbott created at 2008-04-01 18:42:48



---

archive/issue_comments_018914.json:
```json
{
    "body": "Patch looks good to me. One slight issue is that Guava has been updated to Guava 3.4. So let's merge this in alpha0 and if it doesn't work we can fix it later.\n\nCheers,\n\nMichael",
    "created_at": "2008-04-01T22:54:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2756",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2756#issuecomment-18914",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Patch looks good to me. One slight issue is that Guava has been updated to Guava 3.4. So let's merge this in alpha0 and if it doesn't work we can fix it later.

Cheers,

Michael



---

archive/issue_comments_018915.json:
```json
{
    "body": "Merged in gap-4.4.10.p5 in Sage 3.0.alpha0",
    "created_at": "2008-04-01T23:06:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2756",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2756#issuecomment-18915",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged in gap-4.4.10.p5 in Sage 3.0.alpha0



---

archive/issue_comments_018916.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-04-01T23:06:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2756",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2756#issuecomment-18916",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed



---

archive/issue_events_002944.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2008-04-01T23:06:58Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/2756",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/2756#event-2944"
}
```

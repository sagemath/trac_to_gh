# Issue 3834: notebook -- massive bug in the notebook -- doing full text search starts a PYthon process for every single worksheet you have!!!

archive/issues_003834.json:
```json
{
    "body": "Assignee: boothby\n\nnotebook -- massive bug in the notebook -- doing full text search starts a PYthon process for every single worksheet you have!!!\n\nThis is a major showstopper bug.\n\nAnd it's either my fault (or Timothy Clemans), but probably me. \n\nThe solution will be to rewrite how full text search works to just look at the filesystem.\nI'm guessing right now it is suddenly doing something really stupid as a result of the \noptimizations I made recently to the notebook.\n\nIssue created by migration from https://trac.sagemath.org/ticket/3834\n\n",
    "created_at": "2008-08-13T06:23:47Z",
    "labels": [
        "component: notebook",
        "blocker",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.1",
    "title": "notebook -- massive bug in the notebook -- doing full text search starts a PYthon process for every single worksheet you have!!!",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/3834",
    "user": "https://github.com/williamstein"
}
```
Assignee: boothby

notebook -- massive bug in the notebook -- doing full text search starts a PYthon process for every single worksheet you have!!!

This is a major showstopper bug.

And it's either my fault (or Timothy Clemans), but probably me. 

The solution will be to rewrite how full text search works to just look at the filesystem.
I'm guessing right now it is suddenly doing something really stupid as a result of the 
optimizations I made recently to the notebook.

Issue created by migration from https://trac.sagemath.org/ticket/3834





---

archive/issue_comments_027204.json:
```json
{
    "body": "Attachment [sage-3834.patch](tarball://root/attachments/some-uuid/ticket3834/sage-3834.patch) by @williamstein created at 2008-08-13 07:39:29",
    "created_at": "2008-08-13T07:39:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3834",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3834#issuecomment-27204",
    "user": "https://github.com/williamstein"
}
```

Attachment [sage-3834.patch](tarball://root/attachments/some-uuid/ticket3834/sage-3834.patch) by @williamstein created at 2008-08-13 07:39:29



---

archive/issue_comments_027205.json:
```json
{
    "body": "I am happy with this patch. Positive review.\n\nCheers,\n\nMichael",
    "created_at": "2008-08-15T09:54:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3834",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3834#issuecomment-27205",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

I am happy with this patch. Positive review.

Cheers,

Michael



---

archive/issue_comments_027206.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-08-15T09:55:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3834",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3834#issuecomment-27206",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_027207.json:
```json
{
    "body": "Merged in Sage 3.1.rc0",
    "created_at": "2008-08-15T09:55:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3834",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3834#issuecomment-27207",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged in Sage 3.1.rc0



---

archive/issue_events_004058.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2008-08-15T09:55:50Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/3834",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/3834#event-4058"
}
```

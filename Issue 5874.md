# Issue 5874: [with patch, needs review] Fix readline build on FreeBSD

archive/issues_005874.json:
```json
{
    "body": "Assignee: mabshoff\n\nCC:  chet.ramey@case.edu\n\nChase shared library name difference on FreeBSD. Without this patch, the build claims that expected files don't exist.\n\nIssue created by migration from https://trac.sagemath.org/ticket/5874\n\n",
    "created_at": "2009-04-23T08:47:52Z",
    "labels": [
        "component: porting: bsd",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.1",
    "title": "[with patch, needs review] Fix readline build on FreeBSD",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/5874",
    "user": "https://github.com/peterjeremy"
}
```
Assignee: mabshoff

CC:  chet.ramey@case.edu

Chase shared library name difference on FreeBSD. Without this patch, the build claims that expected files don't exist.

Issue created by migration from https://trac.sagemath.org/ticket/5874





---

archive/issue_comments_046314.json:
```json
{
    "body": "Attachment [readline-5.2.p6.patch](tarball://root/attachments/some-uuid/ticket5874/readline-5.2.p6.patch) by @peterjeremy created at 2009-04-23 08:48:23",
    "created_at": "2009-04-23T08:48:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5874",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5874#issuecomment-46314",
    "user": "https://github.com/peterjeremy"
}
```

Attachment [readline-5.2.p6.patch](tarball://root/attachments/some-uuid/ticket5874/readline-5.2.p6.patch) by @peterjeremy created at 2009-04-23 08:48:23



---

archive/issue_comments_046315.json:
```json
{
    "body": "Changing assignee from mabshoff to @mwhansen.",
    "created_at": "2009-06-20T02:26:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5874",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5874#issuecomment-46315",
    "user": "https://github.com/mwhansen"
}
```

Changing assignee from mabshoff to @mwhansen.



---

archive/issue_comments_046316.json:
```json
{
    "body": "Looks good to me.\n\nThe spkg with the patch incorporated is at http://sage.math.washington.edu/home/mhansen/readline-5.2.p7.spkg",
    "created_at": "2009-06-20T02:26:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5874",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5874#issuecomment-46316",
    "user": "https://github.com/mwhansen"
}
```

Looks good to me.

The spkg with the patch incorporated is at http://sage.math.washington.edu/home/mhansen/readline-5.2.p7.spkg



---

archive/issue_comments_046317.json:
```json
{
    "body": "Cc maintainer.  Apologies for neglecting this before",
    "created_at": "2009-06-27T08:18:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5874",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5874#issuecomment-46317",
    "user": "https://github.com/peterjeremy"
}
```

Cc maintainer.  Apologies for neglecting this before



---

archive/issue_comments_046318.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-07-02T23:07:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5874",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5874#issuecomment-46318",
    "user": "https://github.com/rlmill"
}
```

Resolution: fixed



---

archive/issue_events_006130.json:
```json
{
    "actor": "https://github.com/rlmill",
    "created_at": "2009-07-02T23:07:32Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/5874",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/5874#event-6130"
}
```

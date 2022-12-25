# Issue 2522: [with patch; positive review] modify "sage -pkg" to not include OSX junk in spkgs

archive/issues_002522.json:
```json
{
    "body": "Assignee: mabshoff\n\nIt looks like maybe we only need to set an environment variable to eliminate at least some of the junk; see http://norman.walsh.name/2008/02/22/tar for details.\n\nIssue created by migration from https://trac.sagemath.org/ticket/2522\n\n",
    "closed_at": "2009-02-16T04:34:44Z",
    "created_at": "2008-03-14T23:54:05Z",
    "labels": [
        "component: packages: standard"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.3",
    "title": "[with patch; positive review] modify \"sage -pkg\" to not include OSX junk in spkgs",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/2522",
    "user": "https://trac.sagemath.org/admin/accounts/users/cwitty"
}
```
Assignee: mabshoff

It looks like maybe we only need to set an environment variable to eliminate at least some of the junk; see http://norman.walsh.name/2008/02/22/tar for details.

Issue created by migration from https://trac.sagemath.org/ticket/2522





---

archive/issue_comments_017165.json:
```json
{
    "body": "Attachment [trac_2522.patch](tarball://root/attachments/some-uuid/ticket2522/trac_2522.patch) by @williamstein created at 2009-02-16 04:31:30\n\nOne just has to set\n\n```\nCOPYFILE_DISABLE=true\n```\non OS X.",
    "created_at": "2009-02-16T04:31:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2522",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2522#issuecomment-17165",
    "user": "https://github.com/williamstein"
}
```

Attachment [trac_2522.patch](tarball://root/attachments/some-uuid/ticket2522/trac_2522.patch) by @williamstein created at 2009-02-16 04:31:30

One just has to set

```
COPYFILE_DISABLE=true
```
on OS X.



---

archive/issue_events_005921.json:
```json
{
    "actor": "https://github.com/williamstein",
    "created_at": "2009-02-16T04:31:38Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/2522",
    "milestone": "sage-3.3",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/2522#event-5921"
}
```



---

archive/issue_comments_017166.json:
```json
{
    "body": "Yep, that does the trick.\n\nCheers,\n\nMichael",
    "created_at": "2009-02-16T04:34:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2522",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2522#issuecomment-17166",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Yep, that does the trick.

Cheers,

Michael



---

archive/issue_events_005922.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2009-02-16T04:34:44Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/2522",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/2522#event-5922"
}
```



---

archive/issue_comments_017167.json:
```json
{
    "body": "Merged in Sage 3.3.rc1.\n\nCheers,\n\nMichael",
    "created_at": "2009-02-16T04:34:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2522",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2522#issuecomment-17167",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged in Sage 3.3.rc1.

Cheers,

Michael



---

archive/issue_comments_017168.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-02-16T04:34:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2522",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2522#issuecomment-17168",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed

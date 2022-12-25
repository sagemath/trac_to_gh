# Issue 5045: sage's "make check" should check that the sage build flags (in sage-flags.txt) are right

archive/issues_005045.json:
```json
{
    "body": "Assignee: mabshoff\n\nSome people do \"make check\" but never even try to run sage.  Thus it is stupid that make check can run without ever verifying that sage-flags.txt is valid.  If it isn't, just stop the check.\n\nIssue created by migration from https://trac.sagemath.org/ticket/5045\n\n",
    "created_at": "2009-01-21T06:00:52Z",
    "labels": [
        "component: doctest coverage",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.3",
    "title": "sage's \"make check\" should check that the sage build flags (in sage-flags.txt) are right",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/5045",
    "user": "https://github.com/williamstein"
}
```
Assignee: mabshoff

Some people do "make check" but never even try to run sage.  Thus it is stupid that make check can run without ever verifying that sage-flags.txt is valid.  If it isn't, just stop the check.

Issue created by migration from https://trac.sagemath.org/ticket/5045





---

archive/issue_comments_038352.json:
```json
{
    "body": "Attachment [trac_5045_scripts-rep.patch](tarball://root/attachments/some-uuid/ticket5045/trac_5045_scripts-rep.patch) by @williamstein created at 2009-01-22 10:10:18",
    "created_at": "2009-01-22T10:10:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5045",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5045#issuecomment-38352",
    "user": "https://github.com/williamstein"
}
```

Attachment [trac_5045_scripts-rep.patch](tarball://root/attachments/some-uuid/ticket5045/trac_5045_scripts-rep.patch) by @williamstein created at 2009-01-22 10:10:18



---

archive/issue_comments_038353.json:
```json
{
    "body": "To test this, edit SAGE_ROOT/local/lib/sage-flags.txt and add some madeup flags like x.  Then test by doing, e.g., \n\n```\nmake check\n```\nand seeing that the build process properly stops.",
    "created_at": "2009-01-22T10:11:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5045",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5045#issuecomment-38353",
    "user": "https://github.com/williamstein"
}
```

To test this, edit SAGE_ROOT/local/lib/sage-flags.txt and add some madeup flags like x.  Then test by doing, e.g., 

```
make check
```
and seeing that the build process properly stops.



---

archive/issue_comments_038354.json:
```json
{
    "body": "Nice.\n\nCheers,\n\nMichael",
    "created_at": "2009-01-22T10:38:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5045",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5045#issuecomment-38354",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Nice.

Cheers,

Michael



---

archive/issue_events_011636.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2009-01-23T08:47:53Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/5045",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/5045#event-11636"
}
```



---

archive/issue_comments_038355.json:
```json
{
    "body": "Merged in Sage 3.3.alpha1",
    "created_at": "2009-01-23T08:47:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5045",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5045#issuecomment-38355",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged in Sage 3.3.alpha1



---

archive/issue_comments_038356.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-01-23T08:47:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5045",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5045#issuecomment-38356",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed

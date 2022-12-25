# Issue 2772: Update Singular to 3-0-4-2

archive/issues_002772.json:
```json
{
    "body": "Assignee: @malb\n\nThis version has GCC 4.3 support.\n\nIssue created by migration from https://trac.sagemath.org/ticket/2772\n\n",
    "created_at": "2008-04-02T15:33:08Z",
    "labels": [
        "component: commutative algebra",
        "blocker"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.0",
    "title": "Update Singular to 3-0-4-2",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/2772",
    "user": "https://github.com/malb"
}
```
Assignee: @malb

This version has GCC 4.3 support.

Issue created by migration from https://trac.sagemath.org/ticket/2772





---

archive/issue_comments_019012.json:
```json
{
    "body": "A new SPKG is available at:\n\n  http://sage.math.washington.edu/home/malb/singular-3-0-4-2-20080404.spkg\n\nHowever, this is not ready for inclusion yet, because of some problem with the GCD. It works correctly from Singular but not correctly via the libSingular interface. I'm working on it.",
    "created_at": "2008-04-04T13:54:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2772",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2772#issuecomment-19012",
    "user": "https://github.com/malb"
}
```

A new SPKG is available at:

  http://sage.math.washington.edu/home/malb/singular-3-0-4-2-20080404.spkg

However, this is not ready for inclusion yet, because of some problem with the GCD. It works correctly from Singular but not correctly via the libSingular interface. I'm working on it.



---

archive/issue_comments_019013.json:
```json
{
    "body": "Attachment [singular-3-0-4-2-gcd-fix.patch](tarball://root/attachments/some-uuid/ticket2772/singular-3-0-4-2-gcd-fix.patch) by @malb created at 2008-04-05 16:31:35",
    "created_at": "2008-04-05T16:31:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2772",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2772#issuecomment-19013",
    "user": "https://github.com/malb"
}
```

Attachment [singular-3-0-4-2-gcd-fix.patch](tarball://root/attachments/some-uuid/ticket2772/singular-3-0-4-2-gcd-fix.patch) by @malb created at 2008-04-05 16:31:35



---

archive/issue_comments_019014.json:
```json
{
    "body": "A new SPKG is available at:\n\n   http://sage.math.washington.edu/home/malb/singular-3-0-4-2-20080405.spkg\n\nwhich in combination with the attached patch should pass all doctests.",
    "created_at": "2008-04-05T16:37:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2772",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2772#issuecomment-19014",
    "user": "https://github.com/malb"
}
```

A new SPKG is available at:

   http://sage.math.washington.edu/home/malb/singular-3-0-4-2-20080405.spkg

which in combination with the attached patch should pass all doctests.



---

archive/issue_comments_019015.json:
```json
{
    "body": "The patch applies cleanly, the spkg compiles cleanly for me on OSX and Linux. Doctests pass. I did find two small issues:\n\n* I removed spkg-install.orig from the spkg\n* I also removed the comment that SPKG.txt is deprecated from that file.\n\nIn total: positive review.\n\nCheers,\n\nMichael",
    "created_at": "2008-04-06T02:18:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2772",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2772#issuecomment-19015",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

The patch applies cleanly, the spkg compiles cleanly for me on OSX and Linux. Doctests pass. I did find two small issues:

* I removed spkg-install.orig from the spkg
* I also removed the comment that SPKG.txt is deprecated from that file.

In total: positive review.

Cheers,

Michael



---

archive/issue_events_002960.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2008-04-06T02:19:03Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/2772",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/2772#event-2960"
}
```



---

archive/issue_comments_019016.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-04-06T02:19:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2772",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2772#issuecomment-19016",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_019017.json:
```json
{
    "body": "Merged in Sage 3.0.alpha2",
    "created_at": "2008-04-06T02:19:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2772",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2772#issuecomment-19017",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged in Sage 3.0.alpha2

# Issue 1271: update Singular to 3-0-4 release

archive/issues_001271.json:
```json
{
    "body": "Assignee: @malb\n\nSingular 3-0-4 should be released shortly. The non-final sources are already available.\n\nThis should also close #1074\n\nCheers,\n\nMichael\n\nIssue created by migration from https://trac.sagemath.org/ticket/1271\n\n",
    "created_at": "2007-11-25T18:32:09Z",
    "labels": [
        "component: packages: standard"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-2.8.15",
    "title": "update Singular to 3-0-4 release",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/1271",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```
Assignee: @malb

Singular 3-0-4 should be released shortly. The non-final sources are already available.

This should also close #1074

Cheers,

Michael

Issue created by migration from https://trac.sagemath.org/ticket/1271





---

archive/issue_comments_007941.json:
```json
{
    "body": "An updated spkg can be found at:\n\nhttp://sage.math.washington.edu/home/malb/pkgs/singular-3-0-4-1-20071202.spkg\n\nwhich installs fine on my notebook and on sage.math. After installing this spkg the attached patch trac1271.patch needs to be applied to fix a trivial doctest failure.\n\nThis new release fixes:\n* Singular is now GPLv2 or GPLv3\n* monitor segfault (#1074)\n* spkg-install modularized",
    "created_at": "2007-12-03T11:42:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1271",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1271#issuecomment-7941",
    "user": "https://github.com/malb"
}
```

An updated spkg can be found at:

http://sage.math.washington.edu/home/malb/pkgs/singular-3-0-4-1-20071202.spkg

which installs fine on my notebook and on sage.math. After installing this spkg the attached patch trac1271.patch needs to be applied to fix a trivial doctest failure.

This new release fixes:
* Singular is now GPLv2 or GPLv3
* monitor segfault (#1074)
* spkg-install modularized



---

archive/issue_comments_007942.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2007-12-03T11:42:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1271",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1271#issuecomment-7942",
    "user": "https://github.com/malb"
}
```

Changing status from new to assigned.



---

archive/issue_comments_007943.json:
```json
{
    "body": "Attachment [trac1271.patch](tarball://root/attachments/some-uuid/ticket1271/trac1271.patch) by mabshoff created at 2007-12-03 12:47:22\n\nPatch looks good to me, build testing the new Singular.spkg on OSX.\n\nCheers,\n\nMichael",
    "created_at": "2007-12-03T12:47:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1271",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1271#issuecomment-7943",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Attachment [trac1271.patch](tarball://root/attachments/some-uuid/ticket1271/trac1271.patch) by mabshoff created at 2007-12-03 12:47:22

Patch looks good to me, build testing the new Singular.spkg on OSX.

Cheers,

Michael



---

archive/issue_events_001415.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2007-12-03T14:52:37Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/1271",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/1271#event-1415"
}
```



---

archive/issue_comments_007944.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2007-12-03T14:52:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1271",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1271#issuecomment-7944",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_007945.json:
```json
{
    "body": "Merged in 2.8.15.rc1.",
    "created_at": "2007-12-03T14:52:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1271",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1271#issuecomment-7945",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged in 2.8.15.rc1.

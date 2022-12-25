# Issue 4449: sage-combinat install script doesn't work with 3.2.alpha2

archive/issues_004449.json:
```json
{
    "body": "Assignee: @saliola\n\nCC:  sage-combinat\n\nKeywords: sage-combinat\n\n'sage -combinat install' on sage-3.2.alpha2 fails (and not on 'hg qpush -a').\n\nIssue created by migration from https://trac.sagemath.org/ticket/4449\n\n",
    "created_at": "2008-11-05T22:23:44Z",
    "labels": [
        "component: combinatorics",
        "minor",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.2",
    "title": "sage-combinat install script doesn't work with 3.2.alpha2",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/4449",
    "user": "https://github.com/saliola"
}
```
Assignee: @saliola

CC:  sage-combinat

Keywords: sage-combinat

'sage -combinat install' on sage-3.2.alpha2 fails (and not on 'hg qpush -a').

Issue created by migration from https://trac.sagemath.org/ticket/4449





---

archive/issue_comments_032740.json:
```json
{
    "body": "Attachment [sage-combinat_4449.patch](tarball://root/attachments/some-uuid/ticket4449/sage-combinat_4449.patch) by @saliola created at 2008-11-05 22:25:59",
    "created_at": "2008-11-05T22:25:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4449",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4449#issuecomment-32740",
    "user": "https://github.com/saliola"
}
```

Attachment [sage-combinat_4449.patch](tarball://root/attachments/some-uuid/ticket4449/sage-combinat_4449.patch) by @saliola created at 2008-11-05 22:25:59



---

archive/issue_comments_032741.json:
```json
{
    "body": "The script fails because the following re.search in get_sage_version\n\n    return re.search('(\\d+\\.\\d+\\.\\d+)',sage_version).group()\n\ndoesn't match anything for \"3.2.alpha0\". One way to get around this is to use a try-except statement (see the attached patch sage-combinat_4449.patch).\n\nNow for 3.2.alpha2, the version number returned is '3.2.0' and for '3.2.1.alpha2' it is '3.2.1'. I think this should be okay since the version number is used to determine the guards (and the guards don't change much between alpha releases).\n\nNow the script runs, and fails at the end during the 'hg qpush -a' (which is acceptable).",
    "created_at": "2008-11-05T22:30:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4449",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4449#issuecomment-32741",
    "user": "https://github.com/saliola"
}
```

The script fails because the following re.search in get_sage_version

    return re.search('(\d+\.\d+\.\d+)',sage_version).group()

doesn't match anything for "3.2.alpha0". One way to get around this is to use a try-except statement (see the attached patch sage-combinat_4449.patch).

Now for 3.2.alpha2, the version number returned is '3.2.0' and for '3.2.1.alpha2' it is '3.2.1'. I think this should be okay since the version number is used to determine the guards (and the guards don't change much between alpha releases).

Now the script runs, and fails at the end during the 'hg qpush -a' (which is acceptable).



---

archive/issue_comments_032742.json:
```json
{
    "body": "Notice that there is also #4415, so hopefully this will not collide.\n\nCheers,\n\nMichael",
    "created_at": "2008-11-05T22:32:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4449",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4449#issuecomment-32742",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Notice that there is also #4415, so hopefully this will not collide.

Cheers,

Michael



---

archive/issue_comments_032743.json:
```json
{
    "body": "Looks good to me. It won't catch all odd version numbers and nothing like x.y.z.w, but we don't use those any more.\n\nCheers,\n\nMichael",
    "created_at": "2008-11-05T22:34:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4449",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4449#issuecomment-32743",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Looks good to me. It won't catch all odd version numbers and nothing like x.y.z.w, but we don't use those any more.

Cheers,

Michael



---

archive/issue_comments_032744.json:
```json
{
    "body": "Merged in Sage 3.2.alpha3",
    "created_at": "2008-11-05T22:34:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4449",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4449#issuecomment-32744",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged in Sage 3.2.alpha3



---

archive/issue_comments_032745.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-11-05T22:34:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4449",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4449#issuecomment-32745",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed



---

archive/issue_events_004695.json:
```json
{
    "actor": "mabshoff",
    "created_at": "2008-11-05T22:34:43Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/4449",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/4449#event-4695"
}
```

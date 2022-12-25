# Issue 2953: gcc 4.3/Itanium: fix givaro 3.2.10.rc3 build

archive/issues_002953.json:
```json
{
    "body": "Assignee: mabshoff\n\nOn Itanium with gcc 4.3 we need to add climits to gmp++.h. The spkg at \n\nhttp://sage.math.washington.edu/home/mabshoff/release-cycles-3.0/alpha6/givaro-3.2.10.rc3.p1.spkg\n\nfixes that.\n\nCheers,\n\nMichael\n\nIssue created by migration from https://trac.sagemath.org/ticket/2953\n\n",
    "created_at": "2008-04-19T02:20:34Z",
    "labels": [
        "component: packages: standard",
        "blocker",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.0",
    "title": "gcc 4.3/Itanium: fix givaro 3.2.10.rc3 build",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/2953",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```
Assignee: mabshoff

On Itanium with gcc 4.3 we need to add climits to gmp++.h. The spkg at 

http://sage.math.washington.edu/home/mabshoff/release-cycles-3.0/alpha6/givaro-3.2.10.rc3.p1.spkg

fixes that.

Cheers,

Michael

Issue created by migration from https://trac.sagemath.org/ticket/2953





---

archive/issue_comments_020321.json:
```json
{
    "body": "Attachment [givaro-3.2.10.rc3-gmp++.h-gcc-4.3-Itanium.patch](tarball://root/attachments/some-uuid/ticket2953/givaro-3.2.10.rc3-gmp++.h-gcc-4.3-Itanium.patch) by mabshoff created at 2008-04-19 02:20:58",
    "created_at": "2008-04-19T02:20:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2953",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2953#issuecomment-20321",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Attachment [givaro-3.2.10.rc3-gmp++.h-gcc-4.3-Itanium.patch](tarball://root/attachments/some-uuid/ticket2953/givaro-3.2.10.rc3-gmp++.h-gcc-4.3-Itanium.patch) by mabshoff created at 2008-04-19 02:20:58



---

archive/issue_comments_020322.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2008-04-19T02:21:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2953",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2953#issuecomment-20322",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Changing status from new to assigned.



---

archive/issue_comments_020323.json:
```json
{
    "body": "The difference between this and the previous spkg is the attached patched. The fix should also go into LinBox upstream.\n\nCheers,\n\nMichael",
    "created_at": "2008-04-19T02:21:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2953",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2953#issuecomment-20323",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

The difference between this and the previous spkg is the attached patched. The fix should also go into LinBox upstream.

Cheers,

Michael



---

archive/issue_comments_020324.json:
```json
{
    "body": "This works on a wide range of architectures where I tested it, and of course the change itself looks good. positive review.",
    "created_at": "2008-04-19T04:59:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2953",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2953#issuecomment-20324",
    "user": "https://github.com/williamstein"
}
```

This works on a wide range of architectures where I tested it, and of course the change itself looks good. positive review.



---

archive/issue_events_003159.json:
```json
{
    "actor": "mabshoff",
    "created_at": "2008-04-19T05:06:36Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/2953",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/2953#event-3159"
}
```



---

archive/issue_comments_020325.json:
```json
{
    "body": "Merged in Sage 3.0.alpha6",
    "created_at": "2008-04-19T05:06:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2953",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2953#issuecomment-20325",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged in Sage 3.0.alpha6



---

archive/issue_comments_020326.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-04-19T05:06:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2953",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2953#issuecomment-20326",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed

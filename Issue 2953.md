# Issue 2953: gcc 4.3/Itanium: fix givaro 3.2.10.rc3 build

archive/issues_002953.json:
```json
{
    "body": "Assignee: mabshoff\n\nOn Itanium with gcc 4.3 we need to add climits to gmp++.h. The spkg at \n\nhttp://sage.math.washington.edu/home/mabshoff/release-cycles-3.0/alpha6/givaro-3.2.10.rc3.p1.spkg\n\nfixes that.\n\nCheers,\n\nMichael\n\nIssue created by migration from https://trac.sagemath.org/ticket/2953\n\n",
    "created_at": "2008-04-19T02:20:34Z",
    "labels": [
        "packages: standard",
        "blocker",
        "bug"
    ],
    "title": "gcc 4.3/Itanium: fix givaro 3.2.10.rc3 build",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/2953",
    "user": "mabshoff"
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

archive/issue_comments_020364.json:
```json
{
    "body": "Attachment [givaro-3.2.10.rc3-gmp++.h-gcc-4.3-Itanium.patch](tarball://root/attachments/some-uuid/ticket2953/givaro-3.2.10.rc3-gmp++.h-gcc-4.3-Itanium.patch) by mabshoff created at 2008-04-19 02:20:58",
    "created_at": "2008-04-19T02:20:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2953",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2953#issuecomment-20364",
    "user": "mabshoff"
}
```

Attachment [givaro-3.2.10.rc3-gmp++.h-gcc-4.3-Itanium.patch](tarball://root/attachments/some-uuid/ticket2953/givaro-3.2.10.rc3-gmp++.h-gcc-4.3-Itanium.patch) by mabshoff created at 2008-04-19 02:20:58



---

archive/issue_comments_020365.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2008-04-19T02:21:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2953",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2953#issuecomment-20365",
    "user": "mabshoff"
}
```

Changing status from new to assigned.



---

archive/issue_comments_020366.json:
```json
{
    "body": "The difference between this and the previous spkg is the attached patched. The fix should also go into LinBox upstream.\n\nCheers,\n\nMichael",
    "created_at": "2008-04-19T02:21:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2953",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2953#issuecomment-20366",
    "user": "mabshoff"
}
```

The difference between this and the previous spkg is the attached patched. The fix should also go into LinBox upstream.

Cheers,

Michael



---

archive/issue_comments_020367.json:
```json
{
    "body": "This works on a wide range of architectures where I tested it, and of course the change itself looks good. positive review.",
    "created_at": "2008-04-19T04:59:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2953",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2953#issuecomment-20367",
    "user": "was"
}
```

This works on a wide range of architectures where I tested it, and of course the change itself looks good. positive review.



---

archive/issue_comments_020368.json:
```json
{
    "body": "Merged in Sage 3.0.alpha6",
    "created_at": "2008-04-19T05:06:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2953",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2953#issuecomment-20368",
    "user": "mabshoff"
}
```

Merged in Sage 3.0.alpha6



---

archive/issue_comments_020369.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-04-19T05:06:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2953",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2953#issuecomment-20369",
    "user": "mabshoff"
}
```

Resolution: fixed

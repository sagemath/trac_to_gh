# Issue 2927: [with spkg, needs review] gcc 4.3: make Singular.spkg compile

archive/issues_002927.json:
```json
{
    "body": "Assignee: mabshoff\n\nHe current Singular.spkg foes not compile with gcc 4.3. We need three small patches to make it work. The updated spkg can be found at\n\nhttp://sage.math.washington.edu/home/mabshoff/release-cycles-3.0/alpha5/singular-3-0-4-2-20080405.p0.spkg\n\nCheers,\n\nMichael\n\nIssue created by migration from https://trac.sagemath.org/ticket/2927\n\n",
    "created_at": "2008-04-15T05:23:56Z",
    "labels": [
        "packages: standard",
        "major",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.0",
    "title": "[with spkg, needs review] gcc 4.3: make Singular.spkg compile",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/2927",
    "user": "mabshoff"
}
```
Assignee: mabshoff

He current Singular.spkg foes not compile with gcc 4.3. We need three small patches to make it work. The updated spkg can be found at

http://sage.math.washington.edu/home/mabshoff/release-cycles-3.0/alpha5/singular-3-0-4-2-20080405.p0.spkg

Cheers,

Michael

Issue created by migration from https://trac.sagemath.org/ticket/2927





---

archive/issue_comments_020148.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2008-04-15T05:24:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2927",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2927#issuecomment-20148",
    "user": "mabshoff"
}
```

Changing status from new to assigned.



---

archive/issue_comments_020149.json:
```json
{
    "body": "Attachment [singular-cf_gcd_charp.cc.patch](tarball://root/attachments/some-uuid/ticket2927/singular-cf_gcd_charp.cc.patch) by mabshoff created at 2008-04-15 05:27:22",
    "created_at": "2008-04-15T05:27:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2927",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2927#issuecomment-20149",
    "user": "mabshoff"
}
```

Attachment [singular-cf_gcd_charp.cc.patch](tarball://root/attachments/some-uuid/ticket2927/singular-cf_gcd_charp.cc.patch) by mabshoff created at 2008-04-15 05:27:22



---

archive/issue_comments_020150.json:
```json
{
    "body": "Attachment [singular-readcf.cc.patch](tarball://root/attachments/some-uuid/ticket2927/singular-readcf.cc.patch) by mabshoff created at 2008-04-15 05:27:31",
    "created_at": "2008-04-15T05:27:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2927",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2927#issuecomment-20150",
    "user": "mabshoff"
}
```

Attachment [singular-readcf.cc.patch](tarball://root/attachments/some-uuid/ticket2927/singular-readcf.cc.patch) by mabshoff created at 2008-04-15 05:27:31



---

archive/issue_comments_020151.json:
```json
{
    "body": "Attachment [singular-readcf.y.patch](tarball://root/attachments/some-uuid/ticket2927/singular-readcf.y.patch) by gfurnish created at 2008-04-15 05:53:31\n\nWorks for me",
    "created_at": "2008-04-15T05:53:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2927",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2927#issuecomment-20151",
    "user": "gfurnish"
}
```

Attachment [singular-readcf.y.patch](tarball://root/attachments/some-uuid/ticket2927/singular-readcf.y.patch) by gfurnish created at 2008-04-15 05:53:31

Works for me



---

archive/issue_comments_020152.json:
```json
{
    "body": "Merged in Sage 3.0.alpha5",
    "created_at": "2008-04-15T06:07:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2927",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2927#issuecomment-20152",
    "user": "mabshoff"
}
```

Merged in Sage 3.0.alpha5



---

archive/issue_comments_020153.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-04-15T06:07:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2927",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2927#issuecomment-20153",
    "user": "mabshoff"
}
```

Resolution: fixed

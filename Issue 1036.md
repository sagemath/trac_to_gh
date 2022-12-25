# Issue 1036: optional macaulay2 package does not install

archive/issues_001036.json:
```json
{
    "body": "Assignee: @williamstein\n\nfirst `bison` is required and after installing that, this happens:\n\n\n```\nIn file included from ../comp.hpp:9,\n                 from ../comp_gb.hpp:6,\n                 from lingb.hpp:8,\n                 from lingb.cpp:1:\n../comp.hpp:7: error: previous declaration of \u2018int gbTrace\u2019 with \u2018C++\u2019 linkage\n../engine.h:1530: error: conflicts with new declaration with \u2018C\u2019 linkage\n```\n\n\nThis is with `GCC 4.2.3` on 64-bit Debian/testing.\n\nIssue created by migration from https://trac.sagemath.org/ticket/1036\n\n",
    "created_at": "2007-10-30T17:18:37Z",
    "labels": [
        "component: packages: standard",
        "minor",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-2.9",
    "title": "optional macaulay2 package does not install",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/1036",
    "user": "https://github.com/malb"
}
```
Assignee: @williamstein

first `bison` is required and after installing that, this happens:


```
In file included from ../comp.hpp:9,
                 from ../comp_gb.hpp:6,
                 from lingb.hpp:8,
                 from lingb.cpp:1:
../comp.hpp:7: error: previous declaration of ‘int gbTrace’ with ‘C++’ linkage
../engine.h:1530: error: conflicts with new declaration with ‘C’ linkage
```


This is with `GCC 4.2.3` on 64-bit Debian/testing.

Issue created by migration from https://trac.sagemath.org/ticket/1036





---

archive/issue_comments_006306.json:
```json
{
    "body": "Hello,\n\nMacaulay2 not building is a known issue and #10 should take care of that. But after initial ativity about a month back the work on a new Macaulay2 release seems to have slowed down.\n\nCheers,\n\nMichael",
    "created_at": "2007-10-30T18:00:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1036",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1036#issuecomment-6306",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Hello,

Macaulay2 not building is a known issue and #10 should take care of that. But after initial ativity about a month back the work on a new Macaulay2 release seems to have slowed down.

Cheers,

Michael



---

archive/issue_comments_006307.json:
```json
{
    "body": "Attached a small patch. The 'extern int gbTrace' in engine.h is in an extern \"C\" {} block, while 'int gbTrace' is defined in a .cpp file.\n\nSince it doesn't appear to be patched in Macaulay2 svn, attaching a small patch.",
    "created_at": "2007-11-14T23:58:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1036",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1036#issuecomment-6307",
    "user": "https://github.com/wjp"
}
```

Attached a small patch. The 'extern int gbTrace' in engine.h is in an extern "C" {} block, while 'int gbTrace' is defined in a .cpp file.

Since it doesn't appear to be patched in Macaulay2 svn, attaching a small patch.



---

archive/issue_comments_006308.json:
```json
{
    "body": "gbTrace C++-linkage patch",
    "created_at": "2007-11-14T23:59:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1036",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1036#issuecomment-6308",
    "user": "https://github.com/wjp"
}
```

gbTrace C++-linkage patch



---

archive/issue_comments_006309.json:
```json
{
    "body": "Attachment [macaulay2_gbTrace_linkage.diff](tarball://root/attachments/some-uuid/ticket1036/macaulay2_gbTrace_linkage.diff) by @williamstein created at 2007-12-06 04:19:39",
    "created_at": "2007-12-06T04:19:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1036",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1036#issuecomment-6309",
    "user": "https://github.com/williamstein"
}
```

Attachment [macaulay2_gbTrace_linkage.diff](tarball://root/attachments/some-uuid/ticket1036/macaulay2_gbTrace_linkage.diff) by @williamstein created at 2007-12-06 04:19:39



---

archive/issue_comments_006310.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2007-12-16T00:25:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1036",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1036#issuecomment-6310",
    "user": "https://github.com/williamstein"
}
```

Resolution: fixed



---

archive/issue_comments_006311.json:
```json
{
    "body": "I've put this into sage.",
    "created_at": "2007-12-16T00:25:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1036",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1036#issuecomment-6311",
    "user": "https://github.com/williamstein"
}
```

I've put this into sage.

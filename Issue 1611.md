# Issue 1611: polybori should use the m4ri library from libm4ri spkg

archive/issues_001611.json:
```json
{
    "body": "Assignee: @burcin\n\nCC:  polybori\n\nPolyBoRi comes with its own copy of m4ri libraries. After #1505, Sage provides these libraries through a package.\n\nThe PolyBoRi build process should be changed to use the library and headers provided by libm4ri-*.spkg.\n\nIssue created by migration from https://trac.sagemath.org/ticket/1611\n\n",
    "created_at": "2007-12-27T10:54:50Z",
    "labels": [
        "packages: standard",
        "major",
        "enhancement"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.1.2",
    "title": "polybori should use the m4ri library from libm4ri spkg",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/1611",
    "user": "@burcin"
}
```
Assignee: @burcin

CC:  polybori

PolyBoRi comes with its own copy of m4ri libraries. After #1505, Sage provides these libraries through a package.

The PolyBoRi build process should be changed to use the library and headers provided by libm4ri-*.spkg.

Issue created by migration from https://trac.sagemath.org/ticket/1611





---

archive/issue_comments_010246.json:
```json
{
    "body": "Michael Brickenstein wrote:\n\n> If you can wait until the end of my holidays, which will begin  \n> tomorrow and end at 6th of January, I will do the switch myself.",
    "created_at": "2007-12-27T12:24:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1611",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1611#issuecomment-10246",
    "user": "@malb"
}
```

Michael Brickenstein wrote:

> If you can wait until the end of my holidays, which will begin  
> tomorrow and end at 6th of January, I will do the switch myself.



---

archive/issue_comments_010247.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2008-01-03T15:07:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1611",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1611#issuecomment-10247",
    "user": "@burcin"
}
```

Changing status from new to assigned.



---

archive/issue_comments_010248.json:
```json
{
    "body": "The issue might be resolved during the update to PolyBoRi 0.2.rcX during Bug Day 10.\n\nCheers,\n\nMichael",
    "created_at": "2008-02-15T23:23:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1611",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1611#issuecomment-10248",
    "user": "mabshoff"
}
```

The issue might be resolved during the update to PolyBoRi 0.2.rcX during Bug Day 10.

Cheers,

Michael



---

archive/issue_comments_010249.json:
```json
{
    "body": "This should be done while updating PolyBori - see #2060.\n\nCheers,\n\nMichael",
    "created_at": "2008-02-17T19:57:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1611",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1611#issuecomment-10249",
    "user": "mabshoff"
}
```

This should be done while updating PolyBori - see #2060.

Cheers,

Michael



---

archive/issue_comments_010250.json:
```json
{
    "body": "`PolyBoRi` requires some changes in the m4ri libraries. They are waiting for changes upstream (in m4ri) to switch over, so newer versions of `PolyBoRi` don't support this.",
    "created_at": "2008-03-08T13:37:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1611",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1611#issuecomment-10250",
    "user": "@burcin"
}
```

`PolyBoRi` requires some changes in the m4ri libraries. They are waiting for changes upstream (in m4ri) to switch over, so newer versions of `PolyBoRi` don't support this.



---

archive/issue_comments_010251.json:
```json
{
    "body": "I guess I am upstream so I should diff their m4ri against ours (upstream).",
    "created_at": "2008-03-09T15:27:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1611",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1611#issuecomment-10251",
    "user": "@malb"
}
```

I guess I am upstream so I should diff their m4ri against ours (upstream).



---

archive/issue_comments_010252.json:
```json
{
    "body": "Fixing this bug is planned for the PolyBoRi 0.5 release.\n\nCheers,\n\nMichael",
    "created_at": "2008-05-12T00:12:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1611",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1611#issuecomment-10252",
    "user": "mabshoff"
}
```

Fixing this bug is planned for the PolyBoRi 0.5 release.

Cheers,

Michael



---

archive/issue_comments_010253.json:
```json
{
    "body": "#3264 does not fix the problem yet. Are there any options to make this happen with PolyBoRi 0.5?\n\nCheers,\n\nMichael",
    "created_at": "2008-09-07T00:41:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1611",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1611#issuecomment-10253",
    "user": "mabshoff"
}
```

#3264 does not fix the problem yet. Are there any options to make this happen with PolyBoRi 0.5?

Cheers,

Michael



---

archive/issue_comments_010254.json:
```json
{
    "body": "There is some movement w.r.t. this issue in PolyBoRi, but I wouldn't suspect it to be available in 0.5.",
    "created_at": "2008-09-07T00:59:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1611",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1611#issuecomment-10254",
    "user": "@malb"
}
```

There is some movement w.r.t. this issue in PolyBoRi, but I wouldn't suspect it to be available in 0.5.



---

archive/issue_comments_010255.json:
```json
{
    "body": "it will be available in 0.5. However, you should make sure, that\nmalloc work also for allocating zero bytes in M4RI, else it will crash\n(doesn't work with mm_malloc on Mac OS X 10.5).",
    "created_at": "2008-09-08T06:23:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1611",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1611#issuecomment-10255",
    "user": "PolyBoRi"
}
```

it will be available in 0.5. However, you should make sure, that
malloc work also for allocating zero bytes in M4RI, else it will crash
(doesn't work with mm_malloc on Mac OS X 10.5).



---

archive/issue_comments_010256.json:
```json
{
    "body": "This is fixed with #6177",
    "created_at": "2009-09-29T08:08:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1611",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1611#issuecomment-10256",
    "user": "@malb"
}
```

This is fixed with #6177



---

archive/issue_comments_010257.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-09-29T08:08:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1611",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1611#issuecomment-10257",
    "user": "@malb"
}
```

Resolution: fixed

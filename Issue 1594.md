# Issue 1594: libm4ri -- in library mode it doesn't work at all on osx -- lots of segfaults

archive/issues_001594.json:
```json
{
    "body": "Assignee: @williamstein\n\nOn all variants of OSX the new libm4ri doesn't work at all.\n\nI just did some poking around and putting my own \n\nIssue created by migration from https://trac.sagemath.org/ticket/1594\n\n",
    "created_at": "2007-12-24T18:15:53Z",
    "labels": [
        "linear algebra",
        "blocker",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-2.9.1",
    "title": "libm4ri -- in library mode it doesn't work at all on osx -- lots of segfaults",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/1594",
    "user": "@williamstein"
}
```
Assignee: @williamstein

On all variants of OSX the new libm4ri doesn't work at all.

I just did some poking around and putting my own 

Issue created by migration from https://trac.sagemath.org/ticket/1594





---

archive/issue_comments_010143.json:
```json
{
    "body": "The backtrace William posted on sage-devel shows m4ri is using a min() defined in a file nu.c instead of the min() in m4ri itself.\n\nThis seems to point at symmetrica, which has a file nu.c with a min() defined in it.",
    "created_at": "2007-12-24T18:21:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1594",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1594#issuecomment-10143",
    "user": "@wjp"
}
```

The backtrace William posted on sage-devel shows m4ri is using a min() defined in a file nu.c instead of the min() in m4ri itself.

This seems to point at symmetrica, which has a file nu.c with a min() defined in it.



---

archive/issue_comments_010144.json:
```json
{
    "body": "I believe this has been fixed in the 2.9.1 release.\n\nCheers,\n\nMichael",
    "created_at": "2007-12-24T21:35:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1594",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1594#issuecomment-10144",
    "user": "mabshoff"
}
```

I believe this has been fixed in the 2.9.1 release.

Cheers,

Michael



---

archive/issue_comments_010145.json:
```json
{
    "body": "William worked around this linker issue by adding a line\n\n#define min(x,y) ((x < y)?x:y)\n\nat the top of brilliantrussian.c and packedmatrix.c. I hope there aren't any other subtle things like this that could hurt us elsewhere. Symmetrica defines a lot of 'common' function names like min.",
    "created_at": "2007-12-25T13:22:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1594",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1594#issuecomment-10145",
    "user": "@wjp"
}
```

William worked around this linker issue by adding a line

#define min(x,y) ((x < y)?x:y)

at the top of brilliantrussian.c and packedmatrix.c. I hope there aren't any other subtle things like this that could hurt us elsewhere. Symmetrica defines a lot of 'common' function names like min.



---

archive/issue_comments_010146.json:
```json
{
    "body": "I can confirm that all tests of `make test` pass on bsd (Intel OSX).",
    "created_at": "2007-12-25T15:04:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1594",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1594#issuecomment-10146",
    "user": "@malb"
}
```

I can confirm that all tests of `make test` pass on bsd (Intel OSX).



---

archive/issue_comments_010147.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2007-12-25T15:10:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1594",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1594#issuecomment-10147",
    "user": "@malb"
}
```

Resolution: fixed

# Issue 1618: Make SCons use the GNU compiler even when Intel's compilers are present

archive/issues_001618.json:
```json
{
    "body": "Assignee: mabshoff\n\nIn http://groups.google.com/group/sage-devel/t/74de10c9f2d3edf7 Francois reported:\n\n```\nHello Michael,\n\nI think I found my problem. A little googling actually helped with\nthis link:\nhttp://bugs.archlinux.org/task/6864\nI did some experiments with the intel _fortran_ compiler (not even the\nC compiler)\nand I still have it on my system.\nSince the intel compiler doesn't compile my lattice QCD code correctly\nanyway\nI will remove it and try again.\nI am busy for the next few hours so I will do that a bit latter.\n\nThanks for looking,\nFrancois\n```\n\n\nCheers,\n\nMichael\n\nIssue created by migration from https://trac.sagemath.org/ticket/1618\n\n",
    "created_at": "2007-12-29T03:55:55Z",
    "labels": [
        "packages: standard",
        "major",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-2.11",
    "title": "Make SCons use the GNU compiler even when Intel's compilers are present",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/1618",
    "user": "mabshoff"
}
```
Assignee: mabshoff

In http://groups.google.com/group/sage-devel/t/74de10c9f2d3edf7 Francois reported:

```
Hello Michael,

I think I found my problem. A little googling actually helped with
this link:
http://bugs.archlinux.org/task/6864
I did some experiments with the intel _fortran_ compiler (not even the
C compiler)
and I still have it on my system.
Since the intel compiler doesn't compile my lattice QCD code correctly
anyway
I will remove it and try again.
I am busy for the next few hours so I will do that a bit latter.

Thanks for looking,
Francois
```


Cheers,

Michael

Issue created by migration from https://trac.sagemath.org/ticket/1618





---

archive/issue_comments_010296.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2007-12-29T03:56:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1618",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1618#issuecomment-10296",
    "user": "mabshoff"
}
```

Changing status from new to assigned.



---

archive/issue_comments_010297.json:
```json
{
    "body": "Changing assignee from mabshoff to @garyfurnish.",
    "created_at": "2008-03-23T18:30:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1618",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1618#issuecomment-10297",
    "user": "@garyfurnish"
}
```

Changing assignee from mabshoff to @garyfurnish.



---

archive/issue_comments_010298.json:
```json
{
    "body": "Changing status from assigned to new.",
    "created_at": "2008-03-23T18:30:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1618",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1618#issuecomment-10298",
    "user": "@garyfurnish"
}
```

Changing status from assigned to new.



---

archive/issue_comments_010299.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2008-03-23T18:30:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1618",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1618#issuecomment-10299",
    "user": "@garyfurnish"
}
```

Changing status from new to assigned.



---

archive/issue_comments_010300.json:
```json
{
    "body": "Since none of the code we compile with SCons is actually Fortran there is no point in selecting a different default Fortran compiler. Since SCons doesn't support g95 or gfortran (even with the December 2007 release!) we just remove the offending linker flag. The update spkg at \n\nhttp://sage.math.washington.edu/home/mabshoff/release-cycles-2.11/alpha2/scons-0.97.0d20071212.spkg\n\nIt updates to the latest stable snapshot release. It also removes some crap from inside the spkg shrinking it about 30%. \n\nCheers,\n\nMichael",
    "created_at": "2008-03-24T16:37:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1618",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1618#issuecomment-10300",
    "user": "mabshoff"
}
```

Since none of the code we compile with SCons is actually Fortran there is no point in selecting a different default Fortran compiler. Since SCons doesn't support g95 or gfortran (even with the December 2007 release!) we just remove the offending linker flag. The update spkg at 

http://sage.math.washington.edu/home/mabshoff/release-cycles-2.11/alpha2/scons-0.97.0d20071212.spkg

It updates to the latest stable snapshot release. It also removes some crap from inside the spkg shrinking it about 30%. 

Cheers,

Michael



---

archive/issue_comments_010301.json:
```json
{
    "body": "Build tested on OSX and Linux.\n\nCheers,\n\nMichael",
    "created_at": "2008-03-24T16:46:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1618",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1618#issuecomment-10301",
    "user": "mabshoff"
}
```

Build tested on OSX and Linux.

Cheers,

Michael



---

archive/issue_comments_010302.json:
```json
{
    "body": "Tested that spkg installs. Rebuilt polybori and clib.",
    "created_at": "2008-03-24T17:30:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1618",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1618#issuecomment-10302",
    "user": "jkantor"
}
```

Tested that spkg installs. Rebuilt polybori and clib.



---

archive/issue_comments_010303.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-03-24T17:30:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1618",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1618#issuecomment-10303",
    "user": "mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_010304.json:
```json
{
    "body": "Merged in Sage 2.11.alpha2",
    "created_at": "2008-03-24T17:30:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1618",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1618#issuecomment-10304",
    "user": "mabshoff"
}
```

Merged in Sage 2.11.alpha2

# Issue 1574: dependencies for non pyx files aren't properly tracked

archive/issues_001574.json:
```json
{
    "body": "Assignee: @williamstein\n\nCC:  @craigcitro @tornaria\n\nWhen applying a patch to a non `pyx|pxi|pxd` file (mwrank.cc in this case) and running `sage -b` odd things happen:\n\n```\n\nrunning install\nrunning build\nrunning build_py\nrunning build_ext\nbuilding 'sage.libs.mwrank.mwrank' extension\nerror: unknown file type '.pyx' (from 'sage/libs/mwrank/mwrank.pyx')\nsage: There was an error installing modified sage library code.\n\nrunning install\nrunning build\nrunning build_py\nrunning build_ext\nbuilding 'sage.libs.mwrank.mwrank' extension\nerror: unknown file type '.pyx' (from 'sage/libs/mwrank/mwrank.pyx')\nsage: There was an error installing modified sage library code.\n```\nTouching a pyx file that the particular file depends upon (mwrank.pyx) in this case fixes the issue and everything is properly recompiled.\n\nCheers,\n\nMichael\n\nIssue created by migration from https://trac.sagemath.org/ticket/1574\n\n",
    "created_at": "2007-12-20T12:14:49Z",
    "labels": [
        "component: distribution",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.2.1",
    "title": "dependencies for non pyx files aren't properly tracked",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/1574",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```
Assignee: @williamstein

CC:  @craigcitro @tornaria

When applying a patch to a non `pyx|pxi|pxd` file (mwrank.cc in this case) and running `sage -b` odd things happen:

```

running install
running build
running build_py
running build_ext
building 'sage.libs.mwrank.mwrank' extension
error: unknown file type '.pyx' (from 'sage/libs/mwrank/mwrank.pyx')
sage: There was an error installing modified sage library code.

running install
running build
running build_py
running build_ext
building 'sage.libs.mwrank.mwrank' extension
error: unknown file type '.pyx' (from 'sage/libs/mwrank/mwrank.pyx')
sage: There was an error installing modified sage library code.
```
Touching a pyx file that the particular file depends upon (mwrank.pyx) in this case fixes the issue and everything is properly recompiled.

Cheers,

Michael

Issue created by migration from https://trac.sagemath.org/ticket/1574





---

archive/issue_comments_009986.json:
```json
{
    "body": "This one just bit me in the ass again:\n\n```\nmabshoff@sage:/scratch/mabshoff/release-cycle/sage-3.1.3.alpha2$ ./sage -b\n\n----------------------------------------------------------\nsage: Building and installing modified SAGE library files.\n\n\nInstalling c_lib\nscons: `install' is up to date.\nrunning install\nrunning build\nrunning build_py\nrunning build_ext\nbuilding 'sage.schemes.hyperelliptic_curves.hypellfrob' extension\nerror: unknown file type '.pyx' (from 'sage/schemes/hyperelliptic_curves/hypellfrob.pyx')\nsage: There was an error installing modified sage library code.\n\n\nreal    0m1.540s\nuser    0m1.124s\nsys     0m0.416s\n```\nAnybody willing to fix this? It seems that all that needs to be done is to add C/C++ files linked extensions to the list of dependencies to track.\n\nCheers,\n\nMichael",
    "created_at": "2008-09-26T09:07:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1574",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1574#issuecomment-9986",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

This one just bit me in the ass again:

```
mabshoff@sage:/scratch/mabshoff/release-cycle/sage-3.1.3.alpha2$ ./sage -b

----------------------------------------------------------
sage: Building and installing modified SAGE library files.


Installing c_lib
scons: `install' is up to date.
running install
running build
running build_py
running build_ext
building 'sage.schemes.hyperelliptic_curves.hypellfrob' extension
error: unknown file type '.pyx' (from 'sage/schemes/hyperelliptic_curves/hypellfrob.pyx')
sage: There was an error installing modified sage library code.


real    0m1.540s
user    0m1.124s
sys     0m0.416s
```
Anybody willing to fix this? It seems that all that needs to be done is to add C/C++ files linked extensions to the list of dependencies to track.

Cheers,

Michael



---

archive/issue_events_003934.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2008-12-02T01:45:48Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/1574",
    "milestone": "sage-3.2.1",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/1574#event-3934"
}
```



---

archive/issue_comments_009987.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-12-02T01:45:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1574",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1574#issuecomment-9987",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed



---

archive/issue_events_003935.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2008-12-02T01:45:48Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/1574",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/1574#event-3935"
}
```



---

archive/issue_comments_009988.json:
```json
{
    "body": "This has been fixed in Sage 3.2/3.2.1 due to the work done by Craig Citro and Gonzalo Tornaria",
    "created_at": "2008-12-02T01:45:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1574",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1574#issuecomment-9988",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

This has been fixed in Sage 3.2/3.2.1 due to the work done by Craig Citro and Gonzalo Tornaria



---

archive/issue_comments_009989.json:
```json
{
    "body": "And Robert Bradshaw. :)",
    "created_at": "2008-12-02T04:06:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1574",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1574#issuecomment-9989",
    "user": "https://github.com/craigcitro"
}
```

And Robert Bradshaw. :)

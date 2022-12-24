# Issue 909: Cython without recompile

archive/issues_000909.json:
```json
{
    "body": "Assignee: was\n\nLoading a file in sage by\n  load foo.spyx \nseems to result in a recompile every time--or at least it is doing something that takes time.  Is this really necessary, or is something else going on?  Shouldn't it instead check to see if there has been a change to foo.spyx?  (This recompiling is expensive if the Cython file is quite long!)\n\nIssue created by migration from https://trac.sagemath.org/ticket/909\n\n",
    "created_at": "2007-10-16T18:42:53Z",
    "labels": [
        "interfaces",
        "minor",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-duplicate/invalid/wontfix",
    "title": "Cython without recompile",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/909",
    "user": "jvoight"
}
```
Assignee: was

Loading a file in sage by
  load foo.spyx 
seems to result in a recompile every time--or at least it is doing something that takes time.  Is this really necessary, or is something else going on?  Shouldn't it instead check to see if there has been a change to foo.spyx?  (This recompiling is expensive if the Cython file is quite long!)

Issue created by migration from https://trac.sagemath.org/ticket/909





---

archive/issue_comments_005590.json:
```json
{
    "body": "Well, \n\nif we had a makefile or SCons based buildsystem for external Cython code like the sagelib this wouldn't happen. I think it used to be the way that the compiled objects would be kept around, but I am not sure why this no longer happens. There is also a problem with C++ files if you change compilers which break ABI compability, but this would be a rather rare occurance for the vast majority of people.\n\nCheers,\n\nMichael",
    "created_at": "2007-10-16T18:57:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/909",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/909#issuecomment-5590",
    "user": "mabshoff"
}
```

Well, 

if we had a makefile or SCons based buildsystem for external Cython code like the sagelib this wouldn't happen. I think it used to be the way that the compiled objects would be kept around, but I am not sure why this no longer happens. There is also a problem with C++ files if you change compilers which break ABI compability, but this would be a rather rare occurance for the vast majority of people.

Cheers,

Michael



---

archive/issue_comments_005591.json:
```json
{
    "body": "RobertWB opened #4238 with a patch, so I am closing this as a dupe.\n\nCheers,\n\nMichael",
    "created_at": "2008-10-03T00:01:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/909",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/909#issuecomment-5591",
    "user": "mabshoff"
}
```

RobertWB opened #4238 with a patch, so I am closing this as a dupe.

Cheers,

Michael



---

archive/issue_comments_005592.json:
```json
{
    "body": "Resolution: duplicate",
    "created_at": "2008-10-03T00:01:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/909",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/909#issuecomment-5592",
    "user": "mabshoff"
}
```

Resolution: duplicate

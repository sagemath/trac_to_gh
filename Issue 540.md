# Issue 540: 3d: move all .jar files to an optional package;

archive/issues_000540.json:
```json
{
    "body": "Assignee: @robertwb\n\nIMPORTANT NOTE: I just realized that SAGE-2.8.3 includes some pre-compiled\njava .jar files in the\n     SAGE_ROOT/data/extcode/notebook/java/3d\ndirectory.  If you're the sort of person who must compile everything from source, wait\nfor SAGE-2.9, when we'll do something about this problem (probably the only option\nis to move these to an optional package since I do not want to require java to be installed\nin order to build SAGE). \n\nThis made the extcode .hg directory *HUGE*, so we're going to have to probably\nrevert to right before these were added.\n\nIssue created by migration from https://trac.sagemath.org/ticket/540\n\n",
    "created_at": "2007-08-31T19:10:57Z",
    "labels": [
        "packages: standard",
        "major",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-2.8.4",
    "title": "3d: move all .jar files to an optional package;",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/540",
    "user": "@williamstein"
}
```
Assignee: @robertwb

IMPORTANT NOTE: I just realized that SAGE-2.8.3 includes some pre-compiled
java .jar files in the
     SAGE_ROOT/data/extcode/notebook/java/3d
directory.  If you're the sort of person who must compile everything from source, wait
for SAGE-2.9, when we'll do something about this problem (probably the only option
is to move these to an optional package since I do not want to require java to be installed
in order to build SAGE). 

This made the extcode .hg directory *HUGE*, so we're going to have to probably
revert to right before these were added.

Issue created by migration from https://trac.sagemath.org/ticket/540





---

archive/issue_comments_002745.json:
```json
{
    "body": "Moreover, it turns out that one of the java libraries isn't GPL compatible, so it definitely has to be moved out of the core of SAGE.   We'll just have to make it easy to install.",
    "created_at": "2007-08-31T20:19:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/540",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/540#issuecomment-2745",
    "user": "@williamstein"
}
```

Moreover, it turns out that one of the java libraries isn't GPL compatible, so it definitely has to be moved out of the core of SAGE.   We'll just have to make it easy to install.



---

archive/issue_comments_002746.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2007-09-06T17:03:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/540",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/540#issuecomment-2746",
    "user": "@robertwb"
}
```

Resolution: fixed

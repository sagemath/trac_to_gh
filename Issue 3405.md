# Issue 3405: [with spkg, needs review] update Singular SPKG to newest upstream release

archive/issues_003405.json:
```json
{
    "body": "Assignee: mabshoff\n\nKeywords: singular\n\n# New upstream release\n\nTue Jun 10 18:51:53 CEST 2008 Singular-3-0-4-3\n\nChanges with respect to 3-0-4-2\n\n*  code depending on certain cpus is now selected by SI_CPU_*\n  in mod2.h (for libsingular.so), set by configure\n*  licence clarified:\n  * kernel/htmlhelp.h changed to LGPL 2.1\n  * kernel/htmlhelp.lib removed\n  * not-up-to-date stuff removed\n*  more static p_Procs: faster on systems which do not support/\n  do not use DL_KERNEL\n* new target libsingular.a (for gfan)\n\nThis includes the fix for Solaris. Also note that libSingular is now also used for gfan :-)\n\nThe SPKG is here:\n\n   http://sage.math.washington.edu/home/malb/spkgs/singular-3-0-4-2-20080611.p0.spkg\n\nIssue created by migration from https://trac.sagemath.org/ticket/3405\n\n",
    "created_at": "2008-06-12T22:36:32Z",
    "labels": [
        "packages: standard",
        "major",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.0.4",
    "title": "[with spkg, needs review] update Singular SPKG to newest upstream release",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/3405",
    "user": "@malb"
}
```
Assignee: mabshoff

Keywords: singular

# New upstream release

Tue Jun 10 18:51:53 CEST 2008 Singular-3-0-4-3

Changes with respect to 3-0-4-2

*  code depending on certain cpus is now selected by SI_CPU_*
  in mod2.h (for libsingular.so), set by configure
*  licence clarified:
  * kernel/htmlhelp.h changed to LGPL 2.1
  * kernel/htmlhelp.lib removed
  * not-up-to-date stuff removed
*  more static p_Procs: faster on systems which do not support/
  do not use DL_KERNEL
* new target libsingular.a (for gfan)

This includes the fix for Solaris. Also note that libSingular is now also used for gfan :-)

The SPKG is here:

   http://sage.math.washington.edu/home/malb/spkgs/singular-3-0-4-2-20080611.p0.spkg

Issue created by migration from https://trac.sagemath.org/ticket/3405





---

archive/issue_comments_023884.json:
```json
{
    "body": "Changing keywords from \"singular\" to \"singular, editor_mabshoff\".",
    "created_at": "2008-06-15T21:53:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3405",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3405#issuecomment-23884",
    "user": "@craigcitro"
}
```

Changing keywords from "singular" to "singular, editor_mabshoff".



---

archive/issue_comments_023885.json:
```json
{
    "body": "Spkg builds and doctests fine on Linux and OSX. Positive review.\n\nCheers,\n\nMichael",
    "created_at": "2008-06-26T06:47:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3405",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3405#issuecomment-23885",
    "user": "mabshoff"
}
```

Spkg builds and doctests fine on Linux and OSX. Positive review.

Cheers,

Michael



---

archive/issue_comments_023886.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-06-26T06:47:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3405",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3405#issuecomment-23886",
    "user": "mabshoff"
}
```

Resolution: fixed

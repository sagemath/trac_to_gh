# Issue 1966: [with spkgs,patch ] inline_fortran broke on OSX

archive/issues_001966.json:
```json
{
    "body": "Assignee: mabshoff\n\nProbably around the upgrade to 1.0.4 the inline_fortran command broke on osx.\n\nThe following spkg fixes it\n\nhttp://sage.math.washington.edu/home/jkantor/spkgs/numpy-20080104-1.0.4.p2.spkg\n\nalso I changed the inline_fortran.py file so the inline_fortran doctests is no longer optional (it was optional when fortran wasn't required, but now it is, so there is no reason for it to be optional).\n\nhttp://sage.math.washington.edu/home/jkantor/spkgs/inline_fortran.patch\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/1966\n\n",
    "created_at": "2008-01-29T07:09:15Z",
    "labels": [
        "packages: standard",
        "major",
        "bug"
    ],
    "title": "[with spkgs,patch ] inline_fortran broke on OSX",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/1966",
    "user": "jkantor"
}
```
Assignee: mabshoff

Probably around the upgrade to 1.0.4 the inline_fortran command broke on osx.

The following spkg fixes it

http://sage.math.washington.edu/home/jkantor/spkgs/numpy-20080104-1.0.4.p2.spkg

also I changed the inline_fortran.py file so the inline_fortran doctests is no longer optional (it was optional when fortran wasn't required, but now it is, so there is no reason for it to be optional).

http://sage.math.washington.edu/home/jkantor/spkgs/inline_fortran.patch


Issue created by migration from https://trac.sagemath.org/ticket/1966





---

archive/issue_comments_012735.json:
```json
{
    "body": "Builds and testall passes with scipy* rebuild on Linux and OSX. `testall` passes.\n\nCheers,\n\nMichael",
    "created_at": "2008-01-30T08:30:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1966",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1966#issuecomment-12735",
    "user": "mabshoff"
}
```

Builds and testall passes with scipy* rebuild on Linux and OSX. `testall` passes.

Cheers,

Michael



---

archive/issue_comments_012736.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-01-30T08:31:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1966",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1966#issuecomment-12736",
    "user": "mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_012737.json:
```json
{
    "body": "Merged in Sage 2.10.1.rc3",
    "created_at": "2008-01-30T08:31:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1966",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1966#issuecomment-12737",
    "user": "mabshoff"
}
```

Merged in Sage 2.10.1.rc3

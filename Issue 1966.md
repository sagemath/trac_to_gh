# Issue 1966: [with spkgs,patch ] inline_fortran broke on OSX

archive/issues_001966.json:
```json
{
    "body": "Assignee: mabshoff\n\nProbably around the upgrade to 1.0.4 the inline_fortran command broke on osx.\n\nThe following spkg fixes it\n\nhttp://sage.math.washington.edu/home/jkantor/spkgs/numpy-20080104-1.0.4.p2.spkg\n\nalso I changed the inline_fortran.py file so the inline_fortran doctests is no longer optional (it was optional when fortran wasn't required, but now it is, so there is no reason for it to be optional).\n\nhttp://sage.math.washington.edu/home/jkantor/spkgs/inline_fortran.patch\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/1966\n\n",
    "created_at": "2008-01-29T07:09:15Z",
    "labels": [
        "component: packages: standard",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-2.10.1",
    "title": "[with spkgs,patch ] inline_fortran broke on OSX",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/1966",
    "user": "https://trac.sagemath.org/admin/accounts/users/jkantor"
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

archive/issue_comments_012704.json:
```json
{
    "body": "Builds and testall passes with scipy* rebuild on Linux and OSX. `testall` passes.\n\nCheers,\n\nMichael",
    "created_at": "2008-01-30T08:30:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1966",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1966#issuecomment-12704",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Builds and testall passes with scipy* rebuild on Linux and OSX. `testall` passes.

Cheers,

Michael



---

archive/issue_comments_012705.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-01-30T08:31:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1966",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1966#issuecomment-12705",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_012706.json:
```json
{
    "body": "Merged in Sage 2.10.1.rc3",
    "created_at": "2008-01-30T08:31:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1966",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1966#issuecomment-12706",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged in Sage 2.10.1.rc3

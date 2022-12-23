# Issue 625: check for system gfortran, g95 or g77 when no binary is available

archive/issues_000625.json:
```json
{
    "body": "Assignee: mabshoff\n\nThe number of binaries in the current Sage 2.8.4 is limited. But many systems, especially more exotic Unixes, have fortran compilers installed. So instead of failing look for one of those, warn user and select them in the order \n\n```\ngfortran > g95 > g77\n```\n\nCheers,\n\nMichael\n\nIssue created by migration from https://trac.sagemath.org/ticket/625\n\n",
    "created_at": "2007-09-08T23:34:04Z",
    "labels": [
        "packages: standard",
        "major",
        "bug"
    ],
    "title": "check for system gfortran, g95 or g77 when no binary is available",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/625",
    "user": "mabshoff"
}
```
Assignee: mabshoff

The number of binaries in the current Sage 2.8.4 is limited. But many systems, especially more exotic Unixes, have fortran compilers installed. So instead of failing look for one of those, warn user and select them in the order 

```
gfortran > g95 > g77
```

Cheers,

Michael

Issue created by migration from https://trac.sagemath.org/ticket/625





---

archive/issue_comments_003216.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2007-09-08T23:34:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/625",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/625#issuecomment-3216",
    "user": "mabshoff"
}
```

Changing status from new to assigned.



---

archive/issue_comments_003217.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2007-09-12T21:19:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/625",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/625#issuecomment-3217",
    "user": "was"
}
```

Resolution: fixed

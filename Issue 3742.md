# Issue 3742: [with spkg, needs review] Fortran.spkg: Detect the location of gfortran properly

archive/issues_003742.json:
```json
{
    "body": "Assignee: mabshoff\n\nFor the cases when we do not provide a binary Fortran compiler we determine the location of libgfortran relative to the gfortran binary. But many installs link gfortran into $PATH somewhere, so we end up linking against a non-existent libgfortran.so. The updated spkg follows any potential gfortran link, so the issue is fixed. This has been observed on iras. The spkg is at\n\nhttp://sage.math.washington.edu/home/mabshoff/release-cycles-3.0.6/final/fortran-20071120.p5.spkg\n\nCheers,\n\nMichael\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/3742\n\n",
    "created_at": "2008-07-29T17:01:17Z",
    "labels": [
        "build",
        "major",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.0.6",
    "title": "[with spkg, needs review] Fortran.spkg: Detect the location of gfortran properly",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/3742",
    "user": "mabshoff"
}
```
Assignee: mabshoff

For the cases when we do not provide a binary Fortran compiler we determine the location of libgfortran relative to the gfortran binary. But many installs link gfortran into $PATH somewhere, so we end up linking against a non-existent libgfortran.so. The updated spkg follows any potential gfortran link, so the issue is fixed. This has been observed on iras. The spkg is at

http://sage.math.washington.edu/home/mabshoff/release-cycles-3.0.6/final/fortran-20071120.p5.spkg

Cheers,

Michael


Issue created by migration from https://trac.sagemath.org/ticket/3742





---

archive/issue_comments_026577.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2008-07-29T17:01:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3742",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3742#issuecomment-26577",
    "user": "mabshoff"
}
```

Changing status from new to assigned.



---

archive/issue_comments_026578.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-07-29T17:04:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3742",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3742#issuecomment-26578",
    "user": "mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_026579.json:
```json
{
    "body": "Merged in Sage 3.0.6.final",
    "created_at": "2008-07-29T17:04:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3742",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3742#issuecomment-26579",
    "user": "mabshoff"
}
```

Merged in Sage 3.0.6.final

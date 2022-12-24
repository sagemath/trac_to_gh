# Issue 2017: crap -- singular includes surfex as a precompiled binary.  Remove it.

archive/issues_002017.json:
```json
{
    "body": "Assignee: mabshoff\n\nRemove it, and make very sure it stays removed in future versions of the singular spkg, e.g., by modifying spkg-install so that if it sees surfex class files, it will bomb out with an error. \n\n\n```\nsage-2.10.1.rc3/spkg/standard/singular-3-0-4-1-20071209.p3/src/Singular/LIB/surfex/SaveMovieDialog$5.class\nsage-2.10.1.rc3/spkg/standard/singular-3-0-4-1-20071209.p3/src/Singular/LIB/surfex/SolitaryPoint$1.class\nsage-2.10.1.rc3/spkg/standard/singular-3-0-4-1-20071209.p3/src/Singular/LIB/surfex/jv4surfex.class\nsage-2.10.1.rc3/spkg/standard/singular-3-0-4-1-20071209.p3/src/Singular/LIB/surfex/Project$9.class\nsage-2.10.1.rc3/spkg/standard/singular-3-0-4-1-20071209.p3/src/Singular/LIB/surfex/Project$11.class\nsage-2.10.1.rc3/spkg/standard/singular-3-0-4-1-20071209.p3/src/Singular/LIB/surfex/algebra/Polynomial$Term.class\nsage-2.10.1.rc3/spkg/standard/singular-3-0-4-1-20071209.p3/src/Singular/LIB/surfex/algebra/Polynomial$Factor.class\nsage-2.10.1.rc3/spkg/standard/singular-3-0-4-1-20071209.p3/src/Singular/LIB/surfex/algebra/Polynomial.class\nsage-2.10.1.rc3/spkg/standard/singular-3-0-4-1-20071209.p3/src/Singular/LIB/surfex/Defns.class\nsage-2.10.1.rc3/spkg/standard/singular-3-0-4-1-20071209.p3/src/Singular/LIB/surfex/SaveMovieDialog$2.class\nsage-2.10.1.rc3/spkg/standard/singular-3-0-4-1-20071209.p3/src/Singular/LIB/surfex/SaveMovieDialog$removeListener.class\nsage-2.10.1.rc3/spkg/standard/singular-3-0-4-1-20071209.p3/src/Singular/LIB/surfex/SavePic.class\nsage-2.10.1.rc3/spkg/standard/singular-3-0-4-1-20071209.p3/src/Singular/LIB/surfex/SaveMovieDialog$6.class\nsage-2.10.1.rc3/spkg/standard/singular-3-0-4-1-20071209.p3/src/Singular/LIB/surfex/pcalc.class\nsage-2.10.1.rc3/spkg/standard/singular-3-0-4-1-20071209.p3/src/Singular/LIB/surfex/ConfigFrame$3.class\nsage-2.10.1.rc3/spkg/standard/singular-3-0-4-1-20071209.p3/src/Singular/LIB/surfex/Equation.class\nsage-2.10.1.rc3/spkg/standard/singular-3-0-4-1-20071209.p3/src/Singular/LIB/surfex/surfex$1.class\nsage-2.10.1.rc3/spkg/standard/singular-3-0-4-1-20071209.p3/src/Singular/LIB/surfex/LampAdmin$2.class\nsage-2.10.1.rc3/spkg/standard/singular-3-0-4-1-20071209.p3/src/Singular/LIB/surfex/SavePicDialog.class\nsage-2.10.1.rc3/spkg/standard/singular-3-0-4-1-20071209.p3/src/Singular/LIB/surfex/Project$10.class\nsage-2.10.1.rc3/spkg/standard/singular-3-0-4-1-20071209.p3/src/Singular/LIB/surfex/SolitaryPointsAdmin.class\nsage-2.10.1.rc3/spkg/standard/singular-3-0-4-1-20071209.p3/src/Singular/LIB/surfex/SwingWorker.class\nsage-2.10.1.rc3/spkg/standard/singular-3-0-4-1-20071209.p3/src/Singular/LIB/surfex/OneParameter.class\nsage-2.10.1.rc3/spkg/standard/singular-3-0-4-1-20071209.p3/src/Singular/LIB/surfex/ConfigFrame$5.class\nsage-2.10.1.rc3/spkg/standard/singular-3-0-4-1-20071209.p3/src/Singular/LIB/surfex/SaveMovie.class\nsage-2.10.1.rc3/spkg/standard/singular-3-0-4-1-20071209.p3/src/Singular/LIB/surfex/ProgressFrame.class\nsage-2.10.1.rc3/spkg/standard/singular-3-0-4-1-20071209.p3/src/Singular/LIB/surfex/surfex$3.class\nsage-2.10.1.rc3/spkg/standard/singular-3-0-4-1-20071209.p3/src/Singular/LIB/surfex/SavePicDialog$3.class\n\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/2017\n\n",
    "created_at": "2008-01-31T23:28:50Z",
    "labels": [
        "packages: standard",
        "major",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.0.5",
    "title": "crap -- singular includes surfex as a precompiled binary.  Remove it.",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/2017",
    "user": "@williamstein"
}
```
Assignee: mabshoff

Remove it, and make very sure it stays removed in future versions of the singular spkg, e.g., by modifying spkg-install so that if it sees surfex class files, it will bomb out with an error. 


```
sage-2.10.1.rc3/spkg/standard/singular-3-0-4-1-20071209.p3/src/Singular/LIB/surfex/SaveMovieDialog$5.class
sage-2.10.1.rc3/spkg/standard/singular-3-0-4-1-20071209.p3/src/Singular/LIB/surfex/SolitaryPoint$1.class
sage-2.10.1.rc3/spkg/standard/singular-3-0-4-1-20071209.p3/src/Singular/LIB/surfex/jv4surfex.class
sage-2.10.1.rc3/spkg/standard/singular-3-0-4-1-20071209.p3/src/Singular/LIB/surfex/Project$9.class
sage-2.10.1.rc3/spkg/standard/singular-3-0-4-1-20071209.p3/src/Singular/LIB/surfex/Project$11.class
sage-2.10.1.rc3/spkg/standard/singular-3-0-4-1-20071209.p3/src/Singular/LIB/surfex/algebra/Polynomial$Term.class
sage-2.10.1.rc3/spkg/standard/singular-3-0-4-1-20071209.p3/src/Singular/LIB/surfex/algebra/Polynomial$Factor.class
sage-2.10.1.rc3/spkg/standard/singular-3-0-4-1-20071209.p3/src/Singular/LIB/surfex/algebra/Polynomial.class
sage-2.10.1.rc3/spkg/standard/singular-3-0-4-1-20071209.p3/src/Singular/LIB/surfex/Defns.class
sage-2.10.1.rc3/spkg/standard/singular-3-0-4-1-20071209.p3/src/Singular/LIB/surfex/SaveMovieDialog$2.class
sage-2.10.1.rc3/spkg/standard/singular-3-0-4-1-20071209.p3/src/Singular/LIB/surfex/SaveMovieDialog$removeListener.class
sage-2.10.1.rc3/spkg/standard/singular-3-0-4-1-20071209.p3/src/Singular/LIB/surfex/SavePic.class
sage-2.10.1.rc3/spkg/standard/singular-3-0-4-1-20071209.p3/src/Singular/LIB/surfex/SaveMovieDialog$6.class
sage-2.10.1.rc3/spkg/standard/singular-3-0-4-1-20071209.p3/src/Singular/LIB/surfex/pcalc.class
sage-2.10.1.rc3/spkg/standard/singular-3-0-4-1-20071209.p3/src/Singular/LIB/surfex/ConfigFrame$3.class
sage-2.10.1.rc3/spkg/standard/singular-3-0-4-1-20071209.p3/src/Singular/LIB/surfex/Equation.class
sage-2.10.1.rc3/spkg/standard/singular-3-0-4-1-20071209.p3/src/Singular/LIB/surfex/surfex$1.class
sage-2.10.1.rc3/spkg/standard/singular-3-0-4-1-20071209.p3/src/Singular/LIB/surfex/LampAdmin$2.class
sage-2.10.1.rc3/spkg/standard/singular-3-0-4-1-20071209.p3/src/Singular/LIB/surfex/SavePicDialog.class
sage-2.10.1.rc3/spkg/standard/singular-3-0-4-1-20071209.p3/src/Singular/LIB/surfex/Project$10.class
sage-2.10.1.rc3/spkg/standard/singular-3-0-4-1-20071209.p3/src/Singular/LIB/surfex/SolitaryPointsAdmin.class
sage-2.10.1.rc3/spkg/standard/singular-3-0-4-1-20071209.p3/src/Singular/LIB/surfex/SwingWorker.class
sage-2.10.1.rc3/spkg/standard/singular-3-0-4-1-20071209.p3/src/Singular/LIB/surfex/OneParameter.class
sage-2.10.1.rc3/spkg/standard/singular-3-0-4-1-20071209.p3/src/Singular/LIB/surfex/ConfigFrame$5.class
sage-2.10.1.rc3/spkg/standard/singular-3-0-4-1-20071209.p3/src/Singular/LIB/surfex/SaveMovie.class
sage-2.10.1.rc3/spkg/standard/singular-3-0-4-1-20071209.p3/src/Singular/LIB/surfex/ProgressFrame.class
sage-2.10.1.rc3/spkg/standard/singular-3-0-4-1-20071209.p3/src/Singular/LIB/surfex/surfex$3.class
sage-2.10.1.rc3/spkg/standard/singular-3-0-4-1-20071209.p3/src/Singular/LIB/surfex/SavePicDialog$3.class

```


Issue created by migration from https://trac.sagemath.org/ticket/2017





---

archive/issue_comments_013021.json:
```json
{
    "body": "Changing priority from major to blocker.",
    "created_at": "2008-03-12T05:00:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2017",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2017#issuecomment-13021",
    "user": "@williamstein"
}
```

Changing priority from major to blocker.



---

archive/issue_comments_013022.json:
```json
{
    "body": "This must be FIXED.",
    "created_at": "2008-03-12T05:00:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2017",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2017#issuecomment-13022",
    "user": "@williamstein"
}
```

This must be FIXED.



---

archive/issue_comments_013023.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-07-19T13:17:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2017",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2017#issuecomment-13023",
    "user": "mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_013024.json:
```json
{
    "body": "William did remove the offending Java files in Sage 3.0.5.\n\nCheers,\n\nMichael",
    "created_at": "2008-07-19T13:17:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2017",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2017#issuecomment-13024",
    "user": "mabshoff"
}
```

William did remove the offending Java files in Sage 3.0.5.

Cheers,

Michael

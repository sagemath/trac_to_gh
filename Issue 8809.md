# Issue 8809: change local/bin/sage_fortran script to respect the SAGE_FORTRAN variable, if it is set

archive/issues_008809.json:
```json
{
    "body": "Assignee: GeorgSWeber\n\nWhen building binaries that include fortran, etc., it would give developers and users a lot more control if the local/bin/sage_fortran script were changed from\n\n```\n!/bin/sh\n\n/usr/bin/gfortran -fPIC $@\n```\n\nto\n\n```\n!/bin/sh\n\nif [ x\"$SAGE_FORTRAN\" != x ]; then\n     \"$SAGE_FORTRAN\" -fPIC $@\nelse\n     /usr/bin/gfortran -fPIC $@\nfi\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/8809\n\n",
    "created_at": "2010-04-28T22:10:59Z",
    "labels": [
        "build",
        "minor",
        "enhancement"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-duplicate/invalid/wontfix",
    "title": "change local/bin/sage_fortran script to respect the SAGE_FORTRAN variable, if it is set",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/8809",
    "user": "@williamstein"
}
```
Assignee: GeorgSWeber

When building binaries that include fortran, etc., it would give developers and users a lot more control if the local/bin/sage_fortran script were changed from

```
!/bin/sh

/usr/bin/gfortran -fPIC $@
```

to

```
!/bin/sh

if [ x"$SAGE_FORTRAN" != x ]; then
     "$SAGE_FORTRAN" -fPIC $@
else
     /usr/bin/gfortran -fPIC $@
fi
```


Issue created by migration from https://trac.sagemath.org/ticket/8809





---

archive/issue_comments_080852.json:
```json
{
    "body": "`SAGE_FORTRAN` is deprecated and the `sage_fortran` script does use `$FC`.",
    "created_at": "2013-05-19T13:16:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8809",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8809#issuecomment-80852",
    "user": "@jdemeyer"
}
```

`SAGE_FORTRAN` is deprecated and the `sage_fortran` script does use `$FC`.



---

archive/issue_comments_080853.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2013-05-19T13:16:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8809",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8809#issuecomment-80853",
    "user": "@jdemeyer"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_080854.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2013-05-19T13:17:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8809",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8809#issuecomment-80854",
    "user": "@jdemeyer"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_080855.json:
```json
{
    "body": "Resolution: invalid",
    "created_at": "2013-05-21T07:26:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8809",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8809#issuecomment-80855",
    "user": "@jdemeyer"
}
```

Resolution: invalid

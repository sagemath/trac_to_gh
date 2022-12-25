# Issue 1767: Add SAGE_ATLAS_LIB, SAGE_ATLAS_TARGZ flags to allow use of external atlas

archive/issues_001767.json:
```json
{
    "body": "Assignee: mabshoff\n\nWe currently provide a SAGE_FORTRAN flag that lets external fortran be used if the user desires.\nSince atlas takes a long time to build, we should have an optional SAGE_ATLAS_LIB flag \nthat would accept the path to a directory that contained libatlas, libcblas, libf77blas, and liblapack. The atlas install script will do some tests to ensure these work and will then create symlinks to them in $SAGE_LOCAL/lib\n\nThere should also be a SAGE_ATLAS_TARGZ with would be the path to a tar or tar.gz with libatlas, libcblas, libf77blas, and liblapack. These would just be copied into $SAGE_LOCAL/lib\n\nAs mentioned some checking needs to be done to ensure the atlas provided is compatible with the fortran we are using, that it actually works, as well as to check that the lapack is the full lapack (8Mb or so) and not a crippled lapack.\n\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/1767\n\n",
    "created_at": "2008-01-13T23:48:24Z",
    "labels": [
        "component: packages: standard",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-duplicate/invalid/wontfix",
    "title": "Add SAGE_ATLAS_LIB, SAGE_ATLAS_TARGZ flags to allow use of external atlas",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/1767",
    "user": "https://trac.sagemath.org/admin/accounts/users/jkantor"
}
```
Assignee: mabshoff

We currently provide a SAGE_FORTRAN flag that lets external fortran be used if the user desires.
Since atlas takes a long time to build, we should have an optional SAGE_ATLAS_LIB flag 
that would accept the path to a directory that contained libatlas, libcblas, libf77blas, and liblapack. The atlas install script will do some tests to ensure these work and will then create symlinks to them in $SAGE_LOCAL/lib

There should also be a SAGE_ATLAS_TARGZ with would be the path to a tar or tar.gz with libatlas, libcblas, libf77blas, and liblapack. These would just be copied into $SAGE_LOCAL/lib

As mentioned some checking needs to be done to ensure the atlas provided is compatible with the fortran we are using, that it actually works, as well as to check that the lapack is the full lapack (8Mb or so) and not a crippled lapack.



Issue created by migration from https://trac.sagemath.org/ticket/1767





---

archive/issue_comments_011155.json:
```json
{
    "body": "`SAGE_ATLAS_LIB` has been introduced long time ago (ticket:1721#comment:7) and IMO there is no need for `SAGE_ATLAS_TARGZ`. So let's close this.",
    "created_at": "2014-07-25T23:12:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1767",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1767#issuecomment-11155",
    "user": "https://github.com/a-andre"
}
```

`SAGE_ATLAS_LIB` has been introduced long time ago (ticket:1721#comment:7) and IMO there is no need for `SAGE_ATLAS_TARGZ`. So let's close this.



---

archive/issue_comments_011156.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2014-07-25T23:12:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1767",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1767#issuecomment-11156",
    "user": "https://github.com/a-andre"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_011157.json:
```json
{
    "body": "I agree. But we should try to make it more easy to learn how to avoid ATLAS compilation, see #15371.",
    "created_at": "2014-07-26T08:23:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1767",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1767#issuecomment-11157",
    "user": "https://github.com/fchapoton"
}
```

I agree. But we should try to make it more easy to learn how to avoid ATLAS compilation, see #15371.



---

archive/issue_comments_011158.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2014-07-26T08:23:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1767",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1767#issuecomment-11158",
    "user": "https://github.com/fchapoton"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_events_001925.json:
```json
{
    "actor": "@vbraun",
    "created_at": "2014-08-20T20:32:31Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/1767",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/1767#event-1925"
}
```



---

archive/issue_comments_011159.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2014-08-20T20:32:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1767",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1767#issuecomment-11159",
    "user": "https://github.com/vbraun"
}
```

Resolution: fixed

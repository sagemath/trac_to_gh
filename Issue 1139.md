# Issue 1139: nintegral fails for large precision (version 2.8.12)

archive/issues_001139.json:
```json
{
    "body": "Assignee: jkantor\n\n\n```\nsage: f=x\nsage: f.nintegral(x,0,1,1e-14)\nMaxima ERROR:\n         ***MESSAGE FROM ROUTINE DQAGS IN LIBRARY SLATEC.\n ***POTENTIALLY RECOVERABLE ERROR, PROG ABORTED, TRACEBACK REQUESTED\n *  ABNORMAL RETURN\n *  ERROR NUMBER = 6\n *   \n ***END OF MESSAGE\n \n ***JOB ABORT DUE TO UNRECOVERED ERROR.\n0          ERROR MESSAGE SUMMARY\n LIBRARY    SUBROUTINE MESSAGE START             NERR     LEVEL     COUNT\n SLATEC     DQAGS      ABNORMAL RETURN              6         1         2\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/1139\n\n",
    "created_at": "2007-11-10T15:39:07Z",
    "labels": [
        "numerical",
        "major",
        "bug"
    ],
    "title": "nintegral fails for large precision (version 2.8.12)",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/1139",
    "user": "zimmerma"
}
```
Assignee: jkantor


```
sage: f=x
sage: f.nintegral(x,0,1,1e-14)
Maxima ERROR:
         ***MESSAGE FROM ROUTINE DQAGS IN LIBRARY SLATEC.
 ***POTENTIALLY RECOVERABLE ERROR, PROG ABORTED, TRACEBACK REQUESTED
 *  ABNORMAL RETURN
 *  ERROR NUMBER = 6
 *   
 ***END OF MESSAGE
 
 ***JOB ABORT DUE TO UNRECOVERED ERROR.
0          ERROR MESSAGE SUMMARY
 LIBRARY    SUBROUTINE MESSAGE START             NERR     LEVEL     COUNT
 SLATEC     DQAGS      ABNORMAL RETURN              6         1         2
```


Issue created by migration from https://trac.sagemath.org/ticket/1139





---

archive/issue_comments_006924.json:
```json
{
    "body": "This is due to a restriction in QUADPACK (which Maxima is using).\n\n\n```\nc                     and epsrel.lt.max(50*rel.mach.acc.,0.5d-28),\nc                     the routine will end with ier = 6.\n```\n\n\nThe exception should be caught, and a more helpful error should be raised.",
    "created_at": "2007-12-06T21:00:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1139",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1139#issuecomment-6924",
    "user": "mhansen"
}
```

This is due to a restriction in QUADPACK (which Maxima is using).


```
c                     and epsrel.lt.max(50*rel.mach.acc.,0.5d-28),
c                     the routine will end with ier = 6.
```


The exception should be caught, and a more helpful error should be raised.



---

archive/issue_comments_006925.json:
```json
{
    "body": "Changing assignee from jkantor to mhansen.",
    "created_at": "2007-12-06T21:00:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1139",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1139#issuecomment-6925",
    "user": "mhansen"
}
```

Changing assignee from jkantor to mhansen.



---

archive/issue_comments_006926.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2007-12-06T21:00:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1139",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1139#issuecomment-6926",
    "user": "mhansen"
}
```

Changing status from new to assigned.



---

archive/issue_comments_006927.json:
```json
{
    "body": "Attachment [1139.patch](tarball://root/attachments/some-uuid/ticket1139/1139.patch) by mhansen created at 2007-12-06 22:00:14",
    "created_at": "2007-12-06T22:00:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1139",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1139#issuecomment-6927",
    "user": "mhansen"
}
```

Attachment [1139.patch](tarball://root/attachments/some-uuid/ticket1139/1139.patch) by mhansen created at 2007-12-06 22:00:14



---

archive/issue_comments_006928.json:
```json
{
    "body": "Patch attached.  Apply after #553 .",
    "created_at": "2007-12-06T22:00:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1139",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1139#issuecomment-6928",
    "user": "mhansen"
}
```

Patch attached.  Apply after #553 .



---

archive/issue_comments_006929.json:
```json
{
    "body": "p",
    "created_at": "2007-12-15T10:32:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1139",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1139#issuecomment-6929",
    "user": "was"
}
```

p



---

archive/issue_comments_006930.json:
```json
{
    "body": "Merged in 2.9.1.alpha1",
    "created_at": "2007-12-17T22:14:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1139",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1139#issuecomment-6930",
    "user": "rlm"
}
```

Merged in 2.9.1.alpha1



---

archive/issue_comments_006931.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2007-12-17T22:14:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1139",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1139#issuecomment-6931",
    "user": "rlm"
}
```

Resolution: fixed

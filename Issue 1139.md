# Issue 1139: nintegral fails for large precision (version 2.8.12)

archive/issues_001139.json:
```json
{
    "body": "Assignee: jkantor\n\n\n```\nsage: f=x\nsage: f.nintegral(x,0,1,1e-14)\nMaxima ERROR:\n         ***MESSAGE FROM ROUTINE DQAGS IN LIBRARY SLATEC.\n ***POTENTIALLY RECOVERABLE ERROR, PROG ABORTED, TRACEBACK REQUESTED\n *  ABNORMAL RETURN\n *  ERROR NUMBER = 6\n *   \n ***END OF MESSAGE\n \n ***JOB ABORT DUE TO UNRECOVERED ERROR.\n0          ERROR MESSAGE SUMMARY\n LIBRARY    SUBROUTINE MESSAGE START             NERR     LEVEL     COUNT\n SLATEC     DQAGS      ABNORMAL RETURN              6         1         2\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/1139\n\n",
    "created_at": "2007-11-10T15:39:07Z",
    "labels": [
        "component: numerical",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-2.9.1",
    "title": "nintegral fails for large precision (version 2.8.12)",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/1139",
    "user": "https://github.com/zimmermann6"
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

archive/issue_comments_006903.json:
```json
{
    "body": "This is due to a restriction in QUADPACK (which Maxima is using).\n\n\n```\nc                     and epsrel.lt.max(50*rel.mach.acc.,0.5d-28),\nc                     the routine will end with ier = 6.\n```\n\n\nThe exception should be caught, and a more helpful error should be raised.",
    "created_at": "2007-12-06T21:00:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1139",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1139#issuecomment-6903",
    "user": "https://github.com/mwhansen"
}
```

This is due to a restriction in QUADPACK (which Maxima is using).


```
c                     and epsrel.lt.max(50*rel.mach.acc.,0.5d-28),
c                     the routine will end with ier = 6.
```


The exception should be caught, and a more helpful error should be raised.



---

archive/issue_comments_006904.json:
```json
{
    "body": "Changing assignee from jkantor to @mwhansen.",
    "created_at": "2007-12-06T21:00:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1139",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1139#issuecomment-6904",
    "user": "https://github.com/mwhansen"
}
```

Changing assignee from jkantor to @mwhansen.



---

archive/issue_comments_006905.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2007-12-06T21:00:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1139",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1139#issuecomment-6905",
    "user": "https://github.com/mwhansen"
}
```

Changing status from new to assigned.



---

archive/issue_comments_006906.json:
```json
{
    "body": "Attachment [1139.patch](tarball://root/attachments/some-uuid/ticket1139/1139.patch) by @mwhansen created at 2007-12-06 22:00:14",
    "created_at": "2007-12-06T22:00:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1139",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1139#issuecomment-6906",
    "user": "https://github.com/mwhansen"
}
```

Attachment [1139.patch](tarball://root/attachments/some-uuid/ticket1139/1139.patch) by @mwhansen created at 2007-12-06 22:00:14



---

archive/issue_comments_006907.json:
```json
{
    "body": "Patch attached.  Apply after #553 .",
    "created_at": "2007-12-06T22:00:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1139",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1139#issuecomment-6907",
    "user": "https://github.com/mwhansen"
}
```

Patch attached.  Apply after #553 .



---

archive/issue_comments_006908.json:
```json
{
    "body": "p",
    "created_at": "2007-12-15T10:32:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1139",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1139#issuecomment-6908",
    "user": "https://github.com/williamstein"
}
```

p



---

archive/issue_comments_006909.json:
```json
{
    "body": "Merged in 2.9.1.alpha1",
    "created_at": "2007-12-17T22:14:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1139",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1139#issuecomment-6909",
    "user": "https://github.com/rlmill"
}
```

Merged in 2.9.1.alpha1



---

archive/issue_events_001266.json:
```json
{
    "actor": "@rlmill",
    "created_at": "2007-12-17T22:14:03Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/1139",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/1139#event-1266"
}
```



---

archive/issue_comments_006910.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2007-12-17T22:14:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1139",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1139#issuecomment-6910",
    "user": "https://github.com/rlmill"
}
```

Resolution: fixed

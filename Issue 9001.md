# Issue 9001: optional package database_cremona_ellcurve-20071019.p0.spkg causes test failure

archive/issues_009001.json:
```json
{
    "body": "Assignee: tbd\n\n\n```\nsage-4.4.2 with the optional package database_cremona_ellcurve-20071019.p0.spkg has the following test failure:\n\n\ntaurus% ./sage -t -long \"devel/sage/sage/schemes/elliptic_curves/ell_point.py\"\nsage -t -long \"devel/sage/sage/schemes/elliptic_curves/ell_point.py\"\n**********************************************************************\nFile \"/home/mariah/sage/sage-4.4.2-x86_64-Linux-nehalem-fc-test2/devel/sage/sage/schemes/elliptic_curves/ell_point.py\", line 1729:\n    sage: Q = E.isomorphism_to(ED.change_ring(K))(P); Q\nExpected:\n    (0 : -7/2*a - 1/2 : 1)\nGot:\n    (0 : 7/2*a - 1/2 : 1)\n**********************************************************************\n1 items had failures:\n   1 of  67 in __main__.example_36\n***Test Failed*** 1 failures.\nFor whitespace errors, see the file /home/mariah/.sage//tmp/.doctest_ell_point.py\n         [32.7 s]\n \n----------------------------------------------------------------------\nThe following tests failed:\n\n\n        sage -t -long \"devel/sage/sage/schemes/elliptic_curves/ell_point.py\"\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/9001\n\n",
    "created_at": "2010-05-20T20:37:26Z",
    "labels": [
        "component: packages: optional",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.4.3",
    "title": "optional package database_cremona_ellcurve-20071019.p0.spkg causes test failure",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/9001",
    "user": "https://trac.sagemath.org/admin/accounts/users/mariah"
}
```
Assignee: tbd


```
sage-4.4.2 with the optional package database_cremona_ellcurve-20071019.p0.spkg has the following test failure:


taurus% ./sage -t -long "devel/sage/sage/schemes/elliptic_curves/ell_point.py"
sage -t -long "devel/sage/sage/schemes/elliptic_curves/ell_point.py"
**********************************************************************
File "/home/mariah/sage/sage-4.4.2-x86_64-Linux-nehalem-fc-test2/devel/sage/sage/schemes/elliptic_curves/ell_point.py", line 1729:
    sage: Q = E.isomorphism_to(ED.change_ring(K))(P); Q
Expected:
    (0 : -7/2*a - 1/2 : 1)
Got:
    (0 : 7/2*a - 1/2 : 1)
**********************************************************************
1 items had failures:
   1 of  67 in __main__.example_36
***Test Failed*** 1 failures.
For whitespace errors, see the file /home/mariah/.sage//tmp/.doctest_ell_point.py
         [32.7 s]
 
----------------------------------------------------------------------
The following tests failed:


        sage -t -long "devel/sage/sage/schemes/elliptic_curves/ell_point.py"
```


Issue created by migration from https://trac.sagemath.org/ticket/9001





---

archive/issue_comments_083095.json:
```json
{
    "body": "Attachment [trac_9001.patch](tarball://root/attachments/some-uuid/ticket9001/trac_9001.patch) by @williamstein created at 2010-06-04 05:53:17",
    "created_at": "2010-06-04T05:53:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9001",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9001#issuecomment-83095",
    "user": "https://github.com/williamstein"
}
```

Attachment [trac_9001.patch](tarball://root/attachments/some-uuid/ticket9001/trac_9001.patch) by @williamstein created at 2010-06-04 05:53:17



---

archive/issue_comments_083096.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-06-04T08:54:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9001",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9001#issuecomment-83096",
    "user": "https://github.com/JohnCremona"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_083097.json:
```json
{
    "body": "Dammit, I thought we had got rid of all of these,  If the ticket had been tagged as being in Elliptic Curves, I would have noticed this and fixed it 2 weeks ago, sorry.\n\nPatch applies fine to 4.4.3.alpha3.  With no optional packages installed I tested the whole sage library (only 10 minutes with -tp 10!), and did it again after installing database_cremona_ellcurve-20071019.  Just to make sure there were not other examples of this lurking!  All pass.",
    "created_at": "2010-06-04T08:54:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9001",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9001#issuecomment-83097",
    "user": "https://github.com/JohnCremona"
}
```

Dammit, I thought we had got rid of all of these,  If the ticket had been tagged as being in Elliptic Curves, I would have noticed this and fixed it 2 weeks ago, sorry.

Patch applies fine to 4.4.3.alpha3.  With no optional packages installed I tested the whole sage library (only 10 minutes with -tp 10!), and did it again after installing database_cremona_ellcurve-20071019.  Just to make sure there were not other examples of this lurking!  All pass.



---

archive/issue_comments_083098.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-06-04T08:54:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9001",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9001#issuecomment-83098",
    "user": "https://github.com/JohnCremona"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_083099.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-06-04T15:30:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9001",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9001#issuecomment-83099",
    "user": "https://github.com/williamstein"
}
```

Resolution: fixed



---

archive/issue_events_022028.json:
```json
{
    "actor": "https://github.com/williamstein",
    "created_at": "2010-06-04T15:30:10Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/9001",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/9001#event-22028"
}
```



---

archive/issue_events_022029.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mvngu",
    "created_at": "2010-06-04T16:42:45Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/9001",
    "milestone": "sage-4.4.3",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/9001#event-22029"
}
```

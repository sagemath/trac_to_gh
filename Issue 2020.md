# Issue 2020: change an error message when running a certain command and the elliptic curve database is too small

archive/issues_002020.json:
```json
{
    "body": "Assignee: was\n\nIn the session below the command fails because the optional LARGE Cremona elliptic curves database is not installed (it works fine if it is).  The error message should clearly say why the failure occurs, instead of Sage mysteriously bombing out. \n\n\n```\nsage@modular:~$ build/sage-2.10.1.rc3/sage\n----------------------------------------------------------------------\n----------------------------------------------------------------------\n| SAGE Version 2.10.1.rc3, Release Date: 2008-01-30                  |\n| Type notebook() for the GUI, and license() for information.        |\nsage: EllipticCurve('14a4').sha().an(use_database=True)\n---------------------------------------------------------------------------\n<type 'exceptions.AttributeError'>        Traceback (most recent call last)\n\n/home2/sage/<ipython console> in <module>()\n\n/home2/sage/build/sage-2.10.1.rc3/local/lib/python2.5/site-packages/sage/schemes/elliptic_curves/sha.py in an(self, use_database)\n    148         if use_database:\n    149             try:\n--> 150                 self.__an = int(round(float(self.E.database_curve().db_extra[4])))\n    151                 return self.__an\n    152             except RuntimeError, AttributeError:\n\n<type 'exceptions.AttributeError'>: 'EllipticCurve_rational_field' object has no attribute 'db_extra'\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/2020\n\n",
    "created_at": "2008-01-31T23:56:42Z",
    "labels": [
        "number theory",
        "major",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.3",
    "title": "change an error message when running a certain command and the elliptic curve database is too small",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/2020",
    "user": "was"
}
```
Assignee: was

In the session below the command fails because the optional LARGE Cremona elliptic curves database is not installed (it works fine if it is).  The error message should clearly say why the failure occurs, instead of Sage mysteriously bombing out. 


```
sage@modular:~$ build/sage-2.10.1.rc3/sage
----------------------------------------------------------------------
----------------------------------------------------------------------
| SAGE Version 2.10.1.rc3, Release Date: 2008-01-30                  |
| Type notebook() for the GUI, and license() for information.        |
sage: EllipticCurve('14a4').sha().an(use_database=True)
---------------------------------------------------------------------------
<type 'exceptions.AttributeError'>        Traceback (most recent call last)

/home2/sage/<ipython console> in <module>()

/home2/sage/build/sage-2.10.1.rc3/local/lib/python2.5/site-packages/sage/schemes/elliptic_curves/sha.py in an(self, use_database)
    148         if use_database:
    149             try:
--> 150                 self.__an = int(round(float(self.E.database_curve().db_extra[4])))
    151                 return self.__an
    152             except RuntimeError, AttributeError:

<type 'exceptions.AttributeError'>: 'EllipticCurve_rational_field' object has no attribute 'db_extra'
```


Issue created by migration from https://trac.sagemath.org/ticket/2020





---

archive/issue_comments_013036.json:
```json
{
    "body": "Attachment [trac_2020.patch](tarball://root/attachments/some-uuid/ticket2020/trac_2020.patch) by craigcitro created at 2009-01-24 10:27:26\n\nLooks good. (Actual review comments were in person, all taken care of.)",
    "created_at": "2009-01-24T10:27:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2020",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2020#issuecomment-13036",
    "user": "craigcitro"
}
```

Attachment [trac_2020.patch](tarball://root/attachments/some-uuid/ticket2020/trac_2020.patch) by craigcitro created at 2009-01-24 10:27:26

Looks good. (Actual review comments were in person, all taken care of.)



---

archive/issue_comments_013037.json:
```json
{
    "body": "This patch exposes a numerical noise issue in sha_tate:\n\n```\nsage -t -long devel/sage/sage/schemes/elliptic_curves/sha_tate.py\n**********************************************************************\nFile \"/scratch/mabshoff/sage-3.3.alpha2/devel/sage-main/sage/schemes/elliptic_curves/sha_tate.py\", line 157:\n    sage: E.sha().an()\nExpected:\n    0.999999999999998\nGot:\n    1.00000000000000\n**********************************************************************\n```\n\n\nCheers,\n\nMichael",
    "created_at": "2009-01-24T14:47:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2020",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2020#issuecomment-13037",
    "user": "mabshoff"
}
```

This patch exposes a numerical noise issue in sha_tate:

```
sage -t -long devel/sage/sage/schemes/elliptic_curves/sha_tate.py
**********************************************************************
File "/scratch/mabshoff/sage-3.3.alpha2/devel/sage-main/sage/schemes/elliptic_curves/sha_tate.py", line 157:
    sage: E.sha().an()
Expected:
    0.999999999999998
Got:
    1.00000000000000
**********************************************************************
```


Cheers,

Michael



---

archive/issue_comments_013038.json:
```json
{
    "body": "I was wrong, the above is not caused by this patch.\n\nCheers,\n\nMichael",
    "created_at": "2009-01-24T14:57:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2020",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2020#issuecomment-13038",
    "user": "mabshoff"
}
```

I was wrong, the above is not caused by this patch.

Cheers,

Michael



---

archive/issue_comments_013039.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-01-24T15:30:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2020",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2020#issuecomment-13039",
    "user": "mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_013040.json:
```json
{
    "body": "Merged in Sage 3.3.alpha2",
    "created_at": "2009-01-24T15:30:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2020",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2020#issuecomment-13040",
    "user": "mabshoff"
}
```

Merged in Sage 3.3.alpha2

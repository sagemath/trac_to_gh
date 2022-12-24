# Issue 3263: [with patch, needs review] typo in lseries_ell.py

archive/issues_003263.json:
```json
{
    "body": "Assignee: craigcitro\n\nThere was a silly typo in `sage/schemes/elliptic_curves/lseries_ell.py` that caused the following:\n\n\n```\nsage: EllipticCurve('37a').lseries().deriv_at1()\n---------------------------------------------------------------------------\n<type 'exceptions.NameError'>             Traceback (most recent call last)\n\n/Users/craigcitro/<ipython console> in <module>()\n\n/sage/local/lib/python2.5/site-packages/sage/schemes/elliptic_curves/lseries_ell\n.py in deriv_at1(self, k)\n    463         k = int(k)\n    464         sqrtN = float(self.__E.conductor().sqrt())\n--> 465         if k == 0: k = int(math.ceil(sqrtN))\n    466         an = self.__E.anlist(k)           # list of C ints\n    467         # Compute z = e^(-2pi/sqrt(N))\n\n<type 'exceptions.NameError'>: global name 'math' is not defined\n```\n\n\nThis was just a simple issue where ceil wasn't getting imported. Patch is the obvious fix, and adds a doctest that would have caught this. \n\nIssue created by migration from https://trac.sagemath.org/ticket/3263\n\n",
    "created_at": "2008-05-21T08:23:57Z",
    "labels": [
        "algebraic geometry",
        "major",
        "bug"
    ],
    "title": "[with patch, needs review] typo in lseries_ell.py",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/3263",
    "user": "craigcitro"
}
```
Assignee: craigcitro

There was a silly typo in `sage/schemes/elliptic_curves/lseries_ell.py` that caused the following:


```
sage: EllipticCurve('37a').lseries().deriv_at1()
---------------------------------------------------------------------------
<type 'exceptions.NameError'>             Traceback (most recent call last)

/Users/craigcitro/<ipython console> in <module>()

/sage/local/lib/python2.5/site-packages/sage/schemes/elliptic_curves/lseries_ell
.py in deriv_at1(self, k)
    463         k = int(k)
    464         sqrtN = float(self.__E.conductor().sqrt())
--> 465         if k == 0: k = int(math.ceil(sqrtN))
    466         an = self.__E.anlist(k)           # list of C ints
    467         # Compute z = e^(-2pi/sqrt(N))

<type 'exceptions.NameError'>: global name 'math' is not defined
```


This was just a simple issue where ceil wasn't getting imported. Patch is the obvious fix, and adds a doctest that would have caught this. 

Issue created by migration from https://trac.sagemath.org/ticket/3263





---

archive/issue_comments_022582.json:
```json
{
    "body": "Attachment [trac-3263.patch](tarball://root/attachments/some-uuid/ticket3263/trac-3263.patch) by ddrake created at 2008-05-21 08:57:38\n\nPositive review.",
    "created_at": "2008-05-21T08:57:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3263",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3263#issuecomment-22582",
    "user": "ddrake"
}
```

Attachment [trac-3263.patch](tarball://root/attachments/some-uuid/ticket3263/trac-3263.patch) by ddrake created at 2008-05-21 08:57:38

Positive review.



---

archive/issue_comments_022583.json:
```json
{
    "body": "Merge in Sage 3.0.2.rc0",
    "created_at": "2008-05-21T13:25:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3263",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3263#issuecomment-22583",
    "user": "mabshoff"
}
```

Merge in Sage 3.0.2.rc0



---

archive/issue_comments_022584.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-05-21T13:25:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3263",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3263#issuecomment-22584",
    "user": "mabshoff"
}
```

Resolution: fixed

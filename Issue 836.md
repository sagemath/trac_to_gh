# Issue 836: L-series dokchitser -- infinite recursion

archive/issues_000836.json:
```json
{
    "body": "Assignee: @williamstein\n\n\n```\nsage: e = EllipticCurve([1,1,0,-63900,-1964465932632])\nsage: L = e.Lseries_dokchitser(15)\n```\n\n\nThis leads to\n\n```\n<type 'exceptions.RuntimeError'>: maximum recursion depth exceeded in cmp\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/836\n\n",
    "created_at": "2007-10-06T22:59:20Z",
    "labels": [
        "number theory",
        "major",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-2.8.12",
    "title": "L-series dokchitser -- infinite recursion",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/836",
    "user": "@williamstein"
}
```
Assignee: @williamstein


```
sage: e = EllipticCurve([1,1,0,-63900,-1964465932632])
sage: L = e.Lseries_dokchitser(15)
```


This leads to

```
<type 'exceptions.RuntimeError'>: maximum recursion depth exceeded in cmp
```


Issue created by migration from https://trac.sagemath.org/ticket/836





---

archive/issue_comments_005168.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2007-10-06T22:59:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/836",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/836#issuecomment-5168",
    "user": "@williamstein"
}
```

Changing status from new to assigned.



---

archive/issue_comments_005169.json:
```json
{
    "body": "Hmm, things go wrong at a different point now:\n\n```\nsage: e = EllipticCurve([1,1,0,-63900,-1964465932632])\nsage: L = e.Lseries().dokchitser(15)\nsage: L(1)\n---------------------------------------------------------------------------\n<type 'exceptions.RuntimeError'>          Traceback (most recent call last)\n\n/Users/was/<ipython console> in <module>()\n\n/Users/was/s/local/lib/python2.5/site-packages/sage/lfunctions/dokchitser.py in __call__(self, s, c)\n    314             raise ArithmeticError, z\n    315         elif '***' in z:\n--> 316             raise RuntimeError, z\n    317         elif 'Warning' in z:\n    318             i = z.rfind('\\n')\n\n<type 'exceptions.RuntimeError'>:   ***   I was expecting an integer here: lfundigits\n                                         ^----------\n```\n",
    "created_at": "2007-11-03T20:08:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/836",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/836#issuecomment-5169",
    "user": "@williamstein"
}
```

Hmm, things go wrong at a different point now:

```
sage: e = EllipticCurve([1,1,0,-63900,-1964465932632])
sage: L = e.Lseries().dokchitser(15)
sage: L(1)
---------------------------------------------------------------------------
<type 'exceptions.RuntimeError'>          Traceback (most recent call last)

/Users/was/<ipython console> in <module>()

/Users/was/s/local/lib/python2.5/site-packages/sage/lfunctions/dokchitser.py in __call__(self, s, c)
    314             raise ArithmeticError, z
    315         elif '***' in z:
--> 316             raise RuntimeError, z
    317         elif 'Warning' in z:
    318             i = z.rfind('\n')

<type 'exceptions.RuntimeError'>:   ***   I was expecting an integer here: lfundigits
                                         ^----------
```




---

archive/issue_comments_005170.json:
```json
{
    "body": "Attachment [trac836.patch](tarball://root/attachments/some-uuid/ticket836/trac836.patch) by @williamstein created at 2007-11-03 20:26:55",
    "created_at": "2007-11-03T20:26:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/836",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/836#issuecomment-5170",
    "user": "@williamstein"
}
```

Attachment [trac836.patch](tarball://root/attachments/some-uuid/ticket836/trac836.patch) by @williamstein created at 2007-11-03 20:26:55



---

archive/issue_comments_005171.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2007-11-03T20:26:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/836",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/836#issuecomment-5171",
    "user": "@williamstein"
}
```

Resolution: fixed

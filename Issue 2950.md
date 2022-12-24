# Issue 2950: point3d misinterpret arguments

archive/issues_002950.json:
```json
{
    "body": "Assignee: @williamstein\n\nIf point3d is called with 3 points and the first point is a vector, there is a strange error. The first three calls below work, the forth should work, but it does not (tested on sage.math, version 2.11):\n\n\n```\nsage: from sage.plot.plot3d.all import line3d, point3d\nsage: pl = point3d([(1, 0, 0), (0, 1, 0), (-1, -1, 0)])\nsage: pl = point3d([(1, 0, 0), vector(ZZ,(0, 1, 0)), (-1, -1, 0)])\nsage: pl = point3d([vector(ZZ,(1, 0, 0)), (-1, -1, 0)])\nsage: pl = point3d([vector(ZZ,(1, 0, 0)), vector(ZZ,(0, 1, 0)), (-1, -1, 0)])\nTraceback (most recent call last):\n...\nTypeError: float() argument must be a string or a number\n```\n\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/2950\n\n",
    "created_at": "2008-04-18T05:46:16Z",
    "labels": [
        "graphics",
        "minor",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.3",
    "title": "point3d misinterpret arguments",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/2950",
    "user": "@novoselt"
}
```
Assignee: @williamstein

If point3d is called with 3 points and the first point is a vector, there is a strange error. The first three calls below work, the forth should work, but it does not (tested on sage.math, version 2.11):


```
sage: from sage.plot.plot3d.all import line3d, point3d
sage: pl = point3d([(1, 0, 0), (0, 1, 0), (-1, -1, 0)])
sage: pl = point3d([(1, 0, 0), vector(ZZ,(0, 1, 0)), (-1, -1, 0)])
sage: pl = point3d([vector(ZZ,(1, 0, 0)), (-1, -1, 0)])
sage: pl = point3d([vector(ZZ,(1, 0, 0)), vector(ZZ,(0, 1, 0)), (-1, -1, 0)])
Traceback (most recent call last):
...
TypeError: float() argument must be a string or a number
```



Issue created by migration from https://trac.sagemath.org/ticket/2950





---

archive/issue_comments_020340.json:
```json
{
    "body": "fix to sage/plot/plot3d/shapes2.py",
    "created_at": "2009-01-23T07:25:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2950",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2950#issuecomment-20340",
    "user": "shumow"
}
```

fix to sage/plot/plot3d/shapes2.py



---

archive/issue_comments_020341.json:
```json
{
    "body": "Changing assignee from @williamstein to shumow.",
    "created_at": "2009-01-23T07:28:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2950",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2950#issuecomment-20341",
    "user": "shumow"
}
```

Changing assignee from @williamstein to shumow.



---

archive/issue_comments_020342.json:
```json
{
    "body": "Attachment [trac_2950-point3d-arg.patch](tarball://root/attachments/some-uuid/ticket2950/trac_2950-point3d-arg.patch) by shumow created at 2009-01-23 07:28:16",
    "created_at": "2009-01-23T07:28:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2950",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2950#issuecomment-20342",
    "user": "shumow"
}
```

Attachment [trac_2950-point3d-arg.patch](tarball://root/attachments/some-uuid/ticket2950/trac_2950-point3d-arg.patch) by shumow created at 2009-01-23 07:28:16



---

archive/issue_comments_020343.json:
```json
{
    "body": "Attachment [trac_2950-2.patch](tarball://root/attachments/some-uuid/ticket2950/trac_2950-2.patch) by @mwhansen created at 2009-01-24 02:51:25\n\nI added a doctest to make sure that this works.",
    "created_at": "2009-01-24T02:51:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2950",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2950#issuecomment-20343",
    "user": "@mwhansen"
}
```

Attachment [trac_2950-2.patch](tarball://root/attachments/some-uuid/ticket2950/trac_2950-2.patch) by @mwhansen created at 2009-01-24 02:51:25

I added a doctest to make sure that this works.



---

archive/issue_comments_020344.json:
```json
{
    "body": "Mike's patch is good and should be applied as well.",
    "created_at": "2009-01-24T06:15:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2950",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2950#issuecomment-20344",
    "user": "shumow"
}
```

Mike's patch is good and should be applied as well.



---

archive/issue_comments_020345.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-01-28T15:17:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2950",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2950#issuecomment-20345",
    "user": "mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_020346.json:
```json
{
    "body": "Merged both patches in Sage 3.3.alpha3",
    "created_at": "2009-01-28T15:17:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2950",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2950#issuecomment-20346",
    "user": "mabshoff"
}
```

Merged both patches in Sage 3.3.alpha3

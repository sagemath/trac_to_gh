# Issue 646: plot3d error on itanium

archive/issues_000646.json:
```json
{
    "body": "Assignee: was\n\n\n```\n---------- Forwarded message ----------\nFrom: Kate Minola <kate01123@gmail.com>\nDate: Sep 12, 2007 7:27 AM\nSubject: [sage-support] sage-2.8.4.1 build report\nTo: sage-support@googlegroups.com\n\n\n\nWilliam,\n\nsage-2.8.4.1 built and successfully passed all\ntests on the following architectures:\n\n  x86-Linux (pentium4-fc6)\n  x86_64-Linux (fc6)\n\nOn ia64-Linux, sage-2.8.4.1 only failed one test:\n      sage -t  devel/sage-main/sage/plot/plot3d/plot3d.py\n      [...]\n      File \"base.pyx\", line 274, in base.TransformGroup.get_transformation\n        self.T = Transformation(self._scale, self._rot, self._trans)\n      File \"transform.pyx\", line 37, in transform.Transformation.__init__\n        t = atan2(vy,vz) + pi/2\n    ValueError: math domain error\n\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/646\n\n",
    "created_at": "2007-09-13T05:42:53Z",
    "labels": [
        "packages: standard",
        "major",
        "bug"
    ],
    "title": "plot3d error on itanium",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/646",
    "user": "robertwb"
}
```
Assignee: was


```
---------- Forwarded message ----------
From: Kate Minola <kate01123@gmail.com>
Date: Sep 12, 2007 7:27 AM
Subject: [sage-support] sage-2.8.4.1 build report
To: sage-support@googlegroups.com



William,

sage-2.8.4.1 built and successfully passed all
tests on the following architectures:

  x86-Linux (pentium4-fc6)
  x86_64-Linux (fc6)

On ia64-Linux, sage-2.8.4.1 only failed one test:
      sage -t  devel/sage-main/sage/plot/plot3d/plot3d.py
      [...]
      File "base.pyx", line 274, in base.TransformGroup.get_transformation
        self.T = Transformation(self._scale, self._rot, self._trans)
      File "transform.pyx", line 37, in transform.Transformation.__init__
        t = atan2(vy,vz) + pi/2
    ValueError: math domain error

```


Issue created by migration from https://trac.sagemath.org/ticket/646





---

archive/issue_comments_003352.json:
```json
{
    "body": "Attachment",
    "created_at": "2007-09-13T05:43:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/646",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/646#issuecomment-3352",
    "user": "robertwb"
}
```

Attachment



---

archive/issue_comments_003353.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2007-09-13T05:47:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/646",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/646#issuecomment-3353",
    "user": "robertwb"
}
```

Changing status from new to assigned.



---

archive/issue_comments_003354.json:
```json
{
    "body": "Looks like itanium sets errno on atan2(0,0), whereas other processors\nreturn 0. Here's a fix.\n\nI am going to rewrite the function to be cleaner and avoid all use of atan.",
    "created_at": "2007-09-13T05:47:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/646",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/646#issuecomment-3354",
    "user": "robertwb"
}
```

Looks like itanium sets errno on atan2(0,0), whereas other processors
return 0. Here's a fix.

I am going to rewrite the function to be cleaner and avoid all use of atan.



---

archive/issue_comments_003355.json:
```json
{
    "body": "Changing assignee from was to robertwb.",
    "created_at": "2007-09-13T05:47:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/646",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/646#issuecomment-3355",
    "user": "robertwb"
}
```

Changing assignee from was to robertwb.



---

archive/issue_comments_003356.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2007-09-13T06:20:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/646",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/646#issuecomment-3356",
    "user": "was"
}
```

Resolution: fixed



---

archive/issue_comments_003357.json:
```json
{
    "body": "Still broken:\n\n```\nWilliam,\n\nThe patch as written gives the same error.  However if you\nchange line 37 of the patch from\n    if vx == vy == 0:\nto\n    if vy == vz == 0:\n(since atan2() is taking arguments vy and vz) then\nI get a different error on ia64-Linux:\n\nsage -t  devel/sage-main/sage/plot/plot3d/plot3d.py\n**********************************************************************\nFile \"plot3d.py\", line 19:\n   sage: S.show()\nExpected nothing\nGot:\n   6.0\n   <type 'sage.rings.real_double.RealDoubleElement'>\n   0.0\n   0.0\n**********************************************************************\n```\n",
    "created_at": "2007-09-13T15:52:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/646",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/646#issuecomment-3357",
    "user": "was"
}
```

Still broken:

```
William,

The patch as written gives the same error.  However if you
change line 37 of the patch from
    if vx == vy == 0:
to
    if vy == vz == 0:
(since atan2() is taking arguments vy and vz) then
I get a different error on ia64-Linux:

sage -t  devel/sage-main/sage/plot/plot3d/plot3d.py
**********************************************************************
File "plot3d.py", line 19:
   sage: S.show()
Expected nothing
Got:
   6.0
   <type 'sage.rings.real_double.RealDoubleElement'>
   0.0
   0.0
**********************************************************************
```




---

archive/issue_comments_003358.json:
```json
{
    "body": "Resolution changed from fixed to ",
    "created_at": "2007-09-13T15:52:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/646",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/646#issuecomment-3358",
    "user": "was"
}
```

Resolution changed from fixed to 



---

archive/issue_comments_003359.json:
```json
{
    "body": "Changing status from closed to reopened.",
    "created_at": "2007-09-13T15:52:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/646",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/646#issuecomment-3359",
    "user": "was"
}
```

Changing status from closed to reopened.



---

archive/issue_comments_003360.json:
```json
{
    "body": "Attachment\n\nHopefully this is not fixed (it's in 2.8.4.2)",
    "created_at": "2007-09-13T18:20:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/646",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/646#issuecomment-3360",
    "user": "was"
}
```

Attachment

Hopefully this is not fixed (it's in 2.8.4.2)



---

archive/issue_comments_003361.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2007-09-13T18:20:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/646",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/646#issuecomment-3361",
    "user": "was"
}
```

Resolution: fixed

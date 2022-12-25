# Issue 646: plot3d error on itanium

archive/issues_000646.json:
```json
{
    "body": "Assignee: @robertwb\n\n```\n---------- Forwarded message ----------\nFrom: Kate Minola <kate01123@gmail.com>\nDate: Sep 12, 2007 7:27 AM\nSubject: [sage-support] sage-2.8.4.1 build report\nTo: sage-support@googlegroups.com\n\n\n\nWilliam,\n\nsage-2.8.4.1 built and successfully passed all\ntests on the following architectures:\n\n  x86-Linux (pentium4-fc6)\n  x86_64-Linux (fc6)\n\nOn ia64-Linux, sage-2.8.4.1 only failed one test:\n      sage -t  devel/sage-main/sage/plot/plot3d/plot3d.py\n      [...]\n      File \"base.pyx\", line 274, in base.TransformGroup.get_transformation\n        self.T = Transformation(self._scale, self._rot, self._trans)\n      File \"transform.pyx\", line 37, in transform.Transformation.__init__\n        t = atan2(vy,vz) + pi/2\n    ValueError: math domain error\n\n```\n\nIssue created by migration from https://trac.sagemath.org/ticket/646\n\n",
    "closed_at": "2007-09-13T18:20:18Z",
    "created_at": "2007-09-13T05:42:53Z",
    "labels": [
        "component: packages: standard",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-2.8.4.2",
    "title": "plot3d error on itanium",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/646",
    "user": "https://github.com/robertwb"
}
```
Assignee: @robertwb

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

archive/issue_comments_003339.json:
```json
{
    "body": "Attachment [itanium-atan2.patch](tarball://root/attachments/some-uuid/ticket646/itanium-atan2.patch) by @robertwb created at 2007-09-13 05:43:35",
    "created_at": "2007-09-13T05:43:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/646",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/646#issuecomment-3339",
    "user": "https://github.com/robertwb"
}
```

Attachment [itanium-atan2.patch](tarball://root/attachments/some-uuid/ticket646/itanium-atan2.patch) by @robertwb created at 2007-09-13 05:43:35



---

archive/issue_comments_003340.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2007-09-13T05:47:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/646",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/646#issuecomment-3340",
    "user": "https://github.com/robertwb"
}
```

Changing status from new to assigned.



---

archive/issue_comments_003341.json:
```json
{
    "body": "Looks like itanium sets errno on atan2(0,0), whereas other processors\nreturn 0. Here's a fix.\n\nI am going to rewrite the function to be cleaner and avoid all use of atan.",
    "created_at": "2007-09-13T05:47:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/646",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/646#issuecomment-3341",
    "user": "https://github.com/robertwb"
}
```

Looks like itanium sets errno on atan2(0,0), whereas other processors
return 0. Here's a fix.

I am going to rewrite the function to be cleaner and avoid all use of atan.



---

archive/issue_comments_003342.json:
```json
{
    "body": "Changing assignee from @williamstein to @robertwb.",
    "created_at": "2007-09-13T05:47:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/646",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/646#issuecomment-3342",
    "user": "https://github.com/robertwb"
}
```

Changing assignee from @williamstein to @robertwb.



---

archive/issue_events_001721.json:
```json
{
    "actor": "https://github.com/williamstein",
    "created_at": "2007-09-13T06:20:36Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/646",
    "milestone": "sage-2.8.4.2",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/646#event-1721"
}
```



---

archive/issue_events_001722.json:
```json
{
    "actor": "https://github.com/williamstein",
    "created_at": "2007-09-13T06:20:36Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/646",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/646#event-1722"
}
```



---

archive/issue_comments_003343.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2007-09-13T06:20:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/646",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/646#issuecomment-3343",
    "user": "https://github.com/williamstein"
}
```

Resolution: fixed



---

archive/issue_comments_003344.json:
```json
{
    "body": "Still broken:\n\n```\nWilliam,\n\nThe patch as written gives the same error.  However if you\nchange line 37 of the patch from\n    if vx == vy == 0:\nto\n    if vy == vz == 0:\n(since atan2() is taking arguments vy and vz) then\nI get a different error on ia64-Linux:\n\nsage -t  devel/sage-main/sage/plot/plot3d/plot3d.py\n**********************************************************************\nFile \"plot3d.py\", line 19:\n   sage: S.show()\nExpected nothing\nGot:\n   6.0\n   <type 'sage.rings.real_double.RealDoubleElement'>\n   0.0\n   0.0\n**********************************************************************\n```",
    "created_at": "2007-09-13T15:52:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/646",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/646#issuecomment-3344",
    "user": "https://github.com/williamstein"
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

archive/issue_comments_003345.json:
```json
{
    "body": "Resolution changed from fixed to ",
    "created_at": "2007-09-13T15:52:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/646",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/646#issuecomment-3345",
    "user": "https://github.com/williamstein"
}
```

Resolution changed from fixed to 



---

archive/issue_comments_003346.json:
```json
{
    "body": "Changing status from closed to reopened.",
    "created_at": "2007-09-13T15:52:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/646",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/646#issuecomment-3346",
    "user": "https://github.com/williamstein"
}
```

Changing status from closed to reopened.



---

archive/issue_events_001723.json:
```json
{
    "actor": "https://github.com/williamstein",
    "created_at": "2007-09-13T15:52:26Z",
    "event": "reopened",
    "issue": "https://github.com/sagemath/sagetest/issues/646",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/646#event-1723"
}
```



---

archive/issue_events_001724.json:
```json
{
    "actor": "https://github.com/williamstein",
    "created_at": "2007-09-13T15:52:32Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/646",
    "milestone": "sage-2.8.4.2",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/646#event-1724"
}
```



---

archive/issue_comments_003347.json:
```json
{
    "body": "Attachment [better-plot3d-rot.patch](tarball://root/attachments/some-uuid/ticket646/better-plot3d-rot.patch) by @williamstein created at 2007-09-13 18:20:18\n\nHopefully this is not fixed (it's in 2.8.4.2)",
    "created_at": "2007-09-13T18:20:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/646",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/646#issuecomment-3347",
    "user": "https://github.com/williamstein"
}
```

Attachment [better-plot3d-rot.patch](tarball://root/attachments/some-uuid/ticket646/better-plot3d-rot.patch) by @williamstein created at 2007-09-13 18:20:18

Hopefully this is not fixed (it's in 2.8.4.2)



---

archive/issue_events_001725.json:
```json
{
    "actor": "https://github.com/williamstein",
    "created_at": "2007-09-13T18:20:18Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/646",
    "milestone": "sage-2.8.4.2",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/646#event-1725"
}
```



---

archive/issue_comments_003348.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2007-09-13T18:20:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/646",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/646#issuecomment-3348",
    "user": "https://github.com/williamstein"
}
```

Resolution: fixed



---

archive/issue_events_001726.json:
```json
{
    "actor": "https://github.com/williamstein",
    "created_at": "2007-09-13T18:20:18Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/646",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/646#event-1726"
}
```

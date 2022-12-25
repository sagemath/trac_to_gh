# Issue 1511: Export 3d objects in jmol format

archive/issues_001511.json:
```json
{
    "body": "Assignee: @williamstein\n\nhttp://jmol.sourceforge.net/ may be a promising answer to 3d graphics in Sage. \n\nIssue created by migration from https://trac.sagemath.org/ticket/1511\n\n",
    "created_at": "2007-12-14T19:58:09Z",
    "labels": [
        "component: graphics"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-2.9",
    "title": "Export 3d objects in jmol format",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/1511",
    "user": "https://github.com/robertwb"
}
```
Assignee: @williamstein

http://jmol.sourceforge.net/ may be a promising answer to 3d graphics in Sage. 

Issue created by migration from https://trac.sagemath.org/ticket/1511





---

archive/issue_comments_009660.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2007-12-14T19:58:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1511",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1511#issuecomment-9660",
    "user": "https://github.com/robertwb"
}
```

Changing status from new to assigned.



---

archive/issue_comments_009661.json:
```json
{
    "body": "Changing assignee from @williamstein to @robertwb.",
    "created_at": "2007-12-14T19:58:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1511",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1511#issuecomment-9661",
    "user": "https://github.com/robertwb"
}
```

Changing assignee from @williamstein to @robertwb.



---

archive/issue_comments_009662.json:
```json
{
    "body": "Bundle also contains #1473",
    "created_at": "2007-12-15T00:36:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1511",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1511#issuecomment-9662",
    "user": "https://github.com/robertwb"
}
```

Bundle also contains #1473



---

archive/issue_comments_009663.json:
```json
{
    "body": "```\n    sage: from sage.plot.plot3d.shapes import *\n    sage: from sage.plot.plot3d.plot3d import plot3d\n    sage: S = Sphere(.5, color='yellow')\n    sage: S += Cone(.5, .5, color='red').translate(0,0,.3)\n    sage: S += Sphere(.1, color='white').translate(.45,-.1,.15) + Sphere(.05, color='black').translate(.51,-.1,.17)\n    sage: S += Sphere(.1, color='white').translate(.45, .1,.15) + Sphere(.05, color='black').translate(.51, .1,.17)\n    sage: S += Sphere(.1, color='yellow').translate(.5, 0, -.2)\n    sage: def f(x,y): return math.exp(x/5)*math.cos(y)\n```\n\n```\n    sage: P = plot3d(f,(-5,5),(-5,5), ['red','yellow'], max_depth=10)\n    sage: cape_man = P.scale(.2)+S.translate(1,0,0)\n    sage: cape_man.export_jmol('/path/to/a.script')\n```\nThen, after downloading jmol, do \n\n```\n./jmol /path/to/a.script\n```",
    "created_at": "2007-12-15T00:39:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1511",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1511#issuecomment-9663",
    "user": "https://github.com/robertwb"
}
```

```
    sage: from sage.plot.plot3d.shapes import *
    sage: from sage.plot.plot3d.plot3d import plot3d
    sage: S = Sphere(.5, color='yellow')
    sage: S += Cone(.5, .5, color='red').translate(0,0,.3)
    sage: S += Sphere(.1, color='white').translate(.45,-.1,.15) + Sphere(.05, color='black').translate(.51,-.1,.17)
    sage: S += Sphere(.1, color='white').translate(.45, .1,.15) + Sphere(.05, color='black').translate(.51, .1,.17)
    sage: S += Sphere(.1, color='yellow').translate(.5, 0, -.2)
    sage: def f(x,y): return math.exp(x/5)*math.cos(y)
```

```
    sage: P = plot3d(f,(-5,5),(-5,5), ['red','yellow'], max_depth=10)
    sage: cape_man = P.scale(.2)+S.translate(1,0,0)
    sage: cape_man.export_jmol('/path/to/a.script')
```
Then, after downloading jmol, do 

```
./jmol /path/to/a.script
```



---

archive/issue_comments_009664.json:
```json
{
    "body": "Attachment [jmol-export.hg](tarball://root/attachments/some-uuid/ticket1511/jmol-export.hg) by @robertwb created at 2007-12-15 01:15:55",
    "created_at": "2007-12-15T01:15:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1511",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1511#issuecomment-9664",
    "user": "https://github.com/robertwb"
}
```

Attachment [jmol-export.hg](tarball://root/attachments/some-uuid/ticket1511/jmol-export.hg) by @robertwb created at 2007-12-15 01:15:55



---

archive/issue_comments_009665.json:
```json
{
    "body": "It works perfectly!!! Of course, it needs some doctests...\n\nTry this out, it's awesome:\n\n```\n sage: from sage.plot.plot3d.shapes import *\n    sage: from sage.plot.plot3d.plot3d import plot3d\n    sage: S = Sphere(.5, color='yellow')\n    sage: S += Cone(.5, .5, color='red').translate(0,0,.3)\n    sage: S += Sphere(.1, color='white').translate(.45,-.1,.15) + Sphere(.05, color='black').translate(.51,-.1,.17)\n    sage: S += Sphere(.1, color='white').translate(.45, .1,.15) + Sphere(.05, color='black').translate(.51, .1,.17)\n    sage: S += Sphere(.1, color='yellow').translate(.5, 0, -.2)\n    sage: def f(x,y): return math.exp(x/5)*math.cos(y)\n    sage: P = plot3d(f,(-200,20),(-200,20), ['red','yellow'], max_depth=10)\n    sage: cape_man = P.scale(.2)+S.translate(1,0,0)\n    sage: cape_man.export_jmol('/Users/was/sage-2.9.alpha7/jmol/a.script')\n```",
    "created_at": "2007-12-15T01:59:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1511",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1511#issuecomment-9665",
    "user": "https://github.com/williamstein"
}
```

It works perfectly!!! Of course, it needs some doctests...

Try this out, it's awesome:

```
 sage: from sage.plot.plot3d.shapes import *
    sage: from sage.plot.plot3d.plot3d import plot3d
    sage: S = Sphere(.5, color='yellow')
    sage: S += Cone(.5, .5, color='red').translate(0,0,.3)
    sage: S += Sphere(.1, color='white').translate(.45,-.1,.15) + Sphere(.05, color='black').translate(.51,-.1,.17)
    sage: S += Sphere(.1, color='white').translate(.45, .1,.15) + Sphere(.05, color='black').translate(.51, .1,.17)
    sage: S += Sphere(.1, color='yellow').translate(.5, 0, -.2)
    sage: def f(x,y): return math.exp(x/5)*math.cos(y)
    sage: P = plot3d(f,(-200,20),(-200,20), ['red','yellow'], max_depth=10)
    sage: cape_man = P.scale(.2)+S.translate(1,0,0)
    sage: cape_man.export_jmol('/Users/was/sage-2.9.alpha7/jmol/a.script')
```



---

archive/issue_comments_009666.json:
```json
{
    "body": "See #1516 for future work.",
    "created_at": "2007-12-15T02:19:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1511",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1511#issuecomment-9666",
    "user": "https://github.com/robertwb"
}
```

See #1516 for future work.



---

archive/issue_comments_009667.json:
```json
{
    "body": "Positi",
    "created_at": "2007-12-15T23:54:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1511",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1511#issuecomment-9667",
    "user": "https://github.com/williamstein"
}
```

Positi



---

archive/issue_events_003824.json:
```json
{
    "actor": "https://github.com/williamstein",
    "created_at": "2007-12-15T23:54:17Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/1511",
    "milestone": "sage-2.9",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/1511#event-3824"
}
```



---

archive/issue_comments_009668.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2007-12-16T00:56:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1511",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1511#issuecomment-9668",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_009669.json:
```json
{
    "body": "Attachment [trac-1511-update.patch](tarball://root/attachments/some-uuid/ticket1511/trac-1511-update.patch) by mabshoff created at 2007-12-16 00:56:33\n\nMerged in 2.9.rc2.",
    "created_at": "2007-12-16T00:56:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1511",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1511#issuecomment-9669",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Attachment [trac-1511-update.patch](tarball://root/attachments/some-uuid/ticket1511/trac-1511-update.patch) by mabshoff created at 2007-12-16 00:56:33

Merged in 2.9.rc2.



---

archive/issue_events_003825.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2007-12-16T00:56:33Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/1511",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/1511#event-3825"
}
```

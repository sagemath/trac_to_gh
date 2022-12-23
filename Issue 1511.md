# Issue 1511: Export 3d objects in jmol format

archive/issues_001511.json:
```json
{
    "body": "Assignee: was\n\nhttp://jmol.sourceforge.net/ may be a promising answer to 3d graphics in Sage. \n\nIssue created by migration from https://trac.sagemath.org/ticket/1511\n\n",
    "created_at": "2007-12-14T19:58:09Z",
    "labels": [
        "graphics",
        "major",
        "enhancement"
    ],
    "title": "Export 3d objects in jmol format",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/1511",
    "user": "robertwb"
}
```
Assignee: was

http://jmol.sourceforge.net/ may be a promising answer to 3d graphics in Sage. 

Issue created by migration from https://trac.sagemath.org/ticket/1511





---

archive/issue_comments_009685.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2007-12-14T19:58:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1511",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1511#issuecomment-9685",
    "user": "robertwb"
}
```

Changing status from new to assigned.



---

archive/issue_comments_009686.json:
```json
{
    "body": "Changing assignee from was to robertwb.",
    "created_at": "2007-12-14T19:58:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1511",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1511#issuecomment-9686",
    "user": "robertwb"
}
```

Changing assignee from was to robertwb.



---

archive/issue_comments_009687.json:
```json
{
    "body": "Bundle also contains #1473",
    "created_at": "2007-12-15T00:36:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1511",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1511#issuecomment-9687",
    "user": "robertwb"
}
```

Bundle also contains #1473



---

archive/issue_comments_009688.json:
```json
{
    "body": "\n```\n    sage: from sage.plot.plot3d.shapes import *\n    sage: from sage.plot.plot3d.plot3d import plot3d\n    sage: S = Sphere(.5, color='yellow')\n    sage: S += Cone(.5, .5, color='red').translate(0,0,.3)\n    sage: S += Sphere(.1, color='white').translate(.45,-.1,.15) + Sphere(.05, color='black').translate(.51,-.1,.17)\n    sage: S += Sphere(.1, color='white').translate(.45, .1,.15) + Sphere(.05, color='black').translate(.51, .1,.17)\n    sage: S += Sphere(.1, color='yellow').translate(.5, 0, -.2)\n    sage: def f(x,y): return math.exp(x/5)*math.cos(y)\n```\n\n\n```\n    sage: P = plot3d(f,(-5,5),(-5,5), ['red','yellow'], max_depth=10)\n    sage: cape_man = P.scale(.2)+S.translate(1,0,0)\n    sage: cape_man.export_jmol('/path/to/a.script')\n```\n\nThen, after downloading jmol, do \n\n```\n./jmol /path/to/a.script\n```\n",
    "created_at": "2007-12-15T00:39:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1511",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1511#issuecomment-9688",
    "user": "robertwb"
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

archive/issue_comments_009689.json:
```json
{
    "body": "Attachment",
    "created_at": "2007-12-15T01:15:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1511",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1511#issuecomment-9689",
    "user": "robertwb"
}
```

Attachment



---

archive/issue_comments_009690.json:
```json
{
    "body": "It works perfectly!!! Of course, it needs some doctests...\n\nTry this out, it's awesome:\n\n```\n sage: from sage.plot.plot3d.shapes import *\n    sage: from sage.plot.plot3d.plot3d import plot3d\n    sage: S = Sphere(.5, color='yellow')\n    sage: S += Cone(.5, .5, color='red').translate(0,0,.3)\n    sage: S += Sphere(.1, color='white').translate(.45,-.1,.15) + Sphere(.05, color='black').translate(.51,-.1,.17)\n    sage: S += Sphere(.1, color='white').translate(.45, .1,.15) + Sphere(.05, color='black').translate(.51, .1,.17)\n    sage: S += Sphere(.1, color='yellow').translate(.5, 0, -.2)\n    sage: def f(x,y): return math.exp(x/5)*math.cos(y)\n    sage: P = plot3d(f,(-200,20),(-200,20), ['red','yellow'], max_depth=10)\n    sage: cape_man = P.scale(.2)+S.translate(1,0,0)\n    sage: cape_man.export_jmol('/Users/was/sage-2.9.alpha7/jmol/a.script')\n```\n",
    "created_at": "2007-12-15T01:59:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1511",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1511#issuecomment-9690",
    "user": "was"
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

archive/issue_comments_009691.json:
```json
{
    "body": "See #1516 for future work.",
    "created_at": "2007-12-15T02:19:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1511",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1511#issuecomment-9691",
    "user": "robertwb"
}
```

See #1516 for future work.



---

archive/issue_comments_009692.json:
```json
{
    "body": "Positi",
    "created_at": "2007-12-15T23:54:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1511",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1511#issuecomment-9692",
    "user": "was"
}
```

Positi



---

archive/issue_comments_009693.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2007-12-16T00:56:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1511",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1511#issuecomment-9693",
    "user": "mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_009694.json:
```json
{
    "body": "Attachment\n\nMerged in 2.9.rc2.",
    "created_at": "2007-12-16T00:56:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1511",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1511#issuecomment-9694",
    "user": "mabshoff"
}
```

Attachment

Merged in 2.9.rc2.

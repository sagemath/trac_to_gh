# Issue 1516: jmol spkg, use from notebook and command line

archive/issues_001516.json:
```json
{
    "body": "Assignee: was\n\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/1516\n\n",
    "created_at": "2007-12-15T02:18:58Z",
    "labels": [
        "graphics",
        "major",
        "enhancement"
    ],
    "title": "jmol spkg, use from notebook and command line",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/1516",
    "user": "robertwb"
}
```
Assignee: was



Issue created by migration from https://trac.sagemath.org/ticket/1516





---

archive/issue_comments_009717.json:
```json
{
    "body": "Changing assignee from was to robertwb.",
    "created_at": "2007-12-15T02:19:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1516",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1516#issuecomment-9717",
    "user": "robertwb"
}
```

Changing assignee from was to robertwb.



---

archive/issue_comments_009718.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2007-12-15T02:19:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1516",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1516#issuecomment-9718",
    "user": "robertwb"
}
```

Changing status from new to assigned.



---

archive/issue_comments_009719.json:
```json
{
    "body": "Attachment\n\nSee spkg at http://sage.math.washington.edu/home/robertwb/3d/jmol-11.2.14.spkg\n\nNote, this is 14MB, but it is just the full Jmol bundle which has about 4MB docs, 6MB source, and 3M redundant applet binaries, not all of which we may want to include. \n\nI realize the bundle has other patches from other tickets (e.g. #1533), but these are needed.",
    "created_at": "2007-12-16T10:08:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1516",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1516#issuecomment-9719",
    "user": "robertwb"
}
```

Attachment

See spkg at http://sage.math.washington.edu/home/robertwb/3d/jmol-11.2.14.spkg

Note, this is 14MB, but it is just the full Jmol bundle which has about 4MB docs, 6MB source, and 3M redundant applet binaries, not all of which we may want to include. 

I realize the bundle has other patches from other tickets (e.g. #1533), but these are needed.



---

archive/issue_comments_009720.json:
```json
{
    "body": "Examples\n\n```\nsage: from sage.plot.plot3d.all import *\nsage: S = plot3d(lambda x, y: abs(zeta(x+y*i)), (-3,3), (-3,3), ['red','blue'])\nsage: S.show(viewer='jmol')\nsage: (S + axes3d(5)).show(viewer='jmol')\n```\n",
    "created_at": "2007-12-16T10:31:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1516",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1516#issuecomment-9720",
    "user": "robertwb"
}
```

Examples

```
sage: from sage.plot.plot3d.all import *
sage: S = plot3d(lambda x, y: abs(zeta(x+y*i)), (-3,3), (-3,3), ['red','blue'])
sage: S.show(viewer='jmol')
sage: (S + axes3d(5)).show(viewer='jmol')
```




---

archive/issue_comments_009721.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-01-05T14:29:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1516",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1516#issuecomment-9721",
    "user": "mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_009722.json:
```json
{
    "body": "This was merged some time in 2.9.2.X.\n\nCheers,\n\nMichael",
    "created_at": "2008-01-05T14:29:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1516",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1516#issuecomment-9722",
    "user": "mabshoff"
}
```

This was merged some time in 2.9.2.X.

Cheers,

Michael

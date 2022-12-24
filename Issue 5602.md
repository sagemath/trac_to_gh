# Issue 5602: make .lighter() and .darker() methods for Sage Color objects

archive/issues_005602.json:
```json
{
    "body": "Assignee: was\n\nCC:  mvngu\n\nSee the end of http://groups.google.com/group/sage-support/browse_thread/thread/44971aa416574675\n\nFor reference, here is what MMA does: \n\nhttp://reference.wolfram.com/mathematica/ref/Darker.html\n\nhttp://reference.wolfram.com/mathematica/ref/Lighter.html\n\nIssue created by migration from https://trac.sagemath.org/ticket/5602\n\n",
    "created_at": "2009-03-24T21:28:09Z",
    "labels": [
        "graphics",
        "major",
        "enhancement"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.4.2",
    "title": "make .lighter() and .darker() methods for Sage Color objects",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/5602",
    "user": "jason"
}
```
Assignee: was

CC:  mvngu

See the end of http://groups.google.com/group/sage-support/browse_thread/thread/44971aa416574675

For reference, here is what MMA does: 

http://reference.wolfram.com/mathematica/ref/Darker.html

http://reference.wolfram.com/mathematica/ref/Lighter.html

Issue created by migration from https://trac.sagemath.org/ticket/5602





---

archive/issue_comments_043732.json:
```json
{
    "body": "Changing priority from major to minor.",
    "created_at": "2009-03-24T21:28:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5602",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5602#issuecomment-43732",
    "user": "jason"
}
```

Changing priority from major to minor.



---

archive/issue_comments_043733.json:
```json
{
    "body": "See the patch at #5601.",
    "created_at": "2009-11-18T04:42:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5602",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5602#issuecomment-43733",
    "user": "mpatel"
}
```

See the patch at #5601.



---

archive/issue_comments_043734.json:
```json
{
    "body": "This works now:\n\n\n```\nsage: sage.plot.colors.red.lighter()\nRGB color (1.0, 0.33333333333333331, 0.33333333333333331)\nsage: sage.plot.colors.red.darker()\nRGB color (0.66666666666666674, 0.0, 0.0)\n```\n\n\nSo this ticket should be closed.",
    "created_at": "2010-05-11T20:31:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5602",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5602#issuecomment-43734",
    "user": "jason"
}
```

This works now:


```
sage: sage.plot.colors.red.lighter()
RGB color (1.0, 0.33333333333333331, 0.33333333333333331)
sage: sage.plot.colors.red.darker()
RGB color (0.66666666666666674, 0.0, 0.0)
```


So this ticket should be closed.



---

archive/issue_comments_043735.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-05-11T20:35:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5602",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5602#issuecomment-43735",
    "user": "mvngu"
}
```

Resolution: fixed



---

archive/issue_comments_043736.json:
```json
{
    "body": "Close as fixed:\n\n\n```sh\n[mvngu@sage ~]$ sage\n----------------------------------------------------------------------\n----------------------------------------------------------------------\nsage: r = sage.plot.colors.red\nsage: r\nRGB color (1.0, 0.0, 0.0)\nsage: r.darker()\nRGB color (0.66666666666666674, 0.0, 0.0)\nsage: r.lighter()\nRGB color (1.0, 0.33333333333333331, 0.33333333333333331)\n```\n",
    "created_at": "2010-05-11T20:35:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5602",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5602#issuecomment-43736",
    "user": "mvngu"
}
```

Close as fixed:


```sh
[mvngu@sage ~]$ sage
----------------------------------------------------------------------
----------------------------------------------------------------------
sage: r = sage.plot.colors.red
sage: r
RGB color (1.0, 0.0, 0.0)
sage: r.darker()
RGB color (0.66666666666666674, 0.0, 0.0)
sage: r.lighter()
RGB color (1.0, 0.33333333333333331, 0.33333333333333331)
```


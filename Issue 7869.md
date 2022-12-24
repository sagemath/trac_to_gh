# Issue 7869: cylindrical plot

archive/issues_007869.json:
```json
{
    "body": "Assignee: was\n\nKeywords: cylindric,plot\n\nI've made a clone of Mathematicas SphericalPlot3d . Only that the 3d seemed redundant to me.\n\nThe code is\n\n```\ndef cylindrical_plot(f,phiran,zran,**kwds):\n   phi=phiran[0]\n   z=zran[0]\n   Rho=(f*cos(phi),f*sin(phi),z)\n   return parametric_plot3d(Rho,phiran,zran,**kwds) \n```\n\n\nSeveral examples can be found in [http://www.sagenb.org/home/pub/1325/](http://www.sagenb.org/home/pub/1325/)\n\nFor simplicity's sake I have not added default values for the ploting domain, that tends to produce undesired results.\n\nIssue created by migration from https://trac.sagemath.org/ticket/7869\n\n",
    "created_at": "2010-01-07T19:11:51Z",
    "labels": [
        "graphics",
        "minor",
        "enhancement"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-duplicate/invalid/wontfix",
    "title": "cylindrical plot",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/7869",
    "user": "olazo"
}
```
Assignee: was

Keywords: cylindric,plot

I've made a clone of Mathematicas SphericalPlot3d . Only that the 3d seemed redundant to me.

The code is

```
def cylindrical_plot(f,phiran,zran,**kwds):
   phi=phiran[0]
   z=zran[0]
   Rho=(f*cos(phi),f*sin(phi),z)
   return parametric_plot3d(Rho,phiran,zran,**kwds) 
```


Several examples can be found in [http://www.sagenb.org/home/pub/1325/](http://www.sagenb.org/home/pub/1325/)

For simplicity's sake I have not added default values for the ploting domain, that tends to produce undesired results.

Issue created by migration from https://trac.sagemath.org/ticket/7869





---

archive/issue_comments_068265.json:
```json
{
    "body": "Changing assignee from was to olazo.",
    "created_at": "2010-01-07T19:13:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7869",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7869#issuecomment-68265",
    "user": "olazo"
}
```

Changing assignee from was to olazo.



---

archive/issue_comments_068266.json:
```json
{
    "body": "Changing status from new to needs_work.",
    "created_at": "2010-01-08T17:55:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7869",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7869#issuecomment-68266",
    "user": "olazo"
}
```

Changing status from new to needs_work.



---

archive/issue_comments_068267.json:
```json
{
    "body": "Attachment [docstring](tarball://root/attachments/some-uuid/ticket7869/docstring) by olazo created at 2010-01-17 21:09:34\n\na proposal for a docstring",
    "created_at": "2010-01-17T21:09:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7869",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7869#issuecomment-68267",
    "user": "olazo"
}
```

Attachment [docstring](tarball://root/attachments/some-uuid/ticket7869/docstring) by olazo created at 2010-01-17 21:09:34

a proposal for a docstring



---

archive/issue_comments_068268.json:
```json
{
    "body": "some corrections made",
    "created_at": "2010-01-17T21:23:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7869",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7869#issuecomment-68268",
    "user": "olazo"
}
```

some corrections made



---

archive/issue_comments_068269.json:
```json
{
    "body": "Attachment [docstring.2](tarball://root/attachments/some-uuid/ticket7869/docstring.2) by olazo created at 2010-01-24 19:36:29",
    "created_at": "2010-01-24T19:36:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7869",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7869#issuecomment-68269",
    "user": "olazo"
}
```

Attachment [docstring.2](tarball://root/attachments/some-uuid/ticket7869/docstring.2) by olazo created at 2010-01-24 19:36:29



---

archive/issue_comments_068270.json:
```json
{
    "body": "Resolution: invalid",
    "created_at": "2010-01-24T19:36:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7869",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7869#issuecomment-68270",
    "user": "olazo"
}
```

Resolution: invalid

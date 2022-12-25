# Issue 7869: cylindrical plot

archive/issues_007869.json:
```json
{
    "body": "Assignee: @williamstein\n\nKeywords: cylindric,plot\n\nI've made a clone of Mathematicas SphericalPlot3d . Only that the 3d seemed redundant to me.\n\nThe code is\n\n```\ndef cylindrical_plot(f,phiran,zran,**kwds):\n   phi=phiran[0]\n   z=zran[0]\n   Rho=(f*cos(phi),f*sin(phi),z)\n   return parametric_plot3d(Rho,phiran,zran,**kwds) \n```\n\nSeveral examples can be found in [http://www.sagenb.org/home/pub/1325/](http://www.sagenb.org/home/pub/1325/)\n\nFor simplicity's sake I have not added default values for the ploting domain, that tends to produce undesired results.\n\nIssue created by migration from https://trac.sagemath.org/ticket/7869\n\n",
    "created_at": "2010-01-07T19:11:51Z",
    "labels": [
        "component: graphics",
        "minor"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-duplicate/invalid/wontfix",
    "title": "cylindrical plot",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/7869",
    "user": "https://trac.sagemath.org/admin/accounts/users/olazo"
}
```
Assignee: @williamstein

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

archive/issue_comments_068148.json:
```json
{
    "body": "Changing assignee from @williamstein to olazo.",
    "created_at": "2010-01-07T19:13:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7869",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7869#issuecomment-68148",
    "user": "https://trac.sagemath.org/admin/accounts/users/olazo"
}
```

Changing assignee from @williamstein to olazo.



---

archive/issue_comments_068149.json:
```json
{
    "body": "Changing status from new to needs_work.",
    "created_at": "2010-01-08T17:55:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7869",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7869#issuecomment-68149",
    "user": "https://trac.sagemath.org/admin/accounts/users/olazo"
}
```

Changing status from new to needs_work.



---

archive/issue_comments_068150.json:
```json
{
    "body": "Attachment [docstring](tarball://root/attachments/some-uuid/ticket7869/docstring) by olazo created at 2010-01-17 21:09:34\n\na proposal for a docstring",
    "created_at": "2010-01-17T21:09:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7869",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7869#issuecomment-68150",
    "user": "https://trac.sagemath.org/admin/accounts/users/olazo"
}
```

Attachment [docstring](tarball://root/attachments/some-uuid/ticket7869/docstring) by olazo created at 2010-01-17 21:09:34

a proposal for a docstring



---

archive/issue_comments_068151.json:
```json
{
    "body": "some corrections made",
    "created_at": "2010-01-17T21:23:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7869",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7869#issuecomment-68151",
    "user": "https://trac.sagemath.org/admin/accounts/users/olazo"
}
```

some corrections made



---

archive/issue_comments_068152.json:
```json
{
    "body": "Attachment [docstring.2](tarball://root/attachments/some-uuid/ticket7869/docstring.2) by olazo created at 2010-01-24 19:36:29",
    "created_at": "2010-01-24T19:36:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7869",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7869#issuecomment-68152",
    "user": "https://trac.sagemath.org/admin/accounts/users/olazo"
}
```

Attachment [docstring.2](tarball://root/attachments/some-uuid/ticket7869/docstring.2) by olazo created at 2010-01-24 19:36:29



---

archive/issue_comments_068153.json:
```json
{
    "body": "Resolution: invalid",
    "created_at": "2010-01-24T19:36:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7869",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7869#issuecomment-68153",
    "user": "https://trac.sagemath.org/admin/accounts/users/olazo"
}
```

Resolution: invalid



---

archive/issue_events_018820.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/olazo",
    "created_at": "2010-01-24T19:36:29Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/7869",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/7869#event-18820"
}
```



---

archive/issue_events_018821.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mvngu",
    "created_at": "2010-01-26T00:16:59Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/7869",
    "milestone": "sage-duplicate/invalid/wontfix",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/7869#event-18821"
}
```

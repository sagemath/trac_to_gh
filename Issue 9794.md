# Issue 9794: Make sure new plot syntax works with Sage polynomials

archive/issues_009794.json:
```json
{
    "body": "Assignee: jason, was\n\nCC:  @jasongrout\n\n\n```\npts = [(1,2),(2,3),(3,2),(4,3),(5,2),(6,3)] \nR.<x>=QQ[] \nf = R.lagrange_polynomial(pts) \nSR(f) \n2. If one has a non-symbolic polynomial currently, it won't plot with \nthe new plotting syntax. \nplot(f,0,5) # works, old-school Sage \nplot(f,(x,0,5)) # doesn't work, new-school Sage \nplot(f,x,0,5) # doesn't work, though sort of makes sense it shouldn't \nsince x isn't a symbolic variable now... ? \n```\n\nObviously any polynomial f is what is at issue, not just this particular one.\n\nIssue created by migration from https://trac.sagemath.org/ticket/9795\n\n",
    "created_at": "2010-08-24T15:19:24Z",
    "labels": [
        "component: graphics",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-6.4",
    "title": "Make sure new plot syntax works with Sage polynomials",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/9794",
    "user": "https://github.com/kcrisman"
}
```
Assignee: jason, was

CC:  @jasongrout


```
pts = [(1,2),(2,3),(3,2),(4,3),(5,2),(6,3)] 
R.<x>=QQ[] 
f = R.lagrange_polynomial(pts) 
SR(f) 
2. If one has a non-symbolic polynomial currently, it won't plot with 
the new plotting syntax. 
plot(f,0,5) # works, old-school Sage 
plot(f,(x,0,5)) # doesn't work, new-school Sage 
plot(f,x,0,5) # doesn't work, though sort of makes sense it shouldn't 
since x isn't a symbolic variable now... ? 
```

Obviously any polynomial f is what is at issue, not just this particular one.

Issue created by migration from https://trac.sagemath.org/ticket/9795





---

archive/issue_comments_096007.json:
```json
{
    "body": "This would be good to work too, if we can fix the above.\n\n```\npts = [(1,2)] \nR.<x>=QQ[] \nf = R.lagrange_polynomial(pts) \nf.plot(0,7) \n<boom because integers have no .plot() method>\n```\n",
    "created_at": "2010-08-24T15:20:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9794",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9794#issuecomment-96007",
    "user": "https://github.com/kcrisman"
}
```

This would be good to work too, if we can fix the above.

```
pts = [(1,2)] 
R.<x>=QQ[] 
f = R.lagrange_polynomial(pts) 
f.plot(0,7) 
<boom because integers have no .plot() method>
```




---

archive/issue_events_024575.json:
```json
{
    "actor": "https://github.com/jdemeyer",
    "created_at": "2013-08-13T15:35:53Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/9794",
    "milestone": "sage-5.12",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/9794#event-24575"
}
```



---

archive/issue_events_024576.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-01-30T21:20:52Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/9794",
    "milestone": "sage-5.12",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/9794#event-24576"
}
```



---

archive/issue_events_024577.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-01-30T21:20:52Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/9794",
    "milestone": "sage-6.2",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/9794#event-24577"
}
```



---

archive/issue_events_024578.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-05-06T15:20:58Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/9794",
    "milestone": "sage-6.2",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/9794#event-24578"
}
```



---

archive/issue_events_024579.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-05-06T15:20:58Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/9794",
    "milestone": "sage-6.3",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/9794#event-24579"
}
```



---

archive/issue_events_024580.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-08-10T16:51:03Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/9794",
    "milestone": "sage-6.3",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/9794#event-24580"
}
```



---

archive/issue_events_024581.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-08-10T16:51:03Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/9794",
    "milestone": "sage-6.4",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/9794#event-24581"
}
```

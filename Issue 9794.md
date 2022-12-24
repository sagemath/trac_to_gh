# Issue 9794: Make sure new plot syntax works with Sage polynomials

archive/issues_009794.json:
```json
{
    "body": "Assignee: jason, was\n\nCC:  jason\n\n\n```\npts = [(1,2),(2,3),(3,2),(4,3),(5,2),(6,3)] \nR.<x>=QQ[] \nf = R.lagrange_polynomial(pts) \nSR(f) \n2. If one has a non-symbolic polynomial currently, it won't plot with \nthe new plotting syntax. \nplot(f,0,5) # works, old-school Sage \nplot(f,(x,0,5)) # doesn't work, new-school Sage \nplot(f,x,0,5) # doesn't work, though sort of makes sense it shouldn't \nsince x isn't a symbolic variable now... ? \n```\n\nObviously any polynomial f is what is at issue, not just this particular one.\n\nIssue created by migration from https://trac.sagemath.org/ticket/9795\n\n",
    "created_at": "2010-08-24T15:19:24Z",
    "labels": [
        "graphics",
        "major",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-6.4",
    "title": "Make sure new plot syntax works with Sage polynomials",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/9794",
    "user": "kcrisman"
}
```
Assignee: jason, was

CC:  jason


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

archive/issue_comments_096166.json:
```json
{
    "body": "This would be good to work too, if we can fix the above.\n\n```\npts = [(1,2)] \nR.<x>=QQ[] \nf = R.lagrange_polynomial(pts) \nf.plot(0,7) \n<boom because integers have no .plot() method>\n```\n",
    "created_at": "2010-08-24T15:20:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9794",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9794#issuecomment-96166",
    "user": "kcrisman"
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


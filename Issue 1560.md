# Issue 1560: Bug in introspection: line3d?? results in lame output

archive/issues_001560.json:
```json
{
    "body": "Assignee: tba\n\n\n```\nsage: line3d??\narg is not a module, class, method, function, traceback, frame, or code object\nSource code for <sage.plot.plot3dmatplotlib.Line3dFactory instance at 0x1505c10> not available.\n```\n\n\nThat isn't right. \n\nIssue created by migration from https://trac.sagemath.org/ticket/1560\n\n",
    "created_at": "2007-12-18T16:53:08Z",
    "labels": [
        "documentation",
        "major",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-2.10.1",
    "title": "Bug in introspection: line3d?? results in lame output",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/1560",
    "user": "@williamstein"
}
```
Assignee: tba


```
sage: line3d??
arg is not a module, class, method, function, traceback, frame, or code object
Source code for <sage.plot.plot3dmatplotlib.Line3dFactory instance at 0x1505c10> not available.
```


That isn't right. 

Issue created by migration from https://trac.sagemath.org/ticket/1560





---

archive/issue_comments_009940.json:
```json
{
    "body": "Resolution: worksforme",
    "created_at": "2008-01-19T22:14:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1560",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1560#issuecomment-9940",
    "user": "@ncalexan"
}
```

Resolution: worksforme

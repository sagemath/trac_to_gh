# Issue 1515: ParametricSurface bug

archive/issues_001515.json:
```json
{
    "body": "Assignee: @williamstein\n\n\n```\ndef f(x,y): return cos(x)*sin(y), sin(x)*sin(y), cos(y)+log(tan(y/2))+0.2*x\nshow(ParametricSurface(f, (srange(0,12.4,0.1), srange(0.1,2,0.1))))\n```\n\ndoesn't render. Also\n\n\n```\n[08:48am] williamstein: This should work but doesn't:\n[08:48am] williamstein: S = ParametricSurface(lambda (x,y):(cos(x),\nsin(x), y), domain=(range(10),range(10)))\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/1515\n\n",
    "created_at": "2007-12-15T01:59:55Z",
    "labels": [
        "component: graphics",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-2.9",
    "title": "ParametricSurface bug",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/1515",
    "user": "https://github.com/robertwb"
}
```
Assignee: @williamstein


```
def f(x,y): return cos(x)*sin(y), sin(x)*sin(y), cos(y)+log(tan(y/2))+0.2*x
show(ParametricSurface(f, (srange(0,12.4,0.1), srange(0.1,2,0.1))))
```

doesn't render. Also


```
[08:48am] williamstein: This should work but doesn't:
[08:48am] williamstein: S = ParametricSurface(lambda (x,y):(cos(x),
sin(x), y), domain=(range(10),range(10)))
```


Issue created by migration from https://trac.sagemath.org/ticket/1515





---

archive/issue_comments_009686.json:
```json
{
    "body": "Attachment [parametric-surface.diff](tarball://root/attachments/some-uuid/ticket1515/parametric-surface.diff) by @robertwb created at 2007-12-15 02:02:07",
    "created_at": "2007-12-15T02:02:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1515",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1515#issuecomment-9686",
    "user": "https://github.com/robertwb"
}
```

Attachment [parametric-surface.diff](tarball://root/attachments/some-uuid/ticket1515/parametric-surface.diff) by @robertwb created at 2007-12-15 02:02:07



---

archive/issue_comments_009687.json:
```json
{
    "body": "Now the first example works. Also, the second example almost does\n\n\n```\nS = ParametricSurface(lambda x,y:(cos(x),sin(x), y), domain=(range(10),range(10)))\n```\n\n\n(Note the missing ()'s, it expects to arguments, not a tuple).",
    "created_at": "2007-12-15T02:04:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1515",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1515#issuecomment-9687",
    "user": "https://github.com/robertwb"
}
```

Now the first example works. Also, the second example almost does


```
S = ParametricSurface(lambda x,y:(cos(x),sin(x), y), domain=(range(10),range(10)))
```


(Note the missing ()'s, it expects to arguments, not a tuple).



---

archive/issue_comments_009688.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2007-12-15T02:04:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1515",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1515#issuecomment-9688",
    "user": "https://github.com/robertwb"
}
```

Changing status from new to assigned.



---

archive/issue_comments_009689.json:
```json
{
    "body": "Changing assignee from @williamstein to @robertwb.",
    "created_at": "2007-12-15T02:04:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1515",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1515#issuecomment-9689",
    "user": "https://github.com/robertwb"
}
```

Changing assignee from @williamstein to @robertwb.



---

archive/issue_comments_009690.json:
```json
{
    "body": "Merged in 2.9.rc0.",
    "created_at": "2007-12-15T14:03:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1515",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1515#issuecomment-9690",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged in 2.9.rc0.



---

archive/issue_comments_009691.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2007-12-15T14:03:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1515",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1515#issuecomment-9691",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed



---

archive/issue_events_003830.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2007-12-15T14:03:19Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/1515",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/1515#event-3830"
}
```

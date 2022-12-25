# Issue 1068: turn off inplace optimizations

archive/issues_001068.json:
```json
{
    "body": "Assignee: mabshoff\n\n\n```\n> The inplace optimizations should be something that have to be\n> > explicitly turned on, and they should be off by default.  I know they\n> > make certain things faster, but correctness by default is *always* a\n> > much more important consideration with serious mathematical software\n> > such as Sage.  Always.\n> >\n> > I will very likely disable in-place optimization for sage-2.8.11,\n> > until this issue gets properly discussed and resolved.\n\n:-(, but I have to concede to your logic. The line to change is 148  \nof coerce.pxi. Setting this value to 0 will turn them completely off.  \nOther than numpy, (and the builtin libraries), do we use any other  \nextension types? If there is a finite list of things for which it  \nwon't work, it would be possible to disable it just for those.\n\n- Robert\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/1068\n\n",
    "created_at": "2007-11-02T19:04:12Z",
    "labels": [
        "component: packages: standard",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-duplicate/invalid/wontfix",
    "title": "turn off inplace optimizations",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/1068",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```
Assignee: mabshoff


```
> The inplace optimizations should be something that have to be
> > explicitly turned on, and they should be off by default.  I know they
> > make certain things faster, but correctness by default is *always* a
> > much more important consideration with serious mathematical software
> > such as Sage.  Always.
> >
> > I will very likely disable in-place optimization for sage-2.8.11,
> > until this issue gets properly discussed and resolved.

:-(, but I have to concede to your logic. The line to change is 148  
of coerce.pxi. Setting this value to 0 will turn them completely off.  
Other than numpy, (and the builtin libraries), do we use any other  
extension types? If there is a finite list of things for which it  
won't work, it would be possible to disable it just for those.

- Robert
```


Issue created by migration from https://trac.sagemath.org/ticket/1068





---

archive/issue_comments_006454.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2007-11-02T19:04:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1068",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1068#issuecomment-6454",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Changing status from new to assigned.



---

archive/issue_comments_006455.json:
```json
{
    "body": "Resolution: duplicate",
    "created_at": "2007-11-02T19:20:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1068",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1068#issuecomment-6455",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: duplicate



---

archive/issue_events_001190.json:
```json
{
    "actor": "mabshoff",
    "created_at": "2007-11-02T19:20:12Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/1068",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/1068#event-1190"
}
```



---

archive/issue_comments_006456.json:
```json
{
    "body": "Oops, dupe of #1018.\n\nCheers,\n\nMichael",
    "created_at": "2007-11-02T19:20:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1068",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1068#issuecomment-6456",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Oops, dupe of #1018.

Cheers,

Michael



---

archive/issue_comments_006457.json:
```json
{
    "body": "Nope, dupe of #1038!",
    "created_at": "2007-11-02T19:20:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1068",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1068#issuecomment-6457",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Nope, dupe of #1038!

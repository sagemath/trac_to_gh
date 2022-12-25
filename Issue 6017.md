# Issue 6017: Provide methods for graphs to set options for latex printing

archive/issues_006017.json:
```json
{
    "body": "Assignee: @rbeezer\n\nCC:  fidelbarrera\n\nUsing the tkz-graph package in latex allows for a variety of customizations in the output.  So methods will allow a graph to set and carry options that can be used by the latex() method.\n\n1.  make set_latex_option(), get_latex_option(), clear_latex_option()  as new methods for a graph\n\n2.  Add a dictionary to a graph that contains the values of these options.\n\n3.  So the latex() method can query the dictionary and act accordingly.\n\nSee #5975\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/6017\n\n",
    "created_at": "2009-05-11T04:34:50Z",
    "labels": [
        "component: graph theory",
        "minor"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.0.2",
    "title": "Provide methods for graphs to set options for latex printing",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/6017",
    "user": "https://github.com/rbeezer"
}
```
Assignee: @rbeezer

CC:  fidelbarrera

Using the tkz-graph package in latex allows for a variety of customizations in the output.  So methods will allow a graph to set and carry options that can be used by the latex() method.

1.  make set_latex_option(), get_latex_option(), clear_latex_option()  as new methods for a graph

2.  Add a dictionary to a graph that contains the values of these options.

3.  So the latex() method can query the dictionary and act accordingly.

See #5975


Issue created by migration from https://trac.sagemath.org/ticket/6017





---

archive/issue_comments_047783.json:
```json
{
    "body": "The proposed changes have been incorporated into #5975, so this is obsolete.",
    "created_at": "2009-05-20T15:30:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6017",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6017#issuecomment-47783",
    "user": "https://github.com/rbeezer"
}
```

The proposed changes have been incorporated into #5975, so this is obsolete.



---

archive/issue_comments_047784.json:
```json
{
    "body": "No, this is not obsolete and this is not how we do things around here ;).\n\nComment on the other ticket that it also fixes this ticket. Then both of them will be closed and credited when the other ticket has been merged.\n\nCheers,\n\nMichael",
    "created_at": "2009-05-20T16:49:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6017",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6017#issuecomment-47784",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

No, this is not obsolete and this is not how we do things around here ;).

Comment on the other ticket that it also fixes this ticket. Then both of them will be closed and credited when the other ticket has been merged.

Cheers,

Michael



---

archive/issue_comments_047785.json:
```json
{
    "body": "Replying to [comment:2 mabshoff]:\n> No, this is not obsolete and this is not how we do things around here ;).\n\nUnderstood.  It was a severely flawed attempt to save you some work.  ;-)",
    "created_at": "2009-05-20T17:57:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6017",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6017#issuecomment-47785",
    "user": "https://github.com/rbeezer"
}
```

Replying to [comment:2 mabshoff]:
> No, this is not obsolete and this is not how we do things around here ;).

Understood.  It was a severely flawed attempt to save you some work.  ;-)



---

archive/issue_comments_047786.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-06-13T23:29:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6017",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6017#issuecomment-47786",
    "user": "https://github.com/ncalexan"
}
```

Resolution: fixed



---

archive/issue_events_006272.json:
```json
{
    "actor": "@ncalexan",
    "created_at": "2009-06-13T23:29:07Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/6017",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/6017#event-6272"
}
```



---

archive/issue_comments_047787.json:
```json
{
    "body": "This is addressed in #5975, merged in 4.0.2.alpha0.",
    "created_at": "2009-06-13T23:29:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6017",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6017#issuecomment-47787",
    "user": "https://github.com/ncalexan"
}
```

This is addressed in #5975, merged in 4.0.2.alpha0.

# Issue 4323: sage-coverage expects doctests for closures

archive/issues_004323.json:
```json
{
    "body": "Assignee: tbd\n\nCC:  @zimmermann6\n\nUnfortunately, there is often no way to doctest such functions directly, and for some re-writing them as lambda functions is impossible or reduces readability. \n\nIssue created by migration from https://trac.sagemath.org/ticket/4323\n\n",
    "created_at": "2008-10-19T05:41:59Z",
    "labels": [
        "component: algebra",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-duplicate/invalid/wontfix",
    "title": "sage-coverage expects doctests for closures",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/4323",
    "user": "https://github.com/robertwb"
}
```
Assignee: tbd

CC:  @zimmermann6

Unfortunately, there is often no way to doctest such functions directly, and for some re-writing them as lambda functions is impossible or reduces readability. 

Issue created by migration from https://trac.sagemath.org/ticket/4323





---

archive/issue_comments_031611.json:
```json
{
    "body": "Changing assignee from tbd to mabshoff.",
    "created_at": "2008-10-19T05:42:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4323",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4323#issuecomment-31611",
    "user": "https://github.com/robertwb"
}
```

Changing assignee from tbd to mabshoff.



---

archive/issue_comments_031612.json:
```json
{
    "body": "Changing component from algebra to doctest.",
    "created_at": "2008-10-19T05:42:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4323",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4323#issuecomment-31612",
    "user": "https://github.com/robertwb"
}
```

Changing component from algebra to doctest.



---

archive/issue_comments_031613.json:
```json
{
    "body": "Is this the same as #877?\n\n  John (who's not quite sure what \"closures\" are)\n\nP.S. By the way, I think it takes a certain amount of hubris to write a program like 'sage-coverage' which itself has no doctests or documentation :)",
    "created_at": "2009-02-09T23:45:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4323",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4323#issuecomment-31613",
    "user": "https://github.com/jhpalmieri"
}
```

Is this the same as #877?

  John (who's not quite sure what "closures" are)

P.S. By the way, I think it takes a certain amount of hubris to write a program like 'sage-coverage' which itself has no doctests or documentation :)



---

archive/issue_comments_031614.json:
```json
{
    "body": "Replying to [comment:4 jhpalmieri]:\n> Is this the same as #877?\n> \n>   John (who's not quite sure what \"closures\" are)\n\nNot sure.\n\n> P.S. By the way, I think it takes a certain amount of hubris to write a program like 'sage-coverage' which itself has no doctests or documentation :)\n\nYes, this certainly registered rather strongly on my irony meter, but right now there is no coverage for the scripts in local/bin, even though most people agreed that it would be a pretty good idea. This will hopefully happen sooner or later.\n\nCheers,\n\nMichael",
    "created_at": "2009-02-09T23:47:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4323",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4323#issuecomment-31614",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Replying to [comment:4 jhpalmieri]:
> Is this the same as #877?
> 
>   John (who's not quite sure what "closures" are)

Not sure.

> P.S. By the way, I think it takes a certain amount of hubris to write a program like 'sage-coverage' which itself has no doctests or documentation :)

Yes, this certainly registered rather strongly on my irony meter, but right now there is no coverage for the scripts in local/bin, even though most people agreed that it would be a pretty good idea. This will hopefully happen sooner or later.

Cheers,

Michael



---

archive/issue_comments_031615.json:
```json
{
    "body": "> Is this the same as #877?\n\nyes.",
    "created_at": "2009-02-10T07:16:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4323",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4323#issuecomment-31615",
    "user": "https://github.com/zimmermann6"
}
```

> Is this the same as #877?

yes.



---

archive/issue_comments_031616.json:
```json
{
    "body": "Resolution: duplicate",
    "created_at": "2009-02-10T07:19:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4323",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4323#issuecomment-31616",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: duplicate



---

archive/issue_comments_031617.json:
```json
{
    "body": "Since this is a dupe of #877 I am closing this ticket as a dupe. \n\nIf someone disagrees please reopen.\n\nCheers,\n\nMichael",
    "created_at": "2009-02-10T07:19:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4323",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4323#issuecomment-31617",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Since this is a dupe of #877 I am closing this ticket as a dupe. 

If someone disagrees please reopen.

Cheers,

Michael



---

archive/issue_events_004568.json:
```json
{
    "actor": "mabshoff",
    "created_at": "2009-02-10T07:19:08Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/4323",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/4323#event-4568"
}
```

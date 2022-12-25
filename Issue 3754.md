# Issue 3754: Would it be possible to add some functionality to sage.rings.number_field.galois_group.GaloisGroup?

archive/issues_003754.json:
```json
{
    "body": "Assignee: joyner\n\nIf K is a number field, then K.galois_group() gives a group with very little functionality. One can get an abstract group with more functionality by calling K.galois_group().group(), but it would be nice to be able to access the functionality of the group type without having to forget the metadata attached to the Galois group (its number field, etc). Would this be difficult?\n\nIssue created by migration from https://trac.sagemath.org/ticket/3754\n\n",
    "created_at": "2008-08-01T15:46:41Z",
    "labels": [
        "component: group theory",
        "minor",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-duplicate/invalid/wontfix",
    "title": "Would it be possible to add some functionality to sage.rings.number_field.galois_group.GaloisGroup?",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/3754",
    "user": "https://trac.sagemath.org/admin/accounts/users/ljpk"
}
```
Assignee: joyner

If K is a number field, then K.galois_group() gives a group with very little functionality. One can get an abstract group with more functionality by calling K.galois_group().group(), but it would be nice to be able to access the functionality of the group type without having to forget the metadata attached to the Galois group (its number field, etc). Would this be difficult?

Issue created by migration from https://trac.sagemath.org/ticket/3754





---

archive/issue_comments_026615.json:
```json
{
    "body": "This is not something that should be a ticket in trac since it is too undefined. The summary does not accurately describe a solvable ticket, so something like this should go to sage-devel before opening a ticket.\n\nI am tempted to invalidate this ticket. William?\n\nCheers,\n\nMichael",
    "created_at": "2008-08-02T00:23:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3754",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3754#issuecomment-26615",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

This is not something that should be a ticket in trac since it is too undefined. The summary does not accurately describe a solvable ticket, so something like this should go to sage-devel before opening a ticket.

I am tempted to invalidate this ticket. William?

Cheers,

Michael



---

archive/issue_comments_026616.json:
```json
{
    "body": "My work at #5159 hopefully provides something a bit closer to what Lloyd was after. In any case it invalidates his description above :-) Shall we close this one now?",
    "created_at": "2009-05-11T19:28:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3754",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3754#issuecomment-26616",
    "user": "https://github.com/loefflerd"
}
```

My work at #5159 hopefully provides something a bit closer to what Lloyd was after. In any case it invalidates his description above :-) Shall we close this one now?



---

archive/issue_events_003976.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2009-05-12T01:39:45Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/3754",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/3754#event-3976"
}
```



---

archive/issue_comments_026617.json:
```json
{
    "body": "Resolution: duplicate",
    "created_at": "2009-05-12T01:39:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3754",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3754#issuecomment-26617",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: duplicate



---

archive/issue_comments_026618.json:
```json
{
    "body": "Fixed via #5159. Any sort of feature request should go to sage-devel or sage-nt anyway since the visibility of tickets tends to be quite low.\n\nThanks David for following up :)\n\nCheers,\n\nMichael",
    "created_at": "2009-05-12T01:39:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3754",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3754#issuecomment-26618",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Fixed via #5159. Any sort of feature request should go to sage-devel or sage-nt anyway since the visibility of tickets tends to be quite low.

Thanks David for following up :)

Cheers,

Michael

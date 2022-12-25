# Issue 6360: [with spkg, needs review] Change -O2 to -O0 in singular spkg

archive/issues_006360.json:
```json
{
    "body": "Assignee: mabshoff\n\nCC:  @malb wstein\n\nCurrently, singular seems to segfault on some architecture/OS combinations, such as SuSE and ia64. (See #6240 for more details.) The spkg available at `/scratch/craigcitro/patches/singular-3-1-0-2-20090618.spkg` on `sage.math` changes `-O2` to `-O0` to fix this problem until we can get to the root of it (i.e. until we fix #6240). \n\nIssue created by migration from https://trac.sagemath.org/ticket/6360\n\n",
    "created_at": "2009-06-19T04:37:01Z",
    "labels": [
        "component: packages: standard",
        "blocker",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.0.2",
    "title": "[with spkg, needs review] Change -O2 to -O0 in singular spkg",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/6360",
    "user": "https://github.com/craigcitro"
}
```
Assignee: mabshoff

CC:  @malb wstein

Currently, singular seems to segfault on some architecture/OS combinations, such as SuSE and ia64. (See #6240 for more details.) The spkg available at `/scratch/craigcitro/patches/singular-3-1-0-2-20090618.spkg` on `sage.math` changes `-O2` to `-O0` to fix this problem until we can get to the root of it (i.e. until we fix #6240). 

Issue created by migration from https://trac.sagemath.org/ticket/6360





---

archive/issue_comments_050773.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-06-19T06:51:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6360",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6360#issuecomment-50773",
    "user": "https://github.com/craigcitro"
}
```

Resolution: fixed



---

archive/issue_events_006610.json:
```json
{
    "actor": "@craigcitro",
    "created_at": "2009-06-19T06:51:35Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/6360",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/6360#event-6610"
}
```



---

archive/issue_comments_050774.json:
```json
{
    "body": "Merged in final 4.0.2.",
    "created_at": "2009-06-19T06:51:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6360",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6360#issuecomment-50774",
    "user": "https://github.com/craigcitro"
}
```

Merged in final 4.0.2.



---

archive/issue_comments_050775.json:
```json
{
    "body": "Sorry for jumping in so late. I guess what the ticket is supposed to do is to switch to `-O0` on Itanium **only**, right?",
    "created_at": "2009-06-19T10:26:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6360",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6360#issuecomment-50775",
    "user": "https://github.com/malb"
}
```

Sorry for jumping in so late. I guess what the ticket is supposed to do is to switch to `-O0` on Itanium **only**, right?



---

archive/issue_comments_050776.json:
```json
{
    "body": "Replying to [comment:4 malb]:\n> Sorry for jumping in so late. I guess what the ticket is supposed to do is to switch to `-O0` on Itanium **only**, right?\n\nCorrect.",
    "created_at": "2009-06-19T16:06:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6360",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6360#issuecomment-50776",
    "user": "https://github.com/ncalexan"
}
```

Replying to [comment:4 malb]:
> Sorry for jumping in so late. I guess what the ticket is supposed to do is to switch to `-O0` on Itanium **only**, right?

Correct.

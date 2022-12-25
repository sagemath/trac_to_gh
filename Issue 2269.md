# Issue 2269: Many classes abuse has_coerce_map

archive/issues_002269.json:
```json
{
    "body": "Assignee: @robertwb\n\nMany classes pass has_coerce_map_from a self value that is not a Parent (when has_coerce_map_from is a member function of Parent), or pass it a value of self that does not have _has_coerce_map_from initialized (this is used for caching).  The initialization problem is almost certainly related to classes not correctly initializing Parent (as described in the TODO in init).  However the values of self that are not Parents are more mysterious.  The doctest failures caused by this can be easily recreated by adding a \"return false\" to the if statement described in enhancement 2268. \n\nIssue created by migration from https://trac.sagemath.org/ticket/2269\n\n",
    "closed_at": "2008-10-30T08:37:04Z",
    "created_at": "2008-02-22T22:30:31Z",
    "labels": [
        "component: coercion",
        "minor",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-duplicate/invalid/wontfix",
    "title": "Many classes abuse has_coerce_map",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/2269",
    "user": "https://github.com/garyfurnish"
}
```
Assignee: @robertwb

Many classes pass has_coerce_map_from a self value that is not a Parent (when has_coerce_map_from is a member function of Parent), or pass it a value of self that does not have _has_coerce_map_from initialized (this is used for caching).  The initialization problem is almost certainly related to classes not correctly initializing Parent (as described in the TODO in init).  However the values of self that are not Parents are more mysterious.  The doctest failures caused by this can be easily recreated by adding a "return false" to the if statement described in enhancement 2268. 

Issue created by migration from https://trac.sagemath.org/ticket/2269





---

archive/issue_events_005369.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2008-02-22T22:31:43Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/2269",
    "milestone": "sage-2.10.3",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/2269#event-5369"
}
```



---

archive/issue_comments_015006.json:
```json
{
    "body": "I believe this can be marked as invalid given the new coercion model.",
    "created_at": "2008-10-30T08:31:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2269",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2269#issuecomment-15006",
    "user": "https://github.com/robertwb"
}
```

I believe this can be marked as invalid given the new coercion model.



---

archive/issue_events_005370.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2008-10-30T08:37:04Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/2269",
    "milestone": "sage-2.10.3",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/2269#event-5370"
}
```



---

archive/issue_events_005371.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2008-10-30T08:37:04Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/2269",
    "milestone": "sage-duplicate/invalid/wontfix",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/2269#event-5371"
}
```



---

archive/issue_comments_015007.json:
```json
{
    "body": "Resolution: invalid",
    "created_at": "2008-10-30T08:37:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2269",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2269#issuecomment-15007",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: invalid



---

archive/issue_events_005372.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2008-10-30T08:37:04Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/2269",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/2269#event-5372"
}
```



---

archive/issue_comments_015008.json:
```json
{
    "body": "Replying to [comment:2 robertwb]:\n> I believe this can be marked as invalid given the new coercion model. \n\n\nRobertWB's wish is my command. Invalid.\n\nCheers,\n\nMichael",
    "created_at": "2008-10-30T08:37:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2269",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2269#issuecomment-15008",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Replying to [comment:2 robertwb]:
> I believe this can be marked as invalid given the new coercion model. 


RobertWB's wish is my command. Invalid.

Cheers,

Michael

# Issue 5449: [with patch, positive review] Implements a variant of @cached_method with cache stored in the parent

archive/issues_005449.json:
```json
{
    "body": "Assignee: @nthiery\n\nCC:  sage-combinat\n\nKeywords: cached_method, cache\n\nWhen the elements of a parent do not have unique representation, it\ncan be desirable to store the cache of (some of) the methods in the\nparent rather than in the element.\n\nThis patches implements a variant `@`cached_in_parent_method of the\ndecorator `@`cached_method which does just this.\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/5449\n\n",
    "closed_at": "2009-05-22T13:57:14Z",
    "created_at": "2009-03-06T15:57:38Z",
    "labels": [
        "component: misc",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.0",
    "title": "[with patch, positive review] Implements a variant of @cached_method with cache stored in the parent",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/5449",
    "user": "https://github.com/nthiery"
}
```
Assignee: @nthiery

CC:  sage-combinat

Keywords: cached_method, cache

When the elements of a parent do not have unique representation, it
can be desirable to store the cache of (some of) the methods in the
parent rather than in the element.

This patches implements a variant `@`cached_in_parent_method of the
decorator `@`cached_method which does just this.


Issue created by migration from https://trac.sagemath.org/ticket/5449





---

archive/issue_comments_042106.json:
```json
{
    "body": "Changing keywords from \"\" to \"cached_method, cache\".",
    "created_at": "2009-05-02T00:41:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5449",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5449#issuecomment-42106",
    "user": "https://github.com/nthiery"
}
```

Changing keywords from "" to "cached_method, cache".



---

archive/issue_comments_042107.json:
```json
{
    "body": "Attachment [cached_in_parent_method-5449-submitted.patch](tarball://root/attachments/some-uuid/ticket5449/cached_in_parent_method-5449-submitted.patch) by @nthiery created at 2009-05-02 00:41:31",
    "created_at": "2009-05-02T00:41:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5449",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5449#issuecomment-42107",
    "user": "https://github.com/nthiery"
}
```

Attachment [cached_in_parent_method-5449-submitted.patch](tarball://root/attachments/some-uuid/ticket5449/cached_in_parent_method-5449-submitted.patch) by @nthiery created at 2009-05-02 00:41:31



---

archive/issue_events_012727.json:
```json
{
    "actor": "https://github.com/nthiery",
    "created_at": "2009-05-02T00:41:31Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/5449",
    "milestone": "sage-4.0",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/5449#event-12727"
}
```



---

archive/issue_comments_042108.json:
```json
{
    "body": "Passes doctests, good documentation.",
    "created_at": "2009-05-12T13:38:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5449",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5449#issuecomment-42108",
    "user": "https://github.com/roed314"
}
```

Passes doctests, good documentation.



---

archive/issue_comments_042109.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2009-05-19T06:24:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5449",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5449#issuecomment-42109",
    "user": "https://github.com/nthiery"
}
```

Changing status from new to assigned.



---

archive/issue_comments_042110.json:
```json
{
    "body": "Merged in Sage 4.0.rc1.\n\nCheers,\n\nMichael",
    "created_at": "2009-05-22T13:57:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5449",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5449#issuecomment-42110",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged in Sage 4.0.rc1.

Cheers,

Michael



---

archive/issue_comments_042111.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-05-22T13:57:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5449",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5449#issuecomment-42111",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed



---

archive/issue_events_012728.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2009-05-22T13:57:14Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/5449",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/5449#event-12728"
}
```



---

archive/issue_events_012729.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2009-05-22T13:57:14Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/5449",
    "milestone": "sage-4.0",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/5449#event-12729"
}
```



---

archive/issue_events_012730.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2009-05-22T13:57:14Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/5449",
    "milestone": "sage-4.0",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/5449#event-12730"
}
```

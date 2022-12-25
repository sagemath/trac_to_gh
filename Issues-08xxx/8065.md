# Issue 8065: irreducible_characters() and word_problem() should sort their output

archive/issues_008065.json:
```json
{
    "body": "Assignee: joyner\n\nThese group functions use the GAP interface and return unsorted lists.  This makes them prone to doctest breakage when GAP is upgraded (and the order of things changes) or when GAP uses non-deterministic algorithms (and the order of things is ill-defined).\n\nThe patch fixes `irreducible_characters` and `word_problem`.  There might be more functions in `sage/groups` that require the same treatment, but that can go on a different ticket.\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/8065\n\n",
    "created_at": "2010-01-25T22:19:53Z",
    "labels": [
        "component: group theory",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-6.4",
    "title": "irreducible_characters() and word_problem() should sort their output",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/8065",
    "user": "https://github.com/aghitza"
}
```
Assignee: joyner

These group functions use the GAP interface and return unsorted lists.  This makes them prone to doctest breakage when GAP is upgraded (and the order of things changes) or when GAP uses non-deterministic algorithms (and the order of things is ill-defined).

The patch fixes `irreducible_characters` and `word_problem`.  There might be more functions in `sage/groups` that require the same treatment, but that can go on a different ticket.


Issue created by migration from https://trac.sagemath.org/ticket/8065





---

archive/issue_comments_070560.json:
```json
{
    "body": "Attachment [trac_8065.patch](tarball://root/attachments/some-uuid/ticket8065/trac_8065.patch) by @aghitza created at 2010-01-25 22:21:22",
    "created_at": "2010-01-25T22:21:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8065",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8065#issuecomment-70560",
    "user": "https://github.com/aghitza"
}
```

Attachment [trac_8065.patch](tarball://root/attachments/some-uuid/ticket8065/trac_8065.patch) by @aghitza created at 2010-01-25 22:21:22



---

archive/issue_comments_070561.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-01-25T22:21:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8065",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8065#issuecomment-70561",
    "user": "https://github.com/aghitza"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_070562.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2010-01-26T09:46:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8065",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8065#issuecomment-70562",
    "user": "https://github.com/dimpase"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_070563.json:
```json
{
    "body": "see http://groups.google.com.sg/group/sage-devel/browse_thread/thread/98245adfb0c45e88/802a0ab633a0fb48#802a0ab633a0fb48",
    "created_at": "2010-01-26T09:46:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8065",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8065#issuecomment-70563",
    "user": "https://github.com/dimpase"
}
```

see http://groups.google.com.sg/group/sage-devel/browse_thread/thread/98245adfb0c45e88/802a0ab633a0fb48#802a0ab633a0fb48



---

archive/issue_events_019310.json:
```json
{
    "actor": "https://github.com/jdemeyer",
    "created_at": "2013-08-13T15:35:53Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/8065",
    "milestone": "sage-5.12",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/8065#event-19310"
}
```



---

archive/issue_events_019311.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-01-30T21:20:52Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/8065",
    "milestone": "sage-5.12",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/8065#event-19311"
}
```



---

archive/issue_events_019312.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-01-30T21:20:52Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/8065",
    "milestone": "sage-6.2",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/8065#event-19312"
}
```



---

archive/issue_events_019313.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-05-06T15:20:58Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/8065",
    "milestone": "sage-6.2",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/8065#event-19313"
}
```



---

archive/issue_events_019314.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-05-06T15:20:58Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/8065",
    "milestone": "sage-6.3",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/8065#event-19314"
}
```



---

archive/issue_events_019315.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-08-10T16:51:03Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/8065",
    "milestone": "sage-6.3",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/8065#event-19315"
}
```



---

archive/issue_events_019316.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-08-10T16:51:03Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/8065",
    "milestone": "sage-6.4",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/8065#event-19316"
}
```

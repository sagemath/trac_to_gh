# Issue 2328: [with patch, positive review] many docstrings in combinat functions are unhelpful, outdated, or wrong

archive/issues_002328.json:
```json
{
    "body": "Assignee: @mwhansen\n\nCC:  sage-combinat\n\n[This link has my original complaints](http://groups.google.com/group/sage-devel/browse_thread/thread/91fb37af7f6bd0a2). On IRC, the consensus was that the uncapitalized versions of these functions should not be used, and may be deprecated in the future. The documentation for such functions should be updated to reflect this, and the documentation for other functions should be improved as well.\n\nIssue created by migration from https://trac.sagemath.org/ticket/2328\n\n",
    "closed_at": "2008-03-14T19:56:28Z",
    "created_at": "2008-02-27T06:32:59Z",
    "labels": [
        "component: combinatorics",
        "minor",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-2.10.4",
    "title": "[with patch, positive review] many docstrings in combinat functions are unhelpful, outdated, or wrong",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/2328",
    "user": "https://github.com/dandrake"
}
```
Assignee: @mwhansen

CC:  sage-combinat

[This link has my original complaints](http://groups.google.com/group/sage-devel/browse_thread/thread/91fb37af7f6bd0a2). On IRC, the consensus was that the uncapitalized versions of these functions should not be used, and may be deprecated in the future. The documentation for such functions should be updated to reflect this, and the documentation for other functions should be improved as well.

Issue created by migration from https://trac.sagemath.org/ticket/2328





---

archive/issue_comments_015458.json:
```json
{
    "body": "The attached patch fixes a few of the docstring problems mentioned by Dan Drake. Really very minor changes. I didn't touch the functions written by Mike Hansen since I wasn't sure what plans he had for them. The issue of the lower case vs upper case functions wasn't dealt with. Perhaps the lower case functions should be removed from combinat/all.py?",
    "created_at": "2008-02-27T16:40:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2328",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2328#issuecomment-15458",
    "user": "https://github.com/wdjoyner"
}
```

The attached patch fixes a few of the docstring problems mentioned by Dan Drake. Really very minor changes. I didn't touch the functions written by Mike Hansen since I wasn't sure what plans he had for them. The issue of the lower case vs upper case functions wasn't dealt with. Perhaps the lower case functions should be removed from combinat/all.py?



---

archive/issue_comments_015459.json:
```json
{
    "body": "Attachment [8710.patch](tarball://root/attachments/some-uuid/ticket2328/8710.patch) by @dandrake created at 2008-02-27 23:44:49\n\nReplying to [comment:1 wdj]:\n> Perhaps the lower case functions should be removed from combinat/all.py? \n\n\nThey should first be marked deprecated, and later removed. The exact process for doing this is not yet determined; there was some discussion on sage-devel in January. Until more has been decided on that front, I think we should just say in the docstrings \"this function will be deprecated in the future, and eventually removed; use Foo.whatever() instead\".",
    "created_at": "2008-02-27T23:44:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2328",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2328#issuecomment-15459",
    "user": "https://github.com/dandrake"
}
```

Attachment [8710.patch](tarball://root/attachments/some-uuid/ticket2328/8710.patch) by @dandrake created at 2008-02-27 23:44:49

Replying to [comment:1 wdj]:
> Perhaps the lower case functions should be removed from combinat/all.py? 


They should first be marked deprecated, and later removed. The exact process for doing this is not yet determined; there was some discussion on sage-devel in January. Until more has been decided on that front, I think we should just say in the docstrings "this function will be deprecated in the future, and eventually removed; use Foo.whatever() instead".



---

archive/issue_comments_015460.json:
```json
{
    "body": "Attachment [combinat-doc.patch](tarball://root/attachments/some-uuid/ticket2328/combinat-doc.patch) by @dandrake created at 2008-03-10 08:53:19",
    "created_at": "2008-03-10T08:53:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2328",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2328#issuecomment-15460",
    "user": "https://github.com/dandrake"
}
```

Attachment [combinat-doc.patch](tarball://root/attachments/some-uuid/ticket2328/combinat-doc.patch) by @dandrake created at 2008-03-10 08:53:19



---

archive/issue_comments_015461.json:
```json
{
    "body": "I've attached a patch which addresses most of my complaining in the email thread. :)\n\nIt's against 2.10.2 with mhansen's [2432 patch](http://sagetrac.org/sage_trac/ticket/2432) and wdj's 8710 patch applied.",
    "created_at": "2008-03-10T08:56:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2328",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2328#issuecomment-15461",
    "user": "https://github.com/dandrake"
}
```

I've attached a patch which addresses most of my complaining in the email thread. :)

It's against 2.10.2 with mhansen's [2432 patch](http://sagetrac.org/sage_trac/ticket/2432) and wdj's 8710 patch applied.



---

archive/issue_comments_015462.json:
```json
{
    "body": "Attachment [combinat-doc.2.patch](tarball://root/attachments/some-uuid/ticket2328/combinat-doc.2.patch) by @mwhansen created at 2008-03-10 09:04:14\n\nI've uploaded combinat-doc.2.patch which replaces the first combinat-doc.patch",
    "created_at": "2008-03-10T09:04:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2328",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2328#issuecomment-15462",
    "user": "https://github.com/mwhansen"
}
```

Attachment [combinat-doc.2.patch](tarball://root/attachments/some-uuid/ticket2328/combinat-doc.2.patch) by @mwhansen created at 2008-03-10 09:04:14

I've uploaded combinat-doc.2.patch which replaces the first combinat-doc.patch



---

archive/issue_comments_015463.json:
```json
{
    "body": "I had trouble applying combinat-doc.2.patch against 2.10.2, 2.10.3.rc2 and 2.10.rc3, so I don't know what this is supposed to apply against.",
    "created_at": "2008-03-10T11:22:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2328",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2328#issuecomment-15463",
    "user": "https://github.com/wdjoyner"
}
```

I had trouble applying combinat-doc.2.patch against 2.10.2, 2.10.3.rc2 and 2.10.rc3, so I don't know what this is supposed to apply against.



---

archive/issue_comments_015464.json:
```json
{
    "body": "Replying to [comment:5 wdj]:\n> I had trouble applying combinat-doc.2.patch against 2.10.2, 2.10.3.rc2 and 2.10.rc3, so I don't know what this is supposed to apply against.\n\nMy patch was against 2.10.2 + your 8710 patch + the #2432 patch...AFAIK mhansen just fiddled with a couple commented lines to get combinat-doc.2.patch.",
    "created_at": "2008-03-10T22:49:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2328",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2328#issuecomment-15464",
    "user": "https://github.com/dandrake"
}
```

Replying to [comment:5 wdj]:
> I had trouble applying combinat-doc.2.patch against 2.10.2, 2.10.3.rc2 and 2.10.rc3, so I don't know what this is supposed to apply against.

My patch was against 2.10.2 + your 8710 patch + the #2432 patch...AFAIK mhansen just fiddled with a couple commented lines to get combinat-doc.2.patch.



---

archive/issue_events_005479.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2008-03-11T03:05:21Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/2328",
    "milestone": "sage-2.10.4",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/2328#event-5479"
}
```



---

archive/issue_comments_015465.json:
```json
{
    "body": "I've looked over the patches and give this a positive review.\n\nSince my patch addressing the referee's concerns for #2432 touches a lot of things, I'll build a patch with the changes in #2328 to be included with #2432.",
    "created_at": "2008-03-11T08:21:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2328",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2328#issuecomment-15465",
    "user": "https://github.com/mwhansen"
}
```

I've looked over the patches and give this a positive review.

Since my patch addressing the referee's concerns for #2432 touches a lot of things, I'll build a patch with the changes in #2328 to be included with #2432.



---

archive/issue_events_005480.json:
```json
{
    "actor": "https://github.com/rlmill",
    "created_at": "2008-03-12T05:19:36Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/2328",
    "milestone": "sage-2.10.4",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/2328#event-5480"
}
```



---

archive/issue_events_005481.json:
```json
{
    "actor": "https://github.com/rlmill",
    "created_at": "2008-03-12T05:19:36Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/2328",
    "milestone": "sage-2.10.4",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/2328#event-5481"
}
```



---

archive/issue_comments_015466.json:
```json
{
    "body": "Attachment [2328.patch](tarball://root/attachments/some-uuid/ticket2328/2328.patch) by @mwhansen created at 2008-03-14 19:20:33\n\nApply only 2328.patch after #2432 is applied.",
    "created_at": "2008-03-14T19:20:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2328",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2328#issuecomment-15466",
    "user": "https://github.com/mwhansen"
}
```

Attachment [2328.patch](tarball://root/attachments/some-uuid/ticket2328/2328.patch) by @mwhansen created at 2008-03-14 19:20:33

Apply only 2328.patch after #2432 is applied.



---

archive/issue_comments_015467.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-03-14T19:56:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2328",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2328#issuecomment-15467",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed



---

archive/issue_events_005482.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2008-03-14T19:56:28Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/2328",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/2328#event-5482"
}
```



---

archive/issue_comments_015468.json:
```json
{
    "body": "Merged in Sage 2.10.4.alpha0",
    "created_at": "2008-03-14T19:56:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2328",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2328#issuecomment-15468",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged in Sage 2.10.4.alpha0

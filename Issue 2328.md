# Issue 2328: many docstrings in combinat functions are unhelpful, outdated, or wrong

archive/issues_002328.json:
```json
{
    "body": "Assignee: mhansen\n\nCC:  sage-combinat\n\n[This link has my original complaints](http://groups.google.com/group/sage-devel/browse_thread/thread/91fb37af7f6bd0a2). On IRC, the consensus was that the uncapitalized versions of these functions should not be used, and may be deprecated in the future. The documentation for such functions should be updated to reflect this, and the documentation for other functions should be improved as well.\n\nIssue created by migration from https://trac.sagemath.org/ticket/2328\n\n",
    "created_at": "2008-02-27T06:32:59Z",
    "labels": [
        "combinatorics",
        "minor",
        "bug"
    ],
    "title": "many docstrings in combinat functions are unhelpful, outdated, or wrong",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/2328",
    "user": "ddrake"
}
```
Assignee: mhansen

CC:  sage-combinat

[This link has my original complaints](http://groups.google.com/group/sage-devel/browse_thread/thread/91fb37af7f6bd0a2). On IRC, the consensus was that the uncapitalized versions of these functions should not be used, and may be deprecated in the future. The documentation for such functions should be updated to reflect this, and the documentation for other functions should be improved as well.

Issue created by migration from https://trac.sagemath.org/ticket/2328





---

archive/issue_comments_015492.json:
```json
{
    "body": "The attached patch fixes a few of the docstring problems mentioned by Dan Drake. Really very minor changes. I didn't touch the functions written by Mike Hansen since I wasn't sure what plans he had for them. The issue of the lower case vs upper case functions wasn't dealt with. Perhaps the lower case functions should be removed from combinat/all.py?",
    "created_at": "2008-02-27T16:40:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2328",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2328#issuecomment-15492",
    "user": "wdj"
}
```

The attached patch fixes a few of the docstring problems mentioned by Dan Drake. Really very minor changes. I didn't touch the functions written by Mike Hansen since I wasn't sure what plans he had for them. The issue of the lower case vs upper case functions wasn't dealt with. Perhaps the lower case functions should be removed from combinat/all.py?



---

archive/issue_comments_015493.json:
```json
{
    "body": "Attachment [8710.patch](tarball://root/attachments/some-uuid/ticket2328/8710.patch) by ddrake created at 2008-02-27 23:44:49\n\nReplying to [comment:1 wdj]:\n> Perhaps the lower case functions should be removed from combinat/all.py? \n\nThey should first be marked deprecated, and later removed. The exact process for doing this is not yet determined; there was some discussion on sage-devel in January. Until more has been decided on that front, I think we should just say in the docstrings \"this function will be deprecated in the future, and eventually removed; use Foo.whatever() instead\".",
    "created_at": "2008-02-27T23:44:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2328",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2328#issuecomment-15493",
    "user": "ddrake"
}
```

Attachment [8710.patch](tarball://root/attachments/some-uuid/ticket2328/8710.patch) by ddrake created at 2008-02-27 23:44:49

Replying to [comment:1 wdj]:
> Perhaps the lower case functions should be removed from combinat/all.py? 

They should first be marked deprecated, and later removed. The exact process for doing this is not yet determined; there was some discussion on sage-devel in January. Until more has been decided on that front, I think we should just say in the docstrings "this function will be deprecated in the future, and eventually removed; use Foo.whatever() instead".



---

archive/issue_comments_015494.json:
```json
{
    "body": "Attachment [combinat-doc.patch](tarball://root/attachments/some-uuid/ticket2328/combinat-doc.patch) by ddrake created at 2008-03-10 08:53:19",
    "created_at": "2008-03-10T08:53:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2328",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2328#issuecomment-15494",
    "user": "ddrake"
}
```

Attachment [combinat-doc.patch](tarball://root/attachments/some-uuid/ticket2328/combinat-doc.patch) by ddrake created at 2008-03-10 08:53:19



---

archive/issue_comments_015495.json:
```json
{
    "body": "I've attached a patch which addresses most of my complaining in the email thread. :)\n\nIt's against 2.10.2 with mhansen's [2432 patch](http://sagetrac.org/sage_trac/ticket/2432) and wdj's 8710 patch applied.",
    "created_at": "2008-03-10T08:56:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2328",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2328#issuecomment-15495",
    "user": "ddrake"
}
```

I've attached a patch which addresses most of my complaining in the email thread. :)

It's against 2.10.2 with mhansen's [2432 patch](http://sagetrac.org/sage_trac/ticket/2432) and wdj's 8710 patch applied.



---

archive/issue_comments_015496.json:
```json
{
    "body": "Attachment [combinat-doc.2.patch](tarball://root/attachments/some-uuid/ticket2328/combinat-doc.2.patch) by mhansen created at 2008-03-10 09:04:14\n\nI've uploaded combinat-doc.2.patch which replaces the first combinat-doc.patch",
    "created_at": "2008-03-10T09:04:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2328",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2328#issuecomment-15496",
    "user": "mhansen"
}
```

Attachment [combinat-doc.2.patch](tarball://root/attachments/some-uuid/ticket2328/combinat-doc.2.patch) by mhansen created at 2008-03-10 09:04:14

I've uploaded combinat-doc.2.patch which replaces the first combinat-doc.patch



---

archive/issue_comments_015497.json:
```json
{
    "body": "I had trouble applying combinat-doc.2.patch against 2.10.2, 2.10.3.rc2 and 2.10.rc3, so I don't know what this is supposed to apply against.",
    "created_at": "2008-03-10T11:22:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2328",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2328#issuecomment-15497",
    "user": "wdj"
}
```

I had trouble applying combinat-doc.2.patch against 2.10.2, 2.10.3.rc2 and 2.10.rc3, so I don't know what this is supposed to apply against.



---

archive/issue_comments_015498.json:
```json
{
    "body": "Replying to [comment:5 wdj]:\n> I had trouble applying combinat-doc.2.patch against 2.10.2, 2.10.3.rc2 and 2.10.rc3, so I don't know what this is supposed to apply against.\nMy patch was against 2.10.2 + your 8710 patch + the #2432 patch...AFAIK mhansen just fiddled with a couple commented lines to get combinat-doc.2.patch.",
    "created_at": "2008-03-10T22:49:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2328",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2328#issuecomment-15498",
    "user": "ddrake"
}
```

Replying to [comment:5 wdj]:
> I had trouble applying combinat-doc.2.patch against 2.10.2, 2.10.3.rc2 and 2.10.rc3, so I don't know what this is supposed to apply against.
My patch was against 2.10.2 + your 8710 patch + the #2432 patch...AFAIK mhansen just fiddled with a couple commented lines to get combinat-doc.2.patch.



---

archive/issue_comments_015499.json:
```json
{
    "body": "I've looked over the patches and give this a positive review.\n\nSince my patch addressing the referee's concerns for #2432 touches a lot of things, I'll build a patch with the changes in #2328 to be included with #2432.",
    "created_at": "2008-03-11T08:21:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2328",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2328#issuecomment-15499",
    "user": "mhansen"
}
```

I've looked over the patches and give this a positive review.

Since my patch addressing the referee's concerns for #2432 touches a lot of things, I'll build a patch with the changes in #2328 to be included with #2432.



---

archive/issue_comments_015500.json:
```json
{
    "body": "Attachment [2328.patch](tarball://root/attachments/some-uuid/ticket2328/2328.patch) by mhansen created at 2008-03-14 19:20:33\n\nApply only 2328.patch after #2432 is applied.",
    "created_at": "2008-03-14T19:20:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2328",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2328#issuecomment-15500",
    "user": "mhansen"
}
```

Attachment [2328.patch](tarball://root/attachments/some-uuid/ticket2328/2328.patch) by mhansen created at 2008-03-14 19:20:33

Apply only 2328.patch after #2432 is applied.



---

archive/issue_comments_015501.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-03-14T19:56:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2328",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2328#issuecomment-15501",
    "user": "mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_015502.json:
```json
{
    "body": "Merged in Sage 2.10.4.alpha0",
    "created_at": "2008-03-14T19:56:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2328",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2328#issuecomment-15502",
    "user": "mabshoff"
}
```

Merged in Sage 2.10.4.alpha0

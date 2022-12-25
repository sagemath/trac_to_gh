# Issue 5751: cartan_type now a method rather than attribute in weyl_characters.py

archive/issues_005751.json:
```json
{
    "body": "Assignee: tbd\n\nCC:  sage-combinat\n\nIn connection with #5729 this makes cartan_type a method rather than attribute in weyl_characters.py.\n\nSee cartan_type now a method rather than attribute in weyl_characters.py\n\nBut this patch has a minor conflict with #5721 which is the more important of the two\npatches. So let us get #5721 merged first.\n\nIssue created by migration from https://trac.sagemath.org/ticket/5751\n\n",
    "created_at": "2009-04-11T15:47:37Z",
    "labels": [
        "component: algebra",
        "minor",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.4.2",
    "title": "cartan_type now a method rather than attribute in weyl_characters.py",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/5751",
    "user": "https://github.com/dwbump"
}
```
Assignee: tbd

CC:  sage-combinat

In connection with #5729 this makes cartan_type a method rather than attribute in weyl_characters.py.

See cartan_type now a method rather than attribute in weyl_characters.py

But this patch has a minor conflict with #5721 which is the more important of the two
patches. So let us get #5721 merged first.

Issue created by migration from https://trac.sagemath.org/ticket/5751





---

archive/issue_comments_044863.json:
```json
{
    "body": "patch revised to apply after the 5721 patches",
    "created_at": "2009-04-15T15:32:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5751",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5751#issuecomment-44863",
    "user": "https://github.com/dwbump"
}
```

patch revised to apply after the 5721 patches



---

archive/issue_comments_044864.json:
```json
{
    "body": "Changing assignee from tbd to @mwhansen.",
    "created_at": "2009-04-15T19:25:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5751",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5751#issuecomment-44864",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Changing assignee from tbd to @mwhansen.



---

archive/issue_comments_044865.json:
```json
{
    "body": "Changing component from algebra to combinatorics.",
    "created_at": "2009-04-15T19:25:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5751",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5751#issuecomment-44865",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Changing component from algebra to combinatorics.



---

archive/issue_comments_044866.json:
```json
{
    "body": "line 316 in sage/combinat/crystal/crystals.py needs to be updated so that\nthe tests in this file will pass.\n\nAnne",
    "created_at": "2009-04-17T07:28:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5751",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5751#issuecomment-44866",
    "user": "https://github.com/anneschilling"
}
```

line 316 in sage/combinat/crystal/crystals.py needs to be updated so that
the tests in this file will pass.

Anne



---

archive/issue_comments_044867.json:
```json
{
    "body": "Except for my previous comment on the tests in crystals.py I give this patch a positive review.",
    "created_at": "2009-04-17T07:36:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5751",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5751#issuecomment-44867",
    "user": "https://github.com/anneschilling"
}
```

Except for my previous comment on the tests in crystals.py I give this patch a positive review.



---

archive/issue_comments_044868.json:
```json
{
    "body": "Well, it is does not pass doctests please do not give a patch positive review. You should write that pending the doctest fix this is a positive review.\n\nCheers,\n\nMichael",
    "created_at": "2009-04-17T07:38:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5751",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5751#issuecomment-44868",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Well, it is does not pass doctests please do not give a patch positive review. You should write that pending the doctest fix this is a positive review.

Cheers,

Michael



---

archive/issue_comments_044869.json:
```json
{
    "body": "I uploaded an additional tiny patch that addresses the problem Anne found. It\ngoes on top of the original patch.\n\nThis time I checked that passes `sage --testall`.",
    "created_at": "2009-04-17T12:34:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5751",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5751#issuecomment-44869",
    "user": "https://github.com/dwbump"
}
```

I uploaded an additional tiny patch that addresses the problem Anne found. It
goes on top of the original patch.

This time I checked that passes `sage --testall`.



---

archive/issue_comments_044870.json:
```json
{
    "body": "Positive review for Dan's fix that Anne suggested. This makes it a positive review in total.\n\nCheers,\n\nMichael",
    "created_at": "2009-04-17T12:44:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5751",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5751#issuecomment-44870",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Positive review for Dan's fix that Anne suggested. This makes it a positive review in total.

Cheers,

Michael



---

archive/issue_comments_044871.json:
```json
{
    "body": "Attachment [trac_5751-rebased-3.4.1.rc4.patch](tarball://root/attachments/some-uuid/ticket5751/trac_5751-rebased-3.4.1.rc4.patch) by @dwbump created at 2009-04-20 14:01:06",
    "created_at": "2009-04-20T14:01:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5751",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5751#issuecomment-44871",
    "user": "https://github.com/dwbump"
}
```

Attachment [trac_5751-rebased-3.4.1.rc4.patch](tarball://root/attachments/some-uuid/ticket5751/trac_5751-rebased-3.4.1.rc4.patch) by @dwbump created at 2009-04-20 14:01:06



---

archive/issue_comments_044872.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2009-04-20T14:04:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5751",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5751#issuecomment-44872",
    "user": "https://github.com/dwbump"
}
```

Changing status from new to assigned.



---

archive/issue_comments_044873.json:
```json
{
    "body": "Changing assignee from @mwhansen to @dwbump.",
    "created_at": "2009-04-20T14:04:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5751",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5751#issuecomment-44873",
    "user": "https://github.com/dwbump"
}
```

Changing assignee from @mwhansen to @dwbump.



---

archive/issue_comments_044874.json:
```json
{
    "body": "I found that the patches didn't apply cleanly to sage-3.4.1.rc4, so I\nrebased. The patch trac_5751-rebased-3.4.1.patch  supercedes the\nprevious two patches.",
    "created_at": "2009-04-20T14:04:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5751",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5751#issuecomment-44874",
    "user": "https://github.com/dwbump"
}
```

I found that the patches didn't apply cleanly to sage-3.4.1.rc4, so I
rebased. The patch trac_5751-rebased-3.4.1.patch  supercedes the
previous two patches.



---

archive/issue_comments_044875.json:
```json
{
    "body": "Merged in Sage 3.4.2.alpha0.\n\nCheers,\n\nMichael",
    "created_at": "2009-04-23T05:42:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5751",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5751#issuecomment-44875",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged in Sage 3.4.2.alpha0.

Cheers,

Michael



---

archive/issue_events_005998.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2009-04-23T05:42:01Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/5751",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/5751#event-5998"
}
```



---

archive/issue_comments_044876.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-04-23T05:42:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5751",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5751#issuecomment-44876",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed

# Issue 5831: [with patch, not ready for review] reducible root system fixes

archive/issues_005831.json:
```json
{
    "body": "Assignee: @dwbump\n\nCC:  sage-combinat\n\nThe methods simple_roots(), fundamental_weights() and simple_coroots() for the ambient space of a root system are supposed to return a family. This was never correctly implemented for the reducible types, and the patch corrects this.\n\nThere are also some changes in weyl_characters.py, where it was assumed that the root system was irreducible in a few places. The patch corrects this.\n\nThe patch is probably correct but I haven't confirmed that it applies cleanly to sage-3.4.1.rc3 or that it passes `sage --testall` so wait to review.\n\nIssue created by migration from https://trac.sagemath.org/ticket/5831\n\n",
    "created_at": "2009-04-20T05:10:13Z",
    "labels": [
        "component: combinatorics",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-duplicate/invalid/wontfix",
    "title": "[with patch, not ready for review] reducible root system fixes",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/5831",
    "user": "https://github.com/dwbump"
}
```
Assignee: @dwbump

CC:  sage-combinat

The methods simple_roots(), fundamental_weights() and simple_coroots() for the ambient space of a root system are supposed to return a family. This was never correctly implemented for the reducible types, and the patch corrects this.

There are also some changes in weyl_characters.py, where it was assumed that the root system was irreducible in a few places. The patch corrects this.

The patch is probably correct but I haven't confirmed that it applies cleanly to sage-3.4.1.rc3 or that it passes `sage --testall` so wait to review.

Issue created by migration from https://trac.sagemath.org/ticket/5831





---

archive/issue_comments_045744.json:
```json
{
    "body": "fixes for reducible root systems",
    "created_at": "2009-04-20T05:15:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5831",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5831#issuecomment-45744",
    "user": "https://github.com/dwbump"
}
```

fixes for reducible root systems



---

archive/issue_comments_045745.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2009-04-20T05:18:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5831",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5831#issuecomment-45745",
    "user": "https://github.com/dwbump"
}
```

Changing status from new to assigned.



---

archive/issue_comments_045746.json:
```json
{
    "body": "Attachment [reducible.patch](tarball://root/attachments/some-uuid/ticket5831/reducible.patch) by @dwbump created at 2009-04-20 05:18:01",
    "created_at": "2009-04-20T05:18:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5831",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5831#issuecomment-45746",
    "user": "https://github.com/dwbump"
}
```

Attachment [reducible.patch](tarball://root/attachments/some-uuid/ticket5831/reducible.patch) by @dwbump created at 2009-04-20 05:18:01



---

archive/issue_comments_045747.json:
```json
{
    "body": "Sounds good to me.\nIs it needed to implement simple_roots? I would have expected the default implementation\nfor ambient spaces (as coroots associated to the simple roots) to work.",
    "created_at": "2009-04-20T21:50:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5831",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5831#issuecomment-45747",
    "user": "https://github.com/nthiery"
}
```

Sounds good to me.
Is it needed to implement simple_roots? I would have expected the default implementation
for ambient spaces (as coroots associated to the simple roots) to work.



---

archive/issue_comments_045748.json:
```json
{
    "body": "Replying to the last message, I think it is necessary to implement simple_roots (and also simple_coroots and fundamental_weights).\n\nNicolas requested a doctest. See:\n\nhttp://groups.google.com/group/sage-combinat-devel/msg/4004c4a8471f3cfa?hl=en&pli=1\n\nI did this. I put the new doctest in type_reducible.py.",
    "created_at": "2009-04-21T00:12:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5831",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5831#issuecomment-45748",
    "user": "https://github.com/dwbump"
}
```

Replying to the last message, I think it is necessary to implement simple_roots (and also simple_coroots and fundamental_weights).

Nicolas requested a doctest. See:

http://groups.google.com/group/sage-combinat-devel/msg/4004c4a8471f3cfa?hl=en&pli=1

I did this. I put the new doctest in type_reducible.py.



---

archive/issue_comments_045749.json:
```json
{
    "body": "> Replying to the last message, I think it is necessary to implement simple_roots (and also simple_coroots and fundamental_weights).\n\nOops, sorry for the confusion. I was wondering wether it was necessary to implement the simple *coroots*.\nFor the roots, definitely yes.\n\n> Nicolas requested a doctest. See:\n> http://groups.google.com/group/sage-combinat-devel/msg/4004c4a8471f3cfa?hl=en&pli=1\n> I did this. I put the new doctest in type_reducible.py.\n\nThanks!",
    "created_at": "2009-04-21T05:24:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5831",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5831#issuecomment-45749",
    "user": "https://github.com/nthiery"
}
```

> Replying to the last message, I think it is necessary to implement simple_roots (and also simple_coroots and fundamental_weights).

Oops, sorry for the confusion. I was wondering wether it was necessary to implement the simple *coroots*.
For the roots, definitely yes.

> Nicolas requested a doctest. See:
> http://groups.google.com/group/sage-combinat-devel/msg/4004c4a8471f3cfa?hl=en&pli=1
> I did this. I put the new doctest in type_reducible.py.

Thanks!



---

archive/issue_comments_045750.json:
```json
{
    "body": "Attachment [trac_5831.patch](tarball://root/attachments/some-uuid/ticket5831/trac_5831.patch) by @dwbump created at 2009-04-23 01:24:09",
    "created_at": "2009-04-23T01:24:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5831",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5831#issuecomment-45750",
    "user": "https://github.com/dwbump"
}
```

Attachment [trac_5831.patch](tarball://root/attachments/some-uuid/ticket5831/trac_5831.patch) by @dwbump created at 2009-04-23 01:24:09



---

archive/issue_comments_045751.json:
```json
{
    "body": "Revised: WeylCharacterRing derives the name of its Cartan Type from its Cartan Type's `__repr__` method.",
    "created_at": "2009-04-23T01:27:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5831",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5831#issuecomment-45751",
    "user": "https://github.com/dwbump"
}
```

Revised: WeylCharacterRing derives the name of its Cartan Type from its Cartan Type's `__repr__` method.



---

archive/issue_comments_045752.json:
```json
{
    "body": "This ticket may be closed if trac_5794-revised.patch is merged. See #5794.",
    "created_at": "2009-05-01T16:29:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5831",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5831#issuecomment-45752",
    "user": "https://github.com/dwbump"
}
```

This ticket may be closed if trac_5794-revised.patch is merged. See #5794.



---

archive/issue_comments_045753.json:
```json
{
    "body": "Closing this ticket as a duplicate of #5794.",
    "created_at": "2009-08-26T21:18:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5831",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5831#issuecomment-45753",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

Closing this ticket as a duplicate of #5794.



---

archive/issue_comments_045754.json:
```json
{
    "body": "Resolution: duplicate",
    "created_at": "2009-08-26T21:18:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5831",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5831#issuecomment-45754",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

Resolution: duplicate

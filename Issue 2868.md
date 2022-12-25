# Issue 2868: Weight revision for fastcrystals

archive/issues_002868.json:
```json
{
    "body": "Assignee: @mwhansen\n\nCC:  sage-combinat\n\nThis extends the revision of the patch in:\n\nhttp://sagetrac.org/sage_trac/ticket/2853\n\nThe previous patch reimplemented the weight function for vertices in crystals of letters and crystals of tableaux. The patch at hand does the corresponding reimplementation for fastcrystals. These are crystals whose definition is limited to types A2, B2, C2. They are isomorphic to crystals of tableaux but have better speed when the crystal is large, since the root operators are implemented by table lookup. \n\nThe revised weight function should be very fast since the weight is computed by adding a few numbers together.\n\nThis patch corrects the same defect for type A2 that the previous patch addressed.\n\nThe tests in the patch were written BEFORE the weight function was reimplemented, so I am confident that it is correct.\n\nIssue created by migration from https://trac.sagemath.org/ticket/2868\n\n",
    "created_at": "2008-04-09T23:48:25Z",
    "labels": [
        "component: combinatorics",
        "minor",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.0",
    "title": "Weight revision for fastcrystals",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/2868",
    "user": "https://github.com/dwbump"
}
```
Assignee: @mwhansen

CC:  sage-combinat

This extends the revision of the patch in:

http://sagetrac.org/sage_trac/ticket/2853

The previous patch reimplemented the weight function for vertices in crystals of letters and crystals of tableaux. The patch at hand does the corresponding reimplementation for fastcrystals. These are crystals whose definition is limited to types A2, B2, C2. They are isomorphic to crystals of tableaux but have better speed when the crystal is large, since the root operators are implemented by table lookup. 

The revised weight function should be very fast since the weight is computed by adding a few numbers together.

This patch corrects the same defect for type A2 that the previous patch addressed.

The tests in the patch were written BEFORE the weight function was reimplemented, so I am confident that it is correct.

Issue created by migration from https://trac.sagemath.org/ticket/2868





---

archive/issue_comments_019639.json:
```json
{
    "body": "Attachment [weight_fastcrystal.patch](tarball://root/attachments/some-uuid/ticket2868/weight_fastcrystal.patch) by @dwbump created at 2008-04-09 23:50:22",
    "created_at": "2008-04-09T23:50:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2868",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2868#issuecomment-19639",
    "user": "https://github.com/dwbump"
}
```

Attachment [weight_fastcrystal.patch](tarball://root/attachments/some-uuid/ticket2868/weight_fastcrystal.patch) by @dwbump created at 2008-04-09 23:50:22



---

archive/issue_comments_019640.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2008-04-09T23:51:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2868",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2868#issuecomment-19640",
    "user": "https://github.com/dwbump"
}
```

Changing status from new to assigned.



---

archive/issue_comments_019641.json:
```json
{
    "body": "Changing assignee from @mwhansen to @dwbump.",
    "created_at": "2008-04-09T23:51:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2868",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2868#issuecomment-19641",
    "user": "https://github.com/dwbump"
}
```

Changing assignee from @mwhansen to @dwbump.



---

archive/issue_comments_019642.json:
```json
{
    "body": "Changing assignee from @dwbump to @mwhansen.",
    "created_at": "2008-04-10T00:24:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2868",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2868#issuecomment-19642",
    "user": "https://github.com/dwbump"
}
```

Changing assignee from @dwbump to @mwhansen.



---

archive/issue_comments_019643.json:
```json
{
    "body": "Changing status from assigned to new.",
    "created_at": "2008-04-10T00:24:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2868",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2868#issuecomment-19643",
    "user": "https://github.com/dwbump"
}
```

Changing status from assigned to new.



---

archive/issue_comments_019644.json:
```json
{
    "body": "Attachment [2868.patch](tarball://root/attachments/some-uuid/ticket2868/2868.patch) by @mwhansen created at 2008-04-10 03:14:30",
    "created_at": "2008-04-10T03:14:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2868",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2868#issuecomment-19644",
    "user": "https://github.com/mwhansen"
}
```

Attachment [2868.patch](tarball://root/attachments/some-uuid/ticket2868/2868.patch) by @mwhansen created at 2008-04-10 03:14:30



---

archive/issue_comments_019645.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2008-04-10T03:15:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2868",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2868#issuecomment-19645",
    "user": "https://github.com/mwhansen"
}
```

Changing status from new to assigned.



---

archive/issue_comments_019646.json:
```json
{
    "body": "I attached a new patch which removes a print statement and moves the tests down to the docstring of weight.",
    "created_at": "2008-04-10T03:15:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2868",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2868#issuecomment-19646",
    "user": "https://github.com/mwhansen"
}
```

I attached a new patch which removes a print statement and moves the tests down to the docstring of weight.



---

archive/issue_comments_019647.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-04-10T03:35:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2868",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2868#issuecomment-19647",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_019648.json:
```json
{
    "body": "Merged 2868.patch in Sage 3.0.alpha4",
    "created_at": "2008-04-10T03:35:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2868",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2868#issuecomment-19648",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged 2868.patch in Sage 3.0.alpha4

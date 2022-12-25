# Issue 5845: Fix precision bug in hilbert_class_polynomial()

archive/issues_005845.json:
```json
{
    "body": "Assignee: tbd\n\nKeywords: hilbert class polynomial quadratic form\n\nThe code introduced in #4990 uses an incorrect precision bound in a paper of Enge.  Enge has supplied a corrected bound, and the code fixed to use it.  At the same time, \n* The code has been extended to non-fundamental discriminants\n* It has been moved to sage/schemes/elliptic_curves/cm.py which had a similar function requiring Magma;  the method for number fields now calls this.\n* The function elliptic_j has been added to sage/functions/special.py\n* A new method is_primitive() has been added for integral binary quadratic forms, as well as a primitive_only flag to the function `BinaryQF_reduced_representatives`.\n* Last but not least, sage/schemes/elliptic_curves/cm.py has been ReST-ified and added to the reference manual\n\nThis started out as just a conversion of one small file with only 3 functions in it to ReST!\n\nIssue created by migration from https://trac.sagemath.org/ticket/5845\n\n",
    "created_at": "2009-04-21T10:41:47Z",
    "labels": [
        "component: algebra",
        "minor",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.0.2",
    "title": "Fix precision bug in hilbert_class_polynomial()",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/5845",
    "user": "https://github.com/JohnCremona"
}
```
Assignee: tbd

Keywords: hilbert class polynomial quadratic form

The code introduced in #4990 uses an incorrect precision bound in a paper of Enge.  Enge has supplied a corrected bound, and the code fixed to use it.  At the same time, 
* The code has been extended to non-fundamental discriminants
* It has been moved to sage/schemes/elliptic_curves/cm.py which had a similar function requiring Magma;  the method for number fields now calls this.
* The function elliptic_j has been added to sage/functions/special.py
* A new method is_primitive() has been added for integral binary quadratic forms, as well as a primitive_only flag to the function `BinaryQF_reduced_representatives`.
* Last but not least, sage/schemes/elliptic_curves/cm.py has been ReST-ified and added to the reference manual

This started out as just a conversion of one small file with only 3 functions in it to ReST!

Issue created by migration from https://trac.sagemath.org/ticket/5845





---

archive/issue_comments_045885.json:
```json
{
    "body": "Applies to 3.4.1.rc4",
    "created_at": "2009-04-21T10:45:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5845",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5845#issuecomment-45885",
    "user": "https://github.com/JohnCremona"
}
```

Applies to 3.4.1.rc4



---

archive/issue_comments_045886.json:
```json
{
    "body": "Attachment [trac_5845.patch](tarball://root/attachments/some-uuid/ticket5845/trac_5845.patch) by @JohnCremona created at 2009-04-21 10:47:00",
    "created_at": "2009-04-21T10:47:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5845",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5845#issuecomment-45886",
    "user": "https://github.com/JohnCremona"
}
```

Attachment [trac_5845.patch](tarball://root/attachments/some-uuid/ticket5845/trac_5845.patch) by @JohnCremona created at 2009-04-21 10:47:00



---

archive/issue_comments_045887.json:
```json
{
    "body": "All doctests pass. It works very well and is a sorely needed addition to sage.\n\nOne minor point: In the patch the paper of Enge calls for a constant of log(2*10.163) while the code has a typo which sets this constant to log(2*10.63). This makes no difference whatsoever in the output of the program(indeed there's no difference in the operation of the code for h<~24) but it's worth noting.",
    "created_at": "2009-05-23T17:45:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5845",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5845#issuecomment-45887",
    "user": "https://trac.sagemath.org/admin/accounts/users/stankewicz"
}
```

All doctests pass. It works very well and is a sorely needed addition to sage.

One minor point: In the patch the paper of Enge calls for a constant of log(2*10.163) while the code has a typo which sets this constant to log(2*10.63). This makes no difference whatsoever in the output of the program(indeed there's no difference in the operation of the code for h<~24) but it's worth noting.



---

archive/issue_comments_045888.json:
```json
{
    "body": "Thanks for the report.  I don't have access to Enge's paper at the moment but I'll see him in person tomorrow so I can perhaps check up on that type (recall that one of his papers had a lot of typos in it, and I took the \"official\" bounds from correspondence with him).",
    "created_at": "2009-05-23T18:49:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5845",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5845#issuecomment-45888",
    "user": "https://github.com/JohnCremona"
}
```

Thanks for the report.  I don't have access to Enge's paper at the moment but I'll see him in person tomorrow so I can perhaps check up on that type (recall that one of his papers had a lot of typos in it, and I took the "official" bounds from correspondence with him).



---

archive/issue_comments_045889.json:
```json
{
    "body": "This needs to rebased against 4.0 since functions/special.py has changed.  The elliptic_j function should be written to match those.",
    "created_at": "2009-06-01T04:28:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5845",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5845#issuecomment-45889",
    "user": "https://github.com/mwhansen"
}
```

This needs to rebased against 4.0 since functions/special.py has changed.  The elliptic_j function should be written to match those.



---

archive/issue_comments_045890.json:
```json
{
    "body": "Replying to [comment:5 mhansen]:\n> This needs to rebased against 4.0 since functions/special.py has changed.  The elliptic_j function should be written to match those.\nWill do -- John",
    "created_at": "2009-06-01T08:01:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5845",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5845#issuecomment-45890",
    "user": "https://github.com/JohnCremona"
}
```

Replying to [comment:5 mhansen]:
> This needs to rebased against 4.0 since functions/special.py has changed.  The elliptic_j function should be written to match those.
Will do -- John



---

archive/issue_comments_045891.json:
```json
{
    "body": "Attachment [trac_5845_rebase.patch](tarball://root/attachments/some-uuid/ticket5845/trac_5845_rebase.patch) by @JohnCremona created at 2009-06-01 08:20:38\n\nRebased to 4.0 (replace previous)",
    "created_at": "2009-06-01T08:20:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5845",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5845#issuecomment-45891",
    "user": "https://github.com/JohnCremona"
}
```

Attachment [trac_5845_rebase.patch](tarball://root/attachments/some-uuid/ticket5845/trac_5845_rebase.patch) by @JohnCremona created at 2009-06-01 08:20:38

Rebased to 4.0 (replace previous)



---

archive/issue_comments_045892.json:
```json
{
    "body": "I have done the rebasing -- not sure whether it's ok to put back \"with positive review\" to I have marked it \"needs review\" again.",
    "created_at": "2009-06-01T08:22:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5845",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5845#issuecomment-45892",
    "user": "https://github.com/JohnCremona"
}
```

I have done the rebasing -- not sure whether it's ok to put back "with positive review" to I have marked it "needs review" again.



---

archive/issue_comments_045893.json:
```json
{
    "body": "Good.",
    "created_at": "2009-06-01T11:15:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5845",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5845#issuecomment-45893",
    "user": "https://github.com/aghitza"
}
```

Good.



---

archive/issue_events_006097.json:
```json
{
    "actor": "@ncalexan",
    "created_at": "2009-06-13T21:12:28Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/5845",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/5845#event-6097"
}
```



---

archive/issue_comments_045894.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-06-13T21:12:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5845",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5845#issuecomment-45894",
    "user": "https://github.com/ncalexan"
}
```

Resolution: fixed

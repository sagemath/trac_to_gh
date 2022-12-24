# Issue 5896: [with patch, needs trivial review] Documentation fix for lcalc interface.

archive/issues_005896.json:
```json
{
    "body": "Assignee: craigcitro\n\nThe documentation for `lcalc.twist_values` and `lcalc.twist_zeros` is wrong. It claims that the function computes all twists for `(d/.)` with `dmin <= d <= dmax`, but in fact, it computes it for all `(d/.)` such that the **conductor** lies between `dmin` and `dmax`. \n\nTrivial patch to fix this is attached.\n\nIssue created by migration from https://trac.sagemath.org/ticket/5896\n\n",
    "created_at": "2009-04-26T00:43:03Z",
    "labels": [
        "number theory",
        "minor",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.4.2",
    "title": "[with patch, needs trivial review] Documentation fix for lcalc interface.",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/5896",
    "user": "craigcitro"
}
```
Assignee: craigcitro

The documentation for `lcalc.twist_values` and `lcalc.twist_zeros` is wrong. It claims that the function computes all twists for `(d/.)` with `dmin <= d <= dmax`, but in fact, it computes it for all `(d/.)` such that the **conductor** lies between `dmin` and `dmax`. 

Trivial patch to fix this is attached.

Issue created by migration from https://trac.sagemath.org/ticket/5896





---

archive/issue_comments_046620.json:
```json
{
    "body": "Minor quibble:  in the lcalc docs it says \"Notice that with the --twist-quadratic option one is specifying the discriminant\nwhich can be negative, while with the --twist-primitive option one is\nspecifying the conductor which should be positive. \"   So one could argue that the character (-3/-) has discriminant -12 and conductor 12.\n\nSince users might expect similar, would it be better to change \"conductor `N`\" to \"discriminant `D`\" in both places in the patch?",
    "created_at": "2009-04-27T09:09:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5896",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5896#issuecomment-46620",
    "user": "cremona"
}
```

Minor quibble:  in the lcalc docs it says "Notice that with the --twist-quadratic option one is specifying the discriminant
which can be negative, while with the --twist-primitive option one is
specifying the conductor which should be positive. "   So one could argue that the character (-3/-) has discriminant -12 and conductor 12.

Since users might expect similar, would it be better to change "conductor `N`" to "discriminant `D`" in both places in the patch?



---

archive/issue_comments_046621.json:
```json
{
    "body": "That's a good point. The example I was playing with had a positive discriminant -- I honestly just didn't think of it. :) New patch.",
    "created_at": "2009-04-27T09:36:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5896",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5896#issuecomment-46621",
    "user": "craigcitro"
}
```

That's a good point. The example I was playing with had a positive discriminant -- I honestly just didn't think of it. :) New patch.



---

archive/issue_comments_046622.json:
```json
{
    "body": "I'm suspicious of the patch I just attached. New one coming right up.",
    "created_at": "2009-04-27T09:37:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5896",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5896#issuecomment-46622",
    "user": "craigcitro"
}
```

I'm suspicious of the patch I just attached. New one coming right up.



---

archive/issue_comments_046623.json:
```json
{
    "body": "Attachment [lcalc-doc.patch](tarball://root/attachments/some-uuid/ticket5896/lcalc-doc.patch) by craigcitro created at 2009-04-27 09:38:44\n\nOk, it's ready to go.",
    "created_at": "2009-04-27T09:38:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5896",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5896#issuecomment-46623",
    "user": "craigcitro"
}
```

Attachment [lcalc-doc.patch](tarball://root/attachments/some-uuid/ticket5896/lcalc-doc.patch) by craigcitro created at 2009-04-27 09:38:44

Ok, it's ready to go.



---

archive/issue_comments_046624.json:
```json
{
    "body": "Would you believe, I picked up the suspicious patch, observed that it failed to apply, came back to the ticket and found that you had already replaced it!\n\nThis one is fine.  Positive review!  (moral: never say something is trivial....)",
    "created_at": "2009-04-27T09:42:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5896",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5896#issuecomment-46624",
    "user": "cremona"
}
```

Would you believe, I picked up the suspicious patch, observed that it failed to apply, came back to the ticket and found that you had already replaced it!

This one is fine.  Positive review!  (moral: never say something is trivial....)



---

archive/issue_comments_046625.json:
```json
{
    "body": "> moral: never say something is trivial....\n\nespecially when trying to use english to express mathematics. :)",
    "created_at": "2009-04-27T09:58:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5896",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5896#issuecomment-46625",
    "user": "craigcitro"
}
```

> moral: never say something is trivial....

especially when trying to use english to express mathematics. :)



---

archive/issue_comments_046626.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-04-30T01:48:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5896",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5896#issuecomment-46626",
    "user": "mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_046627.json:
```json
{
    "body": "Merged in Sage 3.4.2.rc0.\n\nCheers,\n\nMichael",
    "created_at": "2009-04-30T01:48:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5896",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5896#issuecomment-46627",
    "user": "mabshoff"
}
```

Merged in Sage 3.4.2.rc0.

Cheers,

Michael

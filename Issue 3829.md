# Issue 3829: wester.py disagrees with Wester!!!

archive/issues_003829.json:
```json
{
    "body": "Assignee: @garyfurnish\n\n\n```\nsage: f = log(tan(x/2 + pi/4)) - arcsin(tan(x))\nsage: bool(f == 0)\nFalse\n```\n\n\nThis just plain disagrees with Wester's benchmarks. The function is identically zero. I'm going to go through `wester.py` and check to see if there are any more...\n\nIssue created by migration from https://trac.sagemath.org/ticket/3829\n\n",
    "created_at": "2008-08-13T00:51:01Z",
    "labels": [
        "component: symbolics",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.0.2",
    "title": "wester.py disagrees with Wester!!!",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/3829",
    "user": "https://github.com/rlmill"
}
```
Assignee: @garyfurnish


```
sage: f = log(tan(x/2 + pi/4)) - arcsin(tan(x))
sage: bool(f == 0)
False
```


This just plain disagrees with Wester's benchmarks. The function is identically zero. I'm going to go through `wester.py` and check to see if there are any more...

Issue created by migration from https://trac.sagemath.org/ticket/3829





---

archive/issue_events_008774.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2008-08-13T02:48:05Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/3829",
    "milestone": "sage-3.1",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/3829#event-8774"
}
```



---

archive/issue_comments_027177.json:
```json
{
    "body": "But, we *still* have bool(...) False, so all the above comments apply.\n\n```\nsage: # (YES) Ln(Tan(x/2+Pi/4))-ArcSinh(Tan(x))=0\nsage: # Yes, in that the thing is clearly not equal to 0!\nsage: f = log(tan(x/2 + pi/4)) - arcsinh(tan(x))\nsage: bool(f == 0)\nFalse\n```\n\n\nAnd there should be a patch attached to this ticket that fixes the doctest to have an h, and also \ndoes not put (YES) in the comment.     \n\nThe reason the above is unfortunately not a Sage bug is that in Maxima bool(...) only returns True when its algorithm can definitely prove Truth, and not otherwise.  And that's documented.",
    "created_at": "2008-08-13T03:56:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3829",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3829#issuecomment-27177",
    "user": "https://github.com/williamstein"
}
```

But, we *still* have bool(...) False, so all the above comments apply.

```
sage: # (YES) Ln(Tan(x/2+Pi/4))-ArcSinh(Tan(x))=0
sage: # Yes, in that the thing is clearly not equal to 0!
sage: f = log(tan(x/2 + pi/4)) - arcsinh(tan(x))
sage: bool(f == 0)
False
```


And there should be a patch attached to this ticket that fixes the doctest to have an h, and also 
does not put (YES) in the comment.     

The reason the above is unfortunately not a Sage bug is that in Maxima bool(...) only returns True when its algorithm can definitely prove Truth, and not otherwise.  And that's documented.



---

archive/issue_comments_027178.json:
```json
{
    "body": "Attachment [trac_3829-wester.patch](tarball://root/attachments/some-uuid/ticket3829/trac_3829-wester.patch) by @burcin created at 2009-02-08 14:57:39",
    "created_at": "2009-02-08T14:57:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3829",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3829#issuecomment-27178",
    "user": "https://github.com/burcin"
}
```

Attachment [trac_3829-wester.patch](tarball://root/attachments/some-uuid/ticket3829/trac_3829-wester.patch) by @burcin created at 2009-02-08 14:57:39



---

archive/issue_comments_027179.json:
```json
{
    "body": "attachment:trac_3829-wester.patch fixes the typo.\n\nI am not sure how to handle the new results of evaluating the function f. I pasted the new values obtained on my laptop. If they vary on different platforms, we could replace that line with a test that they are < 1e-10.",
    "created_at": "2009-02-08T15:02:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3829",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3829#issuecomment-27179",
    "user": "https://github.com/burcin"
}
```

attachment:trac_3829-wester.patch fixes the typo.

I am not sure how to handle the new results of evaluating the function f. I pasted the new values obtained on my laptop. If they vary on different platforms, we could replace that line with a test that they are < 1e-10.



---

archive/issue_comments_027180.json:
```json
{
    "body": "Having `(NO)` in the comment is worse, because the identity is true! What should be there is a short explanation of why `bool(f == 0)` returns False, even though we know it is true.",
    "created_at": "2009-02-09T16:06:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3829",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3829#issuecomment-27180",
    "user": "https://github.com/rlmill"
}
```

Having `(NO)` in the comment is worse, because the identity is true! What should be there is a short explanation of why `bool(f == 0)` returns False, even though we know it is true.



---

archive/issue_comments_027181.json:
```json
{
    "body": "Attachment [trac_3829-wester.take2.patch](tarball://root/attachments/some-uuid/ticket3829/trac_3829-wester.take2.patch) by @burcin created at 2009-02-09 16:51:49",
    "created_at": "2009-02-09T16:51:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3829",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3829#issuecomment-27181",
    "user": "https://github.com/burcin"
}
```

Attachment [trac_3829-wester.take2.patch](tarball://root/attachments/some-uuid/ticket3829/trac_3829-wester.take2.patch) by @burcin created at 2009-02-09 16:51:49



---

archive/issue_comments_027182.json:
```json
{
    "body": "I thought the (NO) in the comments indicates that Sage does not give the answer Wester says it should.\n\nI added a comment explaning the Sage/Maxima policy on equality of symbolic expressions.",
    "created_at": "2009-02-09T16:56:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3829",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3829#issuecomment-27182",
    "user": "https://github.com/burcin"
}
```

I thought the (NO) in the comments indicates that Sage does not give the answer Wester says it should.

I added a comment explaning the Sage/Maxima policy on equality of symbolic expressions.



---

archive/issue_comments_027183.json:
```json
{
    "body": "Why should this be considered true? The equality clearly doesn't hold for all x. Try for example evaluating numerically with x = 3.\n\nOr is some nonstandard branch cut convention implied here?",
    "created_at": "2009-02-10T15:36:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3829",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3829#issuecomment-27183",
    "user": "https://github.com/fredrik-johansson"
}
```

Why should this be considered true? The equality clearly doesn't hold for all x. Try for example evaluating numerically with x = 3.

Or is some nonstandard branch cut convention implied here?



---

archive/issue_comments_027184.json:
```json
{
    "body": "Replying to [comment:8 fredrik.johansson]:\n> Why should this be considered true? The equality clearly doesn't hold for all x. Try for example evaluating numerically with x = 3.\n> \n> Or is some nonstandard branch cut convention implied here?\n\nFredrik,\n\nI spent quite some time convincing myself that that identity is true. The proof is attached as PDF. You must be able to take the logarithm of `tan(x/2 + pi/4)` in order for the identity to make sense, but for any branch you take where it makes sense it is true. The problem with evaluating numerically at `x = 3` is that symbolic log doesn't like negative numbers, and `tan(3/2 + pi/4) = -1.15265520898227` so it returns a `NaN`.",
    "created_at": "2009-02-10T16:12:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3829",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3829#issuecomment-27184",
    "user": "https://github.com/rlmill"
}
```

Replying to [comment:8 fredrik.johansson]:
> Why should this be considered true? The equality clearly doesn't hold for all x. Try for example evaluating numerically with x = 3.
> 
> Or is some nonstandard branch cut convention implied here?

Fredrik,

I spent quite some time convincing myself that that identity is true. The proof is attached as PDF. You must be able to take the logarithm of `tan(x/2 + pi/4)` in order for the identity to make sense, but for any branch you take where it makes sense it is true. The problem with evaluating numerically at `x = 3` is that symbolic log doesn't like negative numbers, and `tan(3/2 + pi/4) = -1.15265520898227` so it returns a `NaN`.



---

archive/issue_comments_027185.json:
```json
{
    "body": "Ooops, unfortunately this patch has bitrotted: \n\n```\nsage-3.4.1.rc3/devel/sage$ patch -p1 --dry-run < trac_3829-wester.take2.patch \npatching file sage/calculus/wester.py\nHunk #1 FAILED at 253.\n1 out of 1 hunk FAILED -- saving rejects to file sage/calculus/wester.py.rej\n```\n\nI was paranoid about merging this since it potentially introduces numerical noise and I thought that 3.4.1 was about done for the last couple weeks, so sorry about that.\n\nCheers,\n\nMichael",
    "created_at": "2009-04-13T02:30:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3829",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3829#issuecomment-27185",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Ooops, unfortunately this patch has bitrotted: 

```
sage-3.4.1.rc3/devel/sage$ patch -p1 --dry-run < trac_3829-wester.take2.patch 
patching file sage/calculus/wester.py
Hunk #1 FAILED at 253.
1 out of 1 hunk FAILED -- saving rejects to file sage/calculus/wester.py.rej
```

I was paranoid about merging this since it potentially introduces numerical noise and I thought that 3.4.1 was about done for the last couple weeks, so sorry about that.

Cheers,

Michael



---

archive/issue_comments_027186.json:
```json
{
    "body": "Apply only `trac_3829-rebased.patch`, which is rebased against 4.0.",
    "created_at": "2009-05-31T13:44:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3829",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3829#issuecomment-27186",
    "user": "https://github.com/aghitza"
}
```

Apply only `trac_3829-rebased.patch`, which is rebased against 4.0.



---

archive/issue_comments_027187.json:
```json
{
    "body": "Attachment [trac_3829-rebased.patch](tarball://root/attachments/some-uuid/ticket3829/trac_3829-rebased.patch) by @aghitza created at 2009-05-31 13:46:06\n\nrebased against 4.0",
    "created_at": "2009-05-31T13:46:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3829",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3829#issuecomment-27187",
    "user": "https://github.com/aghitza"
}
```

Attachment [trac_3829-rebased.patch](tarball://root/attachments/some-uuid/ticket3829/trac_3829-rebased.patch) by @aghitza created at 2009-05-31 13:46:06

rebased against 4.0



---

archive/issue_comments_027188.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-06-13T20:33:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3829",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3829#issuecomment-27188",
    "user": "https://github.com/ncalexan"
}
```

Resolution: fixed



---

archive/issue_events_008775.json:
```json
{
    "actor": "https://github.com/ncalexan",
    "created_at": "2009-06-13T20:33:12Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/3829",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/3829#event-8775"
}
```

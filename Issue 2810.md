# Issue 2810: Use new generic code in elliptic_curve_finite_field

archive/issues_002810.json:
```json
{
    "body": "Assignee: mabshoff\n\nAfter merging the new generic group functions (#210) there is no need for the specific versions implemented for elliptic curve groups.  This patch removes those and adjusts the code accordingly.\n\nBased on 3.0.alpha1.\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/2810\n\n",
    "created_at": "2008-04-05T16:47:47Z",
    "labels": [
        "Cygwin",
        "major",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.0",
    "title": "Use new generic code in elliptic_curve_finite_field",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/2810",
    "user": "@JohnCremona"
}
```
Assignee: mabshoff

After merging the new generic group functions (#210) there is no need for the specific versions implemented for elliptic curve groups.  This patch removes those and adjusts the code accordingly.

Based on 3.0.alpha1.


Issue created by migration from https://trac.sagemath.org/ticket/2810





---

archive/issue_comments_019283.json:
```json
{
    "body": "Attachment [9384.patch](tarball://root/attachments/some-uuid/ticket2810/9384.patch) by @JohnCremona created at 2008-04-05 16:49:30",
    "created_at": "2008-04-05T16:49:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2810",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2810#issuecomment-19283",
    "user": "@JohnCremona"
}
```

Attachment [9384.patch](tarball://root/attachments/some-uuid/ticket2810/9384.patch) by @JohnCremona created at 2008-04-05 16:49:30



---

archive/issue_comments_019284.json:
```json
{
    "body": "Changing component from Cygwin to algebra.",
    "created_at": "2008-04-05T17:03:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2810",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2810#issuecomment-19284",
    "user": "mabshoff"
}
```

Changing component from Cygwin to algebra.



---

archive/issue_comments_019285.json:
```json
{
    "body": "Changing assignee from mabshoff to tbd.",
    "created_at": "2008-04-05T17:03:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2810",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2810#issuecomment-19285",
    "user": "mabshoff"
}
```

Changing assignee from mabshoff to tbd.



---

archive/issue_comments_019286.json:
```json
{
    "body": "Looks good.\n\nIt causes a small doctest failure on line 95 of schemes/elliptic_curves/gp_cremona.py, since in elliptic_curve_finite_field you have gotten rid of _cremona_abgrp_data().  I think that doctest should just be removed from gp_cremona.py anyway, but I don't know whether you have good reasons to keep it around.\n\nAnyway, after this doctest failure gets fixed one way or another I'm happy to give this a positive review.",
    "created_at": "2008-04-05T19:06:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2810",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2810#issuecomment-19286",
    "user": "@aghitza"
}
```

Looks good.

It causes a small doctest failure on line 95 of schemes/elliptic_curves/gp_cremona.py, since in elliptic_curve_finite_field you have gotten rid of _cremona_abgrp_data().  I think that doctest should just be removed from gp_cremona.py anyway, but I don't know whether you have good reasons to keep it around.

Anyway, after this doctest failure gets fixed one way or another I'm happy to give this a positive review.



---

archive/issue_comments_019287.json:
```json
{
    "body": "Sorry, I forgot to trim gp_cremona.py.\n\nThe only useful bits left in there now that the elliptic curves mod p construction is redundant are (1) analytic rank and (2) isogenies.\n\nIn both cases I regrard these as temporary, waiting bettwe implementations in Sage.\n\nFor the moement you can delete that one test which refers to ._cremona_abgrp_data().  But in fact you can also delete ellinit(e,p) and ellzp(e,p) too, and then that might require further trimming in other elliptic curves files.\n\nI'll do it tomorrow.",
    "created_at": "2008-04-05T20:34:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2810",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2810#issuecomment-19287",
    "user": "@JohnCremona"
}
```

Sorry, I forgot to trim gp_cremona.py.

The only useful bits left in there now that the elliptic curves mod p construction is redundant are (1) analytic rank and (2) isogenies.

In both cases I regrard these as temporary, waiting bettwe implementations in Sage.

For the moement you can delete that one test which refers to ._cremona_abgrp_data().  But in fact you can also delete ellinit(e,p) and ellzp(e,p) too, and then that might require further trimming in other elliptic curves files.

I'll do it tomorrow.



---

archive/issue_comments_019288.json:
```json
{
    "body": "Replying to [comment:4 cremona]:\n> Sorry, I forgot to trim gp_cremona.py.\n> \n> The only useful bits left in there now that the elliptic curves mod p construction is redundant are (1) analytic rank and (2) isogenies.\n> \n> In both cases I regrard these as temporary, waiting bettwe implementations in Sage.\n> \n> For the moement you can delete that one test which refers to ._cremona_abgrp_data().  But in fact you can also delete ellinit(e,p) and ellzp(e,p) too, and then that might require further trimming in other elliptic curves files.\n> \n\nOn second thoughts we should still keep those in -- they provide the Weil pairing, which people regularly ask for, and it just needs a wrapper to my gp code to do that.\n\n> I'll do it tomorrow.",
    "created_at": "2008-04-05T22:23:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2810",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2810#issuecomment-19288",
    "user": "@JohnCremona"
}
```

Replying to [comment:4 cremona]:
> Sorry, I forgot to trim gp_cremona.py.
> 
> The only useful bits left in there now that the elliptic curves mod p construction is redundant are (1) analytic rank and (2) isogenies.
> 
> In both cases I regrard these as temporary, waiting bettwe implementations in Sage.
> 
> For the moement you can delete that one test which refers to ._cremona_abgrp_data().  But in fact you can also delete ellinit(e,p) and ellzp(e,p) too, and then that might require further trimming in other elliptic curves files.
> 

On second thoughts we should still keep those in -- they provide the Weil pairing, which people regularly ask for, and it just needs a wrapper to my gp code to do that.

> I'll do it tomorrow.



---

archive/issue_comments_019289.json:
```json
{
    "body": "**Review**\n* patch applies cleanly, looks good\n* I'll provide a fix for the `._cremona_abgrp_data()` in a sec.\n* I say apply.",
    "created_at": "2008-04-05T22:57:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2810",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2810#issuecomment-19289",
    "user": "@malb"
}
```

**Review**
* patch applies cleanly, looks good
* I'll provide a fix for the `._cremona_abgrp_data()` in a sec.
* I say apply.



---

archive/issue_comments_019290.json:
```json
{
    "body": "Attachment [fixes_for_trac_2810_generic_code_ell_curve.patch](tarball://root/attachments/some-uuid/ticket2810/fixes_for_trac_2810_generic_code_ell_curve.patch) by @malb created at 2008-04-05 22:59:34",
    "created_at": "2008-04-05T22:59:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2810",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2810#issuecomment-19290",
    "user": "@malb"
}
```

Attachment [fixes_for_trac_2810_generic_code_ell_curve.patch](tarball://root/attachments/some-uuid/ticket2810/fixes_for_trac_2810_generic_code_ell_curve.patch) by @malb created at 2008-04-05 22:59:34



---

archive/issue_comments_019291.json:
```json
{
    "body": "Doctests pass with both patches applied.\n\nCheers,\n\nMichael",
    "created_at": "2008-04-05T23:38:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2810",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2810#issuecomment-19291",
    "user": "mabshoff"
}
```

Doctests pass with both patches applied.

Cheers,

Michael



---

archive/issue_comments_019292.json:
```json
{
    "body": "Merged in Sage 3.0.alpha2",
    "created_at": "2008-04-05T23:38:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2810",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2810#issuecomment-19292",
    "user": "mabshoff"
}
```

Merged in Sage 3.0.alpha2



---

archive/issue_comments_019293.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-04-05T23:38:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2810",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2810#issuecomment-19293",
    "user": "mabshoff"
}
```

Resolution: fixed

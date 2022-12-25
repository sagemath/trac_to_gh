# Issue 8332: Changes FiniteField_givaro to Python

archive/issues_008332.json:
```json
{
    "body": "Assignee: @aghitza\n\nResidue fields and others would like to be able to multiply inherit from finite field parents.  This is the first of the two switches needed to enable that (the other being sage.rings.finite_rings.element_ntl_gf2e.FiniteField_ntl_gf2e).\n\nThis depends on 8218.\n\nIssue created by migration from https://trac.sagemath.org/ticket/8332\n\n",
    "created_at": "2010-02-23T14:48:18Z",
    "labels": [
        "component: algebra"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.4",
    "title": "Changes FiniteField_givaro to Python",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/8332",
    "user": "https://github.com/roed314"
}
```
Assignee: @aghitza

Residue fields and others would like to be able to multiply inherit from finite field parents.  This is the first of the two switches needed to enable that (the other being sage.rings.finite_rings.element_ntl_gf2e.FiniteField_ntl_gf2e).

This depends on 8218.

Issue created by migration from https://trac.sagemath.org/ticket/8332





---

archive/issue_comments_074071.json:
```json
{
    "body": "Attachment [trac_8332_givaro_python.patch](tarball://root/attachments/some-uuid/ticket8332/trac_8332_givaro_python.patch) by @roed314 created at 2010-02-23 14:50:58",
    "created_at": "2010-02-23T14:50:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8332",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8332#issuecomment-74071",
    "user": "https://github.com/roed314"
}
```

Attachment [trac_8332_givaro_python.patch](tarball://root/attachments/some-uuid/ticket8332/trac_8332_givaro_python.patch) by @roed314 created at 2010-02-23 14:50:58



---

archive/issue_comments_074072.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-02-23T14:52:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8332",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8332#issuecomment-74072",
    "user": "https://github.com/roed314"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_074073.json:
```json
{
    "body": "Part of a series:\n\n```\n8218 -> 8332 -> 7880 -> 7883 -> 8333 -> 8334 -> 8335\n```\nI tried to make each of these mostly self contained, with doctests passing after every ticket, but I didn't entirely succeed.  If you're reviewing one of these tickets, applying later tickets will hopefully fix doctest failures that you're seeing.",
    "created_at": "2010-02-23T17:38:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8332",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8332#issuecomment-74073",
    "user": "https://github.com/roed314"
}
```

Part of a series:

```
8218 -> 8332 -> 7880 -> 7883 -> 8333 -> 8334 -> 8335
```
I tried to make each of these mostly self contained, with doctests passing after every ticket, but I didn't entirely succeed.  If you're reviewing one of these tickets, applying later tickets will hopefully fix doctest failures that you're seeing.



---

archive/issue_comments_074074.json:
```json
{
    "body": "This applies fine to 4.3.4.rc0 (on top of 8218), and all doctests pass on 64-bit Linux except for a tiny failure in sage/structure/parent.pyx. This is just because some random code has used `GF(9,'a')` as an example of a Cython object, so it's trivial to fix. I am still waiting for Sage to build on T2, and once that happens I will test this there as well, but if that passes I think this is fine to go in.",
    "created_at": "2010-03-17T20:03:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8332",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8332#issuecomment-74074",
    "user": "https://github.com/loefflerd"
}
```

This applies fine to 4.3.4.rc0 (on top of 8218), and all doctests pass on 64-bit Linux except for a tiny failure in sage/structure/parent.pyx. This is just because some random code has used `GF(9,'a')` as an example of a Cython object, so it's trivial to fix. I am still waiting for Sage to build on T2, and once that happens I will test this there as well, but if that passes I think this is fine to go in.



---

archive/issue_comments_074075.json:
```json
{
    "body": "(BTW, the aforementioned failure doesn't seem to be dealt with by any of the other tickets in the series -- none of them change that line of code.)",
    "created_at": "2010-03-17T20:04:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8332",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8332#issuecomment-74075",
    "user": "https://github.com/loefflerd"
}
```

(BTW, the aforementioned failure doesn't seem to be dealt with by any of the other tickets in the series -- none of them change that line of code.)



---

archive/issue_comments_074076.json:
```json
{
    "body": "apply over previous patch",
    "created_at": "2010-04-04T14:27:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8332",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8332#issuecomment-74076",
    "user": "https://github.com/loefflerd"
}
```

apply over previous patch



---

archive/issue_comments_074077.json:
```json
{
    "body": "Attachment [trac_8332_fix.patch](tarball://root/attachments/some-uuid/ticket8332/trac_8332_fix.patch) by @loefflerd created at 2010-04-04 14:33:38\n\nHere is a tiny patch to fix that failure. With this patch installed, all tests (including long) pass on selmer.warwick.ac.uk (Ubuntu x86_64), except an unrelated existing problem in sage/schemes/elliptic_curves/heegner.py; and a selection of tests in sage/rings/finite_rings pass on t2.math.washington.edu (Solaris) as well.",
    "created_at": "2010-04-04T14:33:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8332",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8332#issuecomment-74077",
    "user": "https://github.com/loefflerd"
}
```

Attachment [trac_8332_fix.patch](tarball://root/attachments/some-uuid/ticket8332/trac_8332_fix.patch) by @loefflerd created at 2010-04-04 14:33:38

Here is a tiny patch to fix that failure. With this patch installed, all tests (including long) pass on selmer.warwick.ac.uk (Ubuntu x86_64), except an unrelated existing problem in sage/schemes/elliptic_curves/heegner.py; and a selection of tests in sage/rings/finite_rings pass on t2.math.washington.edu (Solaris) as well.



---

archive/issue_comments_074078.json:
```json
{
    "body": "Changing assignee from @aghitza to @loefflerd.",
    "created_at": "2010-04-04T14:33:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8332",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8332#issuecomment-74078",
    "user": "https://github.com/loefflerd"
}
```

Changing assignee from @aghitza to @loefflerd.



---

archive/issue_comments_074079.json:
```json
{
    "body": "I applied both patches on top of a 4.3.5 build on 32-bit ubuntu, after previously applying the relevant bundle & patches from #8128.\n\nWith the first patch I tested all and found only the one failure mentioned aboue in sage/structures/parent.pyx.  With the second patch this now passes.\n\nPositive review!  Now on to #7880...",
    "created_at": "2010-04-05T13:52:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8332",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8332#issuecomment-74079",
    "user": "https://github.com/JohnCremona"
}
```

I applied both patches on top of a 4.3.5 build on 32-bit ubuntu, after previously applying the relevant bundle & patches from #8128.

With the first patch I tested all and found only the one failure mentioned aboue in sage/structures/parent.pyx.  With the second patch this now passes.

Positive review!  Now on to #7880...



---

archive/issue_comments_074080.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-04-05T13:52:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8332",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8332#issuecomment-74080",
    "user": "https://github.com/JohnCremona"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_074081.json:
```json
{
    "body": "Replying to [comment:6 cremona]:\n> I applied both patches on top of a 4.3.5 build on 32-bit ubuntu, after previously applying the relevant bundle & patches from #8128.\n> \n> With the first patch I tested all and found only the one failure mentioned aboue in sage/structures/parent.pyx.  With the second patch this now passes.\n> \n> Positive review!  Now on to #7880...\n\n\nSorry that should read #8218.",
    "created_at": "2010-04-05T13:52:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8332",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8332#issuecomment-74081",
    "user": "https://github.com/JohnCremona"
}
```

Replying to [comment:6 cremona]:
> I applied both patches on top of a 4.3.5 build on 32-bit ubuntu, after previously applying the relevant bundle & patches from #8128.
> 
> With the first patch I tested all and found only the one failure mentioned aboue in sage/structures/parent.pyx.  With the second patch this now passes.
> 
> Positive review!  Now on to #7880...


Sorry that should read #8218.



---

archive/issue_events_019948.json:
```json
{
    "actor": "https://github.com/jhpalmieri",
    "created_at": "2010-04-15T23:40:56Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/8332",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/8332#event-19948"
}
```



---

archive/issue_comments_074082.json:
```json
{
    "body": "Merged into 4.4.alpha0:\n- trac_8332_givaro_python.patch\n- trac_8332_fix.patch",
    "created_at": "2010-04-15T23:40:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8332",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8332#issuecomment-74082",
    "user": "https://github.com/jhpalmieri"
}
```

Merged into 4.4.alpha0:
- trac_8332_givaro_python.patch
- trac_8332_fix.patch



---

archive/issue_comments_074083.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-04-15T23:40:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8332",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8332#issuecomment-74083",
    "user": "https://github.com/jhpalmieri"
}
```

Resolution: fixed

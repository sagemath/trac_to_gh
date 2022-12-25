# Issue 7751: Kazhdan-Lusztig polynomials, Bruhat order, and related features [with patch, needs review]

archive/issues_007751.json:
```json
{
    "body": "Assignee: @aghitza\n\nCC:  sage-combinat\n\nKeywords: Kazhdan-Lusztig, Bruhat order\n\nThis patch includes algorithms for the Bruhat order, Kazhdan-Lusztig polynomials, improvements to the `__repr__` method of WeylGroup elements, and other enhancements.\n\nSome of the methods should be moved to `coxeter_group.py`.\n\nMike Hansen is working on an interface to coxeter3, which is be able to compute Kazhdan-Lusztig polynomials rather faster. However I think this patch still contains things that are needed.\n\nFor discussion see this thread:\n\nhttp://groups.google.com/group/sage-combinat-devel/browse_thread/thread/d324f6fcb6d2a436?hl=en\n\nIssue created by migration from https://trac.sagemath.org/ticket/7751\n\n",
    "created_at": "2009-12-22T21:56:00Z",
    "labels": [
        "component: algebra"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.3.3",
    "title": "Kazhdan-Lusztig polynomials, Bruhat order, and related features [with patch, needs review]",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/7751",
    "user": "https://github.com/dwbump"
}
```
Assignee: @aghitza

CC:  sage-combinat

Keywords: Kazhdan-Lusztig, Bruhat order

This patch includes algorithms for the Bruhat order, Kazhdan-Lusztig polynomials, improvements to the `__repr__` method of WeylGroup elements, and other enhancements.

Some of the methods should be moved to `coxeter_group.py`.

Mike Hansen is working on an interface to coxeter3, which is be able to compute Kazhdan-Lusztig polynomials rather faster. However I think this patch still contains things that are needed.

For discussion see this thread:

http://groups.google.com/group/sage-combinat-devel/browse_thread/thread/d324f6fcb6d2a436?hl=en

Issue created by migration from https://trac.sagemath.org/ticket/7751





---

archive/issue_comments_066627.json:
```json
{
    "body": "Changing component from algebra to combinatorics.",
    "created_at": "2009-12-22T22:54:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7751",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7751#issuecomment-66627",
    "user": "https://github.com/dwbump"
}
```

Changing component from algebra to combinatorics.



---

archive/issue_comments_066628.json:
```json
{
    "body": "Changing assignee from @aghitza to @dwbump.",
    "created_at": "2009-12-22T22:54:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7751",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7751#issuecomment-66628",
    "user": "https://github.com/dwbump"
}
```

Changing assignee from @aghitza to @dwbump.



---

archive/issue_comments_066629.json:
```json
{
    "body": "I made a minor change so that the Kazhdan-Lusztig computation doesn't\nhang in the affine case. I've only done much testing for finite Weyl groups\nbut I suppose it is correct in the affine case.",
    "created_at": "2009-12-23T15:02:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7751",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7751#issuecomment-66629",
    "user": "https://github.com/dwbump"
}
```

I made a minor change so that the Kazhdan-Lusztig computation doesn't
hang in the affine case. I've only done much testing for finite Weyl groups
but I suppose it is correct in the affine case.



---

archive/issue_comments_066630.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-01-03T05:26:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7751",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7751#issuecomment-66630",
    "user": "https://github.com/dwbump"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_066631.json:
```json
{
    "body": "I have revised the patch. It now depends on #7753 and #7754. The revised patch makes use of the Bruhat order as implemented in #7753 and makes the Kazhdan-Lusztig polynomials using ``@`cached_method`. Other changes allow the base ring to be a `LaurentPolynomialRing`.\n\nThe patch is much faster now, something like 50% faster.",
    "created_at": "2010-01-03T05:26:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7751",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7751#issuecomment-66631",
    "user": "https://github.com/dwbump"
}
```

I have revised the patch. It now depends on #7753 and #7754. The revised patch makes use of the Bruhat order as implemented in #7753 and makes the Kazhdan-Lusztig polynomials using ``@`cached_method`. Other changes allow the base ring to be a `LaurentPolynomialRing`.

The patch is much faster now, something like 50% faster.



---

archive/issue_comments_066632.json:
```json
{
    "body": "Rebased to Sage 4.3.1.",
    "created_at": "2010-01-23T12:49:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7751",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7751#issuecomment-66632",
    "user": "https://github.com/dwbump"
}
```

Rebased to Sage 4.3.1.



---

archive/issue_comments_066633.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2010-02-09T04:27:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7751",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7751#issuecomment-66633",
    "user": "https://github.com/roed314"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_066634.json:
```json
{
    "body": "Looks good.  Here are a few comments.  After these are addressed, I'll be happy to give this a positive review.\n\n* `sage/combinat/kazhdan_lusztig.py`\n  * typo in your e-mail address.\n  * the method of determining KL._base_ring_type seems a little strange.  Why not use is_Polynomial and isinstance(q, LaurentPolynomial)?\n  * KazhdanLusztigPolynomial should inherit from SageObject.  That allows pickling, etc.\n\n* `sage/combinat/root_system/weyl_group.py`\n  *In `WeylGroup_gens`, `__classcall_` needs another trailing underscore.  Include a doctest to make sure that this feature works!\n  * Can you include a doctest in `WeylGroupElement.__repr__`?  I know it's tested elsewhere, but...\n\nIn general, do you have a reason to use `__call__` explicitly, rather than parentheses?  Similarly, you don't need to explicitly call __repr__: using %s in a string will do that for you automatically.",
    "created_at": "2010-02-09T04:27:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7751",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7751#issuecomment-66634",
    "user": "https://github.com/roed314"
}
```

Looks good.  Here are a few comments.  After these are addressed, I'll be happy to give this a positive review.

* `sage/combinat/kazhdan_lusztig.py`
  * typo in your e-mail address.
  * the method of determining KL._base_ring_type seems a little strange.  Why not use is_Polynomial and isinstance(q, LaurentPolynomial)?
  * KazhdanLusztigPolynomial should inherit from SageObject.  That allows pickling, etc.

* `sage/combinat/root_system/weyl_group.py`
  *In `WeylGroup_gens`, `__classcall_` needs another trailing underscore.  Include a doctest to make sure that this feature works!
  * Can you include a doctest in `WeylGroupElement.__repr__`?  I know it's tested elsewhere, but...

In general, do you have a reason to use `__call__` explicitly, rather than parentheses?  Similarly, you don't need to explicitly call __repr__: using %s in a string will do that for you automatically.



---

archive/issue_comments_066635.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2010-02-11T01:45:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7751",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7751#issuecomment-66635",
    "user": "https://github.com/dwbump"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_066636.json:
```json
{
    "body": "I addressed most of David Roe's comments.\n\nBut the email address is not a typo.\n\nBrant Jones is also looking at the patch.",
    "created_at": "2010-02-11T01:45:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7751",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7751#issuecomment-66636",
    "user": "https://github.com/dwbump"
}
```

I addressed most of David Roe's comments.

But the email address is not a typo.

Brant Jones is also looking at the patch.



---

archive/issue_comments_066637.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-02-11T03:40:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7751",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7751#issuecomment-66637",
    "user": "https://trac.sagemath.org/admin/accounts/users/brant.c.jones"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_066638.json:
```json
{
    "body": "Patch review: trac_7751\n\nThis patch implements Kazhdan--Lusztig polynomials and R-polynomials associated to pairs of Weyl group elements in arbitrary type using standard recursive formulas.  I have verified the results of this code against the Kazhdan--Lusztig polynomials produced by GAP/Chevie for all pairs of elements in finite type A_4.  I also verified this code against GAP/Chevie for all pairs in affine type A_2 (having 3 generators) for all pairs of elements with Coxeter length less than or equal to 5.  This patch correctly implements useful mathematics and the documentation includes references to relevant mathematical literature.  \n\n-- Brant Jones",
    "created_at": "2010-02-11T03:40:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7751",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7751#issuecomment-66638",
    "user": "https://trac.sagemath.org/admin/accounts/users/brant.c.jones"
}
```

Patch review: trac_7751

This patch implements Kazhdan--Lusztig polynomials and R-polynomials associated to pairs of Weyl group elements in arbitrary type using standard recursive formulas.  I have verified the results of this code against the Kazhdan--Lusztig polynomials produced by GAP/Chevie for all pairs of elements in finite type A_4.  I also verified this code against GAP/Chevie for all pairs in affine type A_2 (having 3 generators) for all pairs of elements with Coxeter length less than or equal to 5.  This patch correctly implements useful mathematics and the documentation includes references to relevant mathematical literature.  

-- Brant Jones



---

archive/issue_comments_066639.json:
```json
{
    "body": "Remove assignee @dwbump.",
    "created_at": "2010-02-11T06:37:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7751",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7751#issuecomment-66639",
    "user": "https://github.com/roed314"
}
```

Remove assignee @dwbump.



---

archive/issue_comments_066640.json:
```json
{
    "body": "I agree.  Positive review.",
    "created_at": "2010-02-11T06:37:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7751",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7751#issuecomment-66640",
    "user": "https://github.com/roed314"
}
```

I agree.  Positive review.



---

archive/issue_comments_066641.json:
```json
{
    "body": "Applying the patch to [this\u00a0hierarchy](http://trac.sagemath.org/sage_trac/ticket/8186#comment:8) (minus #8232), I get\n\n```\npatching file sage/combinat/root_system/weyl_group.py\nHunk #5 FAILED at 145\n1 out of 13 hunks FAILED -- saving rejects to file sage/combinat/root_system/weyl_group.py.rej\n```\n\nThe reject:\n\n```diff\n--- weyl_group.py\n+++ weyl_group.py\n@@ -138,6 +146,7 @@\n         self.n = lattice.dimension() # Really needed?\n         # MatrixGroup_gens takes plain matrices as input. So we can't do:\n         #MatrixGroup_gens.__init__(self, list(self.simple_reflections()))\n+        self._prefix = prefix\n         MatrixGroup_gens.__init__(self, [self.morphism_matrix(self.lattice().si\nmple_reflection(i)) for i in self.index_set()])\n \n     @cached_method\n```\n",
    "created_at": "2010-02-11T13:38:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7751",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7751#issuecomment-66641",
    "user": "https://github.com/qed777"
}
```

Applying the patch to [this hierarchy](http://trac.sagemath.org/sage_trac/ticket/8186#comment:8) (minus #8232), I get

```
patching file sage/combinat/root_system/weyl_group.py
Hunk #5 FAILED at 145
1 out of 13 hunks FAILED -- saving rejects to file sage/combinat/root_system/weyl_group.py.rej
```

The reject:

```diff
--- weyl_group.py
+++ weyl_group.py
@@ -138,6 +146,7 @@
         self.n = lattice.dimension() # Really needed?
         # MatrixGroup_gens takes plain matrices as input. So we can't do:
         #MatrixGroup_gens.__init__(self, list(self.simple_reflections()))
+        self._prefix = prefix
         MatrixGroup_gens.__init__(self, [self.morphism_matrix(self.lattice().si
mple_reflection(i)) for i in self.index_set()])
 
     @cached_method
```




---

archive/issue_comments_066642.json:
```json
{
    "body": "If this conflict occurs, you may resolve just making sure the line\n`self._prefix = prefix` occurs somewhere in the __init__ method of\nWeylGroup.",
    "created_at": "2010-02-12T13:23:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7751",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7751#issuecomment-66642",
    "user": "https://github.com/dwbump"
}
```

If this conflict occurs, you may resolve just making sure the line
`self._prefix = prefix` occurs somewhere in the __init__ method of
WeylGroup.



---

archive/issue_comments_066643.json:
```json
{
    "body": "Correction: the line self._prefix = prefix should be somewhere in the init method of `WeylGroup_gens`\n(not `WeylGroup`).",
    "created_at": "2010-02-12T14:20:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7751",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7751#issuecomment-66643",
    "user": "https://github.com/dwbump"
}
```

Correction: the line self._prefix = prefix should be somewhere in the init method of `WeylGroup_gens`
(not `WeylGroup`).



---

archive/issue_comments_066644.json:
```json
{
    "body": "Kazhdan-Lusztig polynomials, Bruhat order, improved `__repr__` for WeylGroups.",
    "created_at": "2010-02-13T01:25:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7751",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7751#issuecomment-66644",
    "user": "https://github.com/dwbump"
}
```

Kazhdan-Lusztig polynomials, Bruhat order, improved `__repr__` for WeylGroups.



---

archive/issue_comments_066645.json:
```json
{
    "body": "Attachment [kazhdan_lusztig.patch](tarball://root/attachments/some-uuid/ticket7751/kazhdan_lusztig.patch) by @dwbump created at 2010-02-13 01:26:45\n\nPatch rebased to sage-4.3.3.alpha0. This fixes the conflict\nreported by mpatel with no other changes.",
    "created_at": "2010-02-13T01:26:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7751",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7751#issuecomment-66645",
    "user": "https://github.com/dwbump"
}
```

Attachment [kazhdan_lusztig.patch](tarball://root/attachments/some-uuid/ticket7751/kazhdan_lusztig.patch) by @dwbump created at 2010-02-13 01:26:45

Patch rebased to sage-4.3.3.alpha0. This fixes the conflict
reported by mpatel with no other changes.



---

archive/issue_events_007963.json:
```json
{
    "actor": "mvngu",
    "created_at": "2010-02-14T14:33:11Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/7751",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/7751#event-7963"
}
```



---

archive/issue_comments_066646.json:
```json
{
    "body": "Daniel, I have committed the attachment [kazhdan_lusztig.patch](http://trac.sagemath.org/sage_trac/attachment/ticket/7751/kazhdan_lusztig.patch) in your name, since the patch doesn't contain your full name.",
    "created_at": "2010-02-14T14:33:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7751",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7751#issuecomment-66646",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

Daniel, I have committed the attachment [kazhdan_lusztig.patch](http://trac.sagemath.org/sage_trac/attachment/ticket/7751/kazhdan_lusztig.patch) in your name, since the patch doesn't contain your full name.



---

archive/issue_comments_066647.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-02-14T14:33:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7751",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7751#issuecomment-66647",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

Resolution: fixed

# Issue 8333: Finite fields to new coercion model

archive/issues_008333.json:
```json
{
    "body": "Assignee: AlexGhitza\n\nMoves finite fields to the new coercion model.\n\nIssue created by migration from https://trac.sagemath.org/ticket/8333\n\n",
    "created_at": "2010-02-23T15:07:26Z",
    "labels": [
        "algebra",
        "major",
        "enhancement"
    ],
    "title": "Finite fields to new coercion model",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/8333",
    "user": "roed"
}
```
Assignee: AlexGhitza

Moves finite fields to the new coercion model.

Issue created by migration from https://trac.sagemath.org/ticket/8333





---

archive/issue_comments_074208.json:
```json
{
    "body": "Attachment [8333_parent_init.patch](tarball://root/attachments/some-uuid/ticket8333/8333_parent_init.patch) by roed created at 2010-02-23 15:10:25",
    "created_at": "2010-02-23T15:10:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8333",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8333#issuecomment-74208",
    "user": "roed"
}
```

Attachment [8333_parent_init.patch](tarball://root/attachments/some-uuid/ticket8333/8333_parent_init.patch) by roed created at 2010-02-23 15:10:25



---

archive/issue_comments_074209.json:
```json
{
    "body": "Attachment [8333_finite_fields_to_new_coercion.patch](tarball://root/attachments/some-uuid/ticket8333/8333_finite_fields_to_new_coercion.patch) by roed created at 2010-02-23 17:37:44\n\nThe two patches can be applied in either order.",
    "created_at": "2010-02-23T17:37:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8333",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8333#issuecomment-74209",
    "user": "roed"
}
```

Attachment [8333_finite_fields_to_new_coercion.patch](tarball://root/attachments/some-uuid/ticket8333/8333_finite_fields_to_new_coercion.patch) by roed created at 2010-02-23 17:37:44

The two patches can be applied in either order.



---

archive/issue_comments_074210.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-02-23T17:37:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8333",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8333#issuecomment-74210",
    "user": "roed"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_074211.json:
```json
{
    "body": "Part of a series:\n\n```\n8218 -> 8332 -> 7880 -> 7883 -> 8333 -> 8334 -> 8335\n```\n\nI tried to make each of these mostly self contained, with doctests passing after every ticket, but I didn't entirely succeed.  If you're reviewing one of these tickets, applying later tickets will hopefully fix doctest failures that you're seeing.",
    "created_at": "2010-02-23T17:37:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8333",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8333#issuecomment-74211",
    "user": "roed"
}
```

Part of a series:

```
8218 -> 8332 -> 7880 -> 7883 -> 8333 -> 8334 -> 8335
```

I tried to make each of these mostly self contained, with doctests passing after every ticket, but I didn't entirely succeed.  If you're reviewing one of these tickets, applying later tickets will hopefully fix doctest failures that you're seeing.



---

archive/issue_comments_074212.json:
```json
{
    "body": "Some strange things going on here. I installed the patches on 4.3.4.rc0 with the preceding patches in the series applied. \n\n(1) It builds fine, but Sage won't start because the patched `finite_field_prime_modn.py` contains the line\n\n```\nfrom sage.rings.integer_mod_ring import IntegerModRing_generic\n```\n\nand that file has been removed by #8218.\n\n(2) There is also a problem in `element_ext_pari.py` caused by the line\n\n```\nelif isinstance(value, FreeModuleElement):\n```\n\nbeing used without FreeModuleElement being imported first. \n\n(3) Next up, there's another issue in `element_ntl_gf2e` caused by trying to import `is_FiniteField` from the wrong place. \n\n(4) I'm getting a bunch of identical errors relating to the Singular library -- it says \n\n```\n File \"/home/masiao/sage-4.3.4.rc0/local/lib/python/site-packages/sage/interfaces/singular.py\", line 672, in has_coerce_map_from_impl\n        raise NotImplementedError\n```\n\n\n(5) Something weird is going on in sage/modular/dirichlet.py which causes an infinite recursion error when reducing an element of a number field modulo a prime; this may well be dealt with by #8334, I haven't checked. Same in three places in sage/schemes/elliptic_curves/ell_point.py and a bunch of other elliptic curves modules, and in sage/rings/residue_field.py\n\n(6) The patch changes a whole load of doctests in sage/libs/flint/zmod_poly_linkage for no apparent reason, and thus causes them to fail. (Are you running a newer FLINT version on your development machine?)\n\n(7)  Various errors in the rings/finite_rings directory, e.g. this one: \n\n```\nFile \"/home/masiao/sage-4.3.4.rc0/local/lib/python/site-packages/sage/rings/finite_rings/finite_field_ext_pari.py\", line 580, in _coerce_map_from_\n        elif self.degree() % K.degree() == 0:\n    NameError: global name 'K' is not defined\n```\n\n\n\nMost of these are trivial, but (4) is beyond my ability to fix. I'm sorry, but that's definitely a \"needs work\".",
    "created_at": "2010-03-18T16:44:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8333",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8333#issuecomment-74212",
    "user": "davidloeffler"
}
```

Some strange things going on here. I installed the patches on 4.3.4.rc0 with the preceding patches in the series applied. 

(1) It builds fine, but Sage won't start because the patched `finite_field_prime_modn.py` contains the line

```
from sage.rings.integer_mod_ring import IntegerModRing_generic
```

and that file has been removed by #8218.

(2) There is also a problem in `element_ext_pari.py` caused by the line

```
elif isinstance(value, FreeModuleElement):
```

being used without FreeModuleElement being imported first. 

(3) Next up, there's another issue in `element_ntl_gf2e` caused by trying to import `is_FiniteField` from the wrong place. 

(4) I'm getting a bunch of identical errors relating to the Singular library -- it says 

```
 File "/home/masiao/sage-4.3.4.rc0/local/lib/python/site-packages/sage/interfaces/singular.py", line 672, in has_coerce_map_from_impl
        raise NotImplementedError
```


(5) Something weird is going on in sage/modular/dirichlet.py which causes an infinite recursion error when reducing an element of a number field modulo a prime; this may well be dealt with by #8334, I haven't checked. Same in three places in sage/schemes/elliptic_curves/ell_point.py and a bunch of other elliptic curves modules, and in sage/rings/residue_field.py

(6) The patch changes a whole load of doctests in sage/libs/flint/zmod_poly_linkage for no apparent reason, and thus causes them to fail. (Are you running a newer FLINT version on your development machine?)

(7)  Various errors in the rings/finite_rings directory, e.g. this one: 

```
File "/home/masiao/sage-4.3.4.rc0/local/lib/python/site-packages/sage/rings/finite_rings/finite_field_ext_pari.py", line 580, in _coerce_map_from_
        elif self.degree() % K.degree() == 0:
    NameError: global name 'K' is not defined
```



Most of these are trivial, but (4) is beyond my ability to fix. I'm sorry, but that's definitely a "needs work".



---

archive/issue_comments_074213.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2010-03-18T16:44:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8333",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8333#issuecomment-74213",
    "user": "davidloeffler"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_074214.json:
```json
{
    "body": "Ah, I see what's going on. Most of these are fixed by the patch `7585_12_1_fixes.patch` at #8334. But that is dependent on #7883, which needs some substantial work.\n\nDavid, I suggest you do one of the following things:\n\n- Fix #7883 as robertwb and I have suggested; once that has a positive review then we can go on and review this ticket and #8334 together.\n\n- Back-port the fixes from #8334 that belong here, and then I will happily review it independently of #7883 and #8334.\n\nDavid",
    "created_at": "2010-03-18T16:56:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8333",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8333#issuecomment-74214",
    "user": "davidloeffler"
}
```

Ah, I see what's going on. Most of these are fixed by the patch `7585_12_1_fixes.patch` at #8334. But that is dependent on #7883, which needs some substantial work.

David, I suggest you do one of the following things:

- Fix #7883 as robertwb and I have suggested; once that has a positive review then we can go on and review this ticket and #8334 together.

- Back-port the fixes from #8334 that belong here, and then I will happily review it independently of #7883 and #8334.

David



---

archive/issue_comments_074215.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2010-09-19T13:21:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8333",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8333#issuecomment-74215",
    "user": "roed"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_074216.json:
```json
{
    "body": "I've addressed your and Robert's suggestions on #7883 I think.  Apply these two patches after the patches at #7883 and before the patches at #8334.  Doctests won't pass until you apply the patches at #8334.  But all three are ready for review.  Sorry for the delay.",
    "created_at": "2010-09-19T13:21:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8333",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8333#issuecomment-74216",
    "user": "roed"
}
```

I've addressed your and Robert's suggestions on #7883 I think.  Apply these two patches after the patches at #7883 and before the patches at #8334.  Doctests won't pass until you apply the patches at #8334.  But all three are ready for review.  Sorry for the delay.



---

archive/issue_comments_074217.json:
```json
{
    "body": "roed, which version of sage are you using? I cannot apply 8333_finite_fields_to_new_coercion.patch cleanly to 4.5.3",
    "created_at": "2010-09-19T16:17:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8333",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8333#issuecomment-74217",
    "user": "lftabera"
}
```

roed, which version of sage are you using? I cannot apply 8333_finite_fields_to_new_coercion.patch cleanly to 4.5.3



---

archive/issue_comments_074218.json:
```json
{
    "body": "I had been using 4.5.2, but I just upgraded and it still applies cleanly.\n\nDid you apply 8333_parent_init.patch first?",
    "created_at": "2010-09-20T03:38:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8333",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8333#issuecomment-74218",
    "user": "roed"
}
```

I had been using 4.5.2, but I just upgraded and it still applies cleanly.

Did you apply 8333_parent_init.patch first?



---

archive/issue_comments_074219.json:
```json
{
    "body": "After applying both patches from #7883 and also 8333_parent_init.patch, I see this in 4.5.3:\n\n```\nsage: hg_sage.import_patch('Downloads/8333_finite_fields_to_new_coercion.patch')\ncd \"/Applications/sage_builds/sage-4.5.3/devel/sage\" && hg status\ncd \"/Applications/sage_builds/sage-4.5.3/devel/sage\" && hg status\ncd \"/Applications/sage_builds/sage-4.5.3/devel/sage\" && hg import   \"/Users/palmieri/Downloads/8333_finite_fields_to_new_coercion.patch\"\napplying /Users/palmieri/Downloads/8333_finite_fields_to_new_coercion.patch\npatching file sage/libs/flint/zmod_poly_linkage.pxi\nHunk #1 FAILED at 455\nHunk #2 FAILED at 470\n2 out of 2 hunks FAILED -- saving rejects to file sage/libs/flint/zmod_poly_linkage.pxi.rej\npatching file sage/rings/finite_rings/finite_field_prime_modn.py\nHunk #1 FAILED at 57\n1 out of 5 hunks FAILED -- saving rejects to file sage/rings/finite_rings/finite_field_prime_modn.py.rej\nabort: patch failed to apply\n```\n\nIn 4.6.alpha1, I see almost the same message:\n\n```\n\nsage: hg_sage.import_patch('Downloads/8333_finite_fields_to_new_coercion.patch')\ncd \"/Applications/sage/devel/sage\" && hg status\ncd \"/Applications/sage/devel/sage\" && hg status\ncd \"/Applications/sage/devel/sage\" && hg import   \"/Users/palmieri/Downloads/8333_finite_fields_to_new_coercion.patch\"\napplying /Users/palmieri/Downloads/8333_finite_fields_to_new_coercion.patch\npatching file sage/libs/flint/zmod_poly_linkage.pxi\nHunk #1 FAILED at 455\nHunk #2 FAILED at 470\n2 out of 2 hunks FAILED -- saving rejects to file sage/libs/flint/zmod_poly_linkage.pxi.rej\npatching file sage/rings/finite_rings/finite_field_ext_pari.py\nHunk #1 succeeded at 243 with fuzz 2 (offset 6 lines).\npatching file sage/rings/finite_rings/finite_field_prime_modn.py\nHunk #1 FAILED at 57\n1 out of 5 hunks FAILED -- saving rejects to file sage/rings/finite_rings/finite_field_prime_modn.py.rej\nabort: patch failed to apply\n```\n",
    "created_at": "2010-09-20T05:19:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8333",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8333#issuecomment-74219",
    "user": "jhpalmieri"
}
```

After applying both patches from #7883 and also 8333_parent_init.patch, I see this in 4.5.3:

```
sage: hg_sage.import_patch('Downloads/8333_finite_fields_to_new_coercion.patch')
cd "/Applications/sage_builds/sage-4.5.3/devel/sage" && hg status
cd "/Applications/sage_builds/sage-4.5.3/devel/sage" && hg status
cd "/Applications/sage_builds/sage-4.5.3/devel/sage" && hg import   "/Users/palmieri/Downloads/8333_finite_fields_to_new_coercion.patch"
applying /Users/palmieri/Downloads/8333_finite_fields_to_new_coercion.patch
patching file sage/libs/flint/zmod_poly_linkage.pxi
Hunk #1 FAILED at 455
Hunk #2 FAILED at 470
2 out of 2 hunks FAILED -- saving rejects to file sage/libs/flint/zmod_poly_linkage.pxi.rej
patching file sage/rings/finite_rings/finite_field_prime_modn.py
Hunk #1 FAILED at 57
1 out of 5 hunks FAILED -- saving rejects to file sage/rings/finite_rings/finite_field_prime_modn.py.rej
abort: patch failed to apply
```

In 4.6.alpha1, I see almost the same message:

```

sage: hg_sage.import_patch('Downloads/8333_finite_fields_to_new_coercion.patch')
cd "/Applications/sage/devel/sage" && hg status
cd "/Applications/sage/devel/sage" && hg status
cd "/Applications/sage/devel/sage" && hg import   "/Users/palmieri/Downloads/8333_finite_fields_to_new_coercion.patch"
applying /Users/palmieri/Downloads/8333_finite_fields_to_new_coercion.patch
patching file sage/libs/flint/zmod_poly_linkage.pxi
Hunk #1 FAILED at 455
Hunk #2 FAILED at 470
2 out of 2 hunks FAILED -- saving rejects to file sage/libs/flint/zmod_poly_linkage.pxi.rej
patching file sage/rings/finite_rings/finite_field_ext_pari.py
Hunk #1 succeeded at 243 with fuzz 2 (offset 6 lines).
patching file sage/rings/finite_rings/finite_field_prime_modn.py
Hunk #1 FAILED at 57
1 out of 5 hunks FAILED -- saving rejects to file sage/rings/finite_rings/finite_field_prime_modn.py.rej
abort: patch failed to apply
```




---

archive/issue_comments_074220.json:
```json
{
    "body": "Rebased against 4.5.3",
    "created_at": "2010-09-20T05:36:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8333",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8333#issuecomment-74220",
    "user": "roed"
}
```

Rebased against 4.5.3



---

archive/issue_comments_074221.json:
```json
{
    "body": "Attachment [8333_finite_fields_to_new_coercion.2.patch](tarball://root/attachments/some-uuid/ticket8333/8333_finite_fields_to_new_coercion.2.patch) by roed created at 2010-09-20 05:37:03\n\nOops.  Try this one.",
    "created_at": "2010-09-20T05:37:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8333",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8333#issuecomment-74221",
    "user": "roed"
}
```

Attachment [8333_finite_fields_to_new_coercion.2.patch](tarball://root/attachments/some-uuid/ticket8333/8333_finite_fields_to_new_coercion.2.patch) by roed created at 2010-09-20 05:37:03

Oops.  Try this one.



---

archive/issue_comments_074222.json:
```json
{
    "body": "I've had a look at this, but with mixed success.\n\nApplying `8333_parent_init.patch` and `8333_finite_fields_to_new_coercion.2.patch` to 4.6.alpha1 on top of the new folded, positively-reviewed patch at #7883, I get one trivial failure (because I backported a hunk of one of these patches to get #7883 to work). This is fine and can happily be ignored. However, it's very broken with just those two patches (Sage won't even start up, because of a broken import statement).\n\nI tried applying all the hunks of `7585_12_1_fixes.2.patch` other than the ones involving residue fields. That almost worked, but not quite: there was still an infinite recursion error occuring in `residue_field.pyx`. \n\nDavid: can you either get this working on its own, or rebase the patches at #8334 so I can review this and #8334 together?",
    "created_at": "2010-09-23T16:16:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8333",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8333#issuecomment-74222",
    "user": "davidloeffler"
}
```

I've had a look at this, but with mixed success.

Applying `8333_parent_init.patch` and `8333_finite_fields_to_new_coercion.2.patch` to 4.6.alpha1 on top of the new folded, positively-reviewed patch at #7883, I get one trivial failure (because I backported a hunk of one of these patches to get #7883 to work). This is fine and can happily be ignored. However, it's very broken with just those two patches (Sage won't even start up, because of a broken import statement).

I tried applying all the hunks of `7585_12_1_fixes.2.patch` other than the ones involving residue fields. That almost worked, but not quite: there was still an infinite recursion error occuring in `residue_field.pyx`. 

David: can you either get this working on its own, or rebase the patches at #8334 so I can review this and #8334 together?



---

archive/issue_comments_074223.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2010-09-23T16:16:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8333",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8333#issuecomment-74223",
    "user": "davidloeffler"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_074224.json:
```json
{
    "body": "I've rebased all the patches against 4.6.alpha1.  Thanks for helping with this!",
    "created_at": "2010-09-23T16:48:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8333",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8333#issuecomment-74224",
    "user": "roed"
}
```

I've rebased all the patches against 4.6.alpha1.  Thanks for helping with this!



---

archive/issue_comments_074225.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2010-09-23T16:48:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8333",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8333#issuecomment-74225",
    "user": "roed"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_074226.json:
```json
{
    "body": "Attachment [trac_8333-finite_fields_coercion_folded.patch](tarball://root/attachments/some-uuid/ticket8333/trac_8333-finite_fields_coercion_folded.patch) by davidloeffler created at 2010-09-24 14:26:31\n\nFolded patch. Apply only this patch. Applies to 4.6.alpha1 + trac_7883-ideals-folded.patch.",
    "created_at": "2010-09-24T14:26:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8333",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8333#issuecomment-74226",
    "user": "davidloeffler"
}
```

Attachment [trac_8333-finite_fields_coercion_folded.patch](tarball://root/attachments/some-uuid/ticket8333/trac_8333-finite_fields_coercion_folded.patch) by davidloeffler created at 2010-09-24 14:26:31

Folded patch. Apply only this patch. Applies to 4.6.alpha1 + trac_7883-ideals-folded.patch.



---

archive/issue_comments_074227.json:
```json
{
    "body": "I've uploaded a folded patch, which should apply cleanly to 4.6.alpha1 on top of the folded patch at #7883. Doctests do not pass if you apply this patch on its own, so **the positive review should be understood to apply to this patch and #8334 together**. See that ticket for precise directions as to which patches to apply.",
    "created_at": "2010-09-24T14:29:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8333",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8333#issuecomment-74227",
    "user": "davidloeffler"
}
```

I've uploaded a folded patch, which should apply cleanly to 4.6.alpha1 on top of the folded patch at #7883. Doctests do not pass if you apply this patch on its own, so **the positive review should be understood to apply to this patch and #8334 together**. See that ticket for precise directions as to which patches to apply.



---

archive/issue_comments_074228.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-09-24T14:29:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8333",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8333#issuecomment-74228",
    "user": "davidloeffler"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_074229.json:
```json
{
    "body": "Right, so we ended up preparing a single folded patch at #8334, so **don't apply any patches from this ticket** but close it when the patch at #8333 is merged.",
    "created_at": "2010-09-24T15:27:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8333",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8333#issuecomment-74229",
    "user": "davidloeffler"
}
```

Right, so we ended up preparing a single folded patch at #8334, so **don't apply any patches from this ticket** but close it when the patch at #8333 is merged.



---

archive/issue_comments_074230.json:
```json
{
    "body": "Resolution: duplicate",
    "created_at": "2010-09-28T11:12:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8333",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8333#issuecomment-74230",
    "user": "mpatel"
}
```

Resolution: duplicate

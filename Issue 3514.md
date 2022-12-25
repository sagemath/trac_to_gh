# Issue 3514: Free modules revision

archive/issues_003514.json:
```json
{
    "body": "Assignee: tbd\n\nCC:  @craigcitro @ncalexan\n\nKeywords: free modules\n\nThis separates quadratic modules into free_quadratic_module.py -- these \nare free modules with a user-specified inner product.\n\nThis adds 100% documentation to free_module.py and free_quadratic_module.py.\n\nTODO: Probably we want to revise free module elements to make efficient use \nof diagonal inner_product_matrices.  I still intend to generalize the inner \nproduct matrix to support different image ring (real, complex, p-adic) for \nthe pairing, as well as integral pairings which are given by rational matrices.\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/3514\n\n",
    "created_at": "2008-06-26T15:28:01Z",
    "labels": [
        "component: algebra"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.1",
    "title": "Free modules revision",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/3514",
    "user": "https://trac.sagemath.org/admin/accounts/users/kohel"
}
```
Assignee: tbd

CC:  @craigcitro @ncalexan

Keywords: free modules

This separates quadratic modules into free_quadratic_module.py -- these 
are free modules with a user-specified inner product.

This adds 100% documentation to free_module.py and free_quadratic_module.py.

TODO: Probably we want to revise free module elements to make efficient use 
of diagonal inner_product_matrices.  I still intend to generalize the inner 
product matrix to support different image ring (real, complex, p-adic) for 
the pairing, as well as integral pairings which are given by rational matrices.


Issue created by migration from https://trac.sagemath.org/ticket/3514





---

archive/issue_comments_024704.json:
```json
{
    "body": "free_modules.patch",
    "created_at": "2008-06-26T15:28:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3514",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3514#issuecomment-24704",
    "user": "https://trac.sagemath.org/admin/accounts/users/kohel"
}
```

free_modules.patch



---

archive/issue_comments_024705.json:
```json
{
    "body": "Attachment [free-modules.patch](tarball://root/attachments/some-uuid/ticket3514/free-modules.patch) by mabshoff created at 2008-06-26 19:02:09",
    "created_at": "2008-06-26T19:02:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3514",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3514#issuecomment-24705",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Attachment [free-modules.patch](tarball://root/attachments/some-uuid/ticket3514/free-modules.patch) by mabshoff created at 2008-06-26 19:02:09



---

archive/issue_comments_024706.json:
```json
{
    "body": "Review by John Cremona:\n\n1.  I read through the code fairly carefully, and was very impressed by the thought which has gone into this.  There are a few typos in docstrings but nothing serious.\n2.  I tried applying the patch to 3.0.4.alpha0 but it failed:\n\n```\napplying /home/jec/free-modules.patch\npatching file sage/modules/free_module.py\nHunk #4 FAILED at 280\nHunk #52 FAILED at 3200\nHunk #54 FAILED at 3310\nHunk #82 FAILED at 4430\nHunk #95 FAILED at 5053\n5 out of 96 hunks FAILED -- saving rejects to file sage/modules/free_module.py.rej\nabort: patch failed to apply\n```\n\nI expect that this is because it is based on a different release.  If I get time I'll try it on 3.0.3, but it would be much better if the author could re-base it!\n\nShould we not have a requirement that the base version for posted patches whould always be specified (like I do...)?",
    "created_at": "2008-06-29T17:49:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3514",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3514#issuecomment-24706",
    "user": "https://github.com/JohnCremona"
}
```

Review by John Cremona:

1.  I read through the code fairly carefully, and was very impressed by the thought which has gone into this.  There are a few typos in docstrings but nothing serious.
2.  I tried applying the patch to 3.0.4.alpha0 but it failed:

```
applying /home/jec/free-modules.patch
patching file sage/modules/free_module.py
Hunk #4 FAILED at 280
Hunk #52 FAILED at 3200
Hunk #54 FAILED at 3310
Hunk #82 FAILED at 4430
Hunk #95 FAILED at 5053
5 out of 96 hunks FAILED -- saving rejects to file sage/modules/free_module.py.rej
abort: patch failed to apply
```

I expect that this is because it is based on a different release.  If I get time I'll try it on 3.0.3, but it would be much better if the author could re-base it!

Should we not have a requirement that the base version for posted patches whould always be specified (like I do...)?



---

archive/issue_comments_024707.json:
```json
{
    "body": "This patch applies to 3.02 (sorry for not specifying, John).\n\nNick Alexander expressed an interest in review this patch, \nand looked over some of it already at SAGE-Devel days.\n\nThis predates changes merging the coercion branch, so should \nfirst be patched to a pre-coercion SAGE.",
    "created_at": "2008-06-30T09:25:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3514",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3514#issuecomment-24707",
    "user": "https://trac.sagemath.org/admin/accounts/users/kohel"
}
```

This patch applies to 3.02 (sorry for not specifying, John).

Nick Alexander expressed an interest in review this patch, 
and looked over some of it already at SAGE-Devel days.

This predates changes merging the coercion branch, so should 
first be patched to a pre-coercion SAGE.



---

archive/issue_comments_024708.json:
```json
{
    "body": "I happened to have a 3.0.2 build lying around, but it fared no better:\n\n```\n\njohn@ubuntu%./sage \n----------------------------------------------------------------------\n----------------------------------------------------------------------\nLoading SAGE library. Current Mercurial branch is: 3514\nsage: hg_sage.apply (\"fre\nfree_module_element     frequency_distribution  \nsage: hg_sage.apply(\"/home/john/free-modules.patch\")\ncd \"/home/john/sage-3.0.2/devel/sage\" && hg status\ncd \"/home/john/sage-3.0.2/devel/sage\" && hg status\ncd \"/home/john/sage-3.0.2/devel/sage\" && hg import   \"/home/john/free-modules.patch\"\napplying /home/john/free-modules.patch\npatching file sage/modules/free_module.py\nHunk #4 FAILED at 280\nHunk #54 FAILED at 3312\nHunk #82 FAILED at 4432\nHunk #95 FAILED at 5055\n4 out of 96 hunks FAILED -- saving rejects to file sage/modules/free_module.py.rej\nabort: patch failed to apply\n```",
    "created_at": "2008-06-30T17:12:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3514",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3514#issuecomment-24708",
    "user": "https://github.com/JohnCremona"
}
```

I happened to have a 3.0.2 build lying around, but it fared no better:

```

john@ubuntu%./sage 
----------------------------------------------------------------------
----------------------------------------------------------------------
Loading SAGE library. Current Mercurial branch is: 3514
sage: hg_sage.apply ("fre
free_module_element     frequency_distribution  
sage: hg_sage.apply("/home/john/free-modules.patch")
cd "/home/john/sage-3.0.2/devel/sage" && hg status
cd "/home/john/sage-3.0.2/devel/sage" && hg status
cd "/home/john/sage-3.0.2/devel/sage" && hg import   "/home/john/free-modules.patch"
applying /home/john/free-modules.patch
patching file sage/modules/free_module.py
Hunk #4 FAILED at 280
Hunk #54 FAILED at 3312
Hunk #82 FAILED at 4432
Hunk #95 FAILED at 5055
4 out of 96 hunks FAILED -- saving rejects to file sage/modules/free_module.py.rej
abort: patch failed to apply
```



---

archive/issue_comments_024709.json:
```json
{
    "body": "Rebased against 3.0.4.alpha1 and fixed all trivial errors/doctest problems.  This now needs review.",
    "created_at": "2008-07-02T00:06:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3514",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3514#issuecomment-24709",
    "user": "https://github.com/garyfurnish"
}
```

Rebased against 3.0.4.alpha1 and fixed all trivial errors/doctest problems.  This now needs review.



---

archive/issue_comments_024710.json:
```json
{
    "body": "The patch posted by Gary does not apply cleanly against 3.0.4.alpha1 or 2:\n\n```\nsage-3.0.4.alpha2/devel/sage$ patch -p1 --dry-run < trac_3514.patch\\?format\\=raw \npatching file sage/modules/all.py\npatching file sage/modules/free_module.py\npatching file sage/modules/free_quadratic_module.py\npatching file sage/modules/quotient_module.py\npatching file sage/coding/code_constructions.py\npatching file sage/modular/modform/hecke_operator_on_qexp.py\npatching file sage/modular/modsym/space.py\npatching file sage/modules/free_module.py\nHunk #1 succeeded at 264 (offset -17 lines).\nHunk #2 succeeded at 289 (offset -17 lines).\nHunk #3 FAILED at 444.\nHunk #4 FAILED at 872.\nHunk #5 FAILED at 3044.\nHunk #6 succeeded at 2843 (offset -390 lines).\nHunk #7 succeeded at 2945 (offset -388 lines).\nHunk #8 FAILED at 3436.\nHunk #9 succeeded at 4140 (offset -927 lines).\nHunk #10 succeeded at 4204 (offset -927 lines).\n4 out of 10 hunks FAILED -- saving rejects to file sage/modules/free_module.py.rej\npatching file sage/modules/quotient_module.py\npatching file sage/rings/number_field/order.py\npatching file sage/schemes/elliptic_curves/period_lattice.py\n```\n\nDavid also posted a diff and Gary's patch commits all of the changes in Gary's name, which is obviously not correct.\n\nCheers,\n\nMichael",
    "created_at": "2008-07-02T20:12:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3514",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3514#issuecomment-24710",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

The patch posted by Gary does not apply cleanly against 3.0.4.alpha1 or 2:

```
sage-3.0.4.alpha2/devel/sage$ patch -p1 --dry-run < trac_3514.patch\?format\=raw 
patching file sage/modules/all.py
patching file sage/modules/free_module.py
patching file sage/modules/free_quadratic_module.py
patching file sage/modules/quotient_module.py
patching file sage/coding/code_constructions.py
patching file sage/modular/modform/hecke_operator_on_qexp.py
patching file sage/modular/modsym/space.py
patching file sage/modules/free_module.py
Hunk #1 succeeded at 264 (offset -17 lines).
Hunk #2 succeeded at 289 (offset -17 lines).
Hunk #3 FAILED at 444.
Hunk #4 FAILED at 872.
Hunk #5 FAILED at 3044.
Hunk #6 succeeded at 2843 (offset -390 lines).
Hunk #7 succeeded at 2945 (offset -388 lines).
Hunk #8 FAILED at 3436.
Hunk #9 succeeded at 4140 (offset -927 lines).
Hunk #10 succeeded at 4204 (offset -927 lines).
4 out of 10 hunks FAILED -- saving rejects to file sage/modules/free_module.py.rej
patching file sage/modules/quotient_module.py
patching file sage/rings/number_field/order.py
patching file sage/schemes/elliptic_curves/period_lattice.py
```

David also posted a diff and Gary's patch commits all of the changes in Gary's name, which is obviously not correct.

Cheers,

Michael



---

archive/issue_comments_024711.json:
```json
{
    "body": "I'll be an editor for this.",
    "created_at": "2008-07-02T21:03:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3514",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3514#issuecomment-24711",
    "user": "https://github.com/mwhansen"
}
```

I'll be an editor for this.



---

archive/issue_comments_024712.json:
```json
{
    "body": "Changing keywords from \"free modules\" to \"free modules editor_mhansen\".",
    "created_at": "2008-07-02T21:03:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3514",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3514#issuecomment-24712",
    "user": "https://github.com/mwhansen"
}
```

Changing keywords from "free modules" to "free modules editor_mhansen".



---

archive/issue_comments_024713.json:
```json
{
    "body": "Attachment [trac_3514.2.patch](tarball://root/attachments/some-uuid/ticket3514/trac_3514.2.patch) by @mwhansen created at 2008-07-09 00:29:23\n\nI've attached trac_3514.2.patch which applies cleanly against 3.0.4.rc0.",
    "created_at": "2008-07-09T00:29:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3514",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3514#issuecomment-24713",
    "user": "https://github.com/mwhansen"
}
```

Attachment [trac_3514.2.patch](tarball://root/attachments/some-uuid/ticket3514/trac_3514.2.patch) by @mwhansen created at 2008-07-09 00:29:23

I've attached trac_3514.2.patch which applies cleanly against 3.0.4.rc0.



---

archive/issue_comments_024714.json:
```json
{
    "body": "Overall, I think that the patch is really good since it adds lots of good documentation and cleans things up by separating out the QuadraticSpaces.  There are a few minor things that I'd like to see addressed:\n\n1) There are a number of \"naked excepts\" on lines 607,2118,2123,2239,2244,... of free_module.py that really should specify the particular type of error they are trying to catch.\n\n2) The tests for a a couple functions that raise NotImplementedErrors do not actually test the function.  The ones I saw were __hash__ on 458, __cmp__ on 770, and echelonized_basis_matrix on 982 of free_module.py.\n\n3) It seems there is a lot of code duplication in the span_of_basis's that could be factored out.\n\n4) The BUG listed on line 4564 actually works fine for me.  On a related note, you need to write special code (using the __reduce__ method) if you want loads(dumps(s)) to be the exact same object as s.  This is relevant to line 111.",
    "created_at": "2008-07-09T00:36:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3514",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3514#issuecomment-24714",
    "user": "https://github.com/mwhansen"
}
```

Overall, I think that the patch is really good since it adds lots of good documentation and cleans things up by separating out the QuadraticSpaces.  There are a few minor things that I'd like to see addressed:

1) There are a number of "naked excepts" on lines 607,2118,2123,2239,2244,... of free_module.py that really should specify the particular type of error they are trying to catch.

2) The tests for a a couple functions that raise NotImplementedErrors do not actually test the function.  The ones I saw were __hash__ on 458, __cmp__ on 770, and echelonized_basis_matrix on 982 of free_module.py.

3) It seems there is a lot of code duplication in the span_of_basis's that could be factored out.

4) The BUG listed on line 4564 actually works fine for me.  On a related note, you need to write special code (using the __reduce__ method) if you want loads(dumps(s)) to be the exact same object as s.  This is relevant to line 111.



---

archive/issue_comments_024715.json:
```json
{
    "body": "I added trac_3514-review.patch that addresses the issues above.  It'd be good for someone to review my new patch -- it should be pretty easy.\n\nI deviated a bit from my own review comments in a few places.\n\n2) I removed __hash__ and __cmp__ since they didn't serve any purpose, but I left echelonized_basis_matrix because the docstring provided nontrivial information for any subclass that hasn't implemented echelonized_basis_matrix.\n\n3) After looking at the code, I thought it was more clear to leave the little bit of duplication that was there.\n\n4) I removed line 111 since loads(dumps()) isn't guaranteed to return the exact same object.",
    "created_at": "2008-08-07T01:26:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3514",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3514#issuecomment-24715",
    "user": "https://github.com/mwhansen"
}
```

I added trac_3514-review.patch that addresses the issues above.  It'd be good for someone to review my new patch -- it should be pretty easy.

I deviated a bit from my own review comments in a few places.

2) I removed __hash__ and __cmp__ since they didn't serve any purpose, but I left echelonized_basis_matrix because the docstring provided nontrivial information for any subclass that hasn't implemented echelonized_basis_matrix.

3) After looking at the code, I thought it was more clear to leave the little bit of duplication that was there.

4) I removed line 111 since loads(dumps()) isn't guaranteed to return the exact same object.



---

archive/issue_comments_024716.json:
```json
{
    "body": "Attachment [trac_3514-review.patch](tarball://root/attachments/some-uuid/ticket3514/trac_3514-review.patch) by @mwhansen created at 2008-08-07 01:26:20",
    "created_at": "2008-08-07T01:26:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3514",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3514#issuecomment-24716",
    "user": "https://github.com/mwhansen"
}
```

Attachment [trac_3514-review.patch](tarball://root/attachments/some-uuid/ticket3514/trac_3514-review.patch) by @mwhansen created at 2008-08-07 01:26:20



---

archive/issue_comments_024717.json:
```json
{
    "body": "Switching the order of the arguments in `span` is backwards incompatible (and I have seen code that will break under this switch). The old ordering should still be accepted even if you want to make it so the basering is optional. \n\nIn that same function, testing {{{\nif not isinstance(R, principal_ideal_domain.PrincipalIdealDomain)\n}}}\n\nis potentially brittle, as there are rings which are PID's depending on their parameters (e.g. polynomial rings, Z/nZ, etc.",
    "created_at": "2008-08-09T07:03:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3514",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3514#issuecomment-24717",
    "user": "https://github.com/robertwb"
}
```

Switching the order of the arguments in `span` is backwards incompatible (and I have seen code that will break under this switch). The old ordering should still be accepted even if you want to make it so the basering is optional. 

In that same function, testing {{{
if not isinstance(R, principal_ideal_domain.PrincipalIdealDomain)
}}}

is potentially brittle, as there are rings which are PID's depending on their parameters (e.g. polynomial rings, Z/nZ, etc.



---

archive/issue_comments_024718.json:
```json
{
    "body": "I read the review patch by Mike Hansen.\nI haven't doctested it.\nI definitely agree with the changes he made though.",
    "created_at": "2008-08-10T22:31:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3514",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3514#issuecomment-24718",
    "user": "https://github.com/williamstein"
}
```

I read the review patch by Mike Hansen.
I haven't doctested it.
I definitely agree with the changes he made though.



---

archive/issue_comments_024719.json:
```json
{
    "body": "The two patches applied after #3652 pass doctests in my current 3.1.alpha1 merge tree. So once we get a positive review here we can finally merge.\n\nCheers,\n\nMichael",
    "created_at": "2008-08-10T22:45:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3514",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3514#issuecomment-24719",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

The two patches applied after #3652 pass doctests in my current 3.1.alpha1 merge tree. So once we get a positive review here we can finally merge.

Cheers,

Michael



---

archive/issue_events_008014.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2008-08-10T22:45:00Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/3514",
    "milestone": "sage-3.1",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/3514#event-8014"
}
```



---

archive/issue_comments_024720.json:
```json
{
    "body": "I think this looks good.  I looked over the original patches, and also mike's comments, and this looks good.  I'm very impressed by the amount of new doctests, etc.  Yeah!",
    "created_at": "2008-08-11T06:17:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3514",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3514#issuecomment-24720",
    "user": "https://github.com/williamstein"
}
```

I think this looks good.  I looked over the original patches, and also mike's comments, and this looks good.  I'm very impressed by the amount of new doctests, etc.  Yeah!



---

archive/issue_comments_024721.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-08-11T06:29:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3514",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3514#issuecomment-24721",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed



---

archive/issue_events_008015.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2008-08-11T06:29:16Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/3514",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/3514#event-8015"
}
```



---

archive/issue_comments_024722.json:
```json
{
    "body": "Merged trac_3514.2.patch and trac_3514-review.patch in Sage 3.1.alpha1",
    "created_at": "2008-08-11T06:29:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3514",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3514#issuecomment-24722",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged trac_3514.2.patch and trac_3514-review.patch in Sage 3.1.alpha1



---

archive/issue_comments_024723.json:
```json
{
    "body": "Robert's comment: \"Switching the order of the arguments in span is backwards incompatible (and I have seen code that will break under this switch). The old ordering should still be accepted even if you want to make it so the basering is optional.\"  \n\nI agree! See patch.",
    "created_at": "2008-08-11T06:33:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3514",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3514#issuecomment-24723",
    "user": "https://github.com/williamstein"
}
```

Robert's comment: "Switching the order of the arguments in span is backwards incompatible (and I have seen code that will break under this switch). The old ordering should still be accepted even if you want to make it so the basering is optional."  

I agree! See patch.



---

archive/issue_comments_024724.json:
```json
{
    "body": "Attachment [sage-3514_span.patch](tarball://root/attachments/some-uuid/ticket3514/sage-3514_span.patch) by mabshoff created at 2008-08-11 06:46:06\n\nMerged sage-3514_span.patch in Sage 3.1.alpha1",
    "created_at": "2008-08-11T06:46:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3514",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3514#issuecomment-24724",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Attachment [sage-3514_span.patch](tarball://root/attachments/some-uuid/ticket3514/sage-3514_span.patch) by mabshoff created at 2008-08-11 06:46:06

Merged sage-3514_span.patch in Sage 3.1.alpha1

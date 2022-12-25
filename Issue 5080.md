# Issue 5080: Bug in decomposing modular symbol subspace

archive/issues_005080.json:
```json
{
    "body": "Assignee: @craigcitro\n\nCC:  @craigcitro\n\n\n```\nsage: E = EllipticCurve(\"128a\") \nsage: E.congruence_number()\n------------------------------------------------------------\nTraceback (most recent call last):\n  File \"<ipython console>\", line 1, in <module>\n  File \"/Users/robert/sage/sage-3.1.3/local/lib/python2.5/site-packages/sage/schemes/elliptic_curves/ell_rational_field.py\", line 2618, in congruence_number\n    self.__congruence_number = W.congruence_number(V)\n  File \"/Users/robert/sage/sage-3.1.3/local/lib/python2.5/site-packages/sage/modular/modsym/space.py\", line 938, in congruence_number\n    W = other.q_expansion_module(prec, ZZ)\n  File \"/Users/robert/sage/sage-3.1.3/local/lib/python2.5/site-packages/sage/modular/modsym/space.py\", line 770, in q_expansion_module\n    return self._q_expansion_module_integral(prec)\n  File \"/Users/robert/sage/sage-3.1.3/local/lib/python2.5/site-packages/sage/modular/modsym/space.py\", line 910, in _q_expansion_module_integral\n    V = self.q_expansion_module(prec, QQ)\n  File \"/Users/robert/sage/sage-3.1.3/local/lib/python2.5/site-packages/sage/modular/modsym/space.py\", line 772, in q_expansion_module\n    return self._q_expansion_module_rational(prec)\n  File \"/Users/robert/sage/sage-3.1.3/local/lib/python2.5/site-packages/sage/modular/modsym/space.py\", line 861, in _q_expansion_module_rational\n    return self._q_expansion_module(prec)\n  File \"/Users/robert/sage/sage-3.1.3/local/lib/python2.5/site-packages/sage/modular/modsym/space.py\", line 820, in _q_expansion_module\n    return A.span([f.padded_list(prec) for f in self.q_expansion_basis(prec, algorithm)])\n  File \"/Users/robert/sage/sage-3.1.3/local/lib/python2.5/site-packages/sage/modular/modsym/space.py\", line 602, in q_expansion_basis\n    return Sequence(self._q_expansion_basis_hecke_dual(prec), cr=True)\n  File \"/Users/robert/sage/sage-3.1.3/local/lib/python2.5/site-packages/sage/modular/modsym/space.py\", line 1073, in _q_expansion_basis_hecke_dual\n    v = [self.dual_hecke_matrix(n).column(i) for n in range(1,prec)]\n  File \"/Users/robert/sage/sage-3.1.3/local/lib/python2.5/site-packages/sage/modular/hecke/module.py\", line 797, in dual_hecke_matrix\n    T = self._compute_dual_hecke_matrix(n)\n  File \"/Users/robert/sage/current/local/lib/python2.5/site-packages/sage/modular/hecke/submodule.py\", line 110, in _compute_dual_hecke_matrix\n    return A.restrict(self.dual_free_module(), check=check)\n  File \"/Users/robert/sage/current/local/lib/python2.5/site-packages/sage/modular/hecke/submodule.py\", line 320, in dual_free_module\n    \"(cut down to rank %s, but should have cut down to rank %s).\"%(V.rank(), self.rank())\nRuntimeError: Computation of embedded dual vector space failed (cut down to rank 9, but should have cut down to rank 8).\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/5080\n\n",
    "created_at": "2009-01-24T00:31:15Z",
    "labels": [
        "component: modular forms",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.1",
    "title": "Bug in decomposing modular symbol subspace",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/5080",
    "user": "https://github.com/robertwb"
}
```
Assignee: @craigcitro

CC:  @craigcitro


```
sage: E = EllipticCurve("128a") 
sage: E.congruence_number()
------------------------------------------------------------
Traceback (most recent call last):
  File "<ipython console>", line 1, in <module>
  File "/Users/robert/sage/sage-3.1.3/local/lib/python2.5/site-packages/sage/schemes/elliptic_curves/ell_rational_field.py", line 2618, in congruence_number
    self.__congruence_number = W.congruence_number(V)
  File "/Users/robert/sage/sage-3.1.3/local/lib/python2.5/site-packages/sage/modular/modsym/space.py", line 938, in congruence_number
    W = other.q_expansion_module(prec, ZZ)
  File "/Users/robert/sage/sage-3.1.3/local/lib/python2.5/site-packages/sage/modular/modsym/space.py", line 770, in q_expansion_module
    return self._q_expansion_module_integral(prec)
  File "/Users/robert/sage/sage-3.1.3/local/lib/python2.5/site-packages/sage/modular/modsym/space.py", line 910, in _q_expansion_module_integral
    V = self.q_expansion_module(prec, QQ)
  File "/Users/robert/sage/sage-3.1.3/local/lib/python2.5/site-packages/sage/modular/modsym/space.py", line 772, in q_expansion_module
    return self._q_expansion_module_rational(prec)
  File "/Users/robert/sage/sage-3.1.3/local/lib/python2.5/site-packages/sage/modular/modsym/space.py", line 861, in _q_expansion_module_rational
    return self._q_expansion_module(prec)
  File "/Users/robert/sage/sage-3.1.3/local/lib/python2.5/site-packages/sage/modular/modsym/space.py", line 820, in _q_expansion_module
    return A.span([f.padded_list(prec) for f in self.q_expansion_basis(prec, algorithm)])
  File "/Users/robert/sage/sage-3.1.3/local/lib/python2.5/site-packages/sage/modular/modsym/space.py", line 602, in q_expansion_basis
    return Sequence(self._q_expansion_basis_hecke_dual(prec), cr=True)
  File "/Users/robert/sage/sage-3.1.3/local/lib/python2.5/site-packages/sage/modular/modsym/space.py", line 1073, in _q_expansion_basis_hecke_dual
    v = [self.dual_hecke_matrix(n).column(i) for n in range(1,prec)]
  File "/Users/robert/sage/sage-3.1.3/local/lib/python2.5/site-packages/sage/modular/hecke/module.py", line 797, in dual_hecke_matrix
    T = self._compute_dual_hecke_matrix(n)
  File "/Users/robert/sage/current/local/lib/python2.5/site-packages/sage/modular/hecke/submodule.py", line 110, in _compute_dual_hecke_matrix
    return A.restrict(self.dual_free_module(), check=check)
  File "/Users/robert/sage/current/local/lib/python2.5/site-packages/sage/modular/hecke/submodule.py", line 320, in dual_free_module
    "(cut down to rank %s, but should have cut down to rank %s)."%(V.rank(), self.rank())
RuntimeError: Computation of embedded dual vector space failed (cut down to rank 9, but should have cut down to rank 8).
```


Issue created by migration from https://trac.sagemath.org/ticket/5080





---

archive/issue_comments_038610.json:
```json
{
    "body": "for the record, here are all the optimal elliptic curves of conductor at most 250 that exhibit the same problem (listed with Cremona labels): 128a1, 128b1, 128c1, 128d1, 144b1, 192a1, 192b1, 192c1, 192d1, 225c1, 225d1, 225e1",
    "created_at": "2009-01-24T01:17:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5080",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5080#issuecomment-38610",
    "user": "https://github.com/aghitza"
}
```

for the record, here are all the optimal elliptic curves of conductor at most 250 that exhibit the same problem (listed with Cremona labels): 128a1, 128b1, 128c1, 128d1, 144b1, 192a1, 192b1, 192c1, 192d1, 225c1, 225d1, 225e1



---

archive/issue_comments_038611.json:
```json
{
    "body": "I have had a careful look at this, and I think I know what's going on. The problem is that for each of these curves, if f is the corresponding newform, then there is a finite set of forms f_1 ... f_m (none of them equal to f) in the space such that for every p, a_p(f) = a_p(f_i) for some i. It was a bit of a surprise to me that this is possible, but it doesn't contradict multiplicity one, and in fact if you take any fixed form and consider its twists by chi1, chi2, and chi1 * chi2 for any two quadratic characters chi1, chi2 of coprime moduli then you get an example.\n\nThis mightily confuses two functions for submodules of Hecke modules: \"complement\" and \"dual_free_module\". The former has a workaround, in that if it can't find a complement using only one Hecke operator at a time, it falls back on calling \"decomposition\" (which is slower, but is immune to this problem) and works out the complement using that. The latter doesn't. But anyway, the two are basically doing the same thing, since the embedded dual free module of a submodule V is by definition the annihilator of the Hecke-stable complement of V (when this exists). So the fix is to get rid of the existing \"dual_free_module\" routine and replace it with a simpler routine that calls \"complement\" and then does some trivial linear algebra.\n\nI will post a patch when I get a chance to code it up.",
    "created_at": "2009-05-13T17:26:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5080",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5080#issuecomment-38611",
    "user": "https://github.com/loefflerd"
}
```

I have had a careful look at this, and I think I know what's going on. The problem is that for each of these curves, if f is the corresponding newform, then there is a finite set of forms f_1 ... f_m (none of them equal to f) in the space such that for every p, a_p(f) = a_p(f_i) for some i. It was a bit of a surprise to me that this is possible, but it doesn't contradict multiplicity one, and in fact if you take any fixed form and consider its twists by chi1, chi2, and chi1 * chi2 for any two quadratic characters chi1, chi2 of coprime moduli then you get an example.

This mightily confuses two functions for submodules of Hecke modules: "complement" and "dual_free_module". The former has a workaround, in that if it can't find a complement using only one Hecke operator at a time, it falls back on calling "decomposition" (which is slower, but is immune to this problem) and works out the complement using that. The latter doesn't. But anyway, the two are basically doing the same thing, since the embedded dual free module of a submodule V is by definition the annihilator of the Hecke-stable complement of V (when this exists). So the fix is to get rid of the existing "dual_free_module" routine and replace it with a simpler routine that calls "complement" and then does some trivial linear algebra.

I will post a patch when I get a chance to code it up.



---

archive/issue_comments_038612.json:
```json
{
    "body": "Attachment [trac_5080.patch](tarball://root/attachments/some-uuid/ticket5080/trac_5080.patch) by @loefflerd created at 2009-05-14 11:42:41\n\napply after #5736, #4357 and #5787",
    "created_at": "2009-05-14T11:42:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5080",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5080#issuecomment-38612",
    "user": "https://github.com/loefflerd"
}
```

Attachment [trac_5080.patch](tarball://root/attachments/some-uuid/ticket5080/trac_5080.patch) by @loefflerd created at 2009-05-14 11:42:41

apply after #5736, #4357 and #5787



---

archive/issue_comments_038613.json:
```json
{
    "body": "Here's a patch.",
    "created_at": "2009-05-14T11:44:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5080",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5080#issuecomment-38613",
    "user": "https://github.com/loefflerd"
}
```

Here's a patch.



---

archive/issue_comments_038614.json:
```json
{
    "body": "I'm about to try this out.  Is there a doctest showing that \n\n```\nsage: E = EllipticCurve(\"128a\") \nsage: E.congruence_number()\n```\n\nnow works?",
    "created_at": "2009-05-18T15:27:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5080",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5080#issuecomment-38614",
    "user": "https://github.com/JohnCremona"
}
```

I'm about to try this out.  Is there a doctest showing that 

```
sage: E = EllipticCurve("128a") 
sage: E.congruence_number()
```

now works?



---

archive/issue_comments_038615.json:
```json
{
    "body": "Replying to [comment:4 cremona]:\n> I'm about to try this out.  Is there a doctest showing that \n> {{{\n> sage: E = EllipticCurve(\"128a\") \n> sage: E.congruence_number()\n> }}}\n> now works?\n\nWhich it does:\n\n```\nsage: sage: E = EllipticCurve(\"128a\")\nsage: sage: E.congruence_number()\n32\n```\n",
    "created_at": "2009-05-18T15:30:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5080",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5080#issuecomment-38615",
    "user": "https://github.com/JohnCremona"
}
```

Replying to [comment:4 cremona]:
> I'm about to try this out.  Is there a doctest showing that 
> {{{
> sage: E = EllipticCurve("128a") 
> sage: E.congruence_number()
> }}}
> now works?

Which it does:

```
sage: sage: E = EllipticCurve("128a")
sage: sage: E.congruence_number()
32
```




---

archive/issue_comments_038616.json:
```json
{
    "body": "Patch looks good, applies fine to 4.0.alpha0 and fixes the bug.  My only quibble is that there is no new doctest to show that the reported bug is fixed.",
    "created_at": "2009-05-18T15:47:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5080",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5080#issuecomment-38616",
    "user": "https://github.com/JohnCremona"
}
```

Patch looks good, applies fine to 4.0.alpha0 and fixes the bug.  My only quibble is that there is no new doctest to show that the reported bug is fixed.



---

archive/issue_comments_038617.json:
```json
{
    "body": "Attachment [trac_5080_doctest.patch](tarball://root/attachments/some-uuid/ticket5080/trac_5080_doctest.patch) by @loefflerd created at 2009-05-18 15:49:12\n\napply after previous patch",
    "created_at": "2009-05-18T15:49:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5080",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5080#issuecomment-38617",
    "user": "https://github.com/loefflerd"
}
```

Attachment [trac_5080_doctest.patch](tarball://root/attachments/some-uuid/ticket5080/trac_5080_doctest.patch) by @loefflerd created at 2009-05-18 15:49:12

apply after previous patch



---

archive/issue_comments_038618.json:
```json
{
    "body": "Sorry, that was very sloppy of me. Here is a patchlet that adds the missing doctest.",
    "created_at": "2009-05-18T15:51:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5080",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5080#issuecomment-38618",
    "user": "https://github.com/loefflerd"
}
```

Sorry, that was very sloppy of me. Here is a patchlet that adds the missing doctest.



---

archive/issue_comments_038619.json:
```json
{
    "body": "Brilliant.  And I forgot to say (on one of these tickets) -- we do now have 100% coverage on all sage/modular/modsym, and all tests pass.",
    "created_at": "2009-05-18T15:58:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5080",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5080#issuecomment-38619",
    "user": "https://github.com/JohnCremona"
}
```

Brilliant.  And I forgot to say (on one of these tickets) -- we do now have 100% coverage on all sage/modular/modsym, and all tests pass.



---

archive/issue_comments_038620.json:
```json
{
    "body": "Unfortunately this patch causes a massive speed regression:\n\n```\nsage: time EllipticCurve('858k2').sha().an_padic(Integer(7))\nCPU times: user 8.90 s, sys: 0.33 s, total: 9.23 s\nWall time: 9.52 s\n7^2 + O(7^3)\n```\n\nWith both patches from this ticket this one alone takes minutes, so sorry, but \"needs work\".\n\nCheers,\n\nMichael",
    "created_at": "2009-05-18T23:53:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5080",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5080#issuecomment-38620",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Unfortunately this patch causes a massive speed regression:

```
sage: time EllipticCurve('858k2').sha().an_padic(Integer(7))
CPU times: user 8.90 s, sys: 0.33 s, total: 9.23 s
Wall time: 9.52 s
7^2 + O(7^3)
```

With both patches from this ticket this one alone takes minutes, so sorry, but "needs work".

Cheers,

Michael



---

archive/issue_comments_038621.json:
```json
{
    "body": "Groan, I suppose that going via complement to get dual free module is probably slower when the Hecke matrices are very sparse, as they are here. I generally worry first about getting a mathematically correct answer, and only then about efficiency issues. Can't look at this right now, sorry -- I've already spent far too much time on Sage stuff in the last week or two -- might get around to it sometime next week.",
    "created_at": "2009-05-19T07:46:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5080",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5080#issuecomment-38621",
    "user": "https://github.com/loefflerd"
}
```

Groan, I suppose that going via complement to get dual free module is probably slower when the Hecke matrices are very sparse, as they are here. I generally worry first about getting a mathematically correct answer, and only then about efficiency issues. Can't look at this right now, sorry -- I've already spent far too much time on Sage stuff in the last week or two -- might get around to it sometime next week.



---

archive/issue_comments_038622.json:
```json
{
    "body": "Hey David,\n\nIt's definitely the right choice to go for correctness over speed first. I'll look into speeding this up in the next few days, if you don't beat me to it. As the simplest possible attempt, though, couldn't we just drop your new code in where the `RuntimeError` is raised? Obviously this isn't the classiest fix, but it wouldn't be bad as a first approximation.",
    "created_at": "2009-05-19T08:44:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5080",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5080#issuecomment-38622",
    "user": "https://github.com/craigcitro"
}
```

Hey David,

It's definitely the right choice to go for correctness over speed first. I'll look into speeding this up in the next few days, if you don't beat me to it. As the simplest possible attempt, though, couldn't we just drop your new code in where the `RuntimeError` is raised? Obviously this isn't the classiest fix, but it wouldn't be bad as a first approximation.



---

archive/issue_comments_038623.json:
```json
{
    "body": "Hi Craig,\n\nIt's a delicate thing. There are two potential first-approximation algorithms for computing complements, or (equivalently) embedded duals: either work on the dual side (cutting down to the smallest space on which Hecke acts like it does on self) or work on the ambient side (cutting down to the smallest space on which Hecke acts like it does on the quotient ambient/self). \n\nWhat we had before was one algorithm in `complement` and the other in `dual_free_module`, never exploiting the fact that the two problems are essentially equivalent. I standardised on the algorithm that `complement` was using, largely because the code to handle the pathological case (for which neither algorithm works) was already there in the `complement` routine.\n\nThe classy fix is to heuristically choose which algorithm to use, because (in non-pathological cases) the dual-side version is much quicker when the given submodule is much smaller than the ambient space, and the ambient-side version is much quicker when the given submodule is most of the ambient space. This is (roughly) what is meant by the comment in `submodule.py` saying:\n\n```\n# TODO: optimize in some cases by computing image of\n# complementary factor instead of kernel...?\n```\n\n\nDavid",
    "created_at": "2009-05-19T09:31:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5080",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5080#issuecomment-38623",
    "user": "https://github.com/loefflerd"
}
```

Hi Craig,

It's a delicate thing. There are two potential first-approximation algorithms for computing complements, or (equivalently) embedded duals: either work on the dual side (cutting down to the smallest space on which Hecke acts like it does on self) or work on the ambient side (cutting down to the smallest space on which Hecke acts like it does on the quotient ambient/self). 

What we had before was one algorithm in `complement` and the other in `dual_free_module`, never exploiting the fact that the two problems are essentially equivalent. I standardised on the algorithm that `complement` was using, largely because the code to handle the pathological case (for which neither algorithm works) was already there in the `complement` routine.

The classy fix is to heuristically choose which algorithm to use, because (in non-pathological cases) the dual-side version is much quicker when the given submodule is much smaller than the ambient space, and the ambient-side version is much quicker when the given submodule is most of the ambient space. This is (roughly) what is meant by the comment in `submodule.py` saying:

```
# TODO: optimize in some cases by computing image of
# complementary factor instead of kernel...?
```


David



---

archive/issue_comments_038624.json:
```json
{
    "body": "replaces all previous patches",
    "created_at": "2009-05-25T19:18:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5080",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5080#issuecomment-38624",
    "user": "https://github.com/loefflerd"
}
```

replaces all previous patches



---

archive/issue_comments_038625.json:
```json
{
    "body": "Attachment [trac_5080_new.patch](tarball://root/attachments/some-uuid/ticket5080/trac_5080_new.patch) by @loefflerd created at 2009-05-25 19:19:58\n\nHere's a new patch, which causes no speed regression at all in the p-adic analytic sha for 858k1, and still solves the original 128a congruence number problem.",
    "created_at": "2009-05-25T19:19:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5080",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5080#issuecomment-38625",
    "user": "https://github.com/loefflerd"
}
```

Attachment [trac_5080_new.patch](tarball://root/attachments/some-uuid/ticket5080/trac_5080_new.patch) by @loefflerd created at 2009-05-25 19:19:58

Here's a new patch, which causes no speed regression at all in the p-adic analytic sha for 858k1, and still solves the original 128a congruence number problem.



---

archive/issue_comments_038626.json:
```json
{
    "body": "Craig, are you going to review David's new patch here?  Or shall I?",
    "created_at": "2009-05-30T16:09:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5080",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5080#issuecomment-38626",
    "user": "https://github.com/JohnCremona"
}
```

Craig, are you going to review David's new patch here?  Or shall I?



---

archive/issue_comments_038627.json:
```json
{
    "body": "Hi John -- I'm planning on looking at it somewhat soon, but feel free to beat me to it! :)",
    "created_at": "2009-05-30T16:15:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5080",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5080#issuecomment-38627",
    "user": "https://github.com/craigcitro"
}
```

Hi John -- I'm planning on looking at it somewhat soon, but feel free to beat me to it! :)



---

archive/issue_comments_038628.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2009-06-08T08:27:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5080",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5080#issuecomment-38628",
    "user": "https://github.com/loefflerd"
}
```

Changing status from new to assigned.



---

archive/issue_comments_038629.json:
```json
{
    "body": "Changing assignee from @craigcitro to @loefflerd.",
    "created_at": "2009-06-08T08:27:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5080",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5080#issuecomment-38629",
    "user": "https://github.com/loefflerd"
}
```

Changing assignee from @craigcitro to @loefflerd.



---

archive/issue_comments_038630.json:
```json
{
    "body": "Sorry I've been so slow about getting to this.\n\nThe patch looks great, but I have one gripe. I hate the fact that we're working around Python's \"private\" obfuscation (the `_HeckeSubmodule__attr` thing). It's brittle, because if the class name changes, or if certain methods get overridden, it'll break. Worse, it's ugly. `:)` I think we should fix it, though I'm not sure I know the \"right\" way. Some options:\n\n* change these to attributes with a single underscore \n* set these attributes to `None` in the constructor, and check if they're not `None`\n* I know the `combinat` branch has a `cached_method` decorator -- I don't know if it has a system for checking if the attribute is set, but it might.\n\nI guess I'd lean towards the third if it works, and if not, the second (and filing a trac ticket asking for the enhancement to `cached_method`). One option I **don't** like: adding flags for each attribute to see if it's set.",
    "created_at": "2009-06-20T09:12:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5080",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5080#issuecomment-38630",
    "user": "https://github.com/craigcitro"
}
```

Sorry I've been so slow about getting to this.

The patch looks great, but I have one gripe. I hate the fact that we're working around Python's "private" obfuscation (the `_HeckeSubmodule__attr` thing). It's brittle, because if the class name changes, or if certain methods get overridden, it'll break. Worse, it's ugly. `:)` I think we should fix it, though I'm not sure I know the "right" way. Some options:

* change these to attributes with a single underscore 
* set these attributes to `None` in the constructor, and check if they're not `None`
* I know the `combinat` branch has a `cached_method` decorator -- I don't know if it has a system for checking if the attribute is set, but it might.

I guess I'd lean towards the third if it works, and if not, the second (and filing a trac ticket asking for the enhancement to `cached_method`). One option I **don't** like: adding flags for each attribute to see if it's set.



---

archive/issue_comments_038631.json:
```json
{
    "body": "Good point. I've become rather fond of `@`cached_function and `@`cached_method -- I have a patch which I haven't uploaded yet which removes about 100 lines of caching code from sage/modular/modform by systematically using `@`cached_method -- but it hadn't occurred to me to use it in this way. It seems that cached methods have a method \"is_in_cache\"; and if the method takes no arguments, you can call \"is_in_cache\" with no arguments either, and it works fine. \n\nI will do a new patch, but in 28 hours I will be catching a plane to Barcelona for SD16, so it might not get done before next weekend.\nDavid",
    "created_at": "2009-06-20T09:34:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5080",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5080#issuecomment-38631",
    "user": "https://github.com/loefflerd"
}
```

Good point. I've become rather fond of `@`cached_function and `@`cached_method -- I have a patch which I haven't uploaded yet which removes about 100 lines of caching code from sage/modular/modform by systematically using `@`cached_method -- but it hadn't occurred to me to use it in this way. It seems that cached methods have a method "is_in_cache"; and if the method takes no arguments, you can call "is_in_cache" with no arguments either, and it works fine. 

I will do a new patch, but in 28 hours I will be catching a plane to Barcelona for SD16, so it might not get done before next weekend.
David



---

archive/issue_comments_038632.json:
```json
{
    "body": "apply over trac_5080_new.patch",
    "created_at": "2009-06-20T10:08:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5080",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5080#issuecomment-38632",
    "user": "https://github.com/loefflerd"
}
```

apply over trac_5080_new.patch



---

archive/issue_comments_038633.json:
```json
{
    "body": "Attachment [trac_5080_cachefix.patch](tarball://root/attachments/some-uuid/ticket5080/trac_5080_cachefix.patch) by @loefflerd created at 2009-06-20 10:12:20\n\nFor the first time I can remember, I wrote a fix and it worked first time. Here is a patch which removes all instances of \"hasattr\".\n\n(There is potential for cleaning up elsewhere in sage/modular/hecke/submodule.py using cached_method -- the is_new, is_old, new_submodule, old_submodule calls have their own caching code which we can now get rid of -- but that is for another ticket.)\n\nDavid",
    "created_at": "2009-06-20T10:12:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5080",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5080#issuecomment-38633",
    "user": "https://github.com/loefflerd"
}
```

Attachment [trac_5080_cachefix.patch](tarball://root/attachments/some-uuid/ticket5080/trac_5080_cachefix.patch) by @loefflerd created at 2009-06-20 10:12:20

For the first time I can remember, I wrote a fix and it worked first time. Here is a patch which removes all instances of "hasattr".

(There is potential for cleaning up elsewhere in sage/modular/hecke/submodule.py using cached_method -- the is_new, is_old, new_submodule, old_submodule calls have their own caching code which we can now get rid of -- but that is for another ticket.)

David



---

archive/issue_comments_038634.json:
```json
{
    "body": "Looks good, and I'm very happy with the changes.",
    "created_at": "2009-06-20T21:38:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5080",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5080#issuecomment-38634",
    "user": "https://github.com/craigcitro"
}
```

Looks good, and I'm very happy with the changes.



---

archive/issue_events_005324.json:
```json
{
    "actor": "https://github.com/rlmill",
    "created_at": "2009-06-24T09:50:12Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/5080",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/5080#event-5324"
}
```



---

archive/issue_comments_038635.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-06-24T09:50:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5080",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5080#issuecomment-38635",
    "user": "https://github.com/rlmill"
}
```

Resolution: fixed



---

archive/issue_comments_038636.json:
```json
{
    "body": "Changing status from closed to reopened.",
    "created_at": "2009-06-28T15:00:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5080",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5080#issuecomment-38636",
    "user": "https://github.com/williamstein"
}
```

Changing status from closed to reopened.



---

archive/issue_events_005325.json:
```json
{
    "actor": "https://github.com/williamstein",
    "created_at": "2009-06-28T15:00:48Z",
    "event": "reopened",
    "issue": "https://github.com/sagemath/sagetest/issues/5080",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/5080#event-5325"
}
```



---

archive/issue_comments_038637.json:
```json
{
    "body": "\n```\nOn Jun 27, 11:54 pm, davidloeffler <dave.loeff...@gmail.com> wrote:\n> On SuSE, 32-bit, sage -testall -long passes except for errors in the\n> same three files Jaap reported above (and a harmless timeout in\n> elliptic curves).\n\nI spoke too soon. Something rather harmful has in fact happened: the\nwrong patches have been merged for track #5080. My first attempt at\nfixing this problem caused a catastrophic slowdown in elliptic curve\nSha routines, so I started again from scratch and did a new patch that\nworked differently. It seems that the old patch has been merged, with\nthe result that\n\nsage: EllipticCurve(\"858k1\").sha().an_padic(7)\n\nhas been slowed down by *several orders of magnitude*. That was why I\nwas seeing timeouts in that file.\n\nTo reiterate: the patch \"trac_5080.patch\" on that ticket is evil, bad\nand wrong, should not have been merged, and must be removed from Sage\nASAP.\n\nDavid\n```\n",
    "created_at": "2009-06-28T15:00:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5080",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5080#issuecomment-38637",
    "user": "https://github.com/williamstein"
}
```


```
On Jun 27, 11:54 pm, davidloeffler <dave.loeff...@gmail.com> wrote:
> On SuSE, 32-bit, sage -testall -long passes except for errors in the
> same three files Jaap reported above (and a harmless timeout in
> elliptic curves).

I spoke too soon. Something rather harmful has in fact happened: the
wrong patches have been merged for track #5080. My first attempt at
fixing this problem caused a catastrophic slowdown in elliptic curve
Sha routines, so I started again from scratch and did a new patch that
worked differently. It seems that the old patch has been merged, with
the result that

sage: EllipticCurve("858k1").sha().an_padic(7)

has been slowed down by *several orders of magnitude*. That was why I
was seeing timeouts in that file.

To reiterate: the patch "trac_5080.patch" on that ticket is evil, bad
and wrong, should not have been merged, and must be removed from Sage
ASAP.

David
```




---

archive/issue_comments_038638.json:
```json
{
    "body": "Resolution changed from fixed to ",
    "created_at": "2009-06-28T15:00:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5080",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5080#issuecomment-38638",
    "user": "https://github.com/williamstein"
}
```

Resolution changed from fixed to 



---

archive/issue_comments_038639.json:
```json
{
    "body": "Changing priority from major to blocker.",
    "created_at": "2009-06-28T15:01:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5080",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5080#issuecomment-38639",
    "user": "https://github.com/williamstein"
}
```

Changing priority from major to blocker.



---

archive/issue_comments_038640.json:
```json
{
    "body": "Attachment [trac_5080_repair.patch](tarball://root/attachments/some-uuid/ticket5080/trac_5080_repair.patch) by @loefflerd created at 2009-06-28 17:32:10\n\nApply to 4.1.alpha2",
    "created_at": "2009-06-28T17:32:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5080",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5080#issuecomment-38640",
    "user": "https://github.com/loefflerd"
}
```

Attachment [trac_5080_repair.patch](tarball://root/attachments/some-uuid/ticket5080/trac_5080_repair.patch) by @loefflerd created at 2009-06-28 17:32:10

Apply to 4.1.alpha2



---

archive/issue_comments_038641.json:
```json
{
    "body": "I've just uploaded the patch trac_5080_repair.patch. Apply this patch (only) to 4.1.alpha2 gets hecke/submodule.py into the intended state. I've checked that this passes doctests in sage/modular/hecke, and that mabshoff's 858k2 example computes within a reasonable time limit.\n\nDavid",
    "created_at": "2009-06-28T17:35:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5080",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5080#issuecomment-38641",
    "user": "https://github.com/loefflerd"
}
```

I've just uploaded the patch trac_5080_repair.patch. Apply this patch (only) to 4.1.alpha2 gets hecke/submodule.py into the intended state. I've checked that this passes doctests in sage/modular/hecke, and that mabshoff's 858k2 example computes within a reasonable time limit.

David



---

archive/issue_comments_038642.json:
```json
{
    "body": "I checked that the new patch applies cleanly to 4.1.alpha2, all tests in modular/hecke pass, and the function mabshoff highlighted runs fine in about 10s.\n\nThe tag still said \"positive review\", but now it deserves it again.",
    "created_at": "2009-06-28T17:58:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5080",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5080#issuecomment-38642",
    "user": "https://github.com/JohnCremona"
}
```

I checked that the new patch applies cleanly to 4.1.alpha2, all tests in modular/hecke pass, and the function mabshoff highlighted runs fine in about 10s.

The tag still said "positive review", but now it deserves it again.



---

archive/issue_comments_038643.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-06-29T20:56:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5080",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5080#issuecomment-38643",
    "user": "https://github.com/rlmill"
}
```

Resolution: fixed



---

archive/issue_events_005326.json:
```json
{
    "actor": "https://github.com/rlmill",
    "created_at": "2009-06-29T20:56:11Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/5080",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/5080#event-5326"
}
```



---

archive/issue_comments_038644.json:
```json
{
    "body": "Merged the fix patch into sage-4.1.alpha3.",
    "created_at": "2009-06-29T20:56:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5080",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5080#issuecomment-38644",
    "user": "https://github.com/rlmill"
}
```

Merged the fix patch into sage-4.1.alpha3.

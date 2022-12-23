# Issue 5921: factoring integer polynomials does not factor the content

archive/issues_005921.json:
```json
{
    "body": "Assignee: tbd\n\nI think this is wrong:\n\n```\nsage: R.<x> = ZZ[]\nsage: f = 30*x\nsage: f.factor()\n30 * x\n```\n\nsince in the ring ZZ[] 30 is not irreducible;  it should return 2*3*5*x.\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/5921\n\n",
    "created_at": "2009-04-28T19:54:00Z",
    "labels": [
        "algebra",
        "major",
        "bug"
    ],
    "title": "factoring integer polynomials does not factor the content",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/5921",
    "user": "cremona"
}
```
Assignee: tbd

I think this is wrong:

```
sage: R.<x> = ZZ[]
sage: f = 30*x
sage: f.factor()
30 * x
```

since in the ring ZZ[] 30 is not irreducible;  it should return 2*3*5*x.


Issue created by migration from https://trac.sagemath.org/ticket/5921





---

archive/issue_comments_046806.json:
```json
{
    "body": "Attachment",
    "created_at": "2009-04-28T20:04:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5921",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5921#issuecomment-46806",
    "user": "cremona"
}
```

Attachment



---

archive/issue_comments_046807.json:
```json
{
    "body": "Hi John,\n\nThe changes in the patch look fine, but for some reason they make doctests fail in two places: `polynomial_zmod_flint.pyx` (with some errors) and `polynomial_modn_dense_ntl.pyx` (killed after timeout).  I'm rushing to teach right now, but I'll try to investigate afterward.",
    "created_at": "2009-04-28T22:47:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5921",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5921#issuecomment-46807",
    "user": "AlexGhitza"
}
```

Hi John,

The changes in the patch look fine, but for some reason they make doctests fail in two places: `polynomial_zmod_flint.pyx` (with some errors) and `polynomial_modn_dense_ntl.pyx` (killed after timeout).  I'm rushing to teach right now, but I'll try to investigate afterward.



---

archive/issue_comments_046808.json:
```json
{
    "body": "OK, I've found a very simple example where this bombs:\n\n\n```\nsage: P.<x> = ZZ[]\nsage: f = 2*x + 2\nsage: f.roots()\n...\nNotImplementedError:\n```\n",
    "created_at": "2009-04-29T00:53:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5921",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5921#issuecomment-46808",
    "user": "AlexGhitza"
}
```

OK, I've found a very simple example where this bombs:


```
sage: P.<x> = ZZ[]
sage: f = 2*x + 2
sage: f.roots()
...
NotImplementedError:
```




---

archive/issue_comments_046809.json:
```json
{
    "body": "Hmmm.  We just had this situation happen on a different ticket: the code in this patch is fine but breaks something, which really exposes a pre-existing bug.\n\nIn this case, John's code factors the content and the \"normalised, content-free\" polynomial separately and multiplies the two factorisations.  The problem is the with the types: the first factorisation consists of integers, while the second one consists of polynomials.  Multiplying them together yields a factorisation where some factors are of type integer and the others of type polynomial, and then this breaks all sorts of things later on.\n\nI've made a new ticket at #5928 and will have a patch up there soon.  Then John's patch on this ticket will be good to go.",
    "created_at": "2009-04-29T01:44:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5921",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5921#issuecomment-46809",
    "user": "AlexGhitza"
}
```

Hmmm.  We just had this situation happen on a different ticket: the code in this patch is fine but breaks something, which really exposes a pre-existing bug.

In this case, John's code factors the content and the "normalised, content-free" polynomial separately and multiplies the two factorisations.  The problem is the with the types: the first factorisation consists of integers, while the second one consists of polynomials.  Multiplying them together yields a factorisation where some factors are of type integer and the others of type polynomial, and then this breaks all sorts of things later on.

I've made a new ticket at #5928 and will have a patch up there soon.  Then John's patch on this ticket will be good to go.



---

archive/issue_comments_046810.json:
```json
{
    "body": "There's now a patch up at #5928.  I've tested again with John's patch applied and the `polynomial_zmod_flint.pyx` problems are gone, but I'm still getting timeouts in `polynomial_modn_dense_ntl.pyx`.  So there's more to this than I thought.",
    "created_at": "2009-04-29T05:53:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5921",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5921#issuecomment-46810",
    "user": "AlexGhitza"
}
```

There's now a patch up at #5928.  I've tested again with John's patch applied and the `polynomial_zmod_flint.pyx` problems are gone, but I'm still getting timeouts in `polynomial_modn_dense_ntl.pyx`.  So there's more to this than I thought.



---

archive/issue_comments_046811.json:
```json
{
    "body": "Yes, the problem is in `f.roots()` for a polynomial f with integer coefficients.  The code used to just run `f.factor()`, but of course now if the content is a huge integer it's gonna take a while for the factoring to finish.  There's a doctest in the sage library that runs into precisely this problem now, since it's an illustration of RSA and has huge coefficients (and a huge content) floating around.  However, you don't care about the content if you just want the roots of the polynomial.\n\nSo the attached patch makes `roots()` divide by the content first, then call `factor()`.  It also adds a warning to this effect in the docstrings of the two `factor()` methods.\n\nI'm happy with John's patch, so if someone reviews my patch we're done.",
    "created_at": "2009-04-29T06:42:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5921",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5921#issuecomment-46811",
    "user": "AlexGhitza"
}
```

Yes, the problem is in `f.roots()` for a polynomial f with integer coefficients.  The code used to just run `f.factor()`, but of course now if the content is a huge integer it's gonna take a while for the factoring to finish.  There's a doctest in the sage library that runs into precisely this problem now, since it's an illustration of RSA and has huge coefficients (and a huge content) floating around.  However, you don't care about the content if you just want the roots of the polynomial.

So the attached patch makes `roots()` divide by the content first, then call `factor()`.  It also adds a warning to this effect in the docstrings of the two `factor()` methods.

I'm happy with John's patch, so if someone reviews my patch we're done.



---

archive/issue_comments_046812.json:
```json
{
    "body": "I forgot to mention this again: this ticket depends on the patch at #5928, so that should be applied first.",
    "created_at": "2009-04-29T06:44:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5921",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5921#issuecomment-46812",
    "user": "AlexGhitza"
}
```

I forgot to mention this again: this ticket depends on the patch at #5928, so that should be applied first.



---

archive/issue_comments_046813.json:
```json
{
    "body": "I am happy with Alex's patch.  I made mine a bit too quickly or I would have thought about the universes being different.  So I will give this a positive review as soon as I have gone to look at #5928.",
    "created_at": "2009-04-29T08:30:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5921",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5921#issuecomment-46813",
    "user": "cremona"
}
```

I am happy with Alex's patch.  I made mine a bit too quickly or I would have thought about the universes being different.  So I will give this a positive review as soon as I have gone to look at #5928.



---

archive/issue_comments_046814.json:
```json
{
    "body": "I applied both patches after #5928 on top of 3.4.2.alpha0, fine.  Ran all tests in sage/rings/polynomial (all fine) and sage/rings/number_field (all fine).\n\nSo I have given this a positive review since Alex and I have reviewed eachothers' patches.",
    "created_at": "2009-04-29T09:05:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5921",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5921#issuecomment-46814",
    "user": "cremona"
}
```

I applied both patches after #5928 on top of 3.4.2.alpha0, fine.  Ran all tests in sage/rings/polynomial (all fine) and sage/rings/number_field (all fine).

So I have given this a positive review since Alex and I have reviewed eachothers' patches.



---

archive/issue_comments_046815.json:
```json
{
    "body": "These two patches break\n\n```\nsage -t -long devel/sage/sage/modular/overconvergent/genus0.py\n```\n\n\nCheers,\n\nMichael",
    "created_at": "2009-04-30T02:56:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5921",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5921#issuecomment-46815",
    "user": "mabshoff"
}
```

These two patches break

```
sage -t -long devel/sage/sage/modular/overconvergent/genus0.py
```


Cheers,

Michael



---

archive/issue_comments_046816.json:
```json
{
    "body": "Replying to [comment:10 mabshoff]:\n> These two patches break\n> {{{\n> sage -t -long devel/sage/sage/modular/overconvergent/genus0.py\n> }}}\n> \n\nThis is due to a bug in p-adics, more precisely in the content method for p-adic polynomials:\n\n\n```\nsage: P.<x> = ZZ[]\nsage: f = x + 2\nsage: f.content()\n1\nsage: fp = f.change_ring(pAdicField(2, 10))\nsage: fp\n(1 + O(2^10))*x + (2 + O(2^11))\nsage: fp.content()\n0\n```\n\n\nI have checked and the monster p-adic patch bomb at #5778 doesn't help with this.  I'll see what we can do.",
    "created_at": "2009-04-30T03:35:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5921",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5921#issuecomment-46816",
    "user": "AlexGhitza"
}
```

Replying to [comment:10 mabshoff]:
> These two patches break
> {{{
> sage -t -long devel/sage/sage/modular/overconvergent/genus0.py
> }}}
> 

This is due to a bug in p-adics, more precisely in the content method for p-adic polynomials:


```
sage: P.<x> = ZZ[]
sage: f = x + 2
sage: f.content()
1
sage: fp = f.change_ring(pAdicField(2, 10))
sage: fp
(1 + O(2^10))*x + (2 + O(2^11))
sage: fp.content()
0
```


I have checked and the monster p-adic patch bomb at #5778 doesn't help with this.  I'll see what we can do.



---

archive/issue_comments_046817.json:
```json
{
    "body": "OK, I've made a simple modification in my patch that sidesteps the p-adic polynomial bug (for which there is now a new trac ticket #5946).\n\nI have replaced my patch with the new version, so one still needs to apply both patches.",
    "created_at": "2009-04-30T06:45:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5921",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5921#issuecomment-46817",
    "user": "AlexGhitza"
}
```

OK, I've made a simple modification in my patch that sidesteps the p-adic polynomial bug (for which there is now a new trac ticket #5946).

I have replaced my patch with the new version, so one still needs to apply both patches.



---

archive/issue_comments_046818.json:
```json
{
    "body": "Attachment\n\nWith Alex's new patch (on top of mine all tests in modular/overconvergent/* pass  as well as all in rings/polynomial\n\nI reinstated Positive Review and am keeping my fingers crossed!",
    "created_at": "2009-04-30T08:29:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5921",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5921#issuecomment-46818",
    "user": "cremona"
}
```

Attachment

With Alex's new patch (on top of mine all tests in modular/overconvergent/* pass  as well as all in rings/polynomial

I reinstated Positive Review and am keeping my fingers crossed!



---

archive/issue_comments_046819.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-04-30T09:20:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5921",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5921#issuecomment-46819",
    "user": "mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_046820.json:
```json
{
    "body": "Merged both patches in Sage 3.4.2.rc0.\n\nCheers,\n\nMichael",
    "created_at": "2009-04-30T09:20:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5921",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5921#issuecomment-46820",
    "user": "mabshoff"
}
```

Merged both patches in Sage 3.4.2.rc0.

Cheers,

Michael

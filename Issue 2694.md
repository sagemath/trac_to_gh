# Issue 2694: Hecke algebra basis not implemented

archive/issues_002694.json:
```json
{
    "body": "Assignee: craigcitro\n\nHecke algebra basis is not implemented.\nhere is how one can reproduce it:\n\n```\nsage: M=ModularSymbols(431,2,1)\nsage: C=M.cuspidal_submodule()\nsage: TT=C.hecke_algebra()\nsage: TT.basis()\n---------------------------------------------------------------------------\n<type 'exceptions.NotImplementedError'>   Traceback (most recent call last)\n\n/home/syazdani/sage-2.11.alpha1/<ipython console> in <module>()\n\n/home/syazdani/sage/local/lib/python2.5/site-packages/sage/modular/hecke/algebra.py in basis(self)\n    145\n    146     def basis(self):\n--> 147         raise NotImplementedError\n    148\n    149     def discriminant(self):\n\n<type 'exceptions.NotImplementedError'>:\n```\n\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/2694\n\n",
    "created_at": "2008-03-28T05:02:07Z",
    "labels": [
        "modular forms",
        "minor",
        "enhancement"
    ],
    "title": "Hecke algebra basis not implemented",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/2694",
    "user": "syazdani"
}
```
Assignee: craigcitro

Hecke algebra basis is not implemented.
here is how one can reproduce it:

```
sage: M=ModularSymbols(431,2,1)
sage: C=M.cuspidal_submodule()
sage: TT=C.hecke_algebra()
sage: TT.basis()
---------------------------------------------------------------------------
<type 'exceptions.NotImplementedError'>   Traceback (most recent call last)

/home/syazdani/sage-2.11.alpha1/<ipython console> in <module>()

/home/syazdani/sage/local/lib/python2.5/site-packages/sage/modular/hecke/algebra.py in basis(self)
    145
    146     def basis(self):
--> 147         raise NotImplementedError
    148
    149     def discriminant(self):

<type 'exceptions.NotImplementedError'>:
```



Issue created by migration from https://trac.sagemath.org/ticket/2694





---

archive/issue_comments_018540.json:
```json
{
    "body": "Craig,\n\nany progress here?\n\nCheers,\n\nMichael",
    "created_at": "2008-07-31T03:33:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2694",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2694#issuecomment-18540",
    "user": "mabshoff"
}
```

Craig,

any progress here?

Cheers,

Michael



---

archive/issue_comments_018541.json:
```json
{
    "body": "This works for me on `5.5.rc0`:\n\n```\nsage: M = ModularSymbols(431,2,1)\nsage: C = M.cuspidal_submodule()\nsage: TT = C.hecke_algebra()\nsage: TT.basis()\n[Hecke operator on Modular Symbols subspace of dimension 36 of Modular Symbols space of dimension 37 for Gamma_0(431) of weight 2 with sign 1 over Rational Field defined by:\n...\n36 x 36 dense matrix over Rational Field]\n```\n",
    "created_at": "2013-02-05T03:23:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2694",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2694#issuecomment-18541",
    "user": "tscrim"
}
```

This works for me on `5.5.rc0`:

```
sage: M = ModularSymbols(431,2,1)
sage: C = M.cuspidal_submodule()
sage: TT = C.hecke_algebra()
sage: TT.basis()
[Hecke operator on Modular Symbols subspace of dimension 36 of Modular Symbols space of dimension 37 for Gamma_0(431) of weight 2 with sign 1 over Rational Field defined by:
...
36 x 36 dense matrix over Rational Field]
```




---

archive/issue_comments_018542.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2013-02-05T03:23:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2694",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2694#issuecomment-18542",
    "user": "tscrim"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_018543.json:
```json
{
    "body": "It also works for me in 5.7.beta4 so I'm giving the `wontfix` a positive review.",
    "created_at": "2013-02-12T09:27:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2694",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2694#issuecomment-18543",
    "user": "cnassau"
}
```

It also works for me in 5.7.beta4 so I'm giving the `wontfix` a positive review.



---

archive/issue_comments_018544.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2013-02-12T09:27:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2694",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2694#issuecomment-18544",
    "user": "cnassau"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_018545.json:
```json
{
    "body": "Resolution: worksforme",
    "created_at": "2013-02-17T20:08:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2694",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2694#issuecomment-18545",
    "user": "jdemeyer"
}
```

Resolution: worksforme

# Issue 1124: ModularSymbol.complement crashes on full subspaces

archive/issues_001124.json:
```json
{
    "body": "Assignee: was\n\nKeywords: zero_subspace\n\nHere is a bug in modular symbols code:\n\n``` \nsage: M=ModularSymbols(11,2,1)\nsage: M.complement()\n---------------------------------------------------------------------------\n<type 'exceptions.AttributeError'>        Traceback (most recent call last)\n\n/net/mathserv/1/home/syazdani/research/programs/<ipython console> in <module>()\n\n/home/syazdani/sage/local/lib/python2.5/site-packages/sage/modular/hecke/ambient_module.py in complement(self)\n     96         Return the largest Hecke-stable complement of this space.\n     97         \"\"\"\n---> 98         return self.zero_subspace()\n     99\n    100     def decomposition_matrix(self):\n\n<type 'exceptions.AttributeError'>: 'ModularSymbolsAmbient_wt2_g0' object has no attribute 'zero_subspace'\n```\n\n\nThe problem is that zero_subspace is not implemented. Although zero_submodule is.\nOne possible fix is to change self.zero_subspace to self.zero_submodule(). That's the included patch.\n\nIssue created by migration from https://trac.sagemath.org/ticket/1124\n\n",
    "created_at": "2007-11-07T18:07:46Z",
    "labels": [
        "modular forms",
        "trivial",
        "bug"
    ],
    "title": "ModularSymbol.complement crashes on full subspaces",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/1124",
    "user": "syazdani"
}
```
Assignee: was

Keywords: zero_subspace

Here is a bug in modular symbols code:

``` 
sage: M=ModularSymbols(11,2,1)
sage: M.complement()
---------------------------------------------------------------------------
<type 'exceptions.AttributeError'>        Traceback (most recent call last)

/net/mathserv/1/home/syazdani/research/programs/<ipython console> in <module>()

/home/syazdani/sage/local/lib/python2.5/site-packages/sage/modular/hecke/ambient_module.py in complement(self)
     96         Return the largest Hecke-stable complement of this space.
     97         """
---> 98         return self.zero_subspace()
     99
    100     def decomposition_matrix(self):

<type 'exceptions.AttributeError'>: 'ModularSymbolsAmbient_wt2_g0' object has no attribute 'zero_subspace'
```


The problem is that zero_subspace is not implemented. Although zero_submodule is.
One possible fix is to change self.zero_subspace to self.zero_submodule(). That's the included patch.

Issue created by migration from https://trac.sagemath.org/ticket/1124





---

archive/issue_comments_006788.json:
```json
{
    "body": "trivial patch",
    "created_at": "2007-11-07T18:08:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1124",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1124#issuecomment-6788",
    "user": "syazdani"
}
```

trivial patch



---

archive/issue_comments_006789.json:
```json
{
    "body": "Attachment\n\n[with patch]",
    "created_at": "2007-11-07T18:15:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1124",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1124#issuecomment-6789",
    "user": "syazdani"
}
```

Attachment

[with patch]



---

archive/issue_comments_006790.json:
```json
{
    "body": "Changing priority from trivial to major.",
    "created_at": "2007-11-07T18:19:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1124",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1124#issuecomment-6790",
    "user": "mabshoff"
}
```

Changing priority from trivial to major.



---

archive/issue_comments_006791.json:
```json
{
    "body": "Added doctest for complement. Both patches should be applied.",
    "created_at": "2007-11-07T18:25:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1124",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1124#issuecomment-6791",
    "user": "syazdani"
}
```

Added doctest for complement. Both patches should be applied.



---

archive/issue_comments_006792.json:
```json
{
    "body": "Attachment",
    "created_at": "2007-11-16T11:56:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1124",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1124#issuecomment-6792",
    "user": "mabshoff"
}
```

Attachment



---

archive/issue_comments_006793.json:
```json
{
    "body": "** \"I have reviewed this patch and it agree with it.\"",
    "created_at": "2007-11-18T03:55:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1124",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1124#issuecomment-6793",
    "user": "was"
}
```

** "I have reviewed this patch and it agree with it."



---

archive/issue_comments_006794.json:
```json
{
    "body": "Merged in 2.8.13.alpha0.",
    "created_at": "2007-11-18T14:22:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1124",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1124#issuecomment-6794",
    "user": "mabshoff"
}
```

Merged in 2.8.13.alpha0.



---

archive/issue_comments_006795.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2007-11-18T14:22:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1124",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1124#issuecomment-6795",
    "user": "mabshoff"
}
```

Resolution: fixed

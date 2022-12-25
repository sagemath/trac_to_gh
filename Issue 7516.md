# Issue 7516: bug in pickling quotient module over pid

archive/issues_007516.json:
```json
{
    "body": "Assignee: @williamstein\n\nThis is from the \"report a problem\" link in the notebook:\n\nIf you have a vector space, that is a quotient of a subspace of\nanother vector space, then after coercing elements into it, something\ngoes wrong in (un)pickling it.\n\n\n```\nsage: V = VectorSpace(QQ, 2)\nsage: W = V.subspace([V([1,1])])\nsage: Z = W.subspace([])\nsage: WmodZ = W / Z\nsage: WmodZ(W(0))\n(0)\nsage: loads(dumps(WmodZ))\n---------------------------------------------------------------------------\nAttributeError                            Traceback (most recent call last)\n\n/home/bosman/sage/<ipython console> in <module>()\n\n/home/bosman/sage-4.2-linux-Ubuntu_9.04-i686-Linux/local/lib/python2.6/site-packages/sage/structure/sage_object.so\nin sage.structure.sage_object.loads\n(sage/structure/sage_object.c:8769)()\n\n/home/bosman/sage-4.2-linux-Ubuntu_9.04-i686-Linux/local/lib/python2.6/site-packages/sage/modules/free_module.pyc\nin __hash__(self)\n  4576             True\n  4577         \"\"\"\n-> 4578         return hash(self.__basis)\n  4579\n  4580     def construction(self):\n\nAttributeError: 'FreeModule_submodule_field' object has no attribute\n'_FreeModule_submodule_with_basis_pid__basis'\n```\n\n\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/7516\n\n",
    "created_at": "2009-11-23T04:56:05Z",
    "labels": [
        "component: linear algebra",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-8.1",
    "title": "bug in pickling quotient module over pid",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/7516",
    "user": "https://github.com/williamstein"
}
```
Assignee: @williamstein

This is from the "report a problem" link in the notebook:

If you have a vector space, that is a quotient of a subspace of
another vector space, then after coercing elements into it, something
goes wrong in (un)pickling it.


```
sage: V = VectorSpace(QQ, 2)
sage: W = V.subspace([V([1,1])])
sage: Z = W.subspace([])
sage: WmodZ = W / Z
sage: WmodZ(W(0))
(0)
sage: loads(dumps(WmodZ))
---------------------------------------------------------------------------
AttributeError                            Traceback (most recent call last)

/home/bosman/sage/<ipython console> in <module>()

/home/bosman/sage-4.2-linux-Ubuntu_9.04-i686-Linux/local/lib/python2.6/site-packages/sage/structure/sage_object.so
in sage.structure.sage_object.loads
(sage/structure/sage_object.c:8769)()

/home/bosman/sage-4.2-linux-Ubuntu_9.04-i686-Linux/local/lib/python2.6/site-packages/sage/modules/free_module.pyc
in __hash__(self)
  4576             True
  4577         """
-> 4578         return hash(self.__basis)
  4579
  4580     def construction(self):

AttributeError: 'FreeModule_submodule_field' object has no attribute
'_FreeModule_submodule_with_basis_pid__basis'
```




Issue created by migration from https://trac.sagemath.org/ticket/7516





---

archive/issue_comments_063549.json:
```json
{
    "body": "NOTE:  This bug does not happen for Free modules over ZZ.  It's only over a field where the issue happens.  \n\n```\nsage: V = FreeModule(ZZ, 2)\nsage: W = V.submodule([V([1,1])])\nsage: Z = W.submodule([])\nsage: WmodZ = W / Z\nsage: loads(dumps(WmodZ))\nFinitely generated module V/W over Integer Ring with invariants (0)\nsage: WmodZ(W(0))\n(0)\nsage: loads(dumps(WmodZ))\nFinitely generated module V/W over Integer Ring with invariants (0)\n```\n",
    "created_at": "2010-01-19T12:13:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7516",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7516#issuecomment-63549",
    "user": "https://github.com/williamstein"
}
```

NOTE:  This bug does not happen for Free modules over ZZ.  It's only over a field where the issue happens.  

```
sage: V = FreeModule(ZZ, 2)
sage: W = V.submodule([V([1,1])])
sage: Z = W.submodule([])
sage: WmodZ = W / Z
sage: loads(dumps(WmodZ))
Finitely generated module V/W over Integer Ring with invariants (0)
sage: WmodZ(W(0))
(0)
sage: loads(dumps(WmodZ))
Finitely generated module V/W over Integer Ring with invariants (0)
```




---

archive/issue_comments_063550.json:
```json
{
    "body": "Attachment [trac_7516.patch](tarball://root/attachments/some-uuid/ticket7516/trac_7516.patch) by @williamstein created at 2010-01-19 13:03:06",
    "created_at": "2010-01-19T13:03:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7516",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7516#issuecomment-63550",
    "user": "https://github.com/williamstein"
}
```

Attachment [trac_7516.patch](tarball://root/attachments/some-uuid/ticket7516/trac_7516.patch) by @williamstein created at 2010-01-19 13:03:06



---

archive/issue_comments_063551.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-01-19T13:04:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7516",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7516#issuecomment-63551",
    "user": "https://github.com/williamstein"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_063552.json:
```json
{
    "body": "If I understand the patch correctly, it violates a very essential assumption about hash codes: The hash has to be the same for objects that are equal. But with the patch, it may be possible that during unpickling the hash \"0\" is returned,  while afterwards a completely different value is returned for *the same* object.\n\nThis is giving me headache. Isn't it be possible that things are put in the wrong hash bucket?\n\nWouldn't it be a cleaner solution to ensure that self.!__basis is defined during unpickling before the hash is requested?\n\nCould you explain why your solution is correct?",
    "created_at": "2010-01-30T23:23:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7516",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7516#issuecomment-63552",
    "user": "https://github.com/simon-king-jena"
}
```

If I understand the patch correctly, it violates a very essential assumption about hash codes: The hash has to be the same for objects that are equal. But with the patch, it may be possible that during unpickling the hash "0" is returned,  while afterwards a completely different value is returned for *the same* object.

This is giving me headache. Isn't it be possible that things are put in the wrong hash bucket?

Wouldn't it be a cleaner solution to ensure that self.!__basis is defined during unpickling before the hash is requested?

Could you explain why your solution is correct?



---

archive/issue_comments_063553.json:
```json
{
    "body": "Changing status from needs_review to needs_info.",
    "created_at": "2010-01-30T23:23:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7516",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7516#issuecomment-63553",
    "user": "https://github.com/simon-king-jena"
}
```

Changing status from needs_review to needs_info.



---

archive/issue_comments_063554.json:
```json
{
    "body": "\n```\nsage: V = VectorSpace(QQ, 2)\nsage: W = V.subspace([V([1,1])])\nsage: Z = W.subspace([])\nsage: WmodZ = W / Z\nsage: WmodZ(W(0))\n(0)\nsage: loads(dumps(WmodZ))\n\nVector space quotient V/W of dimension 1 over Rational Field where\nV: Vector space of degree 2 and dimension 1 over Rational Field\nBasis matrix:\n[1 1]\nW: Vector space of degree 2 and dimension 0 over Rational Field\nBasis matrix:\n[]\n```\n\n\nWorks for me. Add a doctest and close?",
    "created_at": "2017-10-06T07:43:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7516",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7516#issuecomment-63554",
    "user": "https://github.com/simonbrandhorst"
}
```


```
sage: V = VectorSpace(QQ, 2)
sage: W = V.subspace([V([1,1])])
sage: Z = W.subspace([])
sage: WmodZ = W / Z
sage: WmodZ(W(0))
(0)
sage: loads(dumps(WmodZ))

Vector space quotient V/W of dimension 1 over Rational Field where
V: Vector space of degree 2 and dimension 1 over Rational Field
Basis matrix:
[1 1]
W: Vector space of degree 2 and dimension 0 over Rational Field
Basis matrix:
[]
```


Works for me. Add a doctest and close?



---

archive/issue_comments_063555.json:
```json
{
    "body": "Replying to [comment:8 sbrandhorst]:\n> Works for me. Add a doctest and close?\n\nYep. Addendum - Also works for me.",
    "created_at": "2017-10-09T04:32:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7516",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7516#issuecomment-63555",
    "user": "https://github.com/tscrim"
}
```

Replying to [comment:8 sbrandhorst]:
> Works for me. Add a doctest and close?

Yep. Addendum - Also works for me.



---

archive/issue_comments_063556.json:
```json
{
    "body": "Changing status from needs_info to needs_review.",
    "created_at": "2017-10-09T07:52:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7516",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7516#issuecomment-63556",
    "user": "https://github.com/simonbrandhorst"
}
```

Changing status from needs_info to needs_review.



---

archive/issue_comments_063557.json:
```json
{
    "body": "New commits:",
    "created_at": "2017-10-09T07:52:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7516",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7516#issuecomment-63557",
    "user": "https://github.com/simonbrandhorst"
}
```

New commits:



---

archive/issue_comments_063558.json:
```json
{
    "body": "Once you put your real name as author, you can set a positive review.",
    "created_at": "2017-10-09T15:30:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7516",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7516#issuecomment-63558",
    "user": "https://github.com/tscrim"
}
```

Once you put your real name as author, you can set a positive review.



---

archive/issue_comments_063559.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2017-10-09T16:10:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7516",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7516#issuecomment-63559",
    "user": "https://github.com/simonbrandhorst"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_063560.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2017-10-15T09:22:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7516",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7516#issuecomment-63560",
    "user": "https://github.com/vbraun"
}
```

Resolution: fixed

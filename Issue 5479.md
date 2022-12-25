# Issue 5479: schemes/generic/spec.py: Spec.__call__ is basically not implemented

archive/issues_005479.json:
```json
{
    "body": "Assignee: @williamstein\n\nRoi Docampo found this:\n\n```\nsage: S = Spec(ZZ)\nsage: S\nSpectrum of Integer Ring\nsage: S(3)\n---------------------------------------------------------------------------\nAttributeError                            Traceback (most recent call last)\n\n/home/aghitza/.sage/temp/cartan/6737/_home_aghitza__sage_init_sage_0.py in <module>()\n\n/opt/sage/local/lib/python2.5/site-packages/sage/schemes/generic/spec.pyc in __call__(self, x)\n    112         Create a point of this scheme.\n    113         \"\"\"\n--> 114         return point.SchemePoint_spec(self, x)\n    115 \n    116     def coordinate_ring(self):\n\nAttributeError: 'module' object has no attribute 'SchemePoint_spec'\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/5479\n\n",
    "created_at": "2009-03-11T04:09:10Z",
    "labels": [
        "component: algebraic geometry",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.4.2",
    "title": "schemes/generic/spec.py: Spec.__call__ is basically not implemented",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/5479",
    "user": "https://github.com/aghitza"
}
```
Assignee: @williamstein

Roi Docampo found this:

```
sage: S = Spec(ZZ)
sage: S
Spectrum of Integer Ring
sage: S(3)
---------------------------------------------------------------------------
AttributeError                            Traceback (most recent call last)

/home/aghitza/.sage/temp/cartan/6737/_home_aghitza__sage_init_sage_0.py in <module>()

/opt/sage/local/lib/python2.5/site-packages/sage/schemes/generic/spec.pyc in __call__(self, x)
    112         Create a point of this scheme.
    113         """
--> 114         return point.SchemePoint_spec(self, x)
    115 
    116     def coordinate_ring(self):

AttributeError: 'module' object has no attribute 'SchemePoint_spec'
```


Issue created by migration from https://trac.sagemath.org/ticket/5479





---

archive/issue_comments_042421.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2009-04-25T11:12:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5479",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5479#issuecomment-42421",
    "user": "https://github.com/aghitza"
}
```

Changing status from new to assigned.



---

archive/issue_comments_042422.json:
```json
{
    "body": "Changing assignee from @williamstein to @aghitza.",
    "created_at": "2009-04-25T11:12:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5479",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5479#issuecomment-42422",
    "user": "https://github.com/aghitza"
}
```

Changing assignee from @williamstein to @aghitza.



---

archive/issue_comments_042423.json:
```json
{
    "body": "The attached patch implements the `__call__` method.  For this I needed to fix a few things in `schemes/generic/point.py` (which has 0 doctests!).  I doctested the methods that I touched there, and I'll improve the doctest coverage further in another patch.",
    "created_at": "2009-04-25T11:12:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5479",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5479#issuecomment-42423",
    "user": "https://github.com/aghitza"
}
```

The attached patch implements the `__call__` method.  For this I needed to fix a few things in `schemes/generic/point.py` (which has 0 doctests!).  I doctested the methods that I touched there, and I'll improve the doctest coverage further in another patch.



---

archive/issue_comments_042424.json:
```json
{
    "body": "Changing keywords from \"\" to \"spectrum ring call\".",
    "created_at": "2009-04-25T11:12:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5479",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5479#issuecomment-42424",
    "user": "https://github.com/aghitza"
}
```

Changing keywords from "" to "spectrum ring call".



---

archive/issue_comments_042425.json:
```json
{
    "body": "Attachment [trac_5479.patch](tarball://root/attachments/some-uuid/ticket5479/trac_5479.patch) by @aghitza created at 2009-04-29 08:22:55\n\nDavid Roe pointed out in IRC that \"generic point\" has a well-defined technical meaning so it shouldn't be used in the `_repr_` method of `SchemeMorphism`.  So I've attached an updated patch that fixes the handful of occurrences of \"Generic point\".",
    "created_at": "2009-04-29T08:22:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5479",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5479#issuecomment-42425",
    "user": "https://github.com/aghitza"
}
```

Attachment [trac_5479.patch](tarball://root/attachments/some-uuid/ticket5479/trac_5479.patch) by @aghitza created at 2009-04-29 08:22:55

David Roe pointed out in IRC that "generic point" has a well-defined technical meaning so it shouldn't be used in the `_repr_` method of `SchemeMorphism`.  So I've attached an updated patch that fixes the handful of occurrences of "Generic point".



---

archive/issue_comments_042426.json:
```json
{
    "body": "Looks good now.",
    "created_at": "2009-04-29T18:04:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5479",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5479#issuecomment-42426",
    "user": "https://github.com/roed314"
}
```

Looks good now.



---

archive/issue_comments_042427.json:
```json
{
    "body": "Merged in Sage 3.4.2.rc0.\n\nCheers,\n\nMichael",
    "created_at": "2009-04-30T01:17:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5479",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5479#issuecomment-42427",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged in Sage 3.4.2.rc0.

Cheers,

Michael



---

archive/issue_comments_042428.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-04-30T01:17:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5479",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5479#issuecomment-42428",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed

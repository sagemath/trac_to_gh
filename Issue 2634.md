# Issue 2634: (easy fix?) Unable to create certain multivariate polynomial rings since libsingular is invoked instead of generic code

archive/issues_002634.json:
```json
{
    "body": "Assignee: malb\n\n\n```\nsage: k = GF(next_prime(2^31)^2,'x')\nsage: k['y,z']\nTraceback (most recent call last):\n...\nOverflowError: long int too large to convert to int\nsage: PolynomialRing(k,2,'x,y')\nTraceback (most recent call last):\n...\nOverflowError: long int too large to convert to int\n```\n\n\n\nThis is caused because Sage is trying to use libsingular\nto create the poly ring, but should be using its own code\nwhen the size of the base ring is too big. \n\nMartin Albrecht will be able to fix this very easily.\n\nIssue created by migration from https://trac.sagemath.org/ticket/2634\n\n",
    "created_at": "2008-03-21T18:48:19Z",
    "labels": [
        "commutative algebra",
        "major",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-2.11",
    "title": "(easy fix?) Unable to create certain multivariate polynomial rings since libsingular is invoked instead of generic code",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/2634",
    "user": "was"
}
```
Assignee: malb


```
sage: k = GF(next_prime(2^31)^2,'x')
sage: k['y,z']
Traceback (most recent call last):
...
OverflowError: long int too large to convert to int
sage: PolynomialRing(k,2,'x,y')
Traceback (most recent call last):
...
OverflowError: long int too large to convert to int
```



This is caused because Sage is trying to use libsingular
to create the poly ring, but should be using its own code
when the size of the base ring is too big. 

Martin Albrecht will be able to fix this very easily.

Issue created by migration from https://trac.sagemath.org/ticket/2634





---

archive/issue_comments_018094.json:
```json
{
    "body": "Attachment [trac_2634.patch](tarball://root/attachments/some-uuid/ticket2634/trac_2634.patch) by malb created at 2008-03-22 14:18:25\n\nThe attached patch implements the easy fix and worksforme. However, my installation is FUBAR right now so a referee would have to run `make test` but there should be no surprises. Sorry for the mess.",
    "created_at": "2008-03-22T14:18:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2634",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2634#issuecomment-18094",
    "user": "malb"
}
```

Attachment [trac_2634.patch](tarball://root/attachments/some-uuid/ticket2634/trac_2634.patch) by malb created at 2008-03-22 14:18:25

The attached patch implements the easy fix and worksforme. However, my installation is FUBAR right now so a referee would have to run `make test` but there should be no surprises. Sorry for the mess.



---

archive/issue_comments_018095.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2008-03-22T14:18:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2634",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2634#issuecomment-18095",
    "user": "malb"
}
```

Changing status from new to assigned.



---

archive/issue_comments_018096.json:
```json
{
    "body": "Hi,\n\nIt's good but there are two issues:\n\n1. sage -t sage/schemes/generic/affine_space.py fails:\n\n\n```\nsage -t  schemes/generic/affine_space.py                    **********************************************************************\nFile \"affine_space.py\", line 196:\n    sage: AffineSpace(ZZ,1, 'a') == AffineSpace(ZZ, 0, 'a')\nException raised:\n    Traceback (most recent call last):\n      File \"/opt/sage/local/lib/python2.5/doctest.py\", line 1212, in __run\n        compileflags, 1) in test.globs\n      File \"<doctest __main__.example_5[1]>\", line 1, in <module>\n        AffineSpace(ZZ,Integer(1), 'a') == AffineSpace(ZZ, Integer(0), 'a')###line 196:\n    sage: AffineSpace(ZZ,1, 'a') == AffineSpace(ZZ, 0, 'a')\n      File \"/opt/sage/local/lib/python2.5/site-packages/sage/schemes/generic/affine_space.py\", line 204, in __cmp__\n        [right.dimension(), right.coordinate_ring()])\n      File \"/opt/sage/local/lib/python2.5/site-packages/sage/schemes/generic/affine_space.py\", line 262, in coordinate_ring\n        self._coordinate_ring = MPolynomialRing(self.base_ring(), self.dimension(), names=self.variable_names())\n      File \"/opt/sage/local/lib/python2.5/site-packages/sage/rings/polynomial/polynomial_ring_constructor.py\", line 248, in PolynomialRing\n        R = _multi_variate(base_ring, names, n, sparse, order)\n      File \"/opt/sage/local/lib/python2.5/site-packages/sage/rings/polynomial/polynomial_ring_constructor.py\", line 365, in _multi_variate\n        R = MPolynomialRing_libsingular(base_ring, n, names, order)\n      File \"multi_polynomial_libsingular.pyx\", line 196, in sage.rings.polynomial.multi_polynomial_libsingular.MPolynomialRing_libsingular.__init__\n    ArithmeticError: number of variables must be at least 1\n**********************************************************************\n```\n\n\n\n2. this is minor; there's a typo in the new error message in multi_polynomial_libsingular.pyx: should be\n\n\n```\nraise NotImplementedError, \"Number fields are not fully supported yet.\" \n```\n\n\ninstead of \n\n\n```\nraise NotImplementedError, \"Number fields are not fully support yet.\"\n```\n\n\nI'll very happily give this a quick positive review as soon as these things get fixed.",
    "created_at": "2008-03-22T14:45:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2634",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2634#issuecomment-18096",
    "user": "AlexGhitza"
}
```

Hi,

It's good but there are two issues:

1. sage -t sage/schemes/generic/affine_space.py fails:


```
sage -t  schemes/generic/affine_space.py                    **********************************************************************
File "affine_space.py", line 196:
    sage: AffineSpace(ZZ,1, 'a') == AffineSpace(ZZ, 0, 'a')
Exception raised:
    Traceback (most recent call last):
      File "/opt/sage/local/lib/python2.5/doctest.py", line 1212, in __run
        compileflags, 1) in test.globs
      File "<doctest __main__.example_5[1]>", line 1, in <module>
        AffineSpace(ZZ,Integer(1), 'a') == AffineSpace(ZZ, Integer(0), 'a')###line 196:
    sage: AffineSpace(ZZ,1, 'a') == AffineSpace(ZZ, 0, 'a')
      File "/opt/sage/local/lib/python2.5/site-packages/sage/schemes/generic/affine_space.py", line 204, in __cmp__
        [right.dimension(), right.coordinate_ring()])
      File "/opt/sage/local/lib/python2.5/site-packages/sage/schemes/generic/affine_space.py", line 262, in coordinate_ring
        self._coordinate_ring = MPolynomialRing(self.base_ring(), self.dimension(), names=self.variable_names())
      File "/opt/sage/local/lib/python2.5/site-packages/sage/rings/polynomial/polynomial_ring_constructor.py", line 248, in PolynomialRing
        R = _multi_variate(base_ring, names, n, sparse, order)
      File "/opt/sage/local/lib/python2.5/site-packages/sage/rings/polynomial/polynomial_ring_constructor.py", line 365, in _multi_variate
        R = MPolynomialRing_libsingular(base_ring, n, names, order)
      File "multi_polynomial_libsingular.pyx", line 196, in sage.rings.polynomial.multi_polynomial_libsingular.MPolynomialRing_libsingular.__init__
    ArithmeticError: number of variables must be at least 1
**********************************************************************
```



2. this is minor; there's a typo in the new error message in multi_polynomial_libsingular.pyx: should be


```
raise NotImplementedError, "Number fields are not fully supported yet." 
```


instead of 


```
raise NotImplementedError, "Number fields are not fully support yet."
```


I'll very happily give this a quick positive review as soon as these things get fixed.



---

archive/issue_comments_018097.json:
```json
{
    "body": "fixes the typo reported by Alex.",
    "created_at": "2008-03-24T00:15:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2634",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2634#issuecomment-18097",
    "user": "malb"
}
```

fixes the typo reported by Alex.



---

archive/issue_comments_018098.json:
```json
{
    "body": "Attachment [2634_0gens.patch](tarball://root/attachments/some-uuid/ticket2634/2634_0gens.patch) by malb created at 2008-03-24 00:16:21\n\nallow 0 gens for multivariate polynomial rings (debatable!)",
    "created_at": "2008-03-24T00:16:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2634",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2634#issuecomment-18098",
    "user": "malb"
}
```

Attachment [2634_0gens.patch](tarball://root/attachments/some-uuid/ticket2634/2634_0gens.patch) by malb created at 2008-03-24 00:16:21

allow 0 gens for multivariate polynomial rings (debatable!)



---

archive/issue_comments_018099.json:
```json
{
    "body": "I've attached patches for both issues reported by Alex, **but** I am not convinced that it is actually desired to allow 0 generators for multivariate polynomial rings. We allowed that before and thus I reintroduced that behaviour but I would like to get rid of it: It will be a no fun to support once the generic multivariate polynomials get closer to C and I don't see the point.",
    "created_at": "2008-03-24T00:18:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2634",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2634#issuecomment-18099",
    "user": "malb"
}
```

I've attached patches for both issues reported by Alex, **but** I am not convinced that it is actually desired to allow 0 generators for multivariate polynomial rings. We allowed that before and thus I reintroduced that behaviour but I would like to get rid of it: It will be a no fun to support once the generic multivariate polynomials get closer to C and I don't see the point.



---

archive/issue_comments_018100.json:
```json
{
    "body": "I understand your objection.  I'm not comfortable deciding about that, so I'll throw it on sage-devel and see what people say.\n\nIn the mean time, the patches look good and doctest well.  I think we should apply them.",
    "created_at": "2008-03-24T02:49:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2634",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2634#issuecomment-18100",
    "user": "AlexGhitza"
}
```

I understand your objection.  I'm not comfortable deciding about that, so I'll throw it on sage-devel and see what people say.

In the mean time, the patches look good and doctest well.  I think we should apply them.



---

archive/issue_comments_018101.json:
```json
{
    "body": "To quote William from https://groups.google.com/group/sage-devel/t/2d722ebda3887a56\n\n```\nI definitely think multivariate polynomial rings with 0 generators\nshould be supported\nfor exactly the same reason matrices with 0 rows or columns should be\nsupported -- algorithms are much more likely to work in corner cases and code\nis cleaner.\n\nI've been incredibly glad on numerous occasions that across the board\nSage works very well with matrices that have 0 rows or columns, though\nthis took a lot of extra work initially.   The only argument put forth for\nremoving multivariate polynomials rings with 0 generators is \"It will\nbe a no fun to support\".   That is not compelling.\n\nWilliam \n```\n\n\nThis leads me to merge this patch now to fix the issue. I assume we will revisit this in the future since Martin commented right after William that\n\n```\n\nlibSingular doesn't support it and as soon as more pointers are involved the\ngeneric implementation will too have problems (== NULL pointers). Maybe a\nspecial implementation for zero generators is in order then?\n\nMartin \n```\n\n\nCheers,\n\nMichael",
    "created_at": "2008-03-24T08:14:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2634",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2634#issuecomment-18101",
    "user": "mabshoff"
}
```

To quote William from https://groups.google.com/group/sage-devel/t/2d722ebda3887a56

```
I definitely think multivariate polynomial rings with 0 generators
should be supported
for exactly the same reason matrices with 0 rows or columns should be
supported -- algorithms are much more likely to work in corner cases and code
is cleaner.

I've been incredibly glad on numerous occasions that across the board
Sage works very well with matrices that have 0 rows or columns, though
this took a lot of extra work initially.   The only argument put forth for
removing multivariate polynomials rings with 0 generators is "It will
be a no fun to support".   That is not compelling.

William 
```


This leads me to merge this patch now to fix the issue. I assume we will revisit this in the future since Martin commented right after William that

```

libSingular doesn't support it and as soon as more pointers are involved the
generic implementation will too have problems (== NULL pointers). Maybe a
special implementation for zero generators is in order then?

Martin 
```


Cheers,

Michael



---

archive/issue_comments_018102.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-03-24T08:35:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2634",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2634#issuecomment-18102",
    "user": "mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_018103.json:
```json
{
    "body": "Merged in Sage 2.11.alpha2",
    "created_at": "2008-03-24T08:35:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2634",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2634#issuecomment-18103",
    "user": "mabshoff"
}
```

Merged in Sage 2.11.alpha2

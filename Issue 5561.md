# Issue 5561: is_primitive does not belong in Polynomial because its definition varies

archive/issues_005561.json:
```json
{
    "body": "Assignee: tbd\n\nCC:  @JohnCremona cwitty\n\n(I'm not a mathematician.  Please correct any mistakes!)\n\nThe current `Polynomial` class (`sage/rings/polynomial/polynomial_element.pyx`) includes an `is_primitive` method.  However, field theory and ring theory have different definitions of a \"primitive polynomial.\"  Consequently, this base class for all polynomials is not an appropriate place for this method.  \n\nC.Witty suggested on IRC that one way to resolve the issue is to split up the polynomial classes into \"polynomials over fields\" and \"polynomials over rings.\"  Then these new base classes (and/or their derived classes) can implement `is_primitive` as appropriate.  In other words, create `PolynomialOverField` class and `PolynomialOverRing` classes that derive from `Polynomial`.  The other (univariate) polynomial classes in sage/rings/polynomial/ should then derive from either `PolynomialOverField` or `PolynomialOverRing` to pick up the correct `is_primitive` definition.\n\nThere may be other and possibly better ways to resolve the issue.\n\nJohn Cremona added this comment:\n\n  What Ryan suggest for is_primitive might be a good way to go;  as far\n  as I know the meaning which is relevant here, namely \"irreducible and\n  the root generates the multiplicative group of the extension\" is only\n  relevant over finite fields (and no other fields).  The other meaning\n  (coprime coefficients) is certainly not very useful over fields as it\n  is the same as \"non-zero\", so we are left with the question \"what, if\n  anything, should we take is_primitive() to mean for polynomials in\n  F[x] where F is an infinite field?\"\n\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/5561\n\n",
    "created_at": "2009-03-18T17:21:16Z",
    "labels": [
        "component: algebra",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.4.1",
    "title": "is_primitive does not belong in Polynomial because its definition varies",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/5561",
    "user": "https://github.com/rhinton"
}
```
Assignee: tbd

CC:  @JohnCremona cwitty

(I'm not a mathematician.  Please correct any mistakes!)

The current `Polynomial` class (`sage/rings/polynomial/polynomial_element.pyx`) includes an `is_primitive` method.  However, field theory and ring theory have different definitions of a "primitive polynomial."  Consequently, this base class for all polynomials is not an appropriate place for this method.  

C.Witty suggested on IRC that one way to resolve the issue is to split up the polynomial classes into "polynomials over fields" and "polynomials over rings."  Then these new base classes (and/or their derived classes) can implement `is_primitive` as appropriate.  In other words, create `PolynomialOverField` class and `PolynomialOverRing` classes that derive from `Polynomial`.  The other (univariate) polynomial classes in sage/rings/polynomial/ should then derive from either `PolynomialOverField` or `PolynomialOverRing` to pick up the correct `is_primitive` definition.

There may be other and possibly better ways to resolve the issue.

John Cremona added this comment:

  What Ryan suggest for is_primitive might be a good way to go;  as far
  as I know the meaning which is relevant here, namely "irreducible and
  the root generates the multiplicative group of the extension" is only
  relevant over finite fields (and no other fields).  The other meaning
  (coprime coefficients) is certainly not very useful over fields as it
  is the same as "non-zero", so we are left with the question "what, if
  anything, should we take is_primitive() to mean for polynomials in
  F[x] where F is an infinite field?"



Issue created by migration from https://trac.sagemath.org/ticket/5561





---

archive/issue_comments_043192.json:
```json
{
    "body": "On second thougths, Carl Witty's suggestion seems to be overdoing things a bit.\n\nWe could just do this (all explained properly in docstrings, of course):   \n\n```\nR=self.base_ring()\nif R.is_field() and R.is_finite():\n# use the current code\nelse:\n   return R.ideal(self.coefficient_list())==R.ideal(1)\n```\n",
    "created_at": "2009-03-18T20:13:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5561",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5561#issuecomment-43192",
    "user": "https://github.com/JohnCremona"
}
```

On second thougths, Carl Witty's suggestion seems to be overdoing things a bit.

We could just do this (all explained properly in docstrings, of course):   

```
R=self.base_ring()
if R.is_field() and R.is_finite():
# use the current code
else:
   return R.ideal(self.coefficient_list())==R.ideal(1)
```




---

archive/issue_comments_043193.json:
```json
{
    "body": "Patch applies against 3.4.1.alpha0 or 3.4.0 on top of patch for #5535.  Note that #5658 provides a performance improvement when q<sup>d</sup>-1 is prime (order<sup>degree</sup> - 1).",
    "created_at": "2009-04-01T15:35:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5561",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5561#issuecomment-43193",
    "user": "https://github.com/rhinton"
}
```

Patch applies against 3.4.1.alpha0 or 3.4.0 on top of patch for #5535.  Note that #5658 provides a performance improvement when q<sup>d</sup>-1 is prime (order<sup>degree</sup> - 1).



---

archive/issue_comments_043194.json:
```json
{
    "body": "review: needs a little work!\n    \n1. insert \"not\" before \"R.is_finite()\" !\n2. the line  return R.ideal(self.coefficient_list())==R.ideal(1)  does not work.\n\nBoth these were discovered using plain \"sage -t\" on the file.\n\nI fear that resolving the second one will reveal nasty inconsistencies in ideal creation for various rings.   First change self.coefficient_list() to self.list(), I think.  And change R.ideal(1) to R.unit_ideal().  then the only thing which fails is the pair of examples over Integers(10).  But this is a different bug:\n\n```\nsage: Integers(10).ideal([5,2])\n---------------------------------------------------------------------------\nAttributeError                            Traceback (most recent call last)\n\n/home/masgaj/.sage/temp/host_56_150/31627/_home_masgaj__sage_init_sage_0.py in <module>()\n\n/local/jec/sage-3.4.1.alpha0/local/lib/python2.5/site-packages/sage/rings/quotient_ring.pyc in ideal(self, *gens, **kwds)\n    487             gens = gens[0]\n    488         from sage.rings.polynomial.multi_polynomial_libsingular import MPolynomialRing_libsingular\n--> 489         if not isinstance(self.__R,MPolynomialRing_libsingular) and not self.__R._has_singular:\n    490             # pass through\n    491             MPolynomialRing_generic.ideal(self,gens,**kwds)\n\nAttributeError: 'sage.rings.integer_ring.IntegerRing_class' object has no attribute '_has_singular'\n```\n\n\nwhich will have to get ticketed and fixed before this one is done (unless we just delete that example for now).",
    "created_at": "2009-04-01T16:02:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5561",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5561#issuecomment-43194",
    "user": "https://github.com/JohnCremona"
}
```

review: needs a little work!
    
1. insert "not" before "R.is_finite()" !
2. the line  return R.ideal(self.coefficient_list())==R.ideal(1)  does not work.

Both these were discovered using plain "sage -t" on the file.

I fear that resolving the second one will reveal nasty inconsistencies in ideal creation for various rings.   First change self.coefficient_list() to self.list(), I think.  And change R.ideal(1) to R.unit_ideal().  then the only thing which fails is the pair of examples over Integers(10).  But this is a different bug:

```
sage: Integers(10).ideal([5,2])
---------------------------------------------------------------------------
AttributeError                            Traceback (most recent call last)

/home/masgaj/.sage/temp/host_56_150/31627/_home_masgaj__sage_init_sage_0.py in <module>()

/local/jec/sage-3.4.1.alpha0/local/lib/python2.5/site-packages/sage/rings/quotient_ring.pyc in ideal(self, *gens, **kwds)
    487             gens = gens[0]
    488         from sage.rings.polynomial.multi_polynomial_libsingular import MPolynomialRing_libsingular
--> 489         if not isinstance(self.__R,MPolynomialRing_libsingular) and not self.__R._has_singular:
    490             # pass through
    491             MPolynomialRing_generic.ideal(self,gens,**kwds)

AttributeError: 'sage.rings.integer_ring.IntegerRing_class' object has no attribute '_has_singular'
```


which will have to get ticketed and fixed before this one is done (unless we just delete that example for now).



---

archive/issue_comments_043195.json:
```json
{
    "body": "Thanks for looking at this!  I had already fixed (1) and the coefficient_list part of (2).  I'll comment out the examples for now -- do you want to create a ticket or shall I?\n\nThis patch needs some examples of the ring functionality.  Can you provide any good (i.e. non-trivial, working) examples of the ring semantics?",
    "created_at": "2009-04-01T16:14:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5561",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5561#issuecomment-43195",
    "user": "https://github.com/rhinton"
}
```

Thanks for looking at this!  I had already fixed (1) and the coefficient_list part of (2).  I'll comment out the examples for now -- do you want to create a ticket or shall I?

This patch needs some examples of the ring functionality.  Can you provide any good (i.e. non-trivial, working) examples of the ring semantics?



---

archive/issue_comments_043196.json:
```json
{
    "body": "Changing assignee from tbd to @rhinton.",
    "created_at": "2009-04-01T16:16:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5561",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5561#issuecomment-43196",
    "user": "https://github.com/rhinton"
}
```

Changing assignee from tbd to @rhinton.



---

archive/issue_comments_043197.json:
```json
{
    "body": "Attachment [trac_5561_is_primitive_ring_field.patch](tarball://root/attachments/some-uuid/ticket5561/trac_5561_is_primitive_ring_field.patch) by @rhinton created at 2009-04-01 20:02:02\n\nThe new patch compiles and passes the doctests, but it has no tests for the new ring functionality.  John, can you provide any good examples (that will work)?  Do you want to report the integer mod ring ideal problem, or shall I?",
    "created_at": "2009-04-01T20:02:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5561",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5561#issuecomment-43197",
    "user": "https://github.com/rhinton"
}
```

Attachment [trac_5561_is_primitive_ring_field.patch](tarball://root/attachments/some-uuid/ticket5561/trac_5561_is_primitive_ring_field.patch) by @rhinton created at 2009-04-01 20:02:02

The new patch compiles and passes the doctests, but it has no tests for the new ring functionality.  John, can you provide any good examples (that will work)?  Do you want to report the integer mod ring ideal problem, or shall I?



---

archive/issue_comments_043198.json:
```json
{
    "body": "Attachment [trac_5561.patch](tarball://root/attachments/some-uuid/ticket5561/trac_5561.patch) by @JohnCremona created at 2009-04-02 08:05:21\n\nreplaces previous",
    "created_at": "2009-04-02T08:05:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5561",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5561#issuecomment-43198",
    "user": "https://github.com/JohnCremona"
}
```

Attachment [trac_5561.patch](tarball://root/attachments/some-uuid/ticket5561/trac_5561.patch) by @JohnCremona created at 2009-04-02 08:05:21

replaces previous



---

archive/issue_comments_043199.json:
```json
{
    "body": "I have added a new patch (replaces previous) which just adds examples for the ring functionality.\n\nI could not find a ticket relevant to the ideal creation problem for Integers(10) but have asked about it on sage-devel and will open a new ticket if appropriate.\n\ncwitty, any chance of a review?",
    "created_at": "2009-04-02T08:06:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5561",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5561#issuecomment-43199",
    "user": "https://github.com/JohnCremona"
}
```

I have added a new patch (replaces previous) which just adds examples for the ring functionality.

I could not find a ticket relevant to the ideal creation problem for Integers(10) but have asked about it on sage-devel and will open a new ticket if appropriate.

cwitty, any chance of a review?



---

archive/issue_comments_043200.json:
```json
{
    "body": "Code looks good, doctests pass.  Positive review.",
    "created_at": "2009-04-11T05:43:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5561",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5561#issuecomment-43200",
    "user": "https://trac.sagemath.org/admin/accounts/users/cwitty"
}
```

Code looks good, doctests pass.  Positive review.



---

archive/issue_comments_043201.json:
```json
{
    "body": "Merged trac_5561.patch in Sage 3.4.1.rc3.\n\nCheers,\n\nMichael",
    "created_at": "2009-04-13T03:36:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5561",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5561#issuecomment-43201",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged trac_5561.patch in Sage 3.4.1.rc3.

Cheers,

Michael



---

archive/issue_comments_043202.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-04-13T03:36:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5561",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5561#issuecomment-43202",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed

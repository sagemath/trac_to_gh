# Issue 9413: Bug in tamagawa_product_bsd for elliptic curves over QQ

archive/issues_009413.json:
```json
{
    "body": "Assignee: cremona\n\n\n```\nsage: E = EllipticCurve('30a')\nsage: E.tamagawa_product_bsd()\n---------------------------------------------------------------------------\nAttributeError                            Traceback (most recent call last)\n\n/storage/masiao/sage-4.5.alpha1/devel/sage-reviewing/sage/schemes/elliptic_curves/<ipython console> in <module>()\n\n/storage/masiao/sage-4.5.alpha1/local/lib/python2.6/site-packages/sage/schemes/elliptic_curves/ell_number_field.pyc in tamagawa_product_bsd(self)\n   1144             # the differential associated to this particular equation E\n   1145             uu = self.isomorphism_to(dav.minimal_model()).u\n-> 1146             uu_abs_val = pp.smallest_integer()**(pp.residue_class_degree()*valuation(uu,pp))\n   1147             pr *= cv * uu_abs_val\n   1148         return pr\n\n/storage/masiao/sage-4.5.alpha1/local/lib/python2.6/site-packages/sage/structure/element.so in sage.structure.element.Element.__getattr__ (sage/structure/element.c:2632)()\n\n/storage/masiao/sage-4.5.alpha1/local/lib/python2.6/site-packages/sage/structure/parent.so in sage.structure.parent.getattr_from_other_class (sage/structure/parent.c:2835)()\n\n/storage/masiao/sage-4.5.alpha1/local/lib/python2.6/site-packages/sage/structure/parent.so in sage.structure.parent.raise_attribute_error (sage/structure/parent.c:2629)()\n\nAttributeError: 'Ideal_pid' object has no attribute 'smallest_integer'\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/9413\n\n",
    "created_at": "2010-07-02T21:50:42Z",
    "labels": [
        "elliptic curves",
        "minor",
        "bug"
    ],
    "title": "Bug in tamagawa_product_bsd for elliptic curves over QQ",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/9413",
    "user": "davidloeffler"
}
```
Assignee: cremona


```
sage: E = EllipticCurve('30a')
sage: E.tamagawa_product_bsd()
---------------------------------------------------------------------------
AttributeError                            Traceback (most recent call last)

/storage/masiao/sage-4.5.alpha1/devel/sage-reviewing/sage/schemes/elliptic_curves/<ipython console> in <module>()

/storage/masiao/sage-4.5.alpha1/local/lib/python2.6/site-packages/sage/schemes/elliptic_curves/ell_number_field.pyc in tamagawa_product_bsd(self)
   1144             # the differential associated to this particular equation E
   1145             uu = self.isomorphism_to(dav.minimal_model()).u
-> 1146             uu_abs_val = pp.smallest_integer()**(pp.residue_class_degree()*valuation(uu,pp))
   1147             pr *= cv * uu_abs_val
   1148         return pr

/storage/masiao/sage-4.5.alpha1/local/lib/python2.6/site-packages/sage/structure/element.so in sage.structure.element.Element.__getattr__ (sage/structure/element.c:2632)()

/storage/masiao/sage-4.5.alpha1/local/lib/python2.6/site-packages/sage/structure/parent.so in sage.structure.parent.getattr_from_other_class (sage/structure/parent.c:2835)()

/storage/masiao/sage-4.5.alpha1/local/lib/python2.6/site-packages/sage/structure/parent.so in sage.structure.parent.raise_attribute_error (sage/structure/parent.c:2629)()

AttributeError: 'Ideal_pid' object has no attribute 'smallest_integer'
```


Issue created by migration from https://trac.sagemath.org/ticket/9413





---

archive/issue_comments_089733.json:
```json
{
    "body": "Attachment",
    "created_at": "2010-07-27T17:59:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9413",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9413#issuecomment-89733",
    "user": "wuthrich"
}
```

Attachment



---

archive/issue_comments_089734.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-07-27T17:59:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9413",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9413#issuecomment-89734",
    "user": "wuthrich"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_089735.json:
```json
{
    "body": "Looks fine, applies ok to 4.5.3.alpha1 (with a little fuzz) and all tests in ell_number_field pass (no other files call this function).",
    "created_at": "2010-08-21T16:19:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9413",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9413#issuecomment-89735",
    "user": "cremona"
}
```

Looks fine, applies ok to 4.5.3.alpha1 (with a little fuzz) and all tests in ell_number_field pass (no other files call this function).



---

archive/issue_comments_089736.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-08-21T16:19:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9413",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9413#issuecomment-89736",
    "user": "cremona"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_089737.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-09-15T11:38:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9413",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9413#issuecomment-89737",
    "user": "mpatel"
}
```

Resolution: fixed

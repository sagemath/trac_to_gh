# Issue 5353: add xgcd for polynomial over GF(2)

archive/issues_005353.json:
```json
{
    "body": "Assignee: malb\n\nCurrently, this fails:\n\n\n```\nsage: R.<x> = GF(2)[]\nsage: fr = ((x+1)/(x^3+x+1) + (x+1)/(x^3+x^2+1));\nsage: fr.partial_fraction_decomposition() \n---------------------------------------------------------------------------\nNotImplementedError                       Traceback (most recent call last)\n\n/home/mhansen/.sage/temp/sage.math.washington.edu/19940/_home_mhansen__sage_init_sage_0.py in <module>()\n\n/home/mhansen/sage-3.3.alpha0-sage.math-only-x86_64-Linux/local/lib/python2.5/site-packages/sage/rings/fraction_field_element.so in sage.rings.fraction_field_element.FractionFieldElement.partial_fraction_decomposition (sage/rings/fraction_field_element.c:3052)()\n\n/home/mhansen/sage-3.3.alpha0-sage.math-only-x86_64-Linux/local/lib/python2.5/site-packages/sage/rings/polynomial/polynomial_element.so in sage.rings.polynomial.polynomial_element.Polynomial.inverse_mod (sage/rings/polynomial/polynomial_element.c:8191)()\n\n/home/mhansen/sage-3.3.alpha0-sage.math-only-x86_64-Linux/local/lib/python2.5/site-packages/sage/rings/polynomial/polynomial_gf2x.so in sage.rings.polynomial.polynomial_gf2x.Polynomial_template.xgcd (sage/rings/polynomial/polynomial_gf2x.cpp:5685)()\n\n/home/mhansen/sage-3.3.alpha0-sage.math-only-x86_64-Linux/local/lib/python2.5/site-packages/sage/rings/polynomial/polynomial_gf2x.so in sage.rings.polynomial.polynomial_gf2x.celement_xgcd (sage/rings/polynomial/polynomial_gf2x.cpp:3517)()\n\nNotImplementedError: \n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/5353\n\n",
    "created_at": "2009-02-23T23:51:42Z",
    "labels": [
        "commutative algebra",
        "minor",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.4.1",
    "title": "add xgcd for polynomial over GF(2)",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/5353",
    "user": "mhansen"
}
```
Assignee: malb

Currently, this fails:


```
sage: R.<x> = GF(2)[]
sage: fr = ((x+1)/(x^3+x+1) + (x+1)/(x^3+x^2+1));
sage: fr.partial_fraction_decomposition() 
---------------------------------------------------------------------------
NotImplementedError                       Traceback (most recent call last)

/home/mhansen/.sage/temp/sage.math.washington.edu/19940/_home_mhansen__sage_init_sage_0.py in <module>()

/home/mhansen/sage-3.3.alpha0-sage.math-only-x86_64-Linux/local/lib/python2.5/site-packages/sage/rings/fraction_field_element.so in sage.rings.fraction_field_element.FractionFieldElement.partial_fraction_decomposition (sage/rings/fraction_field_element.c:3052)()

/home/mhansen/sage-3.3.alpha0-sage.math-only-x86_64-Linux/local/lib/python2.5/site-packages/sage/rings/polynomial/polynomial_element.so in sage.rings.polynomial.polynomial_element.Polynomial.inverse_mod (sage/rings/polynomial/polynomial_element.c:8191)()

/home/mhansen/sage-3.3.alpha0-sage.math-only-x86_64-Linux/local/lib/python2.5/site-packages/sage/rings/polynomial/polynomial_gf2x.so in sage.rings.polynomial.polynomial_gf2x.Polynomial_template.xgcd (sage/rings/polynomial/polynomial_gf2x.cpp:5685)()

/home/mhansen/sage-3.3.alpha0-sage.math-only-x86_64-Linux/local/lib/python2.5/site-packages/sage/rings/polynomial/polynomial_gf2x.so in sage.rings.polynomial.polynomial_gf2x.celement_xgcd (sage/rings/polynomial/polynomial_gf2x.cpp:3517)()

NotImplementedError: 
```


Issue created by migration from https://trac.sagemath.org/ticket/5353





---

archive/issue_comments_041243.json:
```json
{
    "body": "Currently, in sage.libs.ntl.ntl_GF2X_linkage.pyx celement_xgcd just raises a NotImplementedError, but NTL does provide a xgcd for GF2X elements.",
    "created_at": "2009-02-23T23:56:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5353",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5353#issuecomment-41243",
    "user": "mhansen"
}
```

Currently, in sage.libs.ntl.ntl_GF2X_linkage.pyx celement_xgcd just raises a NotImplementedError, but NTL does provide a xgcd for GF2X elements.



---

archive/issue_comments_041244.json:
```json
{
    "body": "Attachment [trac_5353.patch](tarball://root/attachments/some-uuid/ticket5353/trac_5353.patch) by mhansen created at 2009-02-24 01:59:05",
    "created_at": "2009-02-24T01:59:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5353",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5353#issuecomment-41244",
    "user": "mhansen"
}
```

Attachment [trac_5353.patch](tarball://root/attachments/some-uuid/ticket5353/trac_5353.patch) by mhansen created at 2009-02-24 01:59:05



---

archive/issue_comments_041245.json:
```json
{
    "body": "Changing assignee from malb to mhansen.",
    "created_at": "2009-02-24T01:59:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5353",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5353#issuecomment-41245",
    "user": "mhansen"
}
```

Changing assignee from malb to mhansen.



---

archive/issue_comments_041246.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2009-02-24T01:59:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5353",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5353#issuecomment-41246",
    "user": "mhansen"
}
```

Changing status from new to assigned.



---

archive/issue_comments_041247.json:
```json
{
    "body": "The patch seems good but why does\n\n```\nf.xgcd?\n```\n\nshow another docstring?",
    "created_at": "2009-02-25T11:12:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5353",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5353#issuecomment-41247",
    "user": "ylchapuy"
}
```

The patch seems good but why does

```
f.xgcd?
```

show another docstring?



---

archive/issue_comments_041248.json:
```json
{
    "body": "This is due to the polynomial templating which allows many of the polynomial types to share lots of boilerplate code.  The generic code for xgcd calls the celement_xgcd defined here.",
    "created_at": "2009-02-25T11:15:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5353",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5353#issuecomment-41248",
    "user": "mhansen"
}
```

This is due to the polynomial templating which allows many of the polynomial types to share lots of boilerplate code.  The generic code for xgcd calls the celement_xgcd defined here.



---

archive/issue_comments_041249.json:
```json
{
    "body": "ok with sage 3.4",
    "created_at": "2009-03-16T17:35:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5353",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5353#issuecomment-41249",
    "user": "ylchapuy"
}
```

ok with sage 3.4



---

archive/issue_comments_041250.json:
```json
{
    "body": "Merged in Sage 3.4.1.alpha0.\n\nCheers,\n\nMichael",
    "created_at": "2009-03-25T06:01:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5353",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5353#issuecomment-41250",
    "user": "mabshoff"
}
```

Merged in Sage 3.4.1.alpha0.

Cheers,

Michael



---

archive/issue_comments_041251.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-03-25T06:01:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5353",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5353#issuecomment-41251",
    "user": "mabshoff"
}
```

Resolution: fixed

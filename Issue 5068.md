# Issue 5068: change_ring fails for polynomials over finite fields in many cases

archive/issues_005068.json:
```json
{
    "body": "Assignee: robertwb\n\n\n```\nsage: R.<x> = GF(9,'a')[]\nsage: x.change_ring(GF(3))\nBOOM!\n\nsage: R.<x,y> = GF(9,'a')[]\nsage: x.change_ring(GF(3))\nBOOM!\nTypeError: unable to coerce <type 'sage.rings.finite_field_givaro.FiniteField_givaroElement'> to an integer\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/5068\n\n",
    "created_at": "2009-01-23T10:38:14Z",
    "labels": [
        "coercion",
        "major",
        "bug"
    ],
    "title": "change_ring fails for polynomials over finite fields in many cases",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/5068",
    "user": "was"
}
```
Assignee: robertwb


```
sage: R.<x> = GF(9,'a')[]
sage: x.change_ring(GF(3))
BOOM!

sage: R.<x,y> = GF(9,'a')[]
sage: x.change_ring(GF(3))
BOOM!
TypeError: unable to coerce <type 'sage.rings.finite_field_givaro.FiniteField_givaroElement'> to an integer
```


Issue created by migration from https://trac.sagemath.org/ticket/5068





---

archive/issue_comments_038604.json:
```json
{
    "body": "The generic MPolynomial_polydict poly's work fine as looking at the code shows, but the libsingular ones break:\n\n```\nsage: p = next_prime(10^30); f = GF(p^2,'a')['x,y'].gen()\nsage: type(f)\n<class 'sage.rings.polynomial.multi_polynomial_element.MPolynomial_polydict'>\nsage: f.change_ring(GF(p))\nx\nsage: p = next_prime(20); f = GF(p^2,'a')['x,y'].gen()\nsage: type(f)\n<type 'sage.rings.polynomial.multi_polynomial_libsingular.MPolynomial_libsingular'>\nsage: f.change_ring(GF(p))\n---------------------------------------------------------------------------\nTypeError                                 Traceback (most recent call last)\n\n/Users/wstein/.sage/temp/teragon.local/22907/_Users_wstein__sage_init_sage_0.py in <module>()\n----> 1 \n      2 \n      3 \n      4 \n      5 \n\n/Users/wstein/build/sage-3.3.alpha0/local/lib/python2.5/site-packages/sage/rings/polynomial/multi_polynomial.so in sage.rings.polynomial.multi_polynomial.MPolynomial.change_ring (sage/rings/polynomial/multi_polynomial.c:6691)()\n    661 \n    662 \n--> 663 \n    664 \n    665 \n\n/Users/wstein/build/sage-3.3.alpha0/local/lib/python2.5/site-packages/sage/rings/polynomial/multi_polynomial_libsingular.so in sage.rings.polynomial.multi_polynomial_libsingular.MPolynomialRing_libsingular.__call__ (sage/rings/polynomial/multi_polynomial_libsingular.cpp:6267)()\n    616 \n    617 \n--> 618 \n    619 \n    620 \n\nTypeError: unable to coerce <type 'sage.rings.finite_field_givaro.FiniteField_givaroElement'> to an integer\n```\n\n\nThis is because the givaro finite field __call__ is wrong:\n\n```\nsage: GF(23)(GF(23^2,'a')(1))\nBOOM!\nTypeError: unable to coerce <type 'sage.rings.finite_field_givaro.FiniteField_givaroElement'> to an integer\n\nbut\n\nsage: GF(next_prime(10^20))(GF(next_prime(10^20)^2,'a')(1))\n1\n```\n",
    "created_at": "2009-01-23T11:00:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5068",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5068#issuecomment-38604",
    "user": "was"
}
```

The generic MPolynomial_polydict poly's work fine as looking at the code shows, but the libsingular ones break:

```
sage: p = next_prime(10^30); f = GF(p^2,'a')['x,y'].gen()
sage: type(f)
<class 'sage.rings.polynomial.multi_polynomial_element.MPolynomial_polydict'>
sage: f.change_ring(GF(p))
x
sage: p = next_prime(20); f = GF(p^2,'a')['x,y'].gen()
sage: type(f)
<type 'sage.rings.polynomial.multi_polynomial_libsingular.MPolynomial_libsingular'>
sage: f.change_ring(GF(p))
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)

/Users/wstein/.sage/temp/teragon.local/22907/_Users_wstein__sage_init_sage_0.py in <module>()
----> 1 
      2 
      3 
      4 
      5 

/Users/wstein/build/sage-3.3.alpha0/local/lib/python2.5/site-packages/sage/rings/polynomial/multi_polynomial.so in sage.rings.polynomial.multi_polynomial.MPolynomial.change_ring (sage/rings/polynomial/multi_polynomial.c:6691)()
    661 
    662 
--> 663 
    664 
    665 

/Users/wstein/build/sage-3.3.alpha0/local/lib/python2.5/site-packages/sage/rings/polynomial/multi_polynomial_libsingular.so in sage.rings.polynomial.multi_polynomial_libsingular.MPolynomialRing_libsingular.__call__ (sage/rings/polynomial/multi_polynomial_libsingular.cpp:6267)()
    616 
    617 
--> 618 
    619 
    620 

TypeError: unable to coerce <type 'sage.rings.finite_field_givaro.FiniteField_givaroElement'> to an integer
```


This is because the givaro finite field __call__ is wrong:

```
sage: GF(23)(GF(23^2,'a')(1))
BOOM!
TypeError: unable to coerce <type 'sage.rings.finite_field_givaro.FiniteField_givaroElement'> to an integer

but

sage: GF(next_prime(10^20))(GF(next_prime(10^20)^2,'a')(1))
1
```




---

archive/issue_comments_038605.json:
```json
{
    "body": "Attachment",
    "created_at": "2009-01-23T12:12:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5068",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5068#issuecomment-38605",
    "user": "was"
}
```

Attachment



---

archive/issue_comments_038606.json:
```json
{
    "body": "looks good.",
    "created_at": "2009-01-23T17:31:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5068",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5068#issuecomment-38606",
    "user": "malb"
}
```

looks good.



---

archive/issue_comments_038607.json:
```json
{
    "body": "Merged in Sage 3.3.alpha2",
    "created_at": "2009-01-24T14:48:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5068",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5068#issuecomment-38607",
    "user": "mabshoff"
}
```

Merged in Sage 3.3.alpha2



---

archive/issue_comments_038608.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-01-24T14:48:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5068",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5068#issuecomment-38608",
    "user": "mabshoff"
}
```

Resolution: fixed

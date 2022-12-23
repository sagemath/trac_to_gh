# Issue 9182: Jacobian of a Hyperelliptic curve doesn't coerces correctly

archive/issues_009182.json:
```json
{
    "body": "Assignee: AlexGhitza\n\nKeywords: Point, Hyperelliptic curve\n\nWhen defining a point on the Jacobian of a Hyperellptic curve, \nif a coordinate is an integer, it does not get coerced to polynomial and the following error raised:\nraise TypeError, \"Argument P (= %s) must have length 2.\"%P\nFor example:\n\n```\nsage: F.<a> = GF(3)\nsage: R.<x> = F[]\nsage: f = x^5-1\nsage: C = HyperellipticCurve(f)\nsage: J = C.jacobian()\nsage: X = J(F)\nsage: a = x^2-x+1\nsage: b = -x +1\nsage: c = x-1\nsage: d = 0 \nsage: D1 = X([a,b])\nsage: D2 = X([c,d])\n---------------------------------------------------------------------------\nTypeError                                 Traceback (most recent call last)\n\n/home/aly/Desktop/sage-4.3.1/<ipython console> in <module>()\n\n/home/aly/Desktop/sage-4.3.1/local/lib/python2.6/site-packages/sage/schemes/hyperelliptic_curves/jacobian_homset.py in __call__(self, P)\n     86                 if is_SchemeMorphism(P1) and is_SchemeMorphism(P2):\n     87                     return self(P1) - self(P2)\n---> 88             raise TypeError, \"Argument P (= %s) must have length 2.\"%P\n     89         elif isinstance(P,JacobianMorphism_divisor_class_field) and self == P.parent():\n     90             return P\n\nTypeError: Argument P (= [x + 2, 0]) must have length 2.\nsage: D2 = X([c,R(d)])                                                                               \nsage: D2\n(x + 2, y)\n\n\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/9182\n\n",
    "created_at": "2010-06-08T00:37:34Z",
    "labels": [
        "algebra",
        "trivial",
        "bug"
    ],
    "title": "Jacobian of a Hyperelliptic curve doesn't coerces correctly",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/9182",
    "user": "aly.deines"
}
```
Assignee: AlexGhitza

Keywords: Point, Hyperelliptic curve

When defining a point on the Jacobian of a Hyperellptic curve, 
if a coordinate is an integer, it does not get coerced to polynomial and the following error raised:
raise TypeError, "Argument P (= %s) must have length 2."%P
For example:

```
sage: F.<a> = GF(3)
sage: R.<x> = F[]
sage: f = x^5-1
sage: C = HyperellipticCurve(f)
sage: J = C.jacobian()
sage: X = J(F)
sage: a = x^2-x+1
sage: b = -x +1
sage: c = x-1
sage: d = 0 
sage: D1 = X([a,b])
sage: D2 = X([c,d])
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)

/home/aly/Desktop/sage-4.3.1/<ipython console> in <module>()

/home/aly/Desktop/sage-4.3.1/local/lib/python2.6/site-packages/sage/schemes/hyperelliptic_curves/jacobian_homset.py in __call__(self, P)
     86                 if is_SchemeMorphism(P1) and is_SchemeMorphism(P2):
     87                     return self(P1) - self(P2)
---> 88             raise TypeError, "Argument P (= %s) must have length 2."%P
     89         elif isinstance(P,JacobianMorphism_divisor_class_field) and self == P.parent():
     90             return P

TypeError: Argument P (= [x + 2, 0]) must have length 2.
sage: D2 = X([c,R(d)])                                                                               
sage: D2
(x + 2, y)


```


Issue created by migration from https://trac.sagemath.org/ticket/9182





---

archive/issue_comments_085900.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-06-08T00:54:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9182",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9182#issuecomment-85900",
    "user": "aly.deines"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_085901.json:
```json
{
    "body": "Attachment",
    "created_at": "2010-06-08T00:54:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9182",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9182#issuecomment-85901",
    "user": "aly.deines"
}
```

Attachment



---

archive/issue_comments_085902.json:
```json
{
    "body": "Those double colon lines should look like they do in the examples here:\n\nhttp://www.sagemath.org/doc/developer/conventions.html\n\nWithout those extra newlines, it won't process correctly. Also, the code coming after a double colon should be further indented than the colons.",
    "created_at": "2010-06-08T13:47:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9182",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9182#issuecomment-85902",
    "user": "rlm"
}
```

Those double colon lines should look like they do in the examples here:

http://www.sagemath.org/doc/developer/conventions.html

Without those extra newlines, it won't process correctly. Also, the code coming after a double colon should be further indented than the colons.



---

archive/issue_comments_085903.json:
```json
{
    "body": "Attachment",
    "created_at": "2010-06-08T14:59:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9182",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9182#issuecomment-85903",
    "user": "aly.deines"
}
```

Attachment



---

archive/issue_comments_085904.json:
```json
{
    "body": "Ok, changed.",
    "created_at": "2010-06-08T15:01:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9182",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9182#issuecomment-85904",
    "user": "aly.deines"
}
```

Ok, changed.



---

archive/issue_comments_085905.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-06-08T17:35:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9182",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9182#issuecomment-85905",
    "user": "rlm"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_085906.json:
```json
{
    "body": "Changing priority from trivial to minor.",
    "created_at": "2010-06-08T17:35:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9182",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9182#issuecomment-85906",
    "user": "rlm"
}
```

Changing priority from trivial to minor.



---

archive/issue_comments_085907.json:
```json
{
    "body": "Looks good to me.",
    "created_at": "2010-06-08T17:35:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9182",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9182#issuecomment-85907",
    "user": "rlm"
}
```

Looks good to me.



---

archive/issue_comments_085908.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-06-09T02:34:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9182",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9182#issuecomment-85908",
    "user": "mhansen"
}
```

Resolution: fixed

# Issue 5225: unhandled case in converting to polynomial ring

archive/issues_005225.json:
```json
{
    "body": "Assignee: malb\n\nNormally, Sage tries to allow explicit conversions between arbitrary polynomial rings, if they share the same variable names.\n\nHere's a case where that doesn't work:\n\n```\nR.<a,b,c,d,e,f,x,y,z,t,s,r>=PolynomialRing(QQ,12,order='lex')\nI=R.ideal(a^2+d^2-x,a*b+d*e-y,a*c+d*f-z,b^2+e^2-t,b*c+e*f-s,c*c+f*f-r)\nj=I.groebner_basis()\nR1.<x,y,z,t,s,r>=QQ[]\nR2=FractionField(R1)\nR3.<a,b,c,d,e,f>=R1.fraction_field()[]\nR3(j[0])\n```\n\n\nFor now, the workaround is:\n\n```\n sage_eval(str(j[0]), locals=locals())\n```\n\nbut IMHO the original code should work.\n\nIssue created by migration from https://trac.sagemath.org/ticket/5225\n\n",
    "created_at": "2009-02-09T22:14:57Z",
    "labels": [
        "commutative algebra",
        "major",
        "bug"
    ],
    "title": "unhandled case in converting to polynomial ring",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/5225",
    "user": "cwitty"
}
```
Assignee: malb

Normally, Sage tries to allow explicit conversions between arbitrary polynomial rings, if they share the same variable names.

Here's a case where that doesn't work:

```
R.<a,b,c,d,e,f,x,y,z,t,s,r>=PolynomialRing(QQ,12,order='lex')
I=R.ideal(a^2+d^2-x,a*b+d*e-y,a*c+d*f-z,b^2+e^2-t,b*c+e*f-s,c*c+f*f-r)
j=I.groebner_basis()
R1.<x,y,z,t,s,r>=QQ[]
R2=FractionField(R1)
R3.<a,b,c,d,e,f>=R1.fraction_field()[]
R3(j[0])
```


For now, the workaround is:

```
 sage_eval(str(j[0]), locals=locals())
```

but IMHO the original code should work.

Issue created by migration from https://trac.sagemath.org/ticket/5225





---

archive/issue_comments_040042.json:
```json
{
    "body": "A smaller example (minimal I hope ;-)):\n\n```python\nsage: R = QQ['a,b,x,y']\nsage: S = Frac(QQ['x,y'])['a,b']\nsage: p = R.gen(0) + R.gen(1) + R.gen(2)\nsage: S(p)\nTraceback (most recent call last):\n...\nTypeError: Could not find a mapping of the passed element to this ring.\n```\n",
    "created_at": "2016-04-13T14:08:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5225",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5225#issuecomment-40042",
    "user": "bruno"
}
```

A smaller example (minimal I hope ;-)):

```python
sage: R = QQ['a,b,x,y']
sage: S = Frac(QQ['x,y'])['a,b']
sage: p = R.gen(0) + R.gen(1) + R.gen(2)
sage: S(p)
Traceback (most recent call last):
...
TypeError: Could not find a mapping of the passed element to this ring.
```




---

archive/issue_comments_040043.json:
```json
{
    "body": "In 9.6.rc3:\n\n```\nsage: R.<a,b,c,d,e,f,x,y,z,t,s,r>=PolynomialRing(QQ,12,order='lex')\n....: I=R.ideal(a^2+d^2-x,a*b+d*e-y,a*c+d*f-z,b^2+e^2-t,b*c+e*f-s,c*c+f*f-r)\n....: j=I.groebner_basis()\n....: R1.<x,y,z,t,s,r>=QQ[]\n....: R2=FractionField(R1)\n....: R3.<a,b,c,d,e,f>=R1.fraction_field()[]\n....: R3(j[0])\na^2 + d^2 + (-x)\n```\n\nand\n\n```\nsage: R = QQ['a,b,x,y']\n....: S = Frac(QQ['x,y'])['a,b']\n....: p = R.gen(0) + R.gen(1) + R.gen(2)\n....: S(p)\na + b + x\n```\n",
    "created_at": "2022-05-04T23:06:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5225",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5225#issuecomment-40043",
    "user": "mkoeppe"
}
```

In 9.6.rc3:

```
sage: R.<a,b,c,d,e,f,x,y,z,t,s,r>=PolynomialRing(QQ,12,order='lex')
....: I=R.ideal(a^2+d^2-x,a*b+d*e-y,a*c+d*f-z,b^2+e^2-t,b*c+e*f-s,c*c+f*f-r)
....: j=I.groebner_basis()
....: R1.<x,y,z,t,s,r>=QQ[]
....: R2=FractionField(R1)
....: R3.<a,b,c,d,e,f>=R1.fraction_field()[]
....: R3(j[0])
a^2 + d^2 + (-x)
```

and

```
sage: R = QQ['a,b,x,y']
....: S = Frac(QQ['x,y'])['a,b']
....: p = R.gen(0) + R.gen(1) + R.gen(2)
....: S(p)
a + b + x
```




---

archive/issue_comments_040044.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2022-05-04T23:06:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5225",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5225#issuecomment-40044",
    "user": "mkoeppe"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_040045.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2022-05-10T16:21:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5225",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5225#issuecomment-40045",
    "user": "vdelecroix"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_040046.json:
```json
{
    "body": "Resolution: invalid",
    "created_at": "2022-05-11T02:14:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5225",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5225#issuecomment-40046",
    "user": "mkoeppe"
}
```

Resolution: invalid

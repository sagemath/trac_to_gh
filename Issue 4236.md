# Issue 4236: magma -- boolean ring conversions

archive/issues_004236.json:
```json
{
    "body": "Assignee: was\n\n\n```\n1) This should work (?)\n\nsage: B.<x,y> = BooleanPolynomialRing()\nsage: B*[x*y + 1, x + y]\nsage: I = B*[x*y + 1, x + y]\nsage: I._magma_()\n\nIdeal of Affine Algebra of rank 2 over GF(2)\nLexicographical Order\nVariables: x, y\nQuotient relations:\n[\nx^2 + x,\ny^2 + y\n]\nGenerating basis:\n[\nx*y + 1,\nx + y\n]\n\nsage: Im = I._magma_()\nsage: Im.GroebnerBasis()\nTypeError: Error evaluation Magma code.\nIN:_sage_[21] := GroebnerBasis(_sage_[20]);\nOUT:\n>> _sage_[21] := GroebnerBasis(_sage_[20]);\n                             ^\nRuntime error in 'GroebnerBasis': Bad argument types\nArgument types given: RngMPolRes\n```\n\n\nReported by Martin Albrecht\n\nIssue created by migration from https://trac.sagemath.org/ticket/4236\n\n",
    "created_at": "2008-10-02T16:28:41Z",
    "labels": [
        "interfaces",
        "major",
        "bug"
    ],
    "title": "magma -- boolean ring conversions",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/4236",
    "user": "was"
}
```
Assignee: was


```
1) This should work (?)

sage: B.<x,y> = BooleanPolynomialRing()
sage: B*[x*y + 1, x + y]
sage: I = B*[x*y + 1, x + y]
sage: I._magma_()

Ideal of Affine Algebra of rank 2 over GF(2)
Lexicographical Order
Variables: x, y
Quotient relations:
[
x^2 + x,
y^2 + y
]
Generating basis:
[
x*y + 1,
x + y
]

sage: Im = I._magma_()
sage: Im.GroebnerBasis()
TypeError: Error evaluation Magma code.
IN:_sage_[21] := GroebnerBasis(_sage_[20]);
OUT:
>> _sage_[21] := GroebnerBasis(_sage_[20]);
                             ^
Runtime error in 'GroebnerBasis': Bad argument types
Argument types given: RngMPolRes
```


Reported by Martin Albrecht

Issue created by migration from https://trac.sagemath.org/ticket/4236





---

archive/issue_comments_030775.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2008-10-02T16:29:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4236",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4236#issuecomment-30775",
    "user": "was"
}
```

Changing status from new to assigned.



---

archive/issue_comments_030776.json:
```json
{
    "body": "This does not seem like a bug in the Sage/Magma interface.  It seems like a misunderstanding of Magma itself, which doesn't have a GroebnerBasis function that takse as input an ideal in a boolean ring.  Magma simply doesn't do that.  It only has Groebner for ideals in *polynomial* rings.  There are some functions on ideals in boolean rings, but not many.  I.e., above\n\n```\nsage: Im.IsMaximal()\ntrue\nsage: Im.PrimaryDecomposition()\n\n[\nAffine Algebra of rank 2 over GF(2)\nLexicographical Order\nVariables: x, y\nQuotient relations:\n[\nx^2 + x,\ny^2 + y\n]\nGenerating basis:\n[\nx + 1,\ny + 1\n]\n]\n```\n",
    "created_at": "2008-12-11T05:55:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4236",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4236#issuecomment-30776",
    "user": "was"
}
```

This does not seem like a bug in the Sage/Magma interface.  It seems like a misunderstanding of Magma itself, which doesn't have a GroebnerBasis function that takse as input an ideal in a boolean ring.  Magma simply doesn't do that.  It only has Groebner for ideals in *polynomial* rings.  There are some functions on ideals in boolean rings, but not many.  I.e., above

```
sage: Im.IsMaximal()
true
sage: Im.PrimaryDecomposition()

[
Affine Algebra of rank 2 over GF(2)
Lexicographical Order
Variables: x, y
Quotient relations:
[
x^2 + x,
y^2 + y
]
Generating basis:
[
x + 1,
y + 1
]
]
```




---

archive/issue_comments_030777.json:
```json
{
    "body": "We could make Magma better than Magma by \n* adding the generators of the quotient to the ideal `J = I + Q`\n* computing `gb := GroebnerBasis(J)`\n* coerce the result to the quotient again. \n\nThis is equivalent to computing the GB in the quotient directly.",
    "created_at": "2008-12-11T10:18:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4236",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4236#issuecomment-30777",
    "user": "malb"
}
```

We could make Magma better than Magma by 
* adding the generators of the quotient to the ideal `J = I + Q`
* computing `gb := GroebnerBasis(J)`
* coerce the result to the quotient again. 

This is equivalent to computing the GB in the quotient directly.



---

archive/issue_comments_030778.json:
```json
{
    "body": "Changing type from defect to enhancement.",
    "created_at": "2009-01-23T02:42:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4236",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4236#issuecomment-30778",
    "user": "AlexGhitza"
}
```

Changing type from defect to enhancement.



---

archive/issue_comments_030779.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-09-29T08:10:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4236",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4236#issuecomment-30779",
    "user": "malb"
}
```

Resolution: fixed



---

archive/issue_comments_030780.json:
```json
{
    "body": "This is fixed with #6177",
    "created_at": "2009-09-29T08:10:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4236",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4236#issuecomment-30780",
    "user": "malb"
}
```

This is fixed with #6177

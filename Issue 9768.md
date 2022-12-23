# Issue 9768: Coercon problems to symbolic ring

archive/issues_009768.json:
```json
{
    "body": "Assignee: burcin\n\nThere seems to be some problems with the coercion of some datatypes to the symbolic ring:\n\nsage: cos(MatrixSpace(ZZ, 2)([1, 2, -4, 7]))\n---------------------------------------------------------------------------\nTypeError                                 Traceback (most recent call last)\n.......\nTypeError: cannot coerce arguments: no canonical coercion from Full MatrixSpace of 2 by 2 dense matrices over Integer Ring to Symbolic Ring\n\nsage: import numpy\nsage: vec = numpy.array([1,2])\nsage: sin(vec)\narray([ 0.84147098,  0.90929743])\nsage: sin(vec[0])\n---------------------------------------------------------------------------\nTypeError                                 Traceback (most recent call last)\n....\nTypeError: cannot coerce arguments: no canonical coercion from <type 'numpy.int64'> to Symbolic Ring\n----\n\nsage: x = PolynomialRing(QQ, 'x').gen()\nsage: sin(x)\nsin(x)\nsage: x = PolynomialRing(RR, 'x').gen()\nsage: sin(x)\n---------------------------------------------------------------------------\nTypeError                                 Traceback (most recent call last)\n.....\nTypeError: cannot coerce arguments: __call__() takes exactly 1 positional argument (0 given)\nsage: x = PolynomialRing(CC, 'x').gen()\nsage: sin(x)\nsin(x)\n\nIssue created by migration from https://trac.sagemath.org/ticket/9769\n\n",
    "created_at": "2010-08-19T23:47:28Z",
    "labels": [
        "symbolics",
        "major",
        "bug"
    ],
    "title": "Coercon problems to symbolic ring",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/9768",
    "user": "maldun"
}
```
Assignee: burcin

There seems to be some problems with the coercion of some datatypes to the symbolic ring:

sage: cos(MatrixSpace(ZZ, 2)([1, 2, -4, 7]))
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)
.......
TypeError: cannot coerce arguments: no canonical coercion from Full MatrixSpace of 2 by 2 dense matrices over Integer Ring to Symbolic Ring

sage: import numpy
sage: vec = numpy.array([1,2])
sage: sin(vec)
array([ 0.84147098,  0.90929743])
sage: sin(vec[0])
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)
....
TypeError: cannot coerce arguments: no canonical coercion from <type 'numpy.int64'> to Symbolic Ring
----

sage: x = PolynomialRing(QQ, 'x').gen()
sage: sin(x)
sin(x)
sage: x = PolynomialRing(RR, 'x').gen()
sage: sin(x)
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)
.....
TypeError: cannot coerce arguments: __call__() takes exactly 1 positional argument (0 given)
sage: x = PolynomialRing(CC, 'x').gen()
sage: sin(x)
sin(x)

Issue created by migration from https://trac.sagemath.org/ticket/9769





---

archive/issue_comments_095719.json:
```json
{
    "body": "Note that there is no coercion when you call\n\n```\nsage: import numpy\nsage: vec = numpy.array([1,2])\nsage: sin(vec)\narray([ 0.84147098,  0.90929743])\n```\n\n\nThe `__call__()` function for `sin` checks if the argument is a numpy array and calls the right numpy function on this input. See line 349 of `sage/symbolic/function.pyx`. We can handle other numpy types there.\n\nWe cannot work with matrices as numeric objects in symbolics. I suppose you expect the sin() function to be applied to each entry of the matrix. The `apply_map()` method should be used for this purpose:\n\n\n```\nsage: t = Matrix(ZZ, 2,2)\nsage: t.randomize()\nsage: t.apply_map(lambda x: sin(x))\n[      0 -sin(1)]\n[ sin(4)       0]\n```\n\n\n-----\n\n\n```\nsage: x = PolynomialRing(RR, 'x').gen()\nsage: sin(x)\n<boom>\n```\n\n\nThe problem here is really coercion, but it should be copied to another ticket (in the basic_arithmetic component):\n\nThe `__call__()` function of RR[x] doesn't conform to the generic definition. You should be able to give the parameters as a keyword argument as well. This should be made to work:\n\n\n```\nsage: R.<x> = RR[]\nsage: (x^2+1)(x=5)\n11\n```\n",
    "created_at": "2011-05-10T17:58:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9768",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9768#issuecomment-95719",
    "user": "burcin"
}
```

Note that there is no coercion when you call

```
sage: import numpy
sage: vec = numpy.array([1,2])
sage: sin(vec)
array([ 0.84147098,  0.90929743])
```


The `__call__()` function for `sin` checks if the argument is a numpy array and calls the right numpy function on this input. See line 349 of `sage/symbolic/function.pyx`. We can handle other numpy types there.

We cannot work with matrices as numeric objects in symbolics. I suppose you expect the sin() function to be applied to each entry of the matrix. The `apply_map()` method should be used for this purpose:


```
sage: t = Matrix(ZZ, 2,2)
sage: t.randomize()
sage: t.apply_map(lambda x: sin(x))
[      0 -sin(1)]
[ sin(4)       0]
```


-----


```
sage: x = PolynomialRing(RR, 'x').gen()
sage: sin(x)
<boom>
```


The problem here is really coercion, but it should be copied to another ticket (in the basic_arithmetic component):

The `__call__()` function of RR[x] doesn't conform to the generic definition. You should be able to give the parameters as a keyword argument as well. This should be made to work:


```
sage: R.<x> = RR[]
sage: (x^2+1)(x=5)
11
```




---

archive/issue_comments_095720.json:
```json
{
    "body": "Replying to [comment:2 burcin]:\n> {{{\n> sage: x = PolynomialRing(RR, 'x').gen()\n> sage: sin(x)\n> <boom>\n> }}}\n> \n> The problem here is really coercion, but it should be copied to another ticket (in the basic_arithmetic component):\nIncidentally the same with power series is part of #16197.\n\n> The `__call__()` function of RR[x] doesn't conform to the generic definition. You should be able to give the parameters as a keyword argument as well. This should be made to work:\n> \n> {{{\n> sage: R.<x> = RR[]\n> sage: (x^2+1)(x=5)\n> 11\n> }}}\n\nEdit: confused poly with series, sorry",
    "created_at": "2014-04-22T16:47:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9768",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9768#issuecomment-95720",
    "user": "rws"
}
```

Replying to [comment:2 burcin]:
> {{{
> sage: x = PolynomialRing(RR, 'x').gen()
> sage: sin(x)
> <boom>
> }}}
> 
> The problem here is really coercion, but it should be copied to another ticket (in the basic_arithmetic component):
Incidentally the same with power series is part of #16197.

> The `__call__()` function of RR[x] doesn't conform to the generic definition. You should be able to give the parameters as a keyword argument as well. This should be made to work:
> 
> {{{
> sage: R.<x> = RR[]
> sage: (x^2+1)(x=5)
> 11
> }}}

Edit: confused poly with series, sorry



---

archive/issue_comments_095721.json:
```json
{
    "body": "Replying to [comment:2 burcin]:\n> The `__call__()` function of RR[x] doesn't conform to the generic definition. You should be able to give the parameters as a keyword argument as well. This should be made to work:\n> \n> {{{\n> sage: R.<x> = RR[]\n> sage: (x^2+1)(x=5)\n> 11\n> }}}\nThis is now #17311",
    "created_at": "2014-11-10T10:01:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9768",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9768#issuecomment-95721",
    "user": "rws"
}
```

Replying to [comment:2 burcin]:
> The `__call__()` function of RR[x] doesn't conform to the generic definition. You should be able to give the parameters as a keyword argument as well. This should be made to work:
> 
> {{{
> sage: R.<x> = RR[]
> sage: (x^2+1)(x=5)
> 11
> }}}
This is now #17311



---

archive/issue_comments_095722.json:
```json
{
    "body": "Hello,\n\nI propose to close this ticket as duplicate because of #18076. With the branch applied\n\n```\nsage: import numpy\nsage: cos(numpy.int32('12'))\ncos(12)\nsage: cos(numpy.float32('1.1'))\n0.453596100177538\n```\n",
    "created_at": "2015-03-28T12:03:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9768",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9768#issuecomment-95722",
    "user": "vdelecroix"
}
```

Hello,

I propose to close this ticket as duplicate because of #18076. With the branch applied

```
sage: import numpy
sage: cos(numpy.int32('12'))
cos(12)
sage: cos(numpy.float32('1.1'))
0.453596100177538
```




---

archive/issue_comments_095723.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2015-03-28T12:03:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9768",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9768#issuecomment-95723",
    "user": "vdelecroix"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_095724.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2015-04-23T10:10:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9768",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9768#issuecomment-95724",
    "user": "jdemeyer"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_095725.json:
```json
{
    "body": "Resolution: duplicate",
    "created_at": "2015-04-23T14:51:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9768",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9768#issuecomment-95725",
    "user": "vbraun"
}
```

Resolution: duplicate

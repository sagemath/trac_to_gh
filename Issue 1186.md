# Issue 1186: Charpoly of a matrix of polynomials sometimes breaks

archive/issues_001186.json:
```json
{
    "body": "Assignee: @williamstein\n\nThe following:\n\n```\nP.<a,b,c> = PolynomialRing(Integers())\nu = MatrixSpace(P,3)([[0,0,a],[1,0,b],[0,1,c]])\nQ.<x> = PolynomialRing(P)\nu.charpoly('x')\n```\n\nreturns as intended:\n\n```\nx^3 + (-1*c)*x^2 + (-1*b)*x - a\n```\n\nbut the following code:\n\n```\nP.<a,b,c> = PolynomialRing(Rationals())\nu = MatrixSpace(P,3)([[0,0,a],[1,0,b],[0,1,c]])\nQ.<x> = PolynomialRing(P)\nu.charpoly('x')\n```\n\ndoes not, instead returning the traceback:\n\n```\n<type 'exceptions.TypeError'>             Traceback (most recent call last)\n\n/home/kedlaya/<ipython console> in <module>()\n\n/home/kedlaya/matrix2.pyx in sage.matrix.matrix2.Matrix.charpoly()\n\n/home/kedlaya/matrix2.pyx in sage.matrix.matrix2.Matrix._charpoly_hessenberg()\n\n/home/kedlaya/sage-complete/local/lib/python2.5/site-packages/sage/rings/polynomial/polynomial_ring.py in __call__(self, x, check, is_gen, construct, absprec)\n    240         C = self.__polynomial_class\n    241         if absprec is None:\n--> 242             return C(self, x, check, is_gen, construct=construct)\n    243         else:\n    244             return C(self, x, check, is_gen, construct=construct, absprec = absprec)\n\n/home/kedlaya/polynomial_element.pyx in sage.rings.polynomial.polynomial_element.Polynomial_generic_dense.__init__()\n\n/home/kedlaya/multi_polynomial_libsingular.pyx in sage.rings.polynomial.multi_polynomial_libsingular.MPolynomialRing_libsingular.__call__()\n\n/home/kedlaya/sage-complete/local/lib/python2.5/site-packages/sage/rings/rational_field.py in __call__(self, x, base)\n    180         if isinstance(x, sage.rings.rational.Rational):\n    181             return x\n--> 182         return sage.rings.rational.Rational(x, base)\n    183 \n    184     def construction(self):\n\n/home/kedlaya/rational.pyx in sage.rings.rational.Rational.__init__()\n\n/home/kedlaya/rational.pyx in sage.rings.rational.Rational.__set_value()\n\n/home/kedlaya/sage-complete/local/lib/python2.5/site-packages/sage/rings/fraction_field_element.py in _rational_(self)\n    270         Z = integer_ring.IntegerRing()\n    271         try:\n--> 272             return Z(self.__numerator) / Z(self.__denominator)\n    273         except AttributeError:\n    274             pass\n\n/home/kedlaya/integer_ring.pyx in sage.rings.integer_ring.IntegerRing_class.__call__()\n\n<type 'exceptions.TypeError'>: lift() takes exactly one argument (0 given)\n```\n\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/1186\n\n",
    "created_at": "2007-11-16T13:31:17Z",
    "labels": [
        "component: linear algebra",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-2.10.3",
    "title": "Charpoly of a matrix of polynomials sometimes breaks",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/1186",
    "user": "https://github.com/kedlaya"
}
```
Assignee: @williamstein

The following:

```
P.<a,b,c> = PolynomialRing(Integers())
u = MatrixSpace(P,3)([[0,0,a],[1,0,b],[0,1,c]])
Q.<x> = PolynomialRing(P)
u.charpoly('x')
```

returns as intended:

```
x^3 + (-1*c)*x^2 + (-1*b)*x - a
```

but the following code:

```
P.<a,b,c> = PolynomialRing(Rationals())
u = MatrixSpace(P,3)([[0,0,a],[1,0,b],[0,1,c]])
Q.<x> = PolynomialRing(P)
u.charpoly('x')
```

does not, instead returning the traceback:

```
<type 'exceptions.TypeError'>             Traceback (most recent call last)

/home/kedlaya/<ipython console> in <module>()

/home/kedlaya/matrix2.pyx in sage.matrix.matrix2.Matrix.charpoly()

/home/kedlaya/matrix2.pyx in sage.matrix.matrix2.Matrix._charpoly_hessenberg()

/home/kedlaya/sage-complete/local/lib/python2.5/site-packages/sage/rings/polynomial/polynomial_ring.py in __call__(self, x, check, is_gen, construct, absprec)
    240         C = self.__polynomial_class
    241         if absprec is None:
--> 242             return C(self, x, check, is_gen, construct=construct)
    243         else:
    244             return C(self, x, check, is_gen, construct=construct, absprec = absprec)

/home/kedlaya/polynomial_element.pyx in sage.rings.polynomial.polynomial_element.Polynomial_generic_dense.__init__()

/home/kedlaya/multi_polynomial_libsingular.pyx in sage.rings.polynomial.multi_polynomial_libsingular.MPolynomialRing_libsingular.__call__()

/home/kedlaya/sage-complete/local/lib/python2.5/site-packages/sage/rings/rational_field.py in __call__(self, x, base)
    180         if isinstance(x, sage.rings.rational.Rational):
    181             return x
--> 182         return sage.rings.rational.Rational(x, base)
    183 
    184     def construction(self):

/home/kedlaya/rational.pyx in sage.rings.rational.Rational.__init__()

/home/kedlaya/rational.pyx in sage.rings.rational.Rational.__set_value()

/home/kedlaya/sage-complete/local/lib/python2.5/site-packages/sage/rings/fraction_field_element.py in _rational_(self)
    270         Z = integer_ring.IntegerRing()
    271         try:
--> 272             return Z(self.__numerator) / Z(self.__denominator)
    273         except AttributeError:
    274             pass

/home/kedlaya/integer_ring.pyx in sage.rings.integer_ring.IntegerRing_class.__call__()

<type 'exceptions.TypeError'>: lift() takes exactly one argument (0 given)
```



Issue created by migration from https://trac.sagemath.org/ticket/1186





---

archive/issue_comments_007298.json:
```json
{
    "body": "I tracked the bug down to the function _charpoly_hessenberg() in matrix2.pyx.  The problem occurs at the very end of the function, when we want to turn the list v of coefficients into the characteristic polynomial.  More precisely, the elements of v live in the fraction field of the polynomial ring P (this is a side effect of hessenbergizing the matrix), and the function was trying to make them into coefficients of a polynomial over P itself; this is where the error was coming up.  I changed this to get a polynomial over the fraction field of P.",
    "created_at": "2007-11-17T18:11:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1186",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1186#issuecomment-7298",
    "user": "https://github.com/aghitza"
}
```

I tracked the bug down to the function _charpoly_hessenberg() in matrix2.pyx.  The problem occurs at the very end of the function, when we want to turn the list v of coefficients into the characteristic polynomial.  More precisely, the elements of v live in the fraction field of the polynomial ring P (this is a side effect of hessenbergizing the matrix), and the function was trying to make them into coefficients of a polynomial over P itself; this is where the error was coming up.  I changed this to get a polynomial over the fraction field of P.



---

archive/issue_comments_007299.json:
```json
{
    "body": "Do not apply this patch. \n\nThough the operations take place in the fraction field, the coefficients all live in the original ring (proof: use the determinant form of charpoly) and this is why this line was there. \n\nThis should be fixed, but this is not the right fix.",
    "created_at": "2007-11-18T08:30:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1186",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1186#issuecomment-7299",
    "user": "https://github.com/robertwb"
}
```

Do not apply this patch. 

Though the operations take place in the fraction field, the coefficients all live in the original ring (proof: use the determinant form of charpoly) and this is why this line was there. 

This should be fixed, but this is not the right fix.



---

archive/issue_comments_007300.json:
```json
{
    "body": "Attachment [7330.patch](tarball://root/attachments/some-uuid/ticket1186/7330.patch) by @aghitza created at 2007-11-20 03:19:02\n\nExcellent point.  I've done some more digging, and here's what I think is at the bottom of all this:\n\n\n```\nP.<a,b> = QQ[]\nQ.<x> = PolynomialRing(P)\nF = P.fraction_field()\nf=F(a)*x\nQ(f)\n```\n\n\nreturns\n\n\n```\n---------------------------------------------------------------------------\n<type 'exceptions.TypeError'>             Traceback (most recent call last)\n\n/opt/sage-2.8.12/devel/sage-alex/sage/matrix/<ipython console> in <module>()\n\n/opt/sage/local/lib/python2.5/site-packages/sage/rings/polynomial/polynomial_ring.py in __call__(self, x, check, is_gen, construct, absprec)\n    240         C = self.__polynomial_class\n    241         if absprec is None:\n--> 242             return C(self, x, check, is_gen, construct=construct)\n    243         else:\n    244             return C(self, x, check, is_gen, construct=construct, absprec = absprec)\n\n/opt/sage-2.8.12/devel/sage-alex/sage/matrix/polynomial_element.pyx in sage.rings.polynomial.polynomial_element.Polynomial_generic_dense.__init__()\n\n/opt/sage-2.8.12/devel/sage-alex/sage/matrix/multi_polynomial_libsingular.pyx in sage.rings.polynomial.multi_polynomial_libsingular.MPolynomialRing_libsingular.__call__()\n\n/opt/sage/local/lib/python2.5/site-packages/sage/rings/rational_field.py in __call__(self, x, base)\n    180         if isinstance(x, sage.rings.rational.Rational):\n    181             return x\n--> 182         return sage.rings.rational.Rational(x, base)\n    183         \n    184     def construction(self):\n\n/opt/sage-2.8.12/devel/sage-alex/sage/matrix/rational.pyx in sage.rings.rational.Rational.__init__()\n\n/opt/sage-2.8.12/devel/sage-alex/sage/matrix/rational.pyx in sage.rings.rational.Rational.__set_value()\n\n/opt/sage/local/lib/python2.5/site-packages/sage/rings/fraction_field_element.py in _rational_(self)\n    270         Z = integer_ring.IntegerRing()\n    271         try:\n--> 272             return Z(self.__numerator) / Z(self.__denominator)\n    273         except AttributeError:\n    274             pass\n\n/opt/sage-2.8.12/devel/sage-alex/sage/matrix/integer_ring.pyx in sage.rings.integer_ring.IntegerRing_class.__call__()\n\n<type 'exceptions.TypeError'>: lift() takes exactly one argument (0 given)\n```\n\n\nThe culprit is __call__ in multi_polynomial_libsingular.pyx, where the function tries a bunch of things and then, before giving up, tries to coerce a into QQ (which of course will not work).  Somehow our polynomial f is slipping through the cracks.  Note that this is a multivariable issue; the same thing works perfectly well over QQ[a].\n\nI don't understand enough about how __call__ works to fix this properly.  I did however notice that, in this situation, working with the string 'a' fixes the issue.  I'm replacing the old patch with a very simple one that does this, but someone with more experience with these things should take a look at it.",
    "created_at": "2007-11-20T03:19:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1186",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1186#issuecomment-7300",
    "user": "https://github.com/aghitza"
}
```

Attachment [7330.patch](tarball://root/attachments/some-uuid/ticket1186/7330.patch) by @aghitza created at 2007-11-20 03:19:02

Excellent point.  I've done some more digging, and here's what I think is at the bottom of all this:


```
P.<a,b> = QQ[]
Q.<x> = PolynomialRing(P)
F = P.fraction_field()
f=F(a)*x
Q(f)
```


returns


```
---------------------------------------------------------------------------
<type 'exceptions.TypeError'>             Traceback (most recent call last)

/opt/sage-2.8.12/devel/sage-alex/sage/matrix/<ipython console> in <module>()

/opt/sage/local/lib/python2.5/site-packages/sage/rings/polynomial/polynomial_ring.py in __call__(self, x, check, is_gen, construct, absprec)
    240         C = self.__polynomial_class
    241         if absprec is None:
--> 242             return C(self, x, check, is_gen, construct=construct)
    243         else:
    244             return C(self, x, check, is_gen, construct=construct, absprec = absprec)

/opt/sage-2.8.12/devel/sage-alex/sage/matrix/polynomial_element.pyx in sage.rings.polynomial.polynomial_element.Polynomial_generic_dense.__init__()

/opt/sage-2.8.12/devel/sage-alex/sage/matrix/multi_polynomial_libsingular.pyx in sage.rings.polynomial.multi_polynomial_libsingular.MPolynomialRing_libsingular.__call__()

/opt/sage/local/lib/python2.5/site-packages/sage/rings/rational_field.py in __call__(self, x, base)
    180         if isinstance(x, sage.rings.rational.Rational):
    181             return x
--> 182         return sage.rings.rational.Rational(x, base)
    183         
    184     def construction(self):

/opt/sage-2.8.12/devel/sage-alex/sage/matrix/rational.pyx in sage.rings.rational.Rational.__init__()

/opt/sage-2.8.12/devel/sage-alex/sage/matrix/rational.pyx in sage.rings.rational.Rational.__set_value()

/opt/sage/local/lib/python2.5/site-packages/sage/rings/fraction_field_element.py in _rational_(self)
    270         Z = integer_ring.IntegerRing()
    271         try:
--> 272             return Z(self.__numerator) / Z(self.__denominator)
    273         except AttributeError:
    274             pass

/opt/sage-2.8.12/devel/sage-alex/sage/matrix/integer_ring.pyx in sage.rings.integer_ring.IntegerRing_class.__call__()

<type 'exceptions.TypeError'>: lift() takes exactly one argument (0 given)
```


The culprit is __call__ in multi_polynomial_libsingular.pyx, where the function tries a bunch of things and then, before giving up, tries to coerce a into QQ (which of course will not work).  Somehow our polynomial f is slipping through the cracks.  Note that this is a multivariable issue; the same thing works perfectly well over QQ[a].

I don't understand enough about how __call__ works to fix this properly.  I did however notice that, in this situation, working with the string 'a' fixes the issue.  I'm replacing the old patch with a very simple one that does this, but someone with more experience with these things should take a look at it.



---

archive/issue_comments_007301.json:
```json
{
    "body": "The patch was changed after robertwb's review above, so somebody should look at the new patch.",
    "created_at": "2008-02-16T02:10:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1186",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1186#issuecomment-7301",
    "user": "https://trac.sagemath.org/admin/accounts/users/cwitty"
}
```

The patch was changed after robertwb's review above, so somebody should look at the new patch.



---

archive/issue_comments_007302.json:
```json
{
    "body": "Attachment [1186-doctests.patch](tarball://root/attachments/some-uuid/ticket1186/1186-doctests.patch) by @mwhansen created at 2008-02-27 19:47:35",
    "created_at": "2008-02-27T19:47:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1186",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1186#issuecomment-7302",
    "user": "https://github.com/mwhansen"
}
```

Attachment [1186-doctests.patch](tarball://root/attachments/some-uuid/ticket1186/1186-doctests.patch) by @mwhansen created at 2008-02-27 19:47:35



---

archive/issue_comments_007303.json:
```json
{
    "body": "Apply both patches.  Works for me against 2.10.3.alpha0.",
    "created_at": "2008-02-27T19:48:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1186",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1186#issuecomment-7303",
    "user": "https://github.com/mwhansen"
}
```

Apply both patches.  Works for me against 2.10.3.alpha0.



---

archive/issue_events_001318.json:
```json
{
    "actor": "mabshoff",
    "created_at": "2008-02-28T00:24:02Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/1186",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/1186#event-1318"
}
```



---

archive/issue_comments_007304.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-02-28T00:24:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1186",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1186#issuecomment-7304",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_007305.json:
```json
{
    "body": "Merged in Sage 2.10.3.rc0",
    "created_at": "2008-02-28T00:24:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1186",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1186#issuecomment-7305",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged in Sage 2.10.3.rc0

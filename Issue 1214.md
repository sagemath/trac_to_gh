# Issue 1214: error in polynomial ideal membership testing

archive/issues_001214.json:
```json
{
    "body": "Assignee: @malb\n\n\n```\nsage: x^2 in I\n---------------------------------------------------------------------------\n<type 'exceptions.AttributeError'>        Traceback (most recent call last)\n\n/opt/maple11/lib/<ipython console> in <module>()\n\n/opt/sage/local/lib/python2.5/site-packages/sage/rings/ideal.py in __contains__(self, x)\n    315         if self.gen().is_zero():\n    316             return x.is_zero()\n--> 317         return self.gen().divides(x)\n    318     \n    319     def __cmp__(self, other):\n\n<type 'exceptions.AttributeError'>: 'Polynomial_rational_dense' object has no attribute 'divides'\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/1214\n\n",
    "created_at": "2007-11-20T05:33:53Z",
    "labels": [
        "component: commutative algebra",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-2.8.15",
    "title": "error in polynomial ideal membership testing",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/1214",
    "user": "https://github.com/mwhansen"
}
```
Assignee: @malb


```
sage: x^2 in I
---------------------------------------------------------------------------
<type 'exceptions.AttributeError'>        Traceback (most recent call last)

/opt/maple11/lib/<ipython console> in <module>()

/opt/sage/local/lib/python2.5/site-packages/sage/rings/ideal.py in __contains__(self, x)
    315         if self.gen().is_zero():
    316             return x.is_zero()
--> 317         return self.gen().divides(x)
    318     
    319     def __cmp__(self, other):

<type 'exceptions.AttributeError'>: 'Polynomial_rational_dense' object has no attribute 'divides'
```


Issue created by migration from https://trac.sagemath.org/ticket/1214





---

archive/issue_comments_007515.json:
```json
{
    "body": "\n```\nsage: P.<x> = PolynomialRing(QQ)\nsage: I = P.ideal(x^2-2)\nsage: x^2 in I\n---------------------------------------------------------------------------\n<type 'exceptions.AttributeError'>        Traceback (most recent call last)\n\n/opt/maple11/lib/<ipython console> in <module>()\n\n/opt/sage/local/lib/python2.5/site-packages/sage/rings/ideal.py in __contains__(self, x)\n    315         if self.gen().is_zero():\n    316             return x.is_zero()\n--> 317         return self.gen().divides(x)\n    318     \n    319     def __cmp__(self, other):\n\n<type 'exceptions.AttributeError'>: 'Polynomial_rational_dense' object has no attribute 'divides'\nsage: P.<x> = PolynomialRing(ZZ)\nsage: I = P.ideal(x^2-2)\nsage: x^2 in I\n---------------------------------------------------------------------------\n<type 'exceptions.AttributeError'>        Traceback (most recent call last)\n\n/opt/maple11/lib/<ipython console> in <module>()\n\n/opt/sage/local/lib/python2.5/site-packages/sage/rings/ideal.py in __contains__(self, x)\n    315         if self.gen().is_zero():\n    316             return x.is_zero()\n--> 317         return self.gen().divides(x)\n    318     \n    319     def __cmp__(self, other):\n\n<type 'exceptions.AttributeError'>: 'sage.rings.polynomial.polynomial_integer_dense_ntl' object has no attribute 'divides'\n```\n",
    "created_at": "2007-11-20T05:43:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1214",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1214#issuecomment-7515",
    "user": "https://github.com/mwhansen"
}
```


```
sage: P.<x> = PolynomialRing(QQ)
sage: I = P.ideal(x^2-2)
sage: x^2 in I
---------------------------------------------------------------------------
<type 'exceptions.AttributeError'>        Traceback (most recent call last)

/opt/maple11/lib/<ipython console> in <module>()

/opt/sage/local/lib/python2.5/site-packages/sage/rings/ideal.py in __contains__(self, x)
    315         if self.gen().is_zero():
    316             return x.is_zero()
--> 317         return self.gen().divides(x)
    318     
    319     def __cmp__(self, other):

<type 'exceptions.AttributeError'>: 'Polynomial_rational_dense' object has no attribute 'divides'
sage: P.<x> = PolynomialRing(ZZ)
sage: I = P.ideal(x^2-2)
sage: x^2 in I
---------------------------------------------------------------------------
<type 'exceptions.AttributeError'>        Traceback (most recent call last)

/opt/maple11/lib/<ipython console> in <module>()

/opt/sage/local/lib/python2.5/site-packages/sage/rings/ideal.py in __contains__(self, x)
    315         if self.gen().is_zero():
    316             return x.is_zero()
--> 317         return self.gen().divides(x)
    318     
    319     def __cmp__(self, other):

<type 'exceptions.AttributeError'>: 'sage.rings.polynomial.polynomial_integer_dense_ntl' object has no attribute 'divides'
```




---

archive/issue_comments_007516.json:
```json
{
    "body": "Attachment [1214.patch](tarball://root/attachments/some-uuid/ticket1214/1214.patch) by @mwhansen created at 2007-11-20 05:51:05",
    "created_at": "2007-11-20T05:51:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1214",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1214#issuecomment-7516",
    "user": "https://github.com/mwhansen"
}
```

Attachment [1214.patch](tarball://root/attachments/some-uuid/ticket1214/1214.patch) by @mwhansen created at 2007-11-20 05:51:05



---

archive/issue_comments_007517.json:
```json
{
    "body": "Changing assignee from @malb to @mwhansen.",
    "created_at": "2007-11-20T05:51:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1214",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1214#issuecomment-7517",
    "user": "https://github.com/mwhansen"
}
```

Changing assignee from @malb to @mwhansen.



---

archive/issue_comments_007518.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2007-11-20T05:51:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1214",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1214#issuecomment-7518",
    "user": "https://github.com/mwhansen"
}
```

Changing status from new to assigned.



---

archive/issue_comments_007519.json:
```json
{
    "body": "This patch should be applied -- doctests are excellent and I think the divides() function is good.\n\nThere is a typo:\n\n```\n \t1624\t    def divides(self, x): \n \t1625\t        \"\"\" \n \t1626\t        Return True if self divides n. \n```\n\n\n$n$ should be $x$.",
    "created_at": "2007-11-23T20:06:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1214",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1214#issuecomment-7519",
    "user": "https://github.com/ncalexan"
}
```

This patch should be applied -- doctests are excellent and I think the divides() function is good.

There is a typo:

```
 	1624	    def divides(self, x): 
 	1625	        """ 
 	1626	        Return True if self divides n. 
```


$n$ should be $x$.



---

archive/issue_comments_007520.json:
```json
{
    "body": "Merged in 2.8.15.alpha1 - I corrected the documentation as Nick suggested.",
    "created_at": "2007-12-01T18:47:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1214",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1214#issuecomment-7520",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged in 2.8.15.alpha1 - I corrected the documentation as Nick suggested.



---

archive/issue_comments_007521.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2007-12-01T18:47:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1214",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1214#issuecomment-7521",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed



---

archive/issue_events_001352.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2007-12-01T18:47:33Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/1214",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/1214#event-1352"
}
```

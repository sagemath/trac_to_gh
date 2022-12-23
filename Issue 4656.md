# Issue 4656: power series with zero p-adic coefficients

archive/issues_004656.json:
```json
{
    "body": "Assignee: was\n\nKeywords: padic powerseries\n\nThe following _repr_ does not look good to me\n\n\n```\nsage: R.<T> = Qp(5,5)[[]]\nsage: O(5^3)*T\n0\nsage: 1+O(5^3)*T\n1 + O(5^5) + O(5^3)*T\n```\n\n\nBut that is due to \n\n```\nsage: s= O(5^3)*T\nsage: s.is_zero()\nTrue\nsage: s == R(0)\nFalse\n```\n\n\nThis I consider to be a bug according to the docstring of s.is_zero? saying\n\n```\nReturn True if self equals self.parent()(0).\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/4656\n\n",
    "created_at": "2008-11-29T21:53:42Z",
    "labels": [
        "number theory",
        "minor",
        "bug"
    ],
    "title": "power series with zero p-adic coefficients",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/4656",
    "user": "wuthrich"
}
```
Assignee: was

Keywords: padic powerseries

The following _repr_ does not look good to me


```
sage: R.<T> = Qp(5,5)[[]]
sage: O(5^3)*T
0
sage: 1+O(5^3)*T
1 + O(5^5) + O(5^3)*T
```


But that is due to 

```
sage: s= O(5^3)*T
sage: s.is_zero()
True
sage: s == R(0)
False
```


This I consider to be a bug according to the docstring of s.is_zero? saying

```
Return True if self equals self.parent()(0).
```


Issue created by migration from https://trac.sagemath.org/ticket/4656





---

archive/issue_comments_035069.json:
```json
{
    "body": "Attachment",
    "created_at": "2009-01-24T11:07:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4656",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4656#issuecomment-35069",
    "user": "roed"
}
```

Attachment



---

archive/issue_comments_035070.json:
```json
{
    "body": "Looks good to me and passes all tests. I changed the patch as the orinigally posted patch does not apply against sage 3.4. Thanks!",
    "created_at": "2009-03-12T19:28:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4656",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4656#issuecomment-35070",
    "user": "wuthrich"
}
```

Looks good to me and passes all tests. I changed the patch as the orinigally posted patch does not apply against sage 3.4. Thanks!



---

archive/issue_comments_035071.json:
```json
{
    "body": "this patch replaces the previous patch. It is the same, but some changes in page lines in order to make it applicable to sage 3.4",
    "created_at": "2009-03-12T19:29:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4656",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4656#issuecomment-35071",
    "user": "wuthrich"
}
```

this patch replaces the previous patch. It is the same, but some changes in page lines in order to make it applicable to sage 3.4



---

archive/issue_comments_035072.json:
```json
{
    "body": "Attachment\n\n4656.second.patch causes the following doctest failure:\n\n```\nsage -t -long \"devel/sage/sage/schemes/elliptic_curves/sha_tate.py\"\n**********************************************************************\nFile \"/scratch/mabshoff/sage-3.4.1.alpha0/devel/sage/sage/schemes/elliptic_curves/sha_tate.py\", line 299:\n    sage: EllipticCurve('1483a1').sha().an_padic(5) # rank 2   (long time)\nException raised:\n    Traceback (most recent call last):\n      File \"/scratch/mabshoff/sage-3.4/local/bin/ncadoctest.py\", line 1231, in run_one_test\n        self.run_one_example(test, example, filename, compileflags)\n      File \"/scratch/mabshoff/sage-3.4/local/bin/sagedoctest.py\", line 38, in run_one_example\n        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)\n      File \"/scratch/mabshoff/sage-3.4/local/bin/ncadoctest.py\", line 1172, in run_one_example\n        compileflags, 1) in test.globs\n      File \"<doctest __main__.example_3[11]>\", line 1, in <module>\n        EllipticCurve('1483a1').sha().an_padic(Integer(5)) # rank 2   (long time)###line 299:\n    sage: EllipticCurve('1483a1').sha().an_padic(5) # rank 2   (long time)\n      File \"/scratch/mabshoff/sage-3.4.1.alpha0/local/lib/python/site-packages/sage/schemes/elliptic_curves/sha_tate.py\", line 418, in an_padic\n        raise RuntimeError, \"There must be a bug in the supersingular routines for the p-adic BSD.\"\n    RuntimeError: There must be a bug in the supersingular routines for the p-adic BSD.\n**********************************************************************\n```\n\n\nCheers,\n\nMichael",
    "created_at": "2009-03-20T21:48:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4656",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4656#issuecomment-35072",
    "user": "mabshoff"
}
```

Attachment

4656.second.patch causes the following doctest failure:

```
sage -t -long "devel/sage/sage/schemes/elliptic_curves/sha_tate.py"
**********************************************************************
File "/scratch/mabshoff/sage-3.4.1.alpha0/devel/sage/sage/schemes/elliptic_curves/sha_tate.py", line 299:
    sage: EllipticCurve('1483a1').sha().an_padic(5) # rank 2   (long time)
Exception raised:
    Traceback (most recent call last):
      File "/scratch/mabshoff/sage-3.4/local/bin/ncadoctest.py", line 1231, in run_one_test
        self.run_one_example(test, example, filename, compileflags)
      File "/scratch/mabshoff/sage-3.4/local/bin/sagedoctest.py", line 38, in run_one_example
        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)
      File "/scratch/mabshoff/sage-3.4/local/bin/ncadoctest.py", line 1172, in run_one_example
        compileflags, 1) in test.globs
      File "<doctest __main__.example_3[11]>", line 1, in <module>
        EllipticCurve('1483a1').sha().an_padic(Integer(5)) # rank 2   (long time)###line 299:
    sage: EllipticCurve('1483a1').sha().an_padic(5) # rank 2   (long time)
      File "/scratch/mabshoff/sage-3.4.1.alpha0/local/lib/python/site-packages/sage/schemes/elliptic_curves/sha_tate.py", line 418, in an_padic
        raise RuntimeError, "There must be a bug in the supersingular routines for the p-adic BSD."
    RuntimeError: There must be a bug in the supersingular routines for the p-adic BSD.
**********************************************************************
```


Cheers,

Michael



---

archive/issue_comments_035073.json:
```json
{
    "body": "That doctest failure is serious and I have to look into that once #4667 is in.",
    "created_at": "2009-03-30T10:18:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4656",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4656#issuecomment-35073",
    "user": "wuthrich"
}
```

That doctest failure is serious and I have to look into that once #4667 is in.



---

archive/issue_comments_035074.json:
```json
{
    "body": "I looked into the problem. It is not due to a bug in supersingular, but due to the following strange behaviour. This happens to me with the above second patch.\n\nI don't think that is ok :\n\n```\nsage: R = Qp(5,10)\nsage: RT.<T> = R[[]]\nsage: f = O(5^3) + O(5)*T +O(T^2)\nsage: f\nO(5^3) + O(5)*T + O(T^2)\nsage: f[1]\n0\n```\n\n\nf is now printed correctly, but the coefficient is not. In fact the precision of the coefficient is lost (and that happens without the patch, too):\n\n```\nsage: a= f[1]\nsage: a\n0\nsage: a.precision_absolute()\n+Infinity\n```\n\n\n\nNow, this looks really bad: \n\n```\nsage: v = matrix([[1,0],[0,1]])*vector([1,f])\nsage: v\n(1 + O(5^10), )\nsage: v[1]\n\nsage: type(v[1])\n<type 'sage.rings.power_series_poly.PowerSeries_poly'>\n```\n\n\nI must admit that I do not understand what is going on and if this ticket is in fact related to other known issues with p-adic series.",
    "created_at": "2009-04-21T17:43:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4656",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4656#issuecomment-35074",
    "user": "wuthrich"
}
```

I looked into the problem. It is not due to a bug in supersingular, but due to the following strange behaviour. This happens to me with the above second patch.

I don't think that is ok :

```
sage: R = Qp(5,10)
sage: RT.<T> = R[[]]
sage: f = O(5^3) + O(5)*T +O(T^2)
sage: f
O(5^3) + O(5)*T + O(T^2)
sage: f[1]
0
```


f is now printed correctly, but the coefficient is not. In fact the precision of the coefficient is lost (and that happens without the patch, too):

```
sage: a= f[1]
sage: a
0
sage: a.precision_absolute()
+Infinity
```



Now, this looks really bad: 

```
sage: v = matrix([[1,0],[0,1]])*vector([1,f])
sage: v
(1 + O(5^10), )
sage: v[1]

sage: type(v[1])
<type 'sage.rings.power_series_poly.PowerSeries_poly'>
```


I must admit that I do not understand what is going on and if this ticket is in fact related to other known issues with p-adic series.



---

archive/issue_comments_035075.json:
```json
{
    "body": "I'm working on p-adic polynomials, and thus on p-adic power series.  If you want a status report on this ticket, let me know.",
    "created_at": "2009-04-26T19:44:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4656",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4656#issuecomment-35075",
    "user": "roed"
}
```

I'm working on p-adic polynomials, and thus on p-adic power series.  If you want a status report on this ticket, let me know.



---

archive/issue_comments_035076.json:
```json
{
    "body": "Replying to [comment:7 roed]:\n> I'm working on p-adic polynomials, and thus on p-adic power series.  If you want a status report on this ticket, let me know.\n\nMore specifically, this appears to be related to #5075. That ticket will (we hope) be resolved by the omnibus patch on #6084.",
    "created_at": "2009-05-20T21:47:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4656",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4656#issuecomment-35076",
    "user": "kedlaya"
}
```

Replying to [comment:7 roed]:
> I'm working on p-adic polynomials, and thus on p-adic power series.  If you want a status report on this ticket, let me know.

More specifically, this appears to be related to #5075. That ticket will (we hope) be resolved by the omnibus patch on #6084.



---

archive/issue_comments_035077.json:
```json
{
    "body": "Finally, I came back to this. I will attach a rebased patch. This patch solves the problem of this ticket, but the doctest failure in sha_tate.py is still present. But this is caused by another problem. I opened a new ticket #8198 for this. Once this new ticket is solved this ticket here should hopefully be resolved with this patch.",
    "created_at": "2010-02-05T23:13:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4656",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4656#issuecomment-35077",
    "user": "wuthrich"
}
```

Finally, I came back to this. I will attach a rebased patch. This patch solves the problem of this ticket, but the doctest failure in sha_tate.py is still present. But this is caused by another problem. I opened a new ticket #8198 for this. Once this new ticket is solved this ticket here should hopefully be resolved with this patch.



---

archive/issue_comments_035078.json:
```json
{
    "body": "Attachment\n\nexported against 4.3.2.alpha1",
    "created_at": "2010-02-05T23:15:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4656",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4656#issuecomment-35078",
    "user": "wuthrich"
}
```

Attachment

exported against 4.3.2.alpha1



---

archive/issue_comments_035079.json:
```json
{
    "body": "The proposed solutions at #9457 are solving this here partially and the problems there are the same as here.",
    "created_at": "2014-01-29T21:42:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4656",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4656#issuecomment-35079",
    "user": "wuthrich"
}
```

The proposed solutions at #9457 are solving this here partially and the problems there are the same as here.



---

archive/issue_comments_035080.json:
```json
{
    "body": "Ping. Does anyone know what is going on here?",
    "created_at": "2017-09-06T03:33:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4656",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4656#issuecomment-35080",
    "user": "kedlaya"
}
```

Ping. Does anyone know what is going on here?



---

archive/issue_comments_035081.json:
```json
{
    "body": "Changing keywords from \"padic powerseries\" to \"padic powerseries padicIMA\".",
    "created_at": "2018-07-26T22:28:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4656",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4656#issuecomment-35081",
    "user": "saraedum"
}
```

Changing keywords from "padic powerseries" to "padic powerseries padicIMA".



---

archive/issue_comments_035082.json:
```json
{
    "body": "Changing component from number theory to padics.",
    "created_at": "2018-07-26T22:28:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4656",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4656#issuecomment-35082",
    "user": "saraedum"
}
```

Changing component from number theory to padics.

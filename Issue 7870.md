# Issue 7870: dozens of failures in magma optional test suite on skynet (eno) with sage-4.3

archive/issues_007870.json:
```json
{
    "body": "Assignee: was\n\nI ran the magma optional test suite on skynet (eno):\n\n```\n./sage -t --only_optional=magma devel/sage/sage > magma.out&\n```\n\n\nAnd the failures are:\n\n```\n        sage -t --only_optional=magma \"devel/sage/sage/rings/polynomial/pbori.pyx\"\n        sage -t --only_optional=magma \"devel/sage/sage/rings/polynomial/multi_polynomial_ring_generic.pyx\"\n        sage -t --only_optional=magma \"devel/sage/sage/rings/polynomial/term_order.py\"\n        sage -t --only_optional=magma \"devel/sage/sage/rings/polynomial/multi_polynomial_ideal.py\"\n        sage -t --only_optional=magma \"devel/sage/sage/crypto/mq/mpolynomialsystem.py\"\n        sage -t --only_optional=magma \"devel/sage/sage/schemes/hyperelliptic_curves/hyperelliptic_g2_generic.py\"\n        sage -t --only_optional=magma \"devel/sage/sage/symbolic/expression.pyx\"\nTotal time for all tests: 364.0 seconds\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/7870\n\n",
    "created_at": "2010-01-07T20:51:18Z",
    "labels": [
        "interfaces",
        "major",
        "bug"
    ],
    "title": "dozens of failures in magma optional test suite on skynet (eno) with sage-4.3",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/7870",
    "user": "was"
}
```
Assignee: was

I ran the magma optional test suite on skynet (eno):

```
./sage -t --only_optional=magma devel/sage/sage > magma.out&
```


And the failures are:

```
        sage -t --only_optional=magma "devel/sage/sage/rings/polynomial/pbori.pyx"
        sage -t --only_optional=magma "devel/sage/sage/rings/polynomial/multi_polynomial_ring_generic.pyx"
        sage -t --only_optional=magma "devel/sage/sage/rings/polynomial/term_order.py"
        sage -t --only_optional=magma "devel/sage/sage/rings/polynomial/multi_polynomial_ideal.py"
        sage -t --only_optional=magma "devel/sage/sage/crypto/mq/mpolynomialsystem.py"
        sage -t --only_optional=magma "devel/sage/sage/schemes/hyperelliptic_curves/hyperelliptic_g2_generic.py"
        sage -t --only_optional=magma "devel/sage/sage/symbolic/expression.pyx"
Total time for all tests: 364.0 seconds
```


Issue created by migration from https://trac.sagemath.org/ticket/7870





---

archive/issue_comments_068271.json:
```json
{
    "body": "this is the output of running the test suite, showing the actual failures.",
    "created_at": "2010-01-07T20:51:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7870",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7870#issuecomment-68271",
    "user": "was"
}
```

this is the output of running the test suite, showing the actual failures.



---

archive/issue_comments_068272.json:
```json
{
    "body": "Attachment [magma.out](tarball://root/attachments/some-uuid/ticket7870/magma.out) by was created at 2010-04-06 15:15:56\n\nI tested again using the new magma V2.16-7 with sage-4.3.5. \n\n```\n[wstein@eno sage-4.3.5]$ magma\nMagma V2.16-7     Tue Apr  6 2010 11:14:18 on eno      [Seed = 3125460604]\nType ? for help.  Type <Ctrl>-D to quit.\n```\n\nThere are now even more failures.  I've attached a new test log created using the following on eno:\n\n```\n./sage -tp 10 -only_optional=magma devel/sage/sage\n```\n",
    "created_at": "2010-04-06T15:15:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7870",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7870#issuecomment-68272",
    "user": "was"
}
```

Attachment [magma.out](tarball://root/attachments/some-uuid/ticket7870/magma.out) by was created at 2010-04-06 15:15:56

I tested again using the new magma V2.16-7 with sage-4.3.5. 

```
[wstein@eno sage-4.3.5]$ magma
Magma V2.16-7     Tue Apr  6 2010 11:14:18 on eno      [Seed = 3125460604]
Type ? for help.  Type <Ctrl>-D to quit.
```

There are now even more failures.  I've attached a new test log created using the following on eno:

```
./sage -tp 10 -only_optional=magma devel/sage/sage
```




---

archive/issue_comments_068273.json:
```json
{
    "body": "it got much worse!",
    "created_at": "2010-04-06T15:16:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7870",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7870#issuecomment-68273",
    "user": "was"
}
```

it got much worse!



---

archive/issue_comments_068274.json:
```json
{
    "body": "Attachment [trac_7870.patch](tarball://root/attachments/some-uuid/ticket7870/trac_7870.patch) by was created at 2010-04-06 16:20:57\n\nThis fixes all the doctest issues on eno with magma V2.16-7",
    "created_at": "2010-04-06T16:20:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7870",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7870#issuecomment-68274",
    "user": "was"
}
```

Attachment [trac_7870.patch](tarball://root/attachments/some-uuid/ticket7870/trac_7870.patch) by was created at 2010-04-06 16:20:57

This fixes all the doctest issues on eno with magma V2.16-7



---

archive/issue_comments_068275.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-04-06T16:21:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7870",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7870#issuecomment-68275",
    "user": "was"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_068276.json:
```json
{
    "body": "Changing assignee from was to cremona.",
    "created_at": "2010-04-06T16:33:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7870",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7870#issuecomment-68276",
    "user": "cremona"
}
```

Changing assignee from was to cremona.



---

archive/issue_comments_068277.json:
```json
{
    "body": "I am testing this now with magma V2.16-1 and will report back.  It will not be a clean result, since I already saw\n\n```\n\n**********************************************************************\nFile \"/storage/jec/sage-4.3.5/devel/sage-tests/sage/symbolic/expression.pyx\", line 499:\n    sage: magma(f)                         # optional - magma\nExpected:\n    sin(cos(x^2) + log(x))\nGot:\n    sin(log(x) + cos(x^2))\n```\n",
    "created_at": "2010-04-06T16:33:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7870",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7870#issuecomment-68277",
    "user": "cremona"
}
```

I am testing this now with magma V2.16-1 and will report back.  It will not be a clean result, since I already saw

```

**********************************************************************
File "/storage/jec/sage-4.3.5/devel/sage-tests/sage/symbolic/expression.pyx", line 499:
    sage: magma(f)                         # optional - magma
Expected:
    sin(cos(x^2) + log(x))
Got:
    sin(log(x) + cos(x^2))
```




---

archive/issue_comments_068278.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2010-04-06T16:36:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7870",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7870#issuecomment-68278",
    "user": "cremona"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_068279.json:
```json
{
    "body": "Full log is at http://www.warwick.ac.uk/staff/J.E.Cremona/magma_test.log .",
    "created_at": "2010-04-06T16:36:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7870",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7870#issuecomment-68279",
    "user": "cremona"
}
```

Full log is at http://www.warwick.ac.uk/staff/J.E.Cremona/magma_test.log .



---

archive/issue_comments_068280.json:
```json
{
    "body": "Replying to [comment:4 cremona]:\n> Full log is at http://www.warwick.ac.uk/staff/J.E.Cremona/magma_test.log .\n\nApologies -- it looks as if I did not apply the patch since the differences look exactly like the ones you fixed!  I will try again.",
    "created_at": "2010-04-06T17:08:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7870",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7870#issuecomment-68280",
    "user": "cremona"
}
```

Replying to [comment:4 cremona]:
> Full log is at http://www.warwick.ac.uk/staff/J.E.Cremona/magma_test.log .

Apologies -- it looks as if I did not apply the patch since the differences look exactly like the ones you fixed!  I will try again.



---

archive/issue_comments_068281.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2010-04-06T17:08:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7870",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7870#issuecomment-68281",
    "user": "cremona"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_068282.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2010-04-06T17:20:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7870",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7870#issuecomment-68282",
    "user": "cremona"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_068283.json:
```json
{
    "body": "OK, so after actually applying the patch (I had forgotten to do hg qpush) I get exactly one failure.  This is on 64-bit ubuntu, Sage 4.3.5 and Magma V2.16-1:\n\n```\nsage -t --only_optional=magma \"./sage/interfaces/magma.py\"  \n**********************************************************************\nFile \"/storage/jec/sage-4.3.5/devel/sage-tests/sage/interfaces/magma.py\", line 187:\n    sage: y * 1.0                                                         # optional - magma\nException raised:\n    Traceback (most recent call last):\n      File \"/home/jec/sage-current/local/bin/ncadoctest.py\", line 1231, in run_one_test\n        self.run_one_example(test, example, filename, compileflags)\n      File \"/home/jec/sage-current/local/bin/sagedoctest.py\", line 38, in run_one_example\n        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)\n      File \"/home/jec/sage-current/local/bin/ncadoctest.py\", line 1172, in run_one_example\n        compileflags, 1) in test.globs\n      File \"<doctest __main__.example_0[46]>\", line 1, in <module>\n        y * RealNumber('1.0')                                                         # optional - magma###line 187:\n    sage: y * 1.0                                                         # optional - magma\n      File \"element.pyx\", line 1398, in sage.structure.element.RingElement.__mul__ (sage/structure/element.c:11337)\n        return coercion_model.bin_op(left, right, mul)\n      File \"coerce.pyx\", line 717, in sage.structure.coerce.CoercionModel_cache_maps.bin_op (sage/structure/coerce.c:6212)\n        raise\n      File \"coerce.pyx\", line 713, in sage.structure.coerce.CoercionModel_cache_maps.bin_op (sage/structure/coerce.c:6151)\n        return PyObject_CallObject(op, xy)\n      File \"element.pyx\", line 1393, in sage.structure.element.RingElement.__mul__ (sage/structure/element.c:11265)\n        return (<RingElement>left)._mul_(<RingElement>right)\n      File \"element.pyx\", line 1400, in sage.structure.element.RingElement._mul_ (sage/structure/element.c:11385)\n        cpdef RingElement _mul_(self, RingElement right):\n      File \"/home/jec/sage-current/local/lib/python/site-packages/sage/interfaces/expect.py\", line 1909, in _mul_\n        return self._operation('*', right)\n      File \"/home/jec/sage-current/local/lib/python/site-packages/sage/interfaces/expect.py\", line 1866, in _operation\n        raise TypeError, msg\n    TypeError: Error evaluating Magma code.\n    IN:\n[27]:=_sage_[19] * _sage_[25];\n    OUT:\n    >> _sage_[27]:=_sage_[19] * _sage_[25];\n                              ^\n    Runtime error in '*': Bad argument types\n    Argument types given: RngUPolElt[RngInt], FldReElt\n\n```\n\nand this looks like some error in parsing the expected output (are you allowed two different \"...\"?) since it looks fine to me.  The only other things I can think of is that there may be different numbers of spaces in the expected and actual magma output!",
    "created_at": "2010-04-06T17:20:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7870",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7870#issuecomment-68283",
    "user": "cremona"
}
```

OK, so after actually applying the patch (I had forgotten to do hg qpush) I get exactly one failure.  This is on 64-bit ubuntu, Sage 4.3.5 and Magma V2.16-1:

```
sage -t --only_optional=magma "./sage/interfaces/magma.py"  
**********************************************************************
File "/storage/jec/sage-4.3.5/devel/sage-tests/sage/interfaces/magma.py", line 187:
    sage: y * 1.0                                                         # optional - magma
Exception raised:
    Traceback (most recent call last):
      File "/home/jec/sage-current/local/bin/ncadoctest.py", line 1231, in run_one_test
        self.run_one_example(test, example, filename, compileflags)
      File "/home/jec/sage-current/local/bin/sagedoctest.py", line 38, in run_one_example
        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)
      File "/home/jec/sage-current/local/bin/ncadoctest.py", line 1172, in run_one_example
        compileflags, 1) in test.globs
      File "<doctest __main__.example_0[46]>", line 1, in <module>
        y * RealNumber('1.0')                                                         # optional - magma###line 187:
    sage: y * 1.0                                                         # optional - magma
      File "element.pyx", line 1398, in sage.structure.element.RingElement.__mul__ (sage/structure/element.c:11337)
        return coercion_model.bin_op(left, right, mul)
      File "coerce.pyx", line 717, in sage.structure.coerce.CoercionModel_cache_maps.bin_op (sage/structure/coerce.c:6212)
        raise
      File "coerce.pyx", line 713, in sage.structure.coerce.CoercionModel_cache_maps.bin_op (sage/structure/coerce.c:6151)
        return PyObject_CallObject(op, xy)
      File "element.pyx", line 1393, in sage.structure.element.RingElement.__mul__ (sage/structure/element.c:11265)
        return (<RingElement>left)._mul_(<RingElement>right)
      File "element.pyx", line 1400, in sage.structure.element.RingElement._mul_ (sage/structure/element.c:11385)
        cpdef RingElement _mul_(self, RingElement right):
      File "/home/jec/sage-current/local/lib/python/site-packages/sage/interfaces/expect.py", line 1909, in _mul_
        return self._operation('*', right)
      File "/home/jec/sage-current/local/lib/python/site-packages/sage/interfaces/expect.py", line 1866, in _operation
        raise TypeError, msg
    TypeError: Error evaluating Magma code.
    IN:
[27]:=_sage_[19] * _sage_[25];
    OUT:
    >> _sage_[27]:=_sage_[19] * _sage_[25];
                              ^
    Runtime error in '*': Bad argument types
    Argument types given: RngUPolElt[RngInt], FldReElt

```

and this looks like some error in parsing the expected output (are you allowed two different "..."?) since it looks fine to me.  The only other things I can think of is that there may be different numbers of spaces in the expected and actual magma output!



---

archive/issue_comments_068284.json:
```json
{
    "body": "Changing keywords from \"\" to \"Magma\".",
    "created_at": "2010-04-06T17:20:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7870",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7870#issuecomment-68284",
    "user": "cremona"
}
```

Changing keywords from "" to "Magma".



---

archive/issue_comments_068285.json:
```json
{
    "body": "John,\n\nI think you should give my patch a positive review anyways.  The problem above is that in Magma V2.16-7, this works fine:\n\n```\n[wstein@eno ~]$ magma\nMagma V2.16-7     Mon Apr 26 2010 22:51:34 on eno      [Seed = 294390646]\nType ? for help.  Type <Ctrl>-D to quit.\n> R<x> := PolynomialRing(Integers());\n> x*1.0;\n$.1\n> \n```\n\nHowever, in older versions of Magma, it doesn't:\n\n```\nflat:~ wstein$ magma\nMagma V2.15-11    Mon Apr 26 2010 19:53:21 on flat     [Seed = 4201111680]\nType ? for help.  Type <Ctrl>-D to quit.\n> R<x> := PolynomialRing(Integers());\n> x*1.0;\n\n>> x*1.0;\n    ^\nRuntime error in '*': Bad argument types\nArgument types given: RngUPolElt[RngInt], FldReElt\n```\n\n\nSince Magma's capabilities, etc., change a *lot* -- even from minor version to version -- I think the Sage optional doctests should be targeted at the latest released version of Magma.   \n\nNote that the computation is multiplying a polynomial over ZZ[x] by a floating point numbers.  In Sage, there is a beautiful coercion model that makes most such things \"just work\".  In Magma, one implements the '*' function for every conceivable choice of pairs of types... and I guess somebody got around to eventually implementing this one. \n\nJust to emphasize how totally arbitrary (and sad) Magma's system still is after all these years, notice that even in Magma V2.16-7, the same computation with polynomials over ZZ and rational numbers doesn't work!\n\n```\n> x + 1/2;        \n\n>> x + 1/2;\n     ^\nRuntime error in '+': Bad argument types\nArgument types given: RngUPolElt[RngInt], FldRatElt\n\n> x*(1/2);\n\n>> x*(1/2);\n    ^\nRuntime error in '*': Bad argument types\nArgument types given: RngUPolElt[RngInt], FldRatElt\n\n> \n```\n\n\nSage had the same sort of silly anomalies until people like David Harvey, Craig Citro, David Roe, and *Robert Bradshaw* and others stepped in and greatly improved the situation. \n\n\n```\nsage: R.<x> = ZZ[]\nsage: x * 1.0\nx\nsage: parent(x * 1.0)\nUnivariate Polynomial Ring in x over Real Field with 53 bits of precision\nsage: x + 1/2\nx + 1/2\nsage: (1/2)*x\n1/2*x\n```\n\n\nSage coercion is still of course far from perfect.  But it's also far from sucking. \n\n -- William",
    "created_at": "2010-04-27T02:59:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7870",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7870#issuecomment-68285",
    "user": "was"
}
```

John,

I think you should give my patch a positive review anyways.  The problem above is that in Magma V2.16-7, this works fine:

```
[wstein@eno ~]$ magma
Magma V2.16-7     Mon Apr 26 2010 22:51:34 on eno      [Seed = 294390646]
Type ? for help.  Type <Ctrl>-D to quit.
> R<x> := PolynomialRing(Integers());
> x*1.0;
$.1
> 
```

However, in older versions of Magma, it doesn't:

```
flat:~ wstein$ magma
Magma V2.15-11    Mon Apr 26 2010 19:53:21 on flat     [Seed = 4201111680]
Type ? for help.  Type <Ctrl>-D to quit.
> R<x> := PolynomialRing(Integers());
> x*1.0;

>> x*1.0;
    ^
Runtime error in '*': Bad argument types
Argument types given: RngUPolElt[RngInt], FldReElt
```


Since Magma's capabilities, etc., change a *lot* -- even from minor version to version -- I think the Sage optional doctests should be targeted at the latest released version of Magma.   

Note that the computation is multiplying a polynomial over ZZ[x] by a floating point numbers.  In Sage, there is a beautiful coercion model that makes most such things "just work".  In Magma, one implements the '*' function for every conceivable choice of pairs of types... and I guess somebody got around to eventually implementing this one. 

Just to emphasize how totally arbitrary (and sad) Magma's system still is after all these years, notice that even in Magma V2.16-7, the same computation with polynomials over ZZ and rational numbers doesn't work!

```
> x + 1/2;        

>> x + 1/2;
     ^
Runtime error in '+': Bad argument types
Argument types given: RngUPolElt[RngInt], FldRatElt

> x*(1/2);

>> x*(1/2);
    ^
Runtime error in '*': Bad argument types
Argument types given: RngUPolElt[RngInt], FldRatElt

> 
```


Sage had the same sort of silly anomalies until people like David Harvey, Craig Citro, David Roe, and *Robert Bradshaw* and others stepped in and greatly improved the situation. 


```
sage: R.<x> = ZZ[]
sage: x * 1.0
x
sage: parent(x * 1.0)
Univariate Polynomial Ring in x over Real Field with 53 bits of precision
sage: x + 1/2
x + 1/2
sage: (1/2)*x
1/2*x
```


Sage coercion is still of course far from perfect.  But it's also far from sucking. 

 -- William



---

archive/issue_comments_068286.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2010-04-27T02:59:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7870",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7870#issuecomment-68286",
    "user": "was"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_068287.json:
```json
{
    "body": "I just lost my posting here (cookie problem) and don't feel like rewriting it all....\n\nI only have C2.16-1 and the patch requires V2.16-7 or higher to pass, it seems, so I cannot verify it at present.\n\nIs it anywhere documented which version of Magma Sage relies on for positive tests?",
    "created_at": "2010-04-27T12:46:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7870",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7870#issuecomment-68287",
    "user": "cremona"
}
```

I just lost my posting here (cookie problem) and don't feel like rewriting it all....

I only have C2.16-1 and the patch requires V2.16-7 or higher to pass, it seems, so I cannot verify it at present.

Is it anywhere documented which version of Magma Sage relies on for positive tests?



---

archive/issue_comments_068288.json:
```json
{
    "body": "With Sage 4.4 and a newly installed magma V1.16-7 I still get falures in these files:\n\n```\n\tsage -t --only_optional=magma \"devel/sage/sage/rings/finite_rings/element_givaro.pyx\"\n\tsage -t --only_optional=magma \"devel/sage/sage/rings/polynomial/multi_polynomial.pyx\"\n\tsage -t --only_optional=magma \"devel/sage/sage/rings/polynomial/polynomial_element.pyx\"\n\tsage -t --only_optional=magma \"devel/sage/sage/rings/polynomial/polynomial_ring.py\"\n\tsage -t --only_optional=magma \"devel/sage/sage/schemes/elliptic_curves/ell_generic.py\"\n\tsage -t --only_optional=magma \"devel/sage/sage/schemes/hyperelliptic_curves/hyperelliptic_generic.py\"\n```\n\nSee http://www.warwick.ac.uk/staff/J.E.Cremona/magma.out for the full log.",
    "created_at": "2010-04-28T09:51:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7870",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7870#issuecomment-68288",
    "user": "cremona"
}
```

With Sage 4.4 and a newly installed magma V1.16-7 I still get falures in these files:

```
	sage -t --only_optional=magma "devel/sage/sage/rings/finite_rings/element_givaro.pyx"
	sage -t --only_optional=magma "devel/sage/sage/rings/polynomial/multi_polynomial.pyx"
	sage -t --only_optional=magma "devel/sage/sage/rings/polynomial/polynomial_element.pyx"
	sage -t --only_optional=magma "devel/sage/sage/rings/polynomial/polynomial_ring.py"
	sage -t --only_optional=magma "devel/sage/sage/schemes/elliptic_curves/ell_generic.py"
	sage -t --only_optional=magma "devel/sage/sage/schemes/hyperelliptic_curves/hyperelliptic_generic.py"
```

See http://www.warwick.ac.uk/staff/J.E.Cremona/magma.out for the full log.



---

archive/issue_comments_068289.json:
```json
{
    "body": "A shorter log file with only the failing files is at http://www.warwick.ac.uk/staff/J.E.Cremona/magma.out.short",
    "created_at": "2010-04-28T10:20:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7870",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7870#issuecomment-68289",
    "user": "cremona"
}
```

A shorter log file with only the failing files is at http://www.warwick.ac.uk/staff/J.E.Cremona/magma.out.short



---

archive/issue_comments_068290.json:
```json
{
    "body": "Oh boy, it looks like sage-4.4 changed (from when I made the patch) and introduced a *bunch* of new issues :-(.   Sigh, I'll have to rewrite a bunch of the interface, evidently. Well at least I know now.",
    "created_at": "2010-05-01T07:11:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7870",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7870#issuecomment-68290",
    "user": "was"
}
```

Oh boy, it looks like sage-4.4 changed (from when I made the patch) and introduced a *bunch* of new issues :-(.   Sigh, I'll have to rewrite a bunch of the interface, evidently. Well at least I know now.



---

archive/issue_comments_068291.json:
```json
{
    "body": "Is there any explanation of why these doc tests need to be revised? I can see \n\nsage/symbolic/expression.pyx\n\nhas a pretty trivial change, since Magma has decided to reverse the order of the outputs. \n\nBut others seem really odd. \n\nmagma(HyperellipticCurve(f)).IgusaClebschInvariants() # optional - magma \nremove: [ 0, -2048/375, -4096/25, -4881645568/84375 ] \nadd: [ -640, -20480, 1310720, 52160364544 ] \n\nWere the first set of Magma results wrong? If so, why was they used as a doctest? \n\nThis is probably my lack of mathematical knowledge showing here, but it appears to me Magma has output something completely different in many cases. Is the new output correct? Was the old output incorrect? \n\nDave",
    "created_at": "2010-06-02T20:29:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7870",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7870#issuecomment-68291",
    "user": "drkirkby"
}
```

Is there any explanation of why these doc tests need to be revised? I can see 

sage/symbolic/expression.pyx

has a pretty trivial change, since Magma has decided to reverse the order of the outputs. 

But others seem really odd. 

magma(HyperellipticCurve(f)).IgusaClebschInvariants() # optional - magma 
remove: [ 0, -2048/375, -4096/25, -4881645568/84375 ] 
add: [ -640, -20480, 1310720, 52160364544 ] 

Were the first set of Magma results wrong? If so, why was they used as a doctest? 

This is probably my lack of mathematical knowledge showing here, but it appears to me Magma has output something completely different in many cases. Is the new output correct? Was the old output incorrect? 

Dave



---

archive/issue_comments_068292.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2010-06-22T17:49:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7870",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7870#issuecomment-68292",
    "user": "rlm"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_068293.json:
```json
{
    "body": "Replying to [comment:12 was]:\n> Oh boy, it looks like sage-4.4 changed (from when I made the patch) and introduced a *bunch* of new issues :-(.   Sigh, I'll have to rewrite a bunch of the interface, evidently. Well at least I know now.\n\nBased on this, I'm changing this to needs_work. Not volunteering to review, just trying to clean up trac a bit!",
    "created_at": "2010-06-22T17:49:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7870",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7870#issuecomment-68293",
    "user": "rlm"
}
```

Replying to [comment:12 was]:
> Oh boy, it looks like sage-4.4 changed (from when I made the patch) and introduced a *bunch* of new issues :-(.   Sigh, I'll have to rewrite a bunch of the interface, evidently. Well at least I know now.

Based on this, I'm changing this to needs_work. Not volunteering to review, just trying to clean up trac a bit!



---

archive/issue_comments_068294.json:
```json
{
    "body": "Attachment [trac_7870-magma-doctest.patch](tarball://root/attachments/some-uuid/ticket7870/trac_7870-magma-doctest.patch) by cremona created at 2011-02-18 23:04:50\n\nReplaces all previous patches;  applies to 4.6.1 and Magma 2.17-4",
    "created_at": "2011-02-18T23:04:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7870",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7870#issuecomment-68294",
    "user": "cremona"
}
```

Attachment [trac_7870-magma-doctest.patch](tarball://root/attachments/some-uuid/ticket7870/trac_7870-magma-doctest.patch) by cremona created at 2011-02-18 23:04:50

Replaces all previous patches;  applies to 4.6.1 and Magma 2.17-4



---

archive/issue_comments_068295.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2011-02-18T23:06:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7870",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7870#issuecomment-68295",
    "user": "cremona"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_068296.json:
```json
{
    "body": "New patch passes all optional doctests on skynet (eno) with 4.6.1 and Magma 2.17-4.",
    "created_at": "2011-02-18T23:06:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7870",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7870#issuecomment-68296",
    "user": "cremona"
}
```

New patch passes all optional doctests on skynet (eno) with 4.6.1 and Magma 2.17-4.



---

archive/issue_comments_068297.json:
```json
{
    "body": "I had to change one doctest, such that it also fits my output. This is definitely no issue, as I just added ... for the time. Apart from this: Perfect!\n\nFor the record, the patchbot and the release manager:\n\nApply trac_7870-magma-doctest.patch\nApply trac-7870-magma-doctest-review.patch",
    "created_at": "2011-03-02T09:57:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7870",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7870#issuecomment-68297",
    "user": "mraum"
}
```

I had to change one doctest, such that it also fits my output. This is definitely no issue, as I just added ... for the time. Apart from this: Perfect!

For the record, the patchbot and the release manager:

Apply trac_7870-magma-doctest.patch
Apply trac-7870-magma-doctest-review.patch



---

archive/issue_comments_068298.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2011-03-02T09:57:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7870",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7870#issuecomment-68298",
    "user": "mraum"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_068299.json:
```json
{
    "body": "Attachment [trac-7870-magma-doctest-review.patch](tarball://root/attachments/some-uuid/ticket7870/trac-7870-magma-doctest-review.patch) by mraum created at 2011-03-02 09:58:18",
    "created_at": "2011-03-02T09:58:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7870",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7870#issuecomment-68299",
    "user": "mraum"
}
```

Attachment [trac-7870-magma-doctest-review.patch](tarball://root/attachments/some-uuid/ticket7870/trac-7870-magma-doctest-review.patch) by mraum created at 2011-03-02 09:58:18



---

archive/issue_comments_068300.json:
```json
{
    "body": "I'm happy with the reviewer's patch, and note that this ticket is still marked \"positive review\".",
    "created_at": "2011-03-02T16:48:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7870",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7870#issuecomment-68300",
    "user": "cremona"
}
```

I'm happy with the reviewer's patch, and note that this ticket is still marked "positive review".



---

archive/issue_comments_068301.json:
```json
{
    "body": "\n```\ntrac_7870-magma-doctest.patch and trac-7870-magma-doctest-review.patch\nwhen applied to 4.6.2 pass all optional doctests\n(-only-optional=magma) on skynet/eno with Magma-2.17-5.\n```\n",
    "created_at": "2011-03-04T16:26:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7870",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7870#issuecomment-68301",
    "user": "mariah"
}
```


```
trac_7870-magma-doctest.patch and trac-7870-magma-doctest-review.patch
when applied to 4.6.2 pass all optional doctests
(-only-optional=magma) on skynet/eno with Magma-2.17-5.
```




---

archive/issue_comments_068302.json:
```json
{
    "body": "Replying to [comment:16 mraum]:\n> For the record, the patchbot and the release manager:\n> \n> Apply trac_7870-magma-doctest.patch\n> Apply trac-7870-magma-doctest-review.patch\n\n**Please** in the future write this in the ticket **description**.  Thanks!",
    "created_at": "2011-03-08T09:02:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7870",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7870#issuecomment-68302",
    "user": "jdemeyer"
}
```

Replying to [comment:16 mraum]:
> For the record, the patchbot and the release manager:
> 
> Apply trac_7870-magma-doctest.patch
> Apply trac-7870-magma-doctest-review.patch

**Please** in the future write this in the ticket **description**.  Thanks!



---

archive/issue_comments_068303.json:
```json
{
    "body": "Replying to [comment:19 jdemeyer]:\n> Replying to [comment:16 mraum]:\n> > For the record, the patchbot and the release manager:\n> > \n> > Apply trac_7870-magma-doctest.patch\n> > Apply trac-7870-magma-doctest-review.patch\n> \n> **Please** in the future write this in the ticket **description**.  Thanks!\n\nThat makes a lot of sence and should probably be put in some sort of guide to using trac. Is there one specifically for Sage? \n\nI know I came unstuck recently when I put a link to an spkg in the description, but that spkg needed tekinfo (or whatever it was), so Francois posted one which did not need it. But mine was in the description, his one was less prominently placed in the notes, so you used mine and found it did not work. \n\nAt the very least, specifying the locations of .spkgs and what patches needed to be applied, should be mentioned on sage-devel, but ideally we need it documented on the trac server. \n\nDave",
    "created_at": "2011-03-08T09:37:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7870",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7870#issuecomment-68303",
    "user": "drkirkby"
}
```

Replying to [comment:19 jdemeyer]:
> Replying to [comment:16 mraum]:
> > For the record, the patchbot and the release manager:
> > 
> > Apply trac_7870-magma-doctest.patch
> > Apply trac-7870-magma-doctest-review.patch
> 
> **Please** in the future write this in the ticket **description**.  Thanks!

That makes a lot of sence and should probably be put in some sort of guide to using trac. Is there one specifically for Sage? 

I know I came unstuck recently when I put a link to an spkg in the description, but that spkg needed tekinfo (or whatever it was), so Francois posted one which did not need it. But mine was in the description, his one was less prominently placed in the notes, so you used mine and found it did not work. 

At the very least, specifying the locations of .spkgs and what patches needed to be applied, should be mentioned on sage-devel, but ideally we need it documented on the trac server. 

Dave



---

archive/issue_comments_068304.json:
```json
{
    "body": "Changing status from positive_review to needs_work.",
    "created_at": "2011-03-08T12:49:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7870",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7870#issuecomment-68304",
    "user": "jdemeyer"
}
```

Changing status from positive_review to needs_work.



---

archive/issue_comments_068305.json:
```json
{
    "body": "All doctests involving magma should be marked `# optional - magma`.  I get various failures in `sage/rings/number_field/number_field.py`.",
    "created_at": "2011-03-08T12:49:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7870",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7870#issuecomment-68305",
    "user": "jdemeyer"
}
```

All doctests involving magma should be marked `# optional - magma`.  I get various failures in `sage/rings/number_field/number_field.py`.



---

archive/issue_comments_068306.json:
```json
{
    "body": "Replying to [comment:21 jdemeyer]:\n> All doctests involving magma should be marked `# optional - magma`.  I get various failures in `sage/rings/number_field/number_field.py`.\n\nApologies, this refers to the new function I put in (_magma_polynomial_) where I did not tag the doctests as optional.  It's my fault (though William was sitting next to me at the time, so I blame him too!)",
    "created_at": "2011-03-08T17:09:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7870",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7870#issuecomment-68306",
    "user": "cremona"
}
```

Replying to [comment:21 jdemeyer]:
> All doctests involving magma should be marked `# optional - magma`.  I get various failures in `sage/rings/number_field/number_field.py`.

Apologies, this refers to the new function I put in (_magma_polynomial_) where I did not tag the doctests as optional.  It's my fault (though William was sitting next to me at the time, so I blame him too!)



---

archive/issue_comments_068307.json:
```json
{
    "body": "Attachment [trac-7870-magma-doctest-review2.patch](tarball://root/attachments/some-uuid/ticket7870/trac-7870-magma-doctest-review2.patch) by mraum created at 2011-03-08 17:42:55\n\nAnd it's my fault as well. I'm terribly sorry!\nJohn, do you have a maschine without magma to run tests for the above fix on? It was only one function that was missed.\n\nMartin",
    "created_at": "2011-03-08T17:42:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7870",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7870#issuecomment-68307",
    "user": "mraum"
}
```

Attachment [trac-7870-magma-doctest-review2.patch](tarball://root/attachments/some-uuid/ticket7870/trac-7870-magma-doctest-review2.patch) by mraum created at 2011-03-08 17:42:55

And it's my fault as well. I'm terribly sorry!
John, do you have a maschine without magma to run tests for the above fix on? It was only one function that was missed.

Martin



---

archive/issue_comments_068308.json:
```json
{
    "body": "I don't think it is necessary to have a machine without magma.  Just run a complete test both with and with out the --optional-magma.  It is faster to run with that flag since only doctests with the optional magma flag are run.",
    "created_at": "2011-03-08T19:02:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7870",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7870#issuecomment-68308",
    "user": "cremona"
}
```

I don't think it is necessary to have a machine without magma.  Just run a complete test both with and with out the --optional-magma.  It is faster to run with that flag since only doctests with the optional magma flag are run.



---

archive/issue_comments_068309.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2011-03-08T21:04:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7870",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7870#issuecomment-68309",
    "user": "jdemeyer"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_068310.json:
```json
{
    "body": "This seems right. So, if everything is ok for you, also, give it a positive review.",
    "created_at": "2011-03-09T01:40:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7870",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7870#issuecomment-68310",
    "user": "mraum"
}
```

This seems right. So, if everything is ok for you, also, give it a positive review.



---

archive/issue_comments_068311.json:
```json
{
    "body": "According to the `sage -h`, the option should be `-only-optional=magma` and **not** `--only-optional=magma`\n\n\nI don't have Magma, but do have Mathematica, so I thought I'd try\n\n\n```\ndrkirkby@hawk:~/sage-4.6.2.rc1$ ./sage -t -only_optional=mathematica devel/sage/sage\nsage -t -only_optional=mathematica \"devel/sage/sage/probability/all.py\"\n\t [0.1 s]\nsage -t -only_optional=mathematica \"devel/sage/sage/probability/__init__.py\"\n\t [0.1 s]\nsage -t -only_optional=mathematica \"devel/sage/sage/probability/random_variable.py\"\n```\n\n\nbut it seems to run every doctest, not just the Mathematica ones, which fail anyway, as noted at #8495. \n\n\nDave",
    "created_at": "2011-03-09T06:26:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7870",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7870#issuecomment-68311",
    "user": "drkirkby"
}
```

According to the `sage -h`, the option should be `-only-optional=magma` and **not** `--only-optional=magma`


I don't have Magma, but do have Mathematica, so I thought I'd try


```
drkirkby@hawk:~/sage-4.6.2.rc1$ ./sage -t -only_optional=mathematica devel/sage/sage
sage -t -only_optional=mathematica "devel/sage/sage/probability/all.py"
	 [0.1 s]
sage -t -only_optional=mathematica "devel/sage/sage/probability/__init__.py"
	 [0.1 s]
sage -t -only_optional=mathematica "devel/sage/sage/probability/random_variable.py"
```


but it seems to run every doctest, not just the Mathematica ones, which fail anyway, as noted at #8495. 


Dave



---

archive/issue_comments_068312.json:
```json
{
    "body": "This needs to be rebased to sage-4.7.alpha1.",
    "created_at": "2011-03-11T22:07:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7870",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7870#issuecomment-68312",
    "user": "jdemeyer"
}
```

This needs to be rebased to sage-4.7.alpha1.



---

archive/issue_comments_068313.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2011-03-11T22:07:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7870",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7870#issuecomment-68313",
    "user": "jdemeyer"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_068314.json:
```json
{
    "body": "Attachment [trac-7870-magma-doctest-review3.patch](tarball://root/attachments/some-uuid/ticket7870/trac-7870-magma-doctest-review3.patch) by mraum created at 2011-03-12 20:55:17",
    "created_at": "2011-03-12T20:55:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7870",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7870#issuecomment-68314",
    "user": "mraum"
}
```

Attachment [trac-7870-magma-doctest-review3.patch](tarball://root/attachments/some-uuid/ticket7870/trac-7870-magma-doctest-review3.patch) by mraum created at 2011-03-12 20:55:17



---

archive/issue_comments_068315.json:
```json
{
    "body": "I rebased the patch to 4.7alpha1. Please only apply the last one: review3.\n\nCould anyone (John?) check this soon, so that we won't need to rebase it again?",
    "created_at": "2011-03-12T20:57:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7870",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7870#issuecomment-68315",
    "user": "mraum"
}
```

I rebased the patch to 4.7alpha1. Please only apply the last one: review3.

Could anyone (John?) check this soon, so that we won't need to rebase it again?



---

archive/issue_comments_068316.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2011-03-12T20:57:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7870",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7870#issuecomment-68316",
    "user": "mraum"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_068317.json:
```json
{
    "body": "Replying to [comment:29 mraum]:\n> I rebased the patch to 4.7alpha1. Please only apply the last one: review3.\n\nThanks.\n\n> \n> Could anyone (John?) check this soon, so that we won't need to rebase it again?\n\nOK, I'll try that soon.  (I have just been away for the weekend or I would have done it already.)",
    "created_at": "2011-03-14T01:26:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7870",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7870#issuecomment-68317",
    "user": "cremona"
}
```

Replying to [comment:29 mraum]:
> I rebased the patch to 4.7alpha1. Please only apply the last one: review3.

Thanks.

> 
> Could anyone (John?) check this soon, so that we won't need to rebase it again?

OK, I'll try that soon.  (I have just been away for the weekend or I would have done it already.)



---

archive/issue_comments_068318.json:
```json
{
    "body": "With magma-V2.17-5 (which I downloaded and installed specially) and sage-4.7.alpha1 I tested everything both with and without -only-optional=magma and in both cases all tests passed.\n\nSo I am giving this a positive review (again).",
    "created_at": "2011-03-15T04:33:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7870",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7870#issuecomment-68318",
    "user": "cremona"
}
```

With magma-V2.17-5 (which I downloaded and installed specially) and sage-4.7.alpha1 I tested everything both with and without -only-optional=magma and in both cases all tests passed.

So I am giving this a positive review (again).



---

archive/issue_comments_068319.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2011-03-15T04:33:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7870",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7870#issuecomment-68319",
    "user": "cremona"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_068320.json:
```json
{
    "body": "It seems that your 'review3' patch is based on an **older** version of the patches, I get the number_field doctest failures again.",
    "created_at": "2011-03-17T14:39:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7870",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7870#issuecomment-68320",
    "user": "jdemeyer"
}
```

It seems that your 'review3' patch is based on an **older** version of the patches, I get the number_field doctest failures again.



---

archive/issue_comments_068321.json:
```json
{
    "body": "Changing status from positive_review to needs_work.",
    "created_at": "2011-03-17T14:39:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7870",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7870#issuecomment-68321",
    "user": "jdemeyer"
}
```

Changing status from positive_review to needs_work.



---

archive/issue_comments_068322.json:
```json
{
    "body": "Well, yes. We really need to run the test on a setup without Magma then. I add the fix for this problem (which is review2 patch rebased to current Sage).",
    "created_at": "2011-03-17T16:29:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7870",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7870#issuecomment-68322",
    "user": "mraum"
}
```

Well, yes. We really need to run the test on a setup without Magma then. I add the fix for this problem (which is review2 patch rebased to current Sage).



---

archive/issue_comments_068323.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2011-03-17T16:29:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7870",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7870#issuecomment-68323",
    "user": "mraum"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_068324.json:
```json
{
    "body": "Attachment [trac-7870-magma-doctest-review4.patch](tarball://root/attachments/some-uuid/ticket7870/trac-7870-magma-doctest-review4.patch) by mraum created at 2011-03-17 16:30:17",
    "created_at": "2011-03-17T16:30:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7870",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7870#issuecomment-68324",
    "user": "mraum"
}
```

Attachment [trac-7870-magma-doctest-review4.patch](tarball://root/attachments/some-uuid/ticket7870/trac-7870-magma-doctest-review4.patch) by mraum created at 2011-03-17 16:30:17



---

archive/issue_comments_068325.json:
```json
{
    "body": "With the earlier patch (patch3) and the latest magma I tested everything and got no errors, so it seems like a waste of (my) time to do it all again.\n\nI do not understand mraum's comments about doing tests on a machine with no magma.  I ran complete tests with and without  -only-optional=magma.",
    "created_at": "2011-03-17T16:43:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7870",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7870#issuecomment-68325",
    "user": "cremona"
}
```

With the earlier patch (patch3) and the latest magma I tested everything and got no errors, so it seems like a waste of (my) time to do it all again.

I do not understand mraum's comments about doing tests on a machine with no magma.  I ran complete tests with and without  -only-optional=magma.



---

archive/issue_comments_068326.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2011-03-18T13:42:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7870",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7870#issuecomment-68326",
    "user": "jdemeyer"
}
```

Resolution: fixed



---

archive/issue_comments_068327.json:
```json
{
    "body": "Works now without magma.",
    "created_at": "2011-03-18T13:42:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7870",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7870#issuecomment-68327",
    "user": "jdemeyer"
}
```

Works now without magma.

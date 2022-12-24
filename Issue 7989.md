# Issue 7989: Minpoly doesn't work for all matrices

archive/issues_007989.json:
```json
{
    "body": "Assignee: was\n\nCC:  kcrisman rbeezer mhansen hedtke tscrim\n\nRight now, not all matrices can compute minpolys.  This patch exposes these matrices.\n\nIssue created by migration from https://trac.sagemath.org/ticket/7989\n\n",
    "created_at": "2010-01-19T02:42:47Z",
    "labels": [
        "linear algebra",
        "major",
        "bug"
    ],
    "title": "Minpoly doesn't work for all matrices",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/7989",
    "user": "jason"
}
```
Assignee: was

CC:  kcrisman rbeezer mhansen hedtke tscrim

Right now, not all matrices can compute minpolys.  This patch exposes these matrices.

Issue created by migration from https://trac.sagemath.org/ticket/7989





---

archive/issue_comments_069774.json:
```json
{
    "body": "Attachment [trac-7989-minpoly-test.patch](tarball://root/attachments/some-uuid/ticket7989/trac-7989-minpoly-test.patch) by jason created at 2010-01-19 02:50:48\n\nHere are the bugs (doctests that fail) this patch exposes:\n\n\n```\n\tsage -t  \"4.3.1.rc0/devel/sage-main/sage/matrix/matrix1.pyx\"\n\tsage -t  \"4.3.1.rc0/devel/sage-main/sage/matrix/matrix_dense.pyx\"\n\tsage -t  \"4.3.1.rc0/devel/sage-main/sage/matrix/matrix_generic_dense.pyx\"\n\tsage -t  \"4.3.1.rc0/devel/sage-main/sage/matrix/matrix_integer_2x2.pyx\"\n```\n",
    "created_at": "2010-01-19T02:50:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7989",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7989#issuecomment-69774",
    "user": "jason"
}
```

Attachment [trac-7989-minpoly-test.patch](tarball://root/attachments/some-uuid/ticket7989/trac-7989-minpoly-test.patch) by jason created at 2010-01-19 02:50:48

Here are the bugs (doctests that fail) this patch exposes:


```
	sage -t  "4.3.1.rc0/devel/sage-main/sage/matrix/matrix1.pyx"
	sage -t  "4.3.1.rc0/devel/sage-main/sage/matrix/matrix_dense.pyx"
	sage -t  "4.3.1.rc0/devel/sage-main/sage/matrix/matrix_generic_dense.pyx"
	sage -t  "4.3.1.rc0/devel/sage-main/sage/matrix/matrix_integer_2x2.pyx"
```




---

archive/issue_comments_069775.json:
```json
{
    "body": "Changing status from new to needs_work.",
    "created_at": "2010-01-19T03:45:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7989",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7989#issuecomment-69775",
    "user": "jason"
}
```

Changing status from new to needs_work.



---

archive/issue_comments_069776.json:
```json
{
    "body": "Sorry, I don't understand the reason for this function. What is the idea behind it?",
    "created_at": "2011-07-17T10:40:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7989",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7989#issuecomment-69776",
    "user": "hedtke"
}
```

Sorry, I don't understand the reason for this function. What is the idea behind it?



---

archive/issue_comments_069777.json:
```json
{
    "body": "This is a great patch.   I can't believe this has got ignored for the last 1.5 years. \n\nRegarding what needs to be fixed, the test failure you claim for matrix_integer_2x2 is:\n\n```\n\ndeep:sage wstein$ sage -t matrix/matrix_integer_2x2.pyx\nsage -t  \"matrix/matrix_integer_2x2.pyx\"                    \n**********************************************************************\nFile \"/Users/wstein/sage/install/sage-4.7.1.rc0/devel/sage-main/sage/matrix/matrix_integer_2x2.pyx\", line 101:\n    sage: TestSuite(m).run()\nExpected nothing\nGot:\n    Failure in _test_minpoly:\n    Traceback (most recent call last):\n      File \"/Users/wstein/sage/install/current/local/lib/python/site-packages/sage/misc/sage_unittest.py\", line 275, in run\n        test_method(tester = tester)\n      File \"matrix2.pyx\", line 1302, in sage.matrix.matrix2.Matrix._test_minpoly (sage/matrix/matrix2.c:8933)\n      File \"polynomial_element.pyx\", line 358, in sage.rings.polynomial.polynomial_element.Polynomial.subs (sage/rings/polynomial/polynomial_element.c:5624)\n      File \"polynomial_element.pyx\", line 557, in sage.rings.polynomial.polynomial_element.Polynomial.__call__ (sage/rings/polynomial/polynomial_element.c:5819)\n      File \"polynomial_element.pyx\", line 638, in sage.rings.polynomial.polynomial_element.Polynomial.__call__ (sage/rings/polynomial/polynomial_element.c:7244)\n      File \"element.pyx\", line 1302, in sage.structure.element.RingElement.__add__ (sage/structure/element.c:11504)\n      File \"coerce.pyx\", line 766, in sage.structure.coerce.CoercionModel_cache_maps.bin_op (sage/structure/coerce.c:7337)\n    TypeError: unsupported operand parent(s) for '+': 'Space of 2x2 integer matrices' and 'Integer Ring'\n    ------------------------------------------------------------\n    The following tests failed: _test_minpoly\n**********************************************************************\n1 items had failures:\n   1 of   6 in __main__.example_7\n***Test Failed*** 1 failures.\nFor whitespace errors, see the file /Users/wstein/.sage//tmp/.doctest_matrix_integer_2x2.py\n\t [4.6 s]\n```\n\n\nThis is because substitution isn't even implemented for that class:\n\n```\nsage: MS = sage.matrix.matrix_integer_2x2.MatrixSpace_ZZ_2x2()\nsage: a = MS([1,2,3,4])\nsage: a.minpoly()\nx^2 - 5*x - 2\nsage: a.minpoly()(a)\n---------------------------------------------------------------------------\nTypeError     \n```\n\n\nAlso, if one adds this for minpoly, it would make sense to also add _test_charpoly.\n\n -- William",
    "created_at": "2011-07-17T13:36:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7989",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7989#issuecomment-69777",
    "user": "was"
}
```

This is a great patch.   I can't believe this has got ignored for the last 1.5 years. 

Regarding what needs to be fixed, the test failure you claim for matrix_integer_2x2 is:

```

deep:sage wstein$ sage -t matrix/matrix_integer_2x2.pyx
sage -t  "matrix/matrix_integer_2x2.pyx"                    
**********************************************************************
File "/Users/wstein/sage/install/sage-4.7.1.rc0/devel/sage-main/sage/matrix/matrix_integer_2x2.pyx", line 101:
    sage: TestSuite(m).run()
Expected nothing
Got:
    Failure in _test_minpoly:
    Traceback (most recent call last):
      File "/Users/wstein/sage/install/current/local/lib/python/site-packages/sage/misc/sage_unittest.py", line 275, in run
        test_method(tester = tester)
      File "matrix2.pyx", line 1302, in sage.matrix.matrix2.Matrix._test_minpoly (sage/matrix/matrix2.c:8933)
      File "polynomial_element.pyx", line 358, in sage.rings.polynomial.polynomial_element.Polynomial.subs (sage/rings/polynomial/polynomial_element.c:5624)
      File "polynomial_element.pyx", line 557, in sage.rings.polynomial.polynomial_element.Polynomial.__call__ (sage/rings/polynomial/polynomial_element.c:5819)
      File "polynomial_element.pyx", line 638, in sage.rings.polynomial.polynomial_element.Polynomial.__call__ (sage/rings/polynomial/polynomial_element.c:7244)
      File "element.pyx", line 1302, in sage.structure.element.RingElement.__add__ (sage/structure/element.c:11504)
      File "coerce.pyx", line 766, in sage.structure.coerce.CoercionModel_cache_maps.bin_op (sage/structure/coerce.c:7337)
    TypeError: unsupported operand parent(s) for '+': 'Space of 2x2 integer matrices' and 'Integer Ring'
    ------------------------------------------------------------
    The following tests failed: _test_minpoly
**********************************************************************
1 items had failures:
   1 of   6 in __main__.example_7
***Test Failed*** 1 failures.
For whitespace errors, see the file /Users/wstein/.sage//tmp/.doctest_matrix_integer_2x2.py
	 [4.6 s]
```


This is because substitution isn't even implemented for that class:

```
sage: MS = sage.matrix.matrix_integer_2x2.MatrixSpace_ZZ_2x2()
sage: a = MS([1,2,3,4])
sage: a.minpoly()
x^2 - 5*x - 2
sage: a.minpoly()(a)
---------------------------------------------------------------------------
TypeError     
```


Also, if one adds this for minpoly, it would make sense to also add _test_charpoly.

 -- William



---

archive/issue_comments_069778.json:
```json
{
    "body": "OK. Works for me, too. Is it favored that we include a test that purposely fails?",
    "created_at": "2011-07-17T18:11:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7989",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7989#issuecomment-69778",
    "user": "hedtke"
}
```

OK. Works for me, too. Is it favored that we include a test that purposely fails?



---

archive/issue_comments_069779.json:
```json
{
    "body": "Replying to [comment:7 hedtke]:\n> OK. Works for me, too. Is it favored that we include a test that purposely fails?\n\nI think the idea is to include the test-suite checking **and** add the fixes needed to make the tests pass.",
    "created_at": "2011-07-17T18:31:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7989",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7989#issuecomment-69779",
    "user": "rbeezer"
}
```

Replying to [comment:7 hedtke]:
> OK. Works for me, too. Is it favored that we include a test that purposely fails?

I think the idea is to include the test-suite checking **and** add the fixes needed to make the tests pass.



---

archive/issue_comments_069780.json:
```json
{
    "body": "sage-6.2.beta4:\n\n```\nsage -t src/sage/matrix/matrix_generic_dense.pyx  # 1 doctest failed\nsage -t src/sage/matrix/matrix_dense.pyx  # 1 doctest failed\n```\n",
    "created_at": "2014-03-15T15:08:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7989",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7989#issuecomment-69780",
    "user": "mmezzarobba"
}
```

sage-6.2.beta4:

```
sage -t src/sage/matrix/matrix_generic_dense.pyx  # 1 doctest failed
sage -t src/sage/matrix/matrix_dense.pyx  # 1 doctest failed
```




---

archive/issue_comments_069781.json:
```json
{
    "body": "New commits:",
    "created_at": "2022-05-19T09:24:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7989",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7989#issuecomment-69781",
    "user": "chapoton"
}
```

New commits:



---

archive/issue_comments_069782.json:
```json
{
    "body": "Branch pushed to git repo; I updated commit sha1. New commits:",
    "created_at": "2022-05-19T14:19:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7989",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7989#issuecomment-69782",
    "user": "git"
}
```

Branch pushed to git repo; I updated commit sha1. New commits:



---

archive/issue_comments_069783.json:
```json
{
    "body": "Branch pushed to git repo; I updated commit sha1. New commits:",
    "created_at": "2022-05-19T14:40:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7989",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7989#issuecomment-69783",
    "user": "git"
}
```

Branch pushed to git repo; I updated commit sha1. New commits:



---

archive/issue_comments_069784.json:
```json
{
    "body": "Branch pushed to git repo; I updated commit sha1. New commits:",
    "created_at": "2022-05-19T17:10:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7989",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7989#issuecomment-69784",
    "user": "git"
}
```

Branch pushed to git repo; I updated commit sha1. New commits:



---

archive/issue_comments_069785.json:
```json
{
    "body": "Branch pushed to git repo; I updated commit sha1. New commits:",
    "created_at": "2022-05-20T11:38:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7989",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7989#issuecomment-69785",
    "user": "git"
}
```

Branch pushed to git repo; I updated commit sha1. New commits:



---

archive/issue_comments_069786.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2022-05-20T11:59:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7989",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7989#issuecomment-69786",
    "user": "chapoton"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_069787.json:
```json
{
    "body": "green patchbot, so please review",
    "created_at": "2022-05-21T11:44:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7989",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7989#issuecomment-69787",
    "user": "chapoton"
}
```

green patchbot, so please review



---

archive/issue_comments_069788.json:
```json
{
    "body": "LGTM.",
    "created_at": "2022-05-23T02:47:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7989",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7989#issuecomment-69788",
    "user": "tscrim"
}
```

LGTM.



---

archive/issue_comments_069789.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2022-05-23T02:47:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7989",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7989#issuecomment-69789",
    "user": "tscrim"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_069790.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2022-05-26T22:49:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7989",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7989#issuecomment-69790",
    "user": "vbraun"
}
```

Resolution: fixed

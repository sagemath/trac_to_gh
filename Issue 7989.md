# Issue 7989: Minpoly doesn't work for all matrices

archive/issues_007989.json:
```json
{
    "body": "Assignee: @williamstein\n\nCC:  @kcrisman @rbeezer @mwhansen @hedtke @tscrim\n\nRight now, not all matrices can compute minpolys.  This patch exposes these matrices.\n\nIssue created by migration from https://trac.sagemath.org/ticket/7989\n\n",
    "created_at": "2010-01-19T02:42:47Z",
    "labels": [
        "component: linear algebra",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-9.7",
    "title": "Minpoly doesn't work for all matrices",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/7989",
    "user": "https://github.com/jasongrout"
}
```
Assignee: @williamstein

CC:  @kcrisman @rbeezer @mwhansen @hedtke @tscrim

Right now, not all matrices can compute minpolys.  This patch exposes these matrices.

Issue created by migration from https://trac.sagemath.org/ticket/7989





---

archive/issue_comments_069654.json:
```json
{
    "body": "Attachment [trac-7989-minpoly-test.patch](tarball://root/attachments/some-uuid/ticket7989/trac-7989-minpoly-test.patch) by @jasongrout created at 2010-01-19 02:50:48\n\nHere are the bugs (doctests that fail) this patch exposes:\n\n\n```\n\tsage -t  \"4.3.1.rc0/devel/sage-main/sage/matrix/matrix1.pyx\"\n\tsage -t  \"4.3.1.rc0/devel/sage-main/sage/matrix/matrix_dense.pyx\"\n\tsage -t  \"4.3.1.rc0/devel/sage-main/sage/matrix/matrix_generic_dense.pyx\"\n\tsage -t  \"4.3.1.rc0/devel/sage-main/sage/matrix/matrix_integer_2x2.pyx\"\n```\n",
    "created_at": "2010-01-19T02:50:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7989",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7989#issuecomment-69654",
    "user": "https://github.com/jasongrout"
}
```

Attachment [trac-7989-minpoly-test.patch](tarball://root/attachments/some-uuid/ticket7989/trac-7989-minpoly-test.patch) by @jasongrout created at 2010-01-19 02:50:48

Here are the bugs (doctests that fail) this patch exposes:


```
	sage -t  "4.3.1.rc0/devel/sage-main/sage/matrix/matrix1.pyx"
	sage -t  "4.3.1.rc0/devel/sage-main/sage/matrix/matrix_dense.pyx"
	sage -t  "4.3.1.rc0/devel/sage-main/sage/matrix/matrix_generic_dense.pyx"
	sage -t  "4.3.1.rc0/devel/sage-main/sage/matrix/matrix_integer_2x2.pyx"
```




---

archive/issue_comments_069655.json:
```json
{
    "body": "Changing status from new to needs_work.",
    "created_at": "2010-01-19T03:45:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7989",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7989#issuecomment-69655",
    "user": "https://github.com/jasongrout"
}
```

Changing status from new to needs_work.



---

archive/issue_comments_069656.json:
```json
{
    "body": "Sorry, I don't understand the reason for this function. What is the idea behind it?",
    "created_at": "2011-07-17T10:40:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7989",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7989#issuecomment-69656",
    "user": "https://github.com/hedtke"
}
```

Sorry, I don't understand the reason for this function. What is the idea behind it?



---

archive/issue_comments_069657.json:
```json
{
    "body": "This is a great patch.   I can't believe this has got ignored for the last 1.5 years. \n\nRegarding what needs to be fixed, the test failure you claim for matrix_integer_2x2 is:\n\n```\n\ndeep:sage wstein$ sage -t matrix/matrix_integer_2x2.pyx\nsage -t  \"matrix/matrix_integer_2x2.pyx\"                    \n**********************************************************************\nFile \"/Users/wstein/sage/install/sage-4.7.1.rc0/devel/sage-main/sage/matrix/matrix_integer_2x2.pyx\", line 101:\n    sage: TestSuite(m).run()\nExpected nothing\nGot:\n    Failure in _test_minpoly:\n    Traceback (most recent call last):\n      File \"/Users/wstein/sage/install/current/local/lib/python/site-packages/sage/misc/sage_unittest.py\", line 275, in run\n        test_method(tester = tester)\n      File \"matrix2.pyx\", line 1302, in sage.matrix.matrix2.Matrix._test_minpoly (sage/matrix/matrix2.c:8933)\n      File \"polynomial_element.pyx\", line 358, in sage.rings.polynomial.polynomial_element.Polynomial.subs (sage/rings/polynomial/polynomial_element.c:5624)\n      File \"polynomial_element.pyx\", line 557, in sage.rings.polynomial.polynomial_element.Polynomial.__call__ (sage/rings/polynomial/polynomial_element.c:5819)\n      File \"polynomial_element.pyx\", line 638, in sage.rings.polynomial.polynomial_element.Polynomial.__call__ (sage/rings/polynomial/polynomial_element.c:7244)\n      File \"element.pyx\", line 1302, in sage.structure.element.RingElement.__add__ (sage/structure/element.c:11504)\n      File \"coerce.pyx\", line 766, in sage.structure.coerce.CoercionModel_cache_maps.bin_op (sage/structure/coerce.c:7337)\n    TypeError: unsupported operand parent(s) for '+': 'Space of 2x2 integer matrices' and 'Integer Ring'\n    ------------------------------------------------------------\n    The following tests failed: _test_minpoly\n**********************************************************************\n1 items had failures:\n   1 of   6 in __main__.example_7\n***Test Failed*** 1 failures.\nFor whitespace errors, see the file /Users/wstein/.sage//tmp/.doctest_matrix_integer_2x2.py\n\t [4.6 s]\n```\n\n\nThis is because substitution isn't even implemented for that class:\n\n```\nsage: MS = sage.matrix.matrix_integer_2x2.MatrixSpace_ZZ_2x2()\nsage: a = MS([1,2,3,4])\nsage: a.minpoly()\nx^2 - 5*x - 2\nsage: a.minpoly()(a)\n---------------------------------------------------------------------------\nTypeError     \n```\n\n\nAlso, if one adds this for minpoly, it would make sense to also add _test_charpoly.\n\n -- William",
    "created_at": "2011-07-17T13:36:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7989",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7989#issuecomment-69657",
    "user": "https://github.com/williamstein"
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

archive/issue_comments_069658.json:
```json
{
    "body": "OK. Works for me, too. Is it favored that we include a test that purposely fails?",
    "created_at": "2011-07-17T18:11:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7989",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7989#issuecomment-69658",
    "user": "https://github.com/hedtke"
}
```

OK. Works for me, too. Is it favored that we include a test that purposely fails?



---

archive/issue_comments_069659.json:
```json
{
    "body": "Replying to [comment:7 hedtke]:\n> OK. Works for me, too. Is it favored that we include a test that purposely fails?\n\nI think the idea is to include the test-suite checking **and** add the fixes needed to make the tests pass.",
    "created_at": "2011-07-17T18:31:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7989",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7989#issuecomment-69659",
    "user": "https://github.com/rbeezer"
}
```

Replying to [comment:7 hedtke]:
> OK. Works for me, too. Is it favored that we include a test that purposely fails?

I think the idea is to include the test-suite checking **and** add the fixes needed to make the tests pass.



---

archive/issue_events_019123.json:
```json
{
    "actor": "https://github.com/jdemeyer",
    "created_at": "2013-08-13T15:35:53Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/7989",
    "milestone": "sage-5.12",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/7989#event-19123"
}
```



---

archive/issue_events_019124.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-01-30T21:20:52Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/7989",
    "milestone": "sage-5.12",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/7989#event-19124"
}
```



---

archive/issue_events_019125.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-01-30T21:20:52Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/7989",
    "milestone": "sage-6.2",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/7989#event-19125"
}
```



---

archive/issue_comments_069660.json:
```json
{
    "body": "sage-6.2.beta4:\n\n```\nsage -t src/sage/matrix/matrix_generic_dense.pyx  # 1 doctest failed\nsage -t src/sage/matrix/matrix_dense.pyx  # 1 doctest failed\n```\n",
    "created_at": "2014-03-15T15:08:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7989",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7989#issuecomment-69660",
    "user": "https://github.com/mezzarobba"
}
```

sage-6.2.beta4:

```
sage -t src/sage/matrix/matrix_generic_dense.pyx  # 1 doctest failed
sage -t src/sage/matrix/matrix_dense.pyx  # 1 doctest failed
```




---

archive/issue_events_019126.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-05-06T15:20:58Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/7989",
    "milestone": "sage-6.2",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/7989#event-19126"
}
```



---

archive/issue_events_019127.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-05-06T15:20:58Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/7989",
    "milestone": "sage-6.3",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/7989#event-19127"
}
```



---

archive/issue_events_019128.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-08-10T16:51:03Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/7989",
    "milestone": "sage-6.3",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/7989#event-19128"
}
```



---

archive/issue_events_019129.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-08-10T16:51:03Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/7989",
    "milestone": "sage-6.4",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/7989#event-19129"
}
```



---

archive/issue_comments_069661.json:
```json
{
    "body": "New commits:",
    "created_at": "2022-05-19T09:24:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7989",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7989#issuecomment-69661",
    "user": "https://github.com/fchapoton"
}
```

New commits:



---

archive/issue_comments_069662.json:
```json
{
    "body": "Branch pushed to git repo; I updated commit sha1. New commits:",
    "created_at": "2022-05-19T14:19:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7989",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7989#issuecomment-69662",
    "user": "https://trac.sagemath.org/admin/accounts/users/git"
}
```

Branch pushed to git repo; I updated commit sha1. New commits:



---

archive/issue_comments_069663.json:
```json
{
    "body": "Branch pushed to git repo; I updated commit sha1. New commits:",
    "created_at": "2022-05-19T14:40:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7989",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7989#issuecomment-69663",
    "user": "https://trac.sagemath.org/admin/accounts/users/git"
}
```

Branch pushed to git repo; I updated commit sha1. New commits:



---

archive/issue_comments_069664.json:
```json
{
    "body": "Branch pushed to git repo; I updated commit sha1. New commits:",
    "created_at": "2022-05-19T17:10:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7989",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7989#issuecomment-69664",
    "user": "https://trac.sagemath.org/admin/accounts/users/git"
}
```

Branch pushed to git repo; I updated commit sha1. New commits:



---

archive/issue_comments_069665.json:
```json
{
    "body": "Branch pushed to git repo; I updated commit sha1. New commits:",
    "created_at": "2022-05-20T11:38:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7989",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7989#issuecomment-69665",
    "user": "https://trac.sagemath.org/admin/accounts/users/git"
}
```

Branch pushed to git repo; I updated commit sha1. New commits:



---

archive/issue_events_019130.json:
```json
{
    "actor": "https://github.com/fchapoton",
    "created_at": "2022-05-20T11:59:42Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/7989",
    "milestone": "sage-6.4",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/7989#event-19130"
}
```



---

archive/issue_events_019131.json:
```json
{
    "actor": "https://github.com/fchapoton",
    "created_at": "2022-05-20T11:59:42Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/7989",
    "milestone": "sage-9.7",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/7989#event-19131"
}
```



---

archive/issue_comments_069666.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2022-05-20T11:59:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7989",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7989#issuecomment-69666",
    "user": "https://github.com/fchapoton"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_069667.json:
```json
{
    "body": "green patchbot, so please review",
    "created_at": "2022-05-21T11:44:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7989",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7989#issuecomment-69667",
    "user": "https://github.com/fchapoton"
}
```

green patchbot, so please review



---

archive/issue_comments_069668.json:
```json
{
    "body": "LGTM.",
    "created_at": "2022-05-23T02:47:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7989",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7989#issuecomment-69668",
    "user": "https://github.com/tscrim"
}
```

LGTM.



---

archive/issue_comments_069669.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2022-05-23T02:47:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7989",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7989#issuecomment-69669",
    "user": "https://github.com/tscrim"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_events_019132.json:
```json
{
    "actor": "https://github.com/vbraun",
    "created_at": "2022-05-26T22:49:44Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/7989",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/7989#event-19132"
}
```



---

archive/issue_comments_069670.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2022-05-26T22:49:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7989",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7989#issuecomment-69670",
    "user": "https://github.com/vbraun"
}
```

Resolution: fixed

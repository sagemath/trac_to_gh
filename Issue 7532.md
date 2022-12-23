# Issue 7532: "return NotImplementedError" in ring.pyx

archive/issues_007532.json:
```json
{
    "body": "Assignee: AlexGhitza\n\n\n```\nOn Wed, Nov 25, 2009 at 7:26 PM, John H Palmieri <jhpalmieri64@gmail.com> wrote:\n> In ring.pyx, there is code like this:\n>\n>        if proof:\n>            return NotImplementedError\n>        else:\n>            return False\n>\n> I would think that the second line should say \"raise\n> NotImplementedError\".  (Changing it makes some doctests fail,\n> though.)  Is there a good reason for doing \"return\n> NotImplementedError\"?\n\nThat's *definitely* a bug.   No question about it. \n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/7532\n\n",
    "created_at": "2009-11-26T05:37:36Z",
    "labels": [
        "algebra",
        "major",
        "bug"
    ],
    "title": "\"return NotImplementedError\" in ring.pyx",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/7532",
    "user": "was"
}
```
Assignee: AlexGhitza


```
On Wed, Nov 25, 2009 at 7:26 PM, John H Palmieri <jhpalmieri64@gmail.com> wrote:
> In ring.pyx, there is code like this:
>
>        if proof:
>            return NotImplementedError
>        else:
>            return False
>
> I would think that the second line should say "raise
> NotImplementedError".  (Changing it makes some doctests fail,
> though.)  Is there a good reason for doing "return
> NotImplementedError"?

That's *definitely* a bug.   No question about it. 
```


Issue created by migration from https://trac.sagemath.org/ticket/7532





---

archive/issue_comments_063848.json:
```json
{
    "body": "grep gives:\n\n* ./symbolic/expression.pyx:        return NotImplementedError\n* ./symbolic/expression_conversions.py:            return NotImplementedError(\"SymPy function '%s' doesn't exist\" % f)\n* ./rings/ring.pyx:            return NotImplementedError\n* ./modular/arithgroup/congroup_gammaH.py:            return NotImplementedError\n* ./geometry/polyhedra.py:            return NotImplementedError",
    "created_at": "2009-11-26T09:07:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7532",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7532#issuecomment-63848",
    "user": "ylchapuy"
}
```

grep gives:

* ./symbolic/expression.pyx:        return NotImplementedError
* ./symbolic/expression_conversions.py:            return NotImplementedError("SymPy function '%s' doesn't exist" % f)
* ./rings/ring.pyx:            return NotImplementedError
* ./modular/arithgroup/congroup_gammaH.py:            return NotImplementedError
* ./geometry/polyhedra.py:            return NotImplementedError



---

archive/issue_comments_063849.json:
```json
{
    "body": "and allowing other error types we get:\n\n* ./interfaces/gap.py:            return RuntimeError, \"Error evaluating %s in %s\"%(line, self)\n* ./modular/abvar/finite_subgroup.py:            return ValueError, \"self and other must be in the same ambient Jacobian\"\n* ./groups/perm_gps/permgroup_named.py:            return ValueError, \"Degree must be 2.\"\n* ./groups/perm_gps/permgroup_named.py:            return ValueError, \"Degree must be 2.\"",
    "created_at": "2009-11-26T09:14:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7532",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7532#issuecomment-63849",
    "user": "ylchapuy"
}
```

and allowing other error types we get:

* ./interfaces/gap.py:            return RuntimeError, "Error evaluating %s in %s"%(line, self)
* ./modular/abvar/finite_subgroup.py:            return ValueError, "self and other must be in the same ambient Jacobian"
* ./groups/perm_gps/permgroup_named.py:            return ValueError, "Degree must be 2."
* ./groups/perm_gps/permgroup_named.py:            return ValueError, "Degree must be 2."



---

archive/issue_comments_063850.json:
```json
{
    "body": "and also (my grep has a strange behavior..?):\n\n *./structure/element.pyx:            return ArithmeticError, \"Multiplicative order of 0 not defined.\"\n *./rings/finite_field_givaro.pyx:                return ArithmeticError, \"Multiplicative order of 0 not defined.\"",
    "created_at": "2009-11-26T09:29:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7532",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7532#issuecomment-63850",
    "user": "ylchapuy"
}
```

and also (my grep has a strange behavior..?):

 *./structure/element.pyx:            return ArithmeticError, "Multiplicative order of 0 not defined."
 *./rings/finite_field_givaro.pyx:                return ArithmeticError, "Multiplicative order of 0 not defined."



---

archive/issue_comments_063851.json:
```json
{
    "body": "See also #7535.",
    "created_at": "2009-11-26T15:45:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7532",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7532#issuecomment-63851",
    "user": "jhpalmieri"
}
```

See also #7535.



---

archive/issue_comments_063852.json:
```json
{
    "body": "Given the patches at #7535, the one remaining case of this is the one in ring.pyx.  If I make the change from\n\n```\nreturn NotImplementedError\n```\n\nto\n\n```\nraise NotImplementedError\n```\n\nthere, I get doctest failures in the files\n\n```\n\tsage -t -long \"devel/sage/sage/schemes/elliptic_curves/monsky_washnitzer.py\"\n\tsage -t -long \"devel/sage/sage/schemes/elliptic_curves/padics.py\"\n\tsage -t -long \"devel/sage/sage/schemes/elliptic_curves/sha_tate.py\"\n```\n\nand maybe some others in this directory.",
    "created_at": "2010-01-19T00:50:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7532",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7532#issuecomment-63852",
    "user": "jhpalmieri"
}
```

Given the patches at #7535, the one remaining case of this is the one in ring.pyx.  If I make the change from

```
return NotImplementedError
```

to

```
raise NotImplementedError
```

there, I get doctest failures in the files

```
	sage -t -long "devel/sage/sage/schemes/elliptic_curves/monsky_washnitzer.py"
	sage -t -long "devel/sage/sage/schemes/elliptic_curves/padics.py"
	sage -t -long "devel/sage/sage/schemes/elliptic_curves/sha_tate.py"
```

and maybe some others in this directory.



---

archive/issue_comments_063853.json:
```json
{
    "body": "Changing assignee from AlexGhitza to cremona.",
    "created_at": "2010-01-19T00:50:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7532",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7532#issuecomment-63853",
    "user": "jhpalmieri"
}
```

Changing assignee from AlexGhitza to cremona.



---

archive/issue_comments_063854.json:
```json
{
    "body": "Changing component from algebra to elliptic curves.",
    "created_at": "2010-01-19T00:50:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7532",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7532#issuecomment-63854",
    "user": "jhpalmieri"
}
```

Changing component from algebra to elliptic curves.



---

archive/issue_comments_063855.json:
```json
{
    "body": "On my 64-bit ubuntu build of 4.3.1.rc0 with #7535 patches applied, I only get failures in ell_rational_field.py  I'll fix that and try again on a 32-bit machine.",
    "created_at": "2010-01-19T09:55:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7532",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7532#issuecomment-63855",
    "user": "cremona"
}
```

On my 64-bit ubuntu build of 4.3.1.rc0 with #7535 patches applied, I only get failures in ell_rational_field.py  I'll fix that and try again on a 32-bit machine.



---

archive/issue_comments_063856.json:
```json
{
    "body": "Apply after the patches at #7535 on 4.3.1.rc0",
    "created_at": "2010-01-19T12:43:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7532",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7532#issuecomment-63856",
    "user": "cremona"
}
```

Apply after the patches at #7535 on 4.3.1.rc0



---

archive/issue_comments_063857.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-01-19T12:45:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7532",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7532#issuecomment-63857",
    "user": "cremona"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_063858.json:
```json
{
    "body": "Attachment\n\nThe attached patch fixes an error in ell_rational_field.py which is the only one I see in that directory after applying the patches at #7535,\n\nJohn (jhpalmieri), can you post the details of the errors you had on the other 3 files in that directory?",
    "created_at": "2010-01-19T12:45:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7532",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7532#issuecomment-63858",
    "user": "cremona"
}
```

Attachment

The attached patch fixes an error in ell_rational_field.py which is the only one I see in that directory after applying the patches at #7535,

John (jhpalmieri), can you post the details of the errors you had on the other 3 files in that directory?



---

archive/issue_comments_063859.json:
```json
{
    "body": "Hi John,\n\nI think your patch really belongs on #7535, not here, since it fixes a doctest which was broken by the patches there.  My comment was, if I make another change, this time to ring.pyx (see the new patch), then I get the following doctest failures:\n\n```\n$ sage -t -long /Applications/sage/devel/sage/sage/schemes/elliptic_curves/monsky_washnitzer.py \nsage -t -long \"devel/sage/sage/schemes/elliptic_curves/monsky_washnitzer.py\"\n**********************************************************************\nFile \"/Applications/sage/devel/sage/sage/schemes/elliptic_curves/monsky_washnitzer.py\", line 1549:\n    sage: A = monsky_washnitzer.matrix_of_frobenius(Q, p, M)    # long time\nException raised:\n    Traceback (most recent call last):\n      File \"/Applications/sage/local/bin/ncadoctest.py\", line 1231, in run_one_test\n        self.run_one_example(test, example, filename, compileflags)\n      File \"/Applications/sage/local/bin/sagedoctest.py\", line 38, in run_one_example\n        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)\n      File \"/Applications/sage/local/bin/ncadoctest.py\", line 1172, in run_one_example\n        compileflags, 1) in test.globs\n      File \"<doctest __main__.example_32[66]>\", line 1, in <module>\n        A = monsky_washnitzer.matrix_of_frobenius(Q, p, M)    # long time###line 1549:\n    sage: A = monsky_washnitzer.matrix_of_frobenius(Q, p, M)    # long time\n      File \"/Applications/sage/local/lib/python/site-packages/sage/schemes/elliptic_curves/monsky_washnitzer.py\", line 1606, in matrix_of_frobenius\n        F0_reduced = reduce_all(Q, p, F0_coeffs, offset)\n      File \"/Applications/sage/local/lib/python/site-packages/sage/schemes/elliptic_curves/monsky_washnitzer.py\", line 1023, in reduce_all\n        exact_form = reduce_negative(Q, p, coeffs, offset, exact_form)\n      File \"/Applications/sage/local/lib/python/site-packages/sage/schemes/elliptic_curves/monsky_washnitzer.py\", line 757, in reduce_negative\n        m = helper_matrix(Q).list()\n      File \"/Applications/sage/local/lib/python/site-packages/sage/schemes/elliptic_curves/monsky_washnitzer.py\", line 689, in helper_matrix\n        return (1/D) * matrix(Q.base_ring(), 3, 3,\n      File \"element.pyx\", line 1326, in sage.structure.element.RingElement.__div__ (sage/structure/element.c:10897)\n      File \"coerce.pyx\", line 707, in sage.structure.coerce.CoercionModel_cache_maps.bin_op (sage/structure/coerce.c:6073)\n      File \"coerce.pyx\", line 1178, in sage.structure.coerce.CoercionModel_cache_maps.get_action (sage/structure/coerce.c:10911)\n      File \"coerce.pyx\", line 1309, in sage.structure.coerce.CoercionModel_cache_maps.discover_action (sage/structure/coerce.c:12070)\n      File \"coerce.pyx\", line 1346, in sage.structure.coerce.CoercionModel_cache_maps.discover_action (sage/structure/coerce.c:12620)\n      File \"ring.pyx\", line 933, in sage.rings.ring.CommutativeRing._pseudo_fraction_field (sage/rings/ring.c:6321)\n      File \"ring.pyx\", line 900, in sage.rings.ring.CommutativeRing.fraction_field (sage/rings/ring.c:6164)\n      File \"ring.pyx\", line 695, in sage.rings.ring.Ring.is_integral_domain (sage/rings/ring.c:5074)\n    NotImplementedError\n**********************************************************************\nFile \"/Applications/sage/devel/sage/sage/schemes/elliptic_curves/monsky_washnitzer.py\", line 1551:\n    sage: B                                                     # long time\nExpected:\n    [1144 + 264*t + 841*t^2 + 1025*t^3 + O(t^4)  176 + 1052*t + 216*t^2 + 523*t^3 + O(t^4)]\n    [   847 + 668*t + 81*t^2 + 424*t^3 + O(t^4)   185 + 341*t + 171*t^2 + 642*t^3 + O(t^4)]\nGot:\n    [ 514  927]\n    [ 702 1036]\n**********************************************************************\nFile \"/Applications/sage/devel/sage/sage/schemes/elliptic_curves/monsky_washnitzer.py\", line 1562:\n    sage: B.det()                                               # long time\nExpected:\n    11 + 484*t^2 + 451*t^3 + O(t^4)\nGot:\n    209\n**********************************************************************\n1 items had failures:\n   3 of  70 in __main__.example_32\n***Test Failed*** 3 failures.\nFor whitespace errors, see the file /Users/palmieri/.sage//tmp/.doctest_monsky_washnitzer.py\n\t [20.6 s]\nexit code: 1024\n```\n\nand\n\n```\nsage -t -long \"devel/sage/sage/schemes/elliptic_curves/padics.py\"\n**********************************************************************\nFile \"/Applications/sage/devel/sage/sage/schemes/elliptic_curves/padics.py\", line 197:\n    sage: E.padic_regulator(5, 10)\nException raised:\n    Traceback (most recent call last):\n      File \"/Applications/sage/local/bin/ncadoctest.py\", line 1231, in run_one_test\n        self.run_one_example(test, example, filename, compileflags)\n      File \"/Applications/sage/local/bin/sagedoctest.py\", line 38, in run_one_example\n        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)\n      File \"/Applications/sage/local/bin/ncadoctest.py\", line 1172, in run_one_example\n        compileflags, 1) in test.globs\n      File \"<doctest __main__.example_2[3]>\", line 1, in <module>\n        E.padic_regulator(Integer(5), Integer(10))###line 197:\n    sage: E.padic_regulator(5, 10)\n      File \"/Applications/sage/local/lib/python/site-packages/sage/schemes/elliptic_curves/padics.py\", line 253, in padic_regulator\n        height = self.padic_height(p, prec, check_hypotheses=False)\n      File \"/Applications/sage/local/lib/python/site-packages/sage/schemes/elliptic_curves/padics.py\", line 659, in padic_height\n        sigma = self.padic_sigma(p, adjusted_prec, check_hypotheses=False)\n      File \"/Applications/sage/local/lib/python/site-packages/sage/schemes/elliptic_curves/padics.py\", line 1009, in padic_sigma\n        f = X.formal_group().differential(N+2)   # f = 1 + ... + O(t^{N+2})\n      File \"/Applications/sage/local/lib/python/site-packages/sage/schemes/elliptic_curves/formal_group.py\", line 360, in differential\n        x = self.x(prec+1)\n      File \"/Applications/sage/local/lib/python/site-packages/sage/schemes/elliptic_curves/formal_group.py\", line 253, in x\n        y = self.y(prec)\n      File \"/Applications/sage/local/lib/python/site-packages/sage/schemes/elliptic_curves/formal_group.py\", line 303, in y\n        y = -1/w + O(t**prec)\n      File \"element.pyx\", line 1326, in sage.structure.element.RingElement.__div__ (sage/structure/element.c:10897)\n      File \"coerce.pyx\", line 707, in sage.structure.coerce.CoercionModel_cache_maps.bin_op (sage/structure/coerce.c:6073)\n      File \"coerce.pyx\", line 1178, in sage.structure.coerce.CoercionModel_cache_maps.get_action (sage/structure/coerce.c:10911)\n      File \"coerce.pyx\", line 1309, in sage.structure.coerce.CoercionModel_cache_maps.discover_action (sage/structure/coerce.c:12070)\n      File \"coerce.pyx\", line 1346, in sage.structure.coerce.CoercionModel_cache_maps.discover_action (sage/structure/coerce.c:12620)\n      File \"ring.pyx\", line 933, in sage.rings.ring.CommutativeRing._pseudo_fraction_field (sage/rings/ring.c:6321)\n      File \"ring.pyx\", line 900, in sage.rings.ring.CommutativeRing.fraction_field (sage/rings/ring.c:6164)\n      File \"ring.pyx\", line 695, in sage.rings.ring.Ring.is_integral_domain (sage/rings/ring.c:5074)\n    NotImplementedError\n**********************************************************************\n```\n\nplus 45 more failures in padics.py (too many to include here), and I expect failures in sha-tate.py -- currently in the middle of testing and I have to go teach, so I can't wait for it to finish.",
    "created_at": "2010-01-19T18:23:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7532",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7532#issuecomment-63859",
    "user": "jhpalmieri"
}
```

Hi John,

I think your patch really belongs on #7535, not here, since it fixes a doctest which was broken by the patches there.  My comment was, if I make another change, this time to ring.pyx (see the new patch), then I get the following doctest failures:

```
$ sage -t -long /Applications/sage/devel/sage/sage/schemes/elliptic_curves/monsky_washnitzer.py 
sage -t -long "devel/sage/sage/schemes/elliptic_curves/monsky_washnitzer.py"
**********************************************************************
File "/Applications/sage/devel/sage/sage/schemes/elliptic_curves/monsky_washnitzer.py", line 1549:
    sage: A = monsky_washnitzer.matrix_of_frobenius(Q, p, M)    # long time
Exception raised:
    Traceback (most recent call last):
      File "/Applications/sage/local/bin/ncadoctest.py", line 1231, in run_one_test
        self.run_one_example(test, example, filename, compileflags)
      File "/Applications/sage/local/bin/sagedoctest.py", line 38, in run_one_example
        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)
      File "/Applications/sage/local/bin/ncadoctest.py", line 1172, in run_one_example
        compileflags, 1) in test.globs
      File "<doctest __main__.example_32[66]>", line 1, in <module>
        A = monsky_washnitzer.matrix_of_frobenius(Q, p, M)    # long time###line 1549:
    sage: A = monsky_washnitzer.matrix_of_frobenius(Q, p, M)    # long time
      File "/Applications/sage/local/lib/python/site-packages/sage/schemes/elliptic_curves/monsky_washnitzer.py", line 1606, in matrix_of_frobenius
        F0_reduced = reduce_all(Q, p, F0_coeffs, offset)
      File "/Applications/sage/local/lib/python/site-packages/sage/schemes/elliptic_curves/monsky_washnitzer.py", line 1023, in reduce_all
        exact_form = reduce_negative(Q, p, coeffs, offset, exact_form)
      File "/Applications/sage/local/lib/python/site-packages/sage/schemes/elliptic_curves/monsky_washnitzer.py", line 757, in reduce_negative
        m = helper_matrix(Q).list()
      File "/Applications/sage/local/lib/python/site-packages/sage/schemes/elliptic_curves/monsky_washnitzer.py", line 689, in helper_matrix
        return (1/D) * matrix(Q.base_ring(), 3, 3,
      File "element.pyx", line 1326, in sage.structure.element.RingElement.__div__ (sage/structure/element.c:10897)
      File "coerce.pyx", line 707, in sage.structure.coerce.CoercionModel_cache_maps.bin_op (sage/structure/coerce.c:6073)
      File "coerce.pyx", line 1178, in sage.structure.coerce.CoercionModel_cache_maps.get_action (sage/structure/coerce.c:10911)
      File "coerce.pyx", line 1309, in sage.structure.coerce.CoercionModel_cache_maps.discover_action (sage/structure/coerce.c:12070)
      File "coerce.pyx", line 1346, in sage.structure.coerce.CoercionModel_cache_maps.discover_action (sage/structure/coerce.c:12620)
      File "ring.pyx", line 933, in sage.rings.ring.CommutativeRing._pseudo_fraction_field (sage/rings/ring.c:6321)
      File "ring.pyx", line 900, in sage.rings.ring.CommutativeRing.fraction_field (sage/rings/ring.c:6164)
      File "ring.pyx", line 695, in sage.rings.ring.Ring.is_integral_domain (sage/rings/ring.c:5074)
    NotImplementedError
**********************************************************************
File "/Applications/sage/devel/sage/sage/schemes/elliptic_curves/monsky_washnitzer.py", line 1551:
    sage: B                                                     # long time
Expected:
    [1144 + 264*t + 841*t^2 + 1025*t^3 + O(t^4)  176 + 1052*t + 216*t^2 + 523*t^3 + O(t^4)]
    [   847 + 668*t + 81*t^2 + 424*t^3 + O(t^4)   185 + 341*t + 171*t^2 + 642*t^3 + O(t^4)]
Got:
    [ 514  927]
    [ 702 1036]
**********************************************************************
File "/Applications/sage/devel/sage/sage/schemes/elliptic_curves/monsky_washnitzer.py", line 1562:
    sage: B.det()                                               # long time
Expected:
    11 + 484*t^2 + 451*t^3 + O(t^4)
Got:
    209
**********************************************************************
1 items had failures:
   3 of  70 in __main__.example_32
***Test Failed*** 3 failures.
For whitespace errors, see the file /Users/palmieri/.sage//tmp/.doctest_monsky_washnitzer.py
	 [20.6 s]
exit code: 1024
```

and

```
sage -t -long "devel/sage/sage/schemes/elliptic_curves/padics.py"
**********************************************************************
File "/Applications/sage/devel/sage/sage/schemes/elliptic_curves/padics.py", line 197:
    sage: E.padic_regulator(5, 10)
Exception raised:
    Traceback (most recent call last):
      File "/Applications/sage/local/bin/ncadoctest.py", line 1231, in run_one_test
        self.run_one_example(test, example, filename, compileflags)
      File "/Applications/sage/local/bin/sagedoctest.py", line 38, in run_one_example
        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)
      File "/Applications/sage/local/bin/ncadoctest.py", line 1172, in run_one_example
        compileflags, 1) in test.globs
      File "<doctest __main__.example_2[3]>", line 1, in <module>
        E.padic_regulator(Integer(5), Integer(10))###line 197:
    sage: E.padic_regulator(5, 10)
      File "/Applications/sage/local/lib/python/site-packages/sage/schemes/elliptic_curves/padics.py", line 253, in padic_regulator
        height = self.padic_height(p, prec, check_hypotheses=False)
      File "/Applications/sage/local/lib/python/site-packages/sage/schemes/elliptic_curves/padics.py", line 659, in padic_height
        sigma = self.padic_sigma(p, adjusted_prec, check_hypotheses=False)
      File "/Applications/sage/local/lib/python/site-packages/sage/schemes/elliptic_curves/padics.py", line 1009, in padic_sigma
        f = X.formal_group().differential(N+2)   # f = 1 + ... + O(t^{N+2})
      File "/Applications/sage/local/lib/python/site-packages/sage/schemes/elliptic_curves/formal_group.py", line 360, in differential
        x = self.x(prec+1)
      File "/Applications/sage/local/lib/python/site-packages/sage/schemes/elliptic_curves/formal_group.py", line 253, in x
        y = self.y(prec)
      File "/Applications/sage/local/lib/python/site-packages/sage/schemes/elliptic_curves/formal_group.py", line 303, in y
        y = -1/w + O(t**prec)
      File "element.pyx", line 1326, in sage.structure.element.RingElement.__div__ (sage/structure/element.c:10897)
      File "coerce.pyx", line 707, in sage.structure.coerce.CoercionModel_cache_maps.bin_op (sage/structure/coerce.c:6073)
      File "coerce.pyx", line 1178, in sage.structure.coerce.CoercionModel_cache_maps.get_action (sage/structure/coerce.c:10911)
      File "coerce.pyx", line 1309, in sage.structure.coerce.CoercionModel_cache_maps.discover_action (sage/structure/coerce.c:12070)
      File "coerce.pyx", line 1346, in sage.structure.coerce.CoercionModel_cache_maps.discover_action (sage/structure/coerce.c:12620)
      File "ring.pyx", line 933, in sage.rings.ring.CommutativeRing._pseudo_fraction_field (sage/rings/ring.c:6321)
      File "ring.pyx", line 900, in sage.rings.ring.CommutativeRing.fraction_field (sage/rings/ring.c:6164)
      File "ring.pyx", line 695, in sage.rings.ring.Ring.is_integral_domain (sage/rings/ring.c:5074)
    NotImplementedError
**********************************************************************
```

plus 45 more failures in padics.py (too many to include here), and I expect failures in sha-tate.py -- currently in the middle of testing and I have to go teach, so I can't wait for it to finish.



---

archive/issue_comments_063860.json:
```json
{
    "body": "Attachment\n\nfor purposes of illustration only -- causes doctest failures in schemes/elliptic_curves",
    "created_at": "2010-01-19T18:24:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7532",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7532#issuecomment-63860",
    "user": "jhpalmieri"
}
```

Attachment

for purposes of illustration only -- causes doctest failures in schemes/elliptic_curves



---

archive/issue_comments_063861.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2010-01-19T20:18:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7532",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7532#issuecomment-63861",
    "user": "cremona"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_063862.json:
```json
{
    "body": "OK, I'll move my patch from here to #7535.  I'll also take a look at those other files to see if I can work out what is going on.",
    "created_at": "2010-01-19T20:18:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7532",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7532#issuecomment-63862",
    "user": "cremona"
}
```

OK, I'll move my patch from here to #7535.  I'll also take a look at those other files to see if I can work out what is going on.



---

archive/issue_comments_063863.json:
```json
{
    "body": "Positive review: see comment:7:ticket:7535",
    "created_at": "2010-01-20T09:41:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7532",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7532#issuecomment-63863",
    "user": "timdumol"
}
```

Positive review: see comment:7:ticket:7535



---

archive/issue_comments_063864.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-01-20T09:41:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7532",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7532#issuecomment-63864",
    "user": "timdumol"
}
```

Resolution: fixed



---

archive/issue_comments_063865.json:
```json
{
    "body": "Changing status from closed to needs_work.",
    "created_at": "2010-01-20T09:41:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7532",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7532#issuecomment-63865",
    "user": "timdumol"
}
```

Changing status from closed to needs_work.



---

archive/issue_comments_063866.json:
```json
{
    "body": "That should have been positive review. Sorry about that.",
    "created_at": "2010-01-20T09:41:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7532",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7532#issuecomment-63866",
    "user": "timdumol"
}
```

That should have been positive review. Sorry about that.



---

archive/issue_comments_063867.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2010-01-20T09:41:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7532",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7532#issuecomment-63867",
    "user": "timdumol"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_063868.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-01-20T09:42:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7532",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7532#issuecomment-63868",
    "user": "timdumol"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_063869.json:
```json
{
    "body": "I have got to the bottom of (at least) the problem with monsky_washnitser.py.  A quantity D is computed which is in `(Z/NZ)[This is the Trac macro *t* that was inherited from the migration](https://trac.sagemath.org/wiki/WikiMacros#t-macro)` and non-zero, where N is a prime power not a prime.  At some point in the code we need 1/D.  This crashes (while `D^(-1)` is OK).  IN the inversion, soemone asks if the parent of D is an integral domain which cannot be determined, which raises a run-time error.  Before the patch it *returned* the error, and as it was returning something nonzero that was interpreted by python as \"True\".\n\nI think I can fix this, but I am still working on it.  It will need a new patch -- sorry to have muddled matters by putting onto this ticket a patch which belonged to #7535.",
    "created_at": "2010-01-20T10:26:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7532",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7532#issuecomment-63869",
    "user": "cremona"
}
```

I have got to the bottom of (at least) the problem with monsky_washnitser.py.  A quantity D is computed which is in `(Z/NZ)[This is the Trac macro *t* that was inherited from the migration](https://trac.sagemath.org/wiki/WikiMacros#t-macro)` and non-zero, where N is a prime power not a prime.  At some point in the code we need 1/D.  This crashes (while `D^(-1)` is OK).  IN the inversion, soemone asks if the parent of D is an integral domain which cannot be determined, which raises a run-time error.  Before the patch it *returned* the error, and as it was returning something nonzero that was interpreted by python as "True".

I think I can fix this, but I am still working on it.  It will need a new patch -- sorry to have muddled matters by putting onto this ticket a patch which belonged to #7535.



---

archive/issue_comments_063870.json:
```json
{
    "body": "Apply instead of previous one to 4.3.1.rc0 (rings.pyx fix)",
    "created_at": "2010-01-20T13:08:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7532",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7532#issuecomment-63870",
    "user": "cremona"
}
```

Apply instead of previous one to 4.3.1.rc0 (rings.pyx fix)



---

archive/issue_comments_063871.json:
```json
{
    "body": "Attachment\n\nThe patch trac_7532-rings.patch  fixes the problem in rings.pyx and all the fallout -- I checked the entire library and it is fine.  The diagnosis was exactly as above, and only a few lines needed to be changed!\n\nI am switchingg this to \"needs work\" and then \"needs review\", hoping that it can get in on the back of #7535 (just this once!)",
    "created_at": "2010-01-20T13:10:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7532",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7532#issuecomment-63871",
    "user": "cremona"
}
```

Attachment

The patch trac_7532-rings.patch  fixes the problem in rings.pyx and all the fallout -- I checked the entire library and it is fine.  The diagnosis was exactly as above, and only a few lines needed to be changed!

I am switchingg this to "needs work" and then "needs review", hoping that it can get in on the back of #7535 (just this once!)



---

archive/issue_comments_063872.json:
```json
{
    "body": "Changing status from positive_review to needs_work.",
    "created_at": "2010-01-20T13:10:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7532",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7532#issuecomment-63872",
    "user": "cremona"
}
```

Changing status from positive_review to needs_work.



---

archive/issue_comments_063873.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2010-01-20T13:10:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7532",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7532#issuecomment-63873",
    "user": "cremona"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_063874.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-01-20T16:38:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7532",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7532#issuecomment-63874",
    "user": "jhpalmieri"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_063875.json:
```json
{
    "body": "Looks good, all tests pass.  Thanks for the fix, John.",
    "created_at": "2010-01-20T16:38:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7532",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7532#issuecomment-63875",
    "user": "jhpalmieri"
}
```

Looks good, all tests pass.  Thanks for the fix, John.



---

archive/issue_comments_063876.json:
```json
{
    "body": "Replying to [comment:18 jhpalmieri]:\n> Looks good, all tests pass.  Thanks for the fix, John.\n\nMy pleasure.  I hope the release manager can see that trac_7532.patch only needs to be applied once, not both here and at #7535!\n\nI only just discovered the joys of \"sage -pt n\" which makes testing the whole library a breeze: my research machine has 16 processors of which only a few are usually in use, so I put n=10 and a full test only takes 6 minutes and the -long test I did here took only 701s!",
    "created_at": "2010-01-20T17:01:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7532",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7532#issuecomment-63876",
    "user": "cremona"
}
```

Replying to [comment:18 jhpalmieri]:
> Looks good, all tests pass.  Thanks for the fix, John.

My pleasure.  I hope the release manager can see that trac_7532.patch only needs to be applied once, not both here and at #7535!

I only just discovered the joys of "sage -pt n" which makes testing the whole library a breeze: my research machine has 16 processors of which only a few are usually in use, so I put n=10 and a full test only takes 6 minutes and the -long test I did here took only 701s!



---

archive/issue_comments_063877.json:
```json
{
    "body": "First I applied patches at #7535 to Sage 4.3.1, then I applied [trac_7532-rings.patch](http://trac.sagemath.org/sage_trac/attachment/ticket/7532/trac_7532-rings.patch). Running doctest on the full Sage library results in the following failure:\n\n```\n[mvngu@sage sage-4.3.1]$ ./sage -t -long devel/sage-main/sage/schemes/elliptic_curves/ell_rational_field.py\nsage -t -long \"devel/sage-main/sage/schemes/elliptic_curves/ell_rational_field.py\"\n**********************************************************************\nFile \"/mnt/usb1/scratch/mvngu/release/sage-4.3.1/devel/sage-main/sage/schemes/elliptic_curves/ell_rational_field.py\", line 4027:\n    sage: E.isogenies_prime_degree(4)\nException raised:\n    Traceback (most recent call last):\n      File \"/mnt/usb1/scratch/mvngu/release/sage-4.3.1/local/bin/ncadoctest.py\", line 1231, in run_one_test\n        self.run_one_example(test, example, filename, compileflags)\n      File \"/mnt/usb1/scratch/mvngu/release/sage-4.3.1/local/bin/sagedoctest.py\", line 38, in run_one_example\n        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)\n      File \"/mnt/usb1/scratch/mvngu/release/sage-4.3.1/local/bin/ncadoctest.py\", line 1172, in run_one_example\n        compileflags, 1) in test.globs\n      File \"<doctest __main__.example_86[14]>\", line 1, in <module>\n        E.isogenies_prime_degree(Integer(4))###line 4027:\n    sage: E.isogenies_prime_degree(4)\n      File \"/mnt/usb1/scratch/mvngu/release/sage-4.3.1/local/lib/python/site-packages/sage/schemes/elliptic_curves/ell_rational_field.py\", line 4036, in isogenies_prime_degree\n        return isogenies_sporadic_Q(self, l)\n      File \"/mnt/usb1/scratch/mvngu/release/sage-4.3.1/local/lib/python/site-packages/sage/schemes/elliptic_curves/ell_curve_isogeny.py\", line 4004, in isogenies_sporadic_Q\n        raise ValueError(\"%s is not prime.\"%l)\n    ValueError: 4 is not prime.\n```\n\nDid I correctly apply the necessary patches? Does this ticket depend on #7535?",
    "created_at": "2010-01-23T17:45:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7532",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7532#issuecomment-63877",
    "user": "mvngu"
}
```

First I applied patches at #7535 to Sage 4.3.1, then I applied [trac_7532-rings.patch](http://trac.sagemath.org/sage_trac/attachment/ticket/7532/trac_7532-rings.patch). Running doctest on the full Sage library results in the following failure:

```
[mvngu@sage sage-4.3.1]$ ./sage -t -long devel/sage-main/sage/schemes/elliptic_curves/ell_rational_field.py
sage -t -long "devel/sage-main/sage/schemes/elliptic_curves/ell_rational_field.py"
**********************************************************************
File "/mnt/usb1/scratch/mvngu/release/sage-4.3.1/devel/sage-main/sage/schemes/elliptic_curves/ell_rational_field.py", line 4027:
    sage: E.isogenies_prime_degree(4)
Exception raised:
    Traceback (most recent call last):
      File "/mnt/usb1/scratch/mvngu/release/sage-4.3.1/local/bin/ncadoctest.py", line 1231, in run_one_test
        self.run_one_example(test, example, filename, compileflags)
      File "/mnt/usb1/scratch/mvngu/release/sage-4.3.1/local/bin/sagedoctest.py", line 38, in run_one_example
        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)
      File "/mnt/usb1/scratch/mvngu/release/sage-4.3.1/local/bin/ncadoctest.py", line 1172, in run_one_example
        compileflags, 1) in test.globs
      File "<doctest __main__.example_86[14]>", line 1, in <module>
        E.isogenies_prime_degree(Integer(4))###line 4027:
    sage: E.isogenies_prime_degree(4)
      File "/mnt/usb1/scratch/mvngu/release/sage-4.3.1/local/lib/python/site-packages/sage/schemes/elliptic_curves/ell_rational_field.py", line 4036, in isogenies_prime_degree
        return isogenies_sporadic_Q(self, l)
      File "/mnt/usb1/scratch/mvngu/release/sage-4.3.1/local/lib/python/site-packages/sage/schemes/elliptic_curves/ell_curve_isogeny.py", line 4004, in isogenies_sporadic_Q
        raise ValueError("%s is not prime."%l)
    ValueError: 4 is not prime.
```

Did I correctly apply the necessary patches? Does this ticket depend on #7535?



---

archive/issue_comments_063878.json:
```json
{
    "body": "Please apply trac_7532.patch as well.  Does that help?  (See the \"addendum\" in the ticket description.)",
    "created_at": "2010-01-23T18:30:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7532",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7532#issuecomment-63878",
    "user": "jhpalmieri"
}
```

Please apply trac_7532.patch as well.  Does that help?  (See the "addendum" in the ticket description.)



---

archive/issue_comments_063879.json:
```json
{
    "body": "Thank you for pointing out the addendum, jhpalmieri.  Merged in this order:\n\n1. patches at #7535\n2. [trac_7532.patch](http://trac.sagemath.org/sage_trac/attachment/ticket/7532/trac_7532.patch)\n3. [trac_7532-rings.patch](http://trac.sagemath.org/sage_trac/attachment/ticket/7532/trac_7532-rings.patch)",
    "created_at": "2010-01-23T20:03:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7532",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7532#issuecomment-63879",
    "user": "mvngu"
}
```

Thank you for pointing out the addendum, jhpalmieri.  Merged in this order:

1. patches at #7535
2. [trac_7532.patch](http://trac.sagemath.org/sage_trac/attachment/ticket/7532/trac_7532.patch)
3. [trac_7532-rings.patch](http://trac.sagemath.org/sage_trac/attachment/ticket/7532/trac_7532-rings.patch)

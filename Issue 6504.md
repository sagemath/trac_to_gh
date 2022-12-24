# Issue 6504: Add doctests to toy_buchberger to get it to 100%

archive/issues_006504.json:
```json
{
    "body": "Assignee: tbd\n\nKeywords: groebner basis, buchberger\n\nSome functions were missing doctests, I think I have corrected that.\n\nIssue created by migration from https://trac.sagemath.org/ticket/6504\n\n",
    "created_at": "2009-07-09T22:52:51Z",
    "labels": [
        "algebra",
        "minor",
        "enhancement"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.1.1",
    "title": "Add doctests to toy_buchberger to get it to 100%",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/6504",
    "user": "mhampton"
}
```
Assignee: tbd

Keywords: groebner basis, buchberger

Some functions were missing doctests, I think I have corrected that.

Issue created by migration from https://trac.sagemath.org/ticket/6504





---

archive/issue_comments_052983.json:
```json
{
    "body": "Attachment [trac_6504_toy_buch.patch](tarball://root/attachments/some-uuid/ticket6504/trac_6504_toy_buch.patch) by mhampton created at 2009-07-09 22:54:41\n\nPatches are the same, I just forgot to put the ticket number on the first one.",
    "created_at": "2009-07-09T22:54:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6504",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6504#issuecomment-52983",
    "user": "mhampton"
}
```

Attachment [trac_6504_toy_buch.patch](tarball://root/attachments/some-uuid/ticket6504/trac_6504_toy_buch.patch) by mhampton created at 2009-07-09 22:54:41

Patches are the same, I just forgot to put the ticket number on the first one.



---

archive/issue_comments_052984.json:
```json
{
    "body": "fixes a few whitespace issues in the original patch",
    "created_at": "2009-07-13T20:12:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6504",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6504#issuecomment-52984",
    "user": "@malb"
}
```

fixes a few whitespace issues in the original patch



---

archive/issue_comments_052985.json:
```json
{
    "body": "Attachment [trac_6504_toy_buch.2.patch](tarball://root/attachments/some-uuid/ticket6504/trac_6504_toy_buch.2.patch) by @malb created at 2009-07-13 20:14:13\n\nI read the patch and it looks fine, it applies cleanly and passes doctest. There were a few whitespace issues w.r.t. the reference manual, which are fixed in the attached patch (only apply this one). The update needs signing off by mhampton.",
    "created_at": "2009-07-13T20:14:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6504",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6504#issuecomment-52985",
    "user": "@malb"
}
```

Attachment [trac_6504_toy_buch.2.patch](tarball://root/attachments/some-uuid/ticket6504/trac_6504_toy_buch.2.patch) by @malb created at 2009-07-13 20:14:13

I read the patch and it looks fine, it applies cleanly and passes doctest. There were a few whitespace issues w.r.t. the reference manual, which are fixed in the attached patch (only apply this one). The update needs signing off by mhampton.



---

archive/issue_comments_052986.json:
```json
{
    "body": "Attachment [trac_6504_toy_buch.3.patch](tarball://root/attachments/some-uuid/ticket6504/trac_6504_toy_buch.3.patch) by mhampton created at 2009-07-14 03:53:19\n\nsupersedes previous versions; better ref manual formatting",
    "created_at": "2009-07-14T03:53:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6504",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6504#issuecomment-52986",
    "user": "mhampton"
}
```

Attachment [trac_6504_toy_buch.3.patch](tarball://root/attachments/some-uuid/ticket6504/trac_6504_toy_buch.3.patch) by mhampton created at 2009-07-14 03:53:19

supersedes previous versions; better ref manual formatting



---

archive/issue_comments_052987.json:
```json
{
    "body": "I switched spol from a lambda definition to a documented function, since it seems important enough in this module.  I also cleaned up a few things for the reference manual formatting (OUTPUT sections were in bold, for example, unintentionally).\n\nMartin Albrect (malb) should get both contributor and reviewer credit for this, I think.  But now that I have made a new version, I think it is appropriate that he reviews again (hopefully for a final time).",
    "created_at": "2009-07-14T03:56:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6504",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6504#issuecomment-52987",
    "user": "mhampton"
}
```

I switched spol from a lambda definition to a documented function, since it seems important enough in this module.  I also cleaned up a few things for the reference manual formatting (OUTPUT sections were in bold, for example, unintentionally).

Martin Albrect (malb) should get both contributor and reviewer credit for this, I think.  But now that I have made a new version, I think it is appropriate that he reviews again (hopefully for a final time).



---

archive/issue_comments_052988.json:
```json
{
    "body": "Apply only trac_6504_toy_buch.3.patch.",
    "created_at": "2009-07-14T09:26:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6504",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6504#issuecomment-52988",
    "user": "@malb"
}
```

Apply only trac_6504_toy_buch.3.patch.



---

archive/issue_comments_052989.json:
```json
{
    "body": "With the patch `trac_6504_toy_buch.3.patch`, I'm seeing some doctest failures:\n\n```\nsage -t -long devel/sage-exp/sage/rings/polynomial/multi_polynomial_ideal.py\n**********************************************************************\nFile \"/scratch/mvngu/release/sage-4.1.1.alpha0/devel/sage-exp/sage/rings/polynomial/multi_polynomial_ideal.py\", line 944:\n    sage: I.dimension()\nException raised:\n    Traceback (most recent call last):\n      File \"/scratch/mvngu/release/sage-4.1.1.alpha0/local/bin/ncadoctest.py\", line 1231, in run_one_test\n        self.run_one_example(test, example, filename, compileflags)\n      File \"/scratch/mvngu/release/sage-4.1.1.alpha0/local/bin/sagedoctest.py\", line 38, in run_one_example\n        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)\n      File \"/scratch/mvngu/release/sage-4.1.1.alpha0/local/bin/ncadoctest.py\", line 1172, in run_one_example\n        compileflags, 1) in test.globs\n      File \"<doctest __main__.example_19[9]>\", line 1, in <module>\n        I.dimension()###line 944:\n    sage: I.dimension()\n      File \"/scratch/mvngu/release/sage-4.1.1.alpha0/local/lib/python/site-packages/sage/rings/polynomial/multi_polynomial_ideal.py\", line 402, in __call__\n        return self.f(self._instance, *args, **kwds)\n      File \"/scratch/mvngu/release/sage-4.1.1.alpha0/local/lib/python/site-packages/sage/rings/polynomial/multi_polynomial_ideal.py\", line 978, in dimension\n        gb = toy_buchberger.buchberger_improved(self)\n      File \"/scratch/mvngu/release/sage-4.1.1.alpha0/local/lib/python/site-packages/sage/rings/polynomial/toy_buchberger.py\", line 279, in buchberger_improved\n        h = spol(g1,g2).reduce(G)\n      File \"/scratch/mvngu/release/sage-4.1.1.alpha0/local/lib/python/site-packages/sage/rings/polynomial/toy_buchberger.py\", line 175, in spol\n        return p(fg_lcm/LT(f)*f - fg_lcm/LT(g)*g)\n      File \"/scratch/mvngu/release/sage-4.1.1.alpha0/local/lib/python/site-packages/sage/rings/polynomial/multi_polynomial_ring.py\", line 422, in __call__\n        raise TypeError, \"unable to coerce since the denominator is not 1\"\n    TypeError: unable to coerce since the denominator is not 1\n**********************************************************************\nFile \"/scratch/mvngu/release/sage-4.1.1.alpha0/devel/sage-exp/sage/rings/polynomial/multi_polynomial_ideal.py\", line 948:\n    sage: I.dimension()\nException raised:\n    Traceback (most recent call last):\n      File \"/scratch/mvngu/release/sage-4.1.1.alpha0/local/bin/ncadoctest.py\", line 1231, in run_one_test\n        self.run_one_example(test, example, filename, compileflags)\n      File \"/scratch/mvngu/release/sage-4.1.1.alpha0/local/bin/sagedoctest.py\", line 38, in run_one_example\n        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)\n      File \"/scratch/mvngu/release/sage-4.1.1.alpha0/local/bin/ncadoctest.py\", line 1172, in run_one_example\n        compileflags, 1) in test.globs\n      File \"<doctest __main__.example_19[11]>\", line 1, in <module>\n        I.dimension()###line 948:\n    sage: I.dimension()\n      File \"/scratch/mvngu/release/sage-4.1.1.alpha0/local/lib/python/site-packages/sage/rings/polynomial/multi_polynomial_ideal.py\", line 402, in __call__\n        return self.f(self._instance, *args, **kwds)\n      File \"/scratch/mvngu/release/sage-4.1.1.alpha0/local/lib/python/site-packages/sage/rings/polynomial/multi_polynomial_ideal.py\", line 978, in dimension\n        gb = toy_buchberger.buchberger_improved(self)\n      File \"/scratch/mvngu/release/sage-4.1.1.alpha0/local/lib/python/site-packages/sage/rings/polynomial/toy_buchberger.py\", line 279, in buchberger_improved\n        h = spol(g1,g2).reduce(G)\n      File \"/scratch/mvngu/release/sage-4.1.1.alpha0/local/lib/python/site-packages/sage/rings/polynomial/toy_buchberger.py\", line 175, in spol\n        return p(fg_lcm/LT(f)*f - fg_lcm/LT(g)*g)\n      File \"/scratch/mvngu/release/sage-4.1.1.alpha0/local/lib/python/site-packages/sage/rings/polynomial/multi_polynomial_ring.py\", line 422, in __call__\n        raise TypeError, \"unable to coerce since the denominator is not 1\"\n    TypeError: unable to coerce since the denominator is not 1\n**********************************************************************\n1 items had failures:\n   2 of  15 in __main__.example_19\n***Test Failed*** 2 failures.\nFor whitespace errors, see the file /scratch/mvngu/release/sage-4.1.1.alpha0/tmp/.doctest_multi_polynomial_ideal.py\n\t [13.4 s]\n\n```\n",
    "created_at": "2009-07-19T00:19:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6504",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6504#issuecomment-52989",
    "user": "mvngu"
}
```

With the patch `trac_6504_toy_buch.3.patch`, I'm seeing some doctest failures:

```
sage -t -long devel/sage-exp/sage/rings/polynomial/multi_polynomial_ideal.py
**********************************************************************
File "/scratch/mvngu/release/sage-4.1.1.alpha0/devel/sage-exp/sage/rings/polynomial/multi_polynomial_ideal.py", line 944:
    sage: I.dimension()
Exception raised:
    Traceback (most recent call last):
      File "/scratch/mvngu/release/sage-4.1.1.alpha0/local/bin/ncadoctest.py", line 1231, in run_one_test
        self.run_one_example(test, example, filename, compileflags)
      File "/scratch/mvngu/release/sage-4.1.1.alpha0/local/bin/sagedoctest.py", line 38, in run_one_example
        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)
      File "/scratch/mvngu/release/sage-4.1.1.alpha0/local/bin/ncadoctest.py", line 1172, in run_one_example
        compileflags, 1) in test.globs
      File "<doctest __main__.example_19[9]>", line 1, in <module>
        I.dimension()###line 944:
    sage: I.dimension()
      File "/scratch/mvngu/release/sage-4.1.1.alpha0/local/lib/python/site-packages/sage/rings/polynomial/multi_polynomial_ideal.py", line 402, in __call__
        return self.f(self._instance, *args, **kwds)
      File "/scratch/mvngu/release/sage-4.1.1.alpha0/local/lib/python/site-packages/sage/rings/polynomial/multi_polynomial_ideal.py", line 978, in dimension
        gb = toy_buchberger.buchberger_improved(self)
      File "/scratch/mvngu/release/sage-4.1.1.alpha0/local/lib/python/site-packages/sage/rings/polynomial/toy_buchberger.py", line 279, in buchberger_improved
        h = spol(g1,g2).reduce(G)
      File "/scratch/mvngu/release/sage-4.1.1.alpha0/local/lib/python/site-packages/sage/rings/polynomial/toy_buchberger.py", line 175, in spol
        return p(fg_lcm/LT(f)*f - fg_lcm/LT(g)*g)
      File "/scratch/mvngu/release/sage-4.1.1.alpha0/local/lib/python/site-packages/sage/rings/polynomial/multi_polynomial_ring.py", line 422, in __call__
        raise TypeError, "unable to coerce since the denominator is not 1"
    TypeError: unable to coerce since the denominator is not 1
**********************************************************************
File "/scratch/mvngu/release/sage-4.1.1.alpha0/devel/sage-exp/sage/rings/polynomial/multi_polynomial_ideal.py", line 948:
    sage: I.dimension()
Exception raised:
    Traceback (most recent call last):
      File "/scratch/mvngu/release/sage-4.1.1.alpha0/local/bin/ncadoctest.py", line 1231, in run_one_test
        self.run_one_example(test, example, filename, compileflags)
      File "/scratch/mvngu/release/sage-4.1.1.alpha0/local/bin/sagedoctest.py", line 38, in run_one_example
        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)
      File "/scratch/mvngu/release/sage-4.1.1.alpha0/local/bin/ncadoctest.py", line 1172, in run_one_example
        compileflags, 1) in test.globs
      File "<doctest __main__.example_19[11]>", line 1, in <module>
        I.dimension()###line 948:
    sage: I.dimension()
      File "/scratch/mvngu/release/sage-4.1.1.alpha0/local/lib/python/site-packages/sage/rings/polynomial/multi_polynomial_ideal.py", line 402, in __call__
        return self.f(self._instance, *args, **kwds)
      File "/scratch/mvngu/release/sage-4.1.1.alpha0/local/lib/python/site-packages/sage/rings/polynomial/multi_polynomial_ideal.py", line 978, in dimension
        gb = toy_buchberger.buchberger_improved(self)
      File "/scratch/mvngu/release/sage-4.1.1.alpha0/local/lib/python/site-packages/sage/rings/polynomial/toy_buchberger.py", line 279, in buchberger_improved
        h = spol(g1,g2).reduce(G)
      File "/scratch/mvngu/release/sage-4.1.1.alpha0/local/lib/python/site-packages/sage/rings/polynomial/toy_buchberger.py", line 175, in spol
        return p(fg_lcm/LT(f)*f - fg_lcm/LT(g)*g)
      File "/scratch/mvngu/release/sage-4.1.1.alpha0/local/lib/python/site-packages/sage/rings/polynomial/multi_polynomial_ring.py", line 422, in __call__
        raise TypeError, "unable to coerce since the denominator is not 1"
    TypeError: unable to coerce since the denominator is not 1
**********************************************************************
1 items had failures:
   2 of  15 in __main__.example_19
***Test Failed*** 2 failures.
For whitespace errors, see the file /scratch/mvngu/release/sage-4.1.1.alpha0/tmp/.doctest_multi_polynomial_ideal.py
	 [13.4 s]

```




---

archive/issue_comments_052990.json:
```json
{
    "body": "Fixed an issue with spol function",
    "created_at": "2009-07-19T14:23:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6504",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6504#issuecomment-52990",
    "user": "mhampton"
}
```

Fixed an issue with spol function



---

archive/issue_comments_052991.json:
```json
{
    "body": "Attachment [trac_6504_toy_buch.4.patch](tarball://root/attachments/some-uuid/ticket6504/trac_6504_toy_buch.4.patch) by mhampton created at 2009-07-19 14:25:03\n\nOK, I fixed the spol function so that multi_polynomial_ideal.py passes tests as well.  I had thought what I had done was equivalent but I guess not over finite fields - actually I wonder if this is a failure in coercion but that's beyond the scope of this ticket.",
    "created_at": "2009-07-19T14:25:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6504",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6504#issuecomment-52991",
    "user": "mhampton"
}
```

Attachment [trac_6504_toy_buch.4.patch](tarball://root/attachments/some-uuid/ticket6504/trac_6504_toy_buch.4.patch) by mhampton created at 2009-07-19 14:25:03

OK, I fixed the spol function so that multi_polynomial_ideal.py passes tests as well.  I had thought what I had done was equivalent but I guess not over finite fields - actually I wonder if this is a failure in coercion but that's beyond the scope of this ticket.



---

archive/issue_comments_052992.json:
```json
{
    "body": "New patch is cumulative, its the only one that needs to be applied.",
    "created_at": "2009-07-19T14:25:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6504",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6504#issuecomment-52992",
    "user": "mhampton"
}
```

New patch is cumulative, its the only one that needs to be applied.



---

archive/issue_comments_052993.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-07-24T08:41:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6504",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6504#issuecomment-52993",
    "user": "mvngu"
}
```

Resolution: fixed

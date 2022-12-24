# Issue 8505: random points on elliptic curve misses half the group

archive/issues_008505.json:
```json
{
    "body": "Assignee: @JohnCremona\n\nThis is because it chooses only the first of the (usually) two possible lifts of a random x. Computing both is not more expensive, and this avoids the (expensive) exception creation and throwing as well. \n\nMay have a bit of fuzz with #8311.\n\nIssue created by migration from https://trac.sagemath.org/ticket/8505\n\n",
    "created_at": "2010-03-12T00:34:32Z",
    "labels": [
        "elliptic curves",
        "major",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.4",
    "title": "random points on elliptic curve misses half the group",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/8505",
    "user": "@robertwb"
}
```
Assignee: @JohnCremona

This is because it chooses only the first of the (usually) two possible lifts of a random x. Computing both is not more expensive, and this avoids the (expensive) exception creation and throwing as well. 

May have a bit of fuzz with #8311.

Issue created by migration from https://trac.sagemath.org/ticket/8505





---

archive/issue_comments_076786.json:
```json
{
    "body": "Attachment [8505-ell-finite-random.patch](tarball://root/attachments/some-uuid/ticket8505/8505-ell-finite-random.patch) by @robertwb created at 2010-03-12 00:35:53",
    "created_at": "2010-03-12T00:35:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8505",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8505#issuecomment-76786",
    "user": "@robertwb"
}
```

Attachment [8505-ell-finite-random.patch](tarball://root/attachments/some-uuid/ticket8505/8505-ell-finite-random.patch) by @robertwb created at 2010-03-12 00:35:53



---

archive/issue_comments_076787.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-03-12T00:36:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8505",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8505#issuecomment-76787",
    "user": "@robertwb"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_076788.json:
```json
{
    "body": "Looks ok, will test and report back shortly.  (Have to go prove the Mordell-Weil Theorem first....)",
    "created_at": "2010-03-12T14:57:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8505",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8505#issuecomment-76788",
    "user": "@JohnCremona"
}
```

Looks ok, will test and report back shortly.  (Have to go prove the Mordell-Weil Theorem first....)



---

archive/issue_comments_076789.json:
```json
{
    "body": "I tested all sage/schemes/elliptic_curves with -long and had one failure:\n\n```\njec@selmer%sage -t -long \"sage/schemes/elliptic_curves/ell_finite_field.py\"\n**********************************************************************\nFile \"/storage/jec/sage-4.3.4.alpha1/devel/sage-tests/sage/schemes/elliptic_curves/ell_finite_field.py\", line 1269:\n    sage: E.gens()\nExpected:\n    ((0 : 7 : 1),)\nGot:\n    ((0 : 4 : 1),)\n**********************************************************************\nFile \"/storage/jec/sage-4.3.4.alpha1/devel/sage-tests/sage/schemes/elliptic_curves/ell_finite_field.py\", line 1423:\n    sage: for p in prime_range(10000):           #long time (~20s)\n          if p != Integer(389):\n              G=E.change_ring(GF(p)).abelian_group()\nException raised:\n    Traceback (most recent call last):\n      File \"/home/jec/sage-current/local/bin/ncadoctest.py\", line 1231, in run_one_test\n        self.run_one_example(test, example, filename, compileflags)\n      File \"/home/jec/sage-current/local/bin/sagedoctest.py\", line 38, in run_one_example\n        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)\n      File \"/home/jec/sage-current/local/bin/ncadoctest.py\", line 1172, in run_one_example\n        compileflags, 1) in test.globs\n      File \"<doctest __main__.example_24[17]>\", line 3, in <module>\n        G=E.change_ring(GF(p)).abelian_group()\n      File \"/home/jec/sage-current/local/lib/python/site-packages/sage/schemes/elliptic_curves/ell_finite_field.py\", line 1512, in abelian_group\n        Q = self.random_point()\n      File \"/home/jec/sage-current/local/lib/python/site-packages/sage/schemes/elliptic_curves/ell_finite_field.py\", line 380, in random_element\n        v = self.lift_x(k.random_element(), all=True)\n      File \"/home/jec/sage-current/local/lib/python/site-packages/sage/schemes/elliptic_curves/ell_generic.py\", line 836, in lift_x\n        return [self.point([x, (-b+d)/2, one], check=False) for d in D.sqrt(all=True)]\n    TypeError: 'sage.rings.integer_mod.IntegerMod_int' object is not iterable\n**********************************************************************\nFile \"/storage/jec/sage-4.3.4.alpha1/devel/sage-tests/sage/schemes/elliptic_curves/ell_finite_field.py\", line 336:\n    sage: P = E.random_element(); P\nExpected:\n    (751 : 10581 : 1)\nGot:\n    (16740 : 12486 : 1)\n**********************************************************************\nFile \"/storage/jec/sage-4.3.4.alpha1/devel/sage-tests/sage/schemes/elliptic_curves/ell_finite_field.py\", line 347:\n    sage: P = E.random_element(); P\nExpected:\n    (a^3 + a + 5 : 5*a^4 + 6*a^3 + 5*a^2 + 3*a + 6 : 1)\nGot:\n    (2*a^4 + 3*a^3 + 5*a^2 + 6*a + 4 : 6*a^4 + 4*a^3 + a + 6 : 1)\n**********************************************************************\nFile \"/storage/jec/sage-4.3.4.alpha1/devel/sage-tests/sage/schemes/elliptic_curves/ell_finite_field.py\", line 358:\n    sage: P = E.random_element(); P\nExpected:\n    (a^4 + a^3 + a : 1 : 1)\nGot:\n    (a^4 + a^2 + 1 : a^3 + a : 1)\n**********************************************************************\n3 items had failures:\n   1 of  10 in __main__.example_21\n   1 of  25 in __main__.example_24\n   3 of  20 in __main__.example_9\n***Test Failed*** 5 failures.\nFor whitespace errors, see the file /home/jec/.sage//tmp/.doctest_ell_finit\n```\n\nThese are all but one trivial and I'll fix them with a reviewer patch.  But the other one looks stranger.  So some more investigation is required...watch this space!",
    "created_at": "2010-03-12T16:27:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8505",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8505#issuecomment-76789",
    "user": "@JohnCremona"
}
```

I tested all sage/schemes/elliptic_curves with -long and had one failure:

```
jec@selmer%sage -t -long "sage/schemes/elliptic_curves/ell_finite_field.py"
**********************************************************************
File "/storage/jec/sage-4.3.4.alpha1/devel/sage-tests/sage/schemes/elliptic_curves/ell_finite_field.py", line 1269:
    sage: E.gens()
Expected:
    ((0 : 7 : 1),)
Got:
    ((0 : 4 : 1),)
**********************************************************************
File "/storage/jec/sage-4.3.4.alpha1/devel/sage-tests/sage/schemes/elliptic_curves/ell_finite_field.py", line 1423:
    sage: for p in prime_range(10000):           #long time (~20s)
          if p != Integer(389):
              G=E.change_ring(GF(p)).abelian_group()
Exception raised:
    Traceback (most recent call last):
      File "/home/jec/sage-current/local/bin/ncadoctest.py", line 1231, in run_one_test
        self.run_one_example(test, example, filename, compileflags)
      File "/home/jec/sage-current/local/bin/sagedoctest.py", line 38, in run_one_example
        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)
      File "/home/jec/sage-current/local/bin/ncadoctest.py", line 1172, in run_one_example
        compileflags, 1) in test.globs
      File "<doctest __main__.example_24[17]>", line 3, in <module>
        G=E.change_ring(GF(p)).abelian_group()
      File "/home/jec/sage-current/local/lib/python/site-packages/sage/schemes/elliptic_curves/ell_finite_field.py", line 1512, in abelian_group
        Q = self.random_point()
      File "/home/jec/sage-current/local/lib/python/site-packages/sage/schemes/elliptic_curves/ell_finite_field.py", line 380, in random_element
        v = self.lift_x(k.random_element(), all=True)
      File "/home/jec/sage-current/local/lib/python/site-packages/sage/schemes/elliptic_curves/ell_generic.py", line 836, in lift_x
        return [self.point([x, (-b+d)/2, one], check=False) for d in D.sqrt(all=True)]
    TypeError: 'sage.rings.integer_mod.IntegerMod_int' object is not iterable
**********************************************************************
File "/storage/jec/sage-4.3.4.alpha1/devel/sage-tests/sage/schemes/elliptic_curves/ell_finite_field.py", line 336:
    sage: P = E.random_element(); P
Expected:
    (751 : 10581 : 1)
Got:
    (16740 : 12486 : 1)
**********************************************************************
File "/storage/jec/sage-4.3.4.alpha1/devel/sage-tests/sage/schemes/elliptic_curves/ell_finite_field.py", line 347:
    sage: P = E.random_element(); P
Expected:
    (a^3 + a + 5 : 5*a^4 + 6*a^3 + 5*a^2 + 3*a + 6 : 1)
Got:
    (2*a^4 + 3*a^3 + 5*a^2 + 6*a + 4 : 6*a^4 + 4*a^3 + a + 6 : 1)
**********************************************************************
File "/storage/jec/sage-4.3.4.alpha1/devel/sage-tests/sage/schemes/elliptic_curves/ell_finite_field.py", line 358:
    sage: P = E.random_element(); P
Expected:
    (a^4 + a^3 + a : 1 : 1)
Got:
    (a^4 + a^2 + 1 : a^3 + a : 1)
**********************************************************************
3 items had failures:
   1 of  10 in __main__.example_21
   1 of  25 in __main__.example_24
   3 of  20 in __main__.example_9
***Test Failed*** 5 failures.
For whitespace errors, see the file /home/jec/.sage//tmp/.doctest_ell_finit
```

These are all but one trivial and I'll fix them with a reviewer patch.  But the other one looks stranger.  So some more investigation is required...watch this space!



---

archive/issue_comments_076790.json:
```json
{
    "body": "replaces previous",
    "created_at": "2010-03-12T17:08:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8505",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8505#issuecomment-76790",
    "user": "@JohnCremona"
}
```

replaces previous



---

archive/issue_comments_076791.json:
```json
{
    "body": "Attachment [trac_8505-review.patch](tarball://root/attachments/some-uuid/ticket8505/trac_8505-review.patch) by @JohnCremona created at 2010-03-12 17:14:00\n\nMy patch (after reviewing and testing the whole sage library) has to be applied *instead* of Robert's, though it still has his tag on it (sorry).  It does two things relative to his:\n1. I changed a few doctest outputs for the random point tests.  I am worried though, since these changes were not only replacing a point by its negative!  Why?\n2. testing with -long revealed a bug in sqrt() for integer-mods: when 0 then the return was 0 and not [0] which broke the new code since it uses the all=true option.  This was *only* revealed in the -long test!  Take note!!\n\nI left this as \"needs review\" since it needs someone else (e.g. robertwb) to check my change, especially the one at 2. above, and also I would like to hear views on my other remark under 1.",
    "created_at": "2010-03-12T17:14:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8505",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8505#issuecomment-76791",
    "user": "@JohnCremona"
}
```

Attachment [trac_8505-review.patch](tarball://root/attachments/some-uuid/ticket8505/trac_8505-review.patch) by @JohnCremona created at 2010-03-12 17:14:00

My patch (after reviewing and testing the whole sage library) has to be applied *instead* of Robert's, though it still has his tag on it (sorry).  It does two things relative to his:
1. I changed a few doctest outputs for the random point tests.  I am worried though, since these changes were not only replacing a point by its negative!  Why?
2. testing with -long revealed a bug in sqrt() for integer-mods: when 0 then the return was 0 and not [0] which broke the new code since it uses the all=true option.  This was *only* revealed in the -long test!  Take note!!

I left this as "needs review" since it needs someone else (e.g. robertwb) to check my change, especially the one at 2. above, and also I would like to hear views on my other remark under 1.



---

archive/issue_comments_076792.json:
```json
{
    "body": "PS Robert: why do you care about missing half the group?  the only places I know where this function is used do not care (finding random points in order to find generators for the group of points).  Are you just being pedantic?  We could always add a paramter to the random_point() function which switches on or off this new behaviour?",
    "created_at": "2010-03-12T17:15:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8505",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8505#issuecomment-76792",
    "user": "@JohnCremona"
}
```

PS Robert: why do you care about missing half the group?  the only places I know where this function is used do not care (finding random points in order to find generators for the group of points).  Are you just being pedantic?  We could always add a paramter to the random_point() function which switches on or off this new behaviour?



---

archive/issue_comments_076793.json:
```json
{
    "body": "Thanks. I thought I had fixed all the doctest changes. The reason that some tests were changed by more then negation is because there is a second call to random() that updates the state of the random number generator. Regarding remark 2, see #8507. My motivation was actually that when using the all=False flag, half the time an (expensive, especially over non-prime fields) error is raised, but I think the current behavior is better as well. It would be like ZZ.random_element() always returning a positive value.",
    "created_at": "2010-03-12T17:32:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8505",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8505#issuecomment-76793",
    "user": "@robertwb"
}
```

Thanks. I thought I had fixed all the doctest changes. The reason that some tests were changed by more then negation is because there is a second call to random() that updates the state of the random number generator. Regarding remark 2, see #8507. My motivation was actually that when using the all=False flag, half the time an (expensive, especially over non-prime fields) error is raised, but I think the current behavior is better as well. It would be like ZZ.random_element() always returning a positive value.



---

archive/issue_comments_076794.json:
```json
{
    "body": "Robert, if you are happy with my patch then you could give this a positive review.  Or tell me, and I will.",
    "created_at": "2010-03-14T14:39:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8505",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8505#issuecomment-76794",
    "user": "@JohnCremona"
}
```

Robert, if you are happy with my patch then you could give this a positive review.  Or tell me, and I will.



---

archive/issue_comments_076795.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-03-15T19:18:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8505",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8505#issuecomment-76795",
    "user": "@robertwb"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_076796.json:
```json
{
    "body": "Attachment [trac_8505-review-post-8507.patch](tarball://root/attachments/some-uuid/ticket8505/trac_8505-review-post-8507.patch) by @robertwb created at 2010-03-15 19:18:21\n\nYes, I'm happy with it. I re-posted the patch removing the conflict with #8507, just in case that gets into an alpha before this. \n\nRelease manager: exactly one of `trac_8505-review.patch` or `trac_8505-review-post-8507.patch` should be applied.",
    "created_at": "2010-03-15T19:18:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8505",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8505#issuecomment-76796",
    "user": "@robertwb"
}
```

Attachment [trac_8505-review-post-8507.patch](tarball://root/attachments/some-uuid/ticket8505/trac_8505-review-post-8507.patch) by @robertwb created at 2010-03-15 19:18:21

Yes, I'm happy with it. I re-posted the patch removing the conflict with #8507, just in case that gets into an alpha before this. 

Release manager: exactly one of `trac_8505-review.patch` or `trac_8505-review-post-8507.patch` should be applied.



---

archive/issue_comments_076797.json:
```json
{
    "body": "Changing status from positive_review to needs_work.",
    "created_at": "2010-04-17T04:12:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8505",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8505#issuecomment-76797",
    "user": "@jhpalmieri"
}
```

Changing status from positive_review to needs_work.



---

archive/issue_comments_076798.json:
```json
{
    "body": "This (\" trac_8505-review-post-8507.patch\") doesn't apply cleanly to 4.3.5 or to Sage 4.4.alpha0.  Please rebase it against 4.4.alpha0, and we'll try hard to get this into 4.4.alpha1.",
    "created_at": "2010-04-17T04:12:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8505",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8505#issuecomment-76798",
    "user": "@jhpalmieri"
}
```

This (" trac_8505-review-post-8507.patch") doesn't apply cleanly to 4.3.5 or to Sage 4.4.alpha0.  Please rebase it against 4.4.alpha0, and we'll try hard to get this into 4.4.alpha1.



---

archive/issue_comments_076799.json:
```json
{
    "body": "Attachment [8505-ell-finite-random-rebased.patch](tarball://root/attachments/some-uuid/ticket8505/8505-ell-finite-random-rebased.patch) by @robertwb created at 2010-04-17 19:26:45\n\nRebased on 4.4.alpha0",
    "created_at": "2010-04-17T19:26:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8505",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8505#issuecomment-76799",
    "user": "@robertwb"
}
```

Attachment [8505-ell-finite-random-rebased.patch](tarball://root/attachments/some-uuid/ticket8505/8505-ell-finite-random-rebased.patch) by @robertwb created at 2010-04-17 19:26:45

Rebased on 4.4.alpha0



---

archive/issue_comments_076800.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2010-04-17T19:27:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8505",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8505#issuecomment-76800",
    "user": "@robertwb"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_076801.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-04-17T19:28:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8505",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8505#issuecomment-76801",
    "user": "@robertwb"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_076802.json:
```json
{
    "body": "Yep, #8311 touched the same code, but it was trivial to merge. I'm remarking this as positive review because it was just a rebase.",
    "created_at": "2010-04-17T19:28:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8505",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8505#issuecomment-76802",
    "user": "@robertwb"
}
```

Yep, #8311 touched the same code, but it was trivial to merge. I'm remarking this as positive review because it was just a rebase.



---

archive/issue_comments_076803.json:
```json
{
    "body": "Merged \"8505-ell-finite-random-rebased.patch\" into 4.4.alpha1.",
    "created_at": "2010-04-19T05:15:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8505",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8505#issuecomment-76803",
    "user": "@jhpalmieri"
}
```

Merged "8505-ell-finite-random-rebased.patch" into 4.4.alpha1.



---

archive/issue_comments_076804.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-04-19T05:15:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8505",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8505#issuecomment-76804",
    "user": "@jhpalmieri"
}
```

Resolution: fixed

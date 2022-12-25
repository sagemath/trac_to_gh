# Issue 9254: A collection of little improvements to BSD.py

archive/issues_009254.json:
```json
{
    "body": "Assignee: @JohnCremona\n\nThese are some of the things I did while working on my thesis.\n\nDepends on #9253, which depends on #9247. Still needs work, since there is now the following error, which is very mysterious to me:\n\n\n```\nsage -t  \"devel/sage-main/sage/schemes/elliptic_curves/BSD.py\"\n**********************************************************************\nFile \"/Users/rlmill/sage-4.4.4.alpha0/devel/sage-main/sage/schemes/elliptic_curves/BSD.py\", line 371:\n    sage: E.prove_BSD(verbosity=2)\nException raised:\n    Traceback (most recent call last):\n      File \"/Users/rlmill/sage-4.4.4.alpha0/local/bin/ncadoctest.py\", line 1231, in run_one_test\n        self.run_one_example(test, example, filename, compileflags)\n      File \"/Users/rlmill/sage-4.4.4.alpha0/local/bin/sagedoctest.py\", line 38, in run_one_example\n        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)\n      File \"/Users/rlmill/sage-4.4.4.alpha0/local/bin/ncadoctest.py\", line 1172, in run_one_example\n        compileflags, 1) in test.globs\n      File \"<doctest __main__.example_6[21]>\", line 1, in <module>\n        E.prove_BSD(verbosity=Integer(2))###line 371:\n    sage: E.prove_BSD(verbosity=2)\n      File \"/Users/rlmill/sage-4.4.4.alpha0/local/lib/python/site-packages/sage/schemes/elliptic_curves/BSD.py\", line 538, in prove_BSD\n        I = BSD.curve.heegner_index(D)\n      File \"/Users/rlmill/sage-4.4.4.alpha0/local/lib/python/site-packages/sage/schemes/elliptic_curves/heegner.py\", line 6464, in heegner_index\n        reg = F.regulator(descent_second_limit=descent_second_limit, verbose=verbose_mwrank)\n      File \"/Users/rlmill/sage-4.4.4.alpha0/local/lib/python/site-packages/sage/schemes/elliptic_curves/ell_rational_field.py\", line 2095, in regulator\n        G = self.gens(proof=proof, use_database=use_database, descent_second_limit=descent_second_limit, verbose=verbose)\n      File \"/Users/rlmill/sage-4.4.4.alpha0/local/lib/python/site-packages/sage/schemes/elliptic_curves/ell_rational_field.py\", line 1934, in gens\n        G = C.gens()\n      File \"/Users/rlmill/sage-4.4.4.alpha0/local/lib/python/site-packages/sage/libs/mwrank/interface.py\", line 595, in gens\n        return eval(preparse(self.__two_descent_data().getbasis().replace(\":\",\",\")))\n    RuntimeError\n**********************************************************************\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/9254\n\n",
    "created_at": "2010-06-17T18:28:22Z",
    "labels": [
        "component: elliptic curves",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.5.3",
    "title": "A collection of little improvements to BSD.py",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/9254",
    "user": "https://github.com/rlmill"
}
```
Assignee: @JohnCremona

These are some of the things I did while working on my thesis.

Depends on #9253, which depends on #9247. Still needs work, since there is now the following error, which is very mysterious to me:


```
sage -t  "devel/sage-main/sage/schemes/elliptic_curves/BSD.py"
**********************************************************************
File "/Users/rlmill/sage-4.4.4.alpha0/devel/sage-main/sage/schemes/elliptic_curves/BSD.py", line 371:
    sage: E.prove_BSD(verbosity=2)
Exception raised:
    Traceback (most recent call last):
      File "/Users/rlmill/sage-4.4.4.alpha0/local/bin/ncadoctest.py", line 1231, in run_one_test
        self.run_one_example(test, example, filename, compileflags)
      File "/Users/rlmill/sage-4.4.4.alpha0/local/bin/sagedoctest.py", line 38, in run_one_example
        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)
      File "/Users/rlmill/sage-4.4.4.alpha0/local/bin/ncadoctest.py", line 1172, in run_one_example
        compileflags, 1) in test.globs
      File "<doctest __main__.example_6[21]>", line 1, in <module>
        E.prove_BSD(verbosity=Integer(2))###line 371:
    sage: E.prove_BSD(verbosity=2)
      File "/Users/rlmill/sage-4.4.4.alpha0/local/lib/python/site-packages/sage/schemes/elliptic_curves/BSD.py", line 538, in prove_BSD
        I = BSD.curve.heegner_index(D)
      File "/Users/rlmill/sage-4.4.4.alpha0/local/lib/python/site-packages/sage/schemes/elliptic_curves/heegner.py", line 6464, in heegner_index
        reg = F.regulator(descent_second_limit=descent_second_limit, verbose=verbose_mwrank)
      File "/Users/rlmill/sage-4.4.4.alpha0/local/lib/python/site-packages/sage/schemes/elliptic_curves/ell_rational_field.py", line 2095, in regulator
        G = self.gens(proof=proof, use_database=use_database, descent_second_limit=descent_second_limit, verbose=verbose)
      File "/Users/rlmill/sage-4.4.4.alpha0/local/lib/python/site-packages/sage/schemes/elliptic_curves/ell_rational_field.py", line 1934, in gens
        G = C.gens()
      File "/Users/rlmill/sage-4.4.4.alpha0/local/lib/python/site-packages/sage/libs/mwrank/interface.py", line 595, in gens
        return eval(preparse(self.__two_descent_data().getbasis().replace(":",",")))
    RuntimeError
**********************************************************************
```


Issue created by migration from https://trac.sagemath.org/ticket/9254





---

archive/issue_comments_086952.json:
```json
{
    "body": "Also, this should be specifically tested on something like `t2` before it gets merged to make sure the timing issues are still fixed.",
    "created_at": "2010-06-17T18:29:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9254",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9254#issuecomment-86952",
    "user": "https://github.com/rlmill"
}
```

Also, this should be specifically tested on something like `t2` before it gets merged to make sure the timing issues are still fixed.



---

archive/issue_comments_086953.json:
```json
{
    "body": "Changing status from new to needs_work.",
    "created_at": "2010-06-17T18:30:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9254",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9254#issuecomment-86953",
    "user": "https://github.com/rlmill"
}
```

Changing status from new to needs_work.



---

archive/issue_comments_086954.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2010-07-18T06:32:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9254",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9254#issuecomment-86954",
    "user": "https://github.com/rlmill"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_086955.json:
```json
{
    "body": "See also #9535",
    "created_at": "2010-07-18T08:11:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9254",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9254#issuecomment-86955",
    "user": "https://github.com/rlmill"
}
```

See also #9535



---

archive/issue_comments_086956.json:
```json
{
    "body": "On t2:\n\n\n```\nsage -t  \"devel/sage-main/sage/schemes/elliptic_curves/BSD.py\"\n         [225.4 s]\n```\n\n\nOh yeah.",
    "created_at": "2010-07-21T15:59:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9254",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9254#issuecomment-86956",
    "user": "https://github.com/williamstein"
}
```

On t2:


```
sage -t  "devel/sage-main/sage/schemes/elliptic_curves/BSD.py"
         [225.4 s]
```


Oh yeah.



---

archive/issue_comments_086957.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-07-21T15:59:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9254",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9254#issuecomment-86957",
    "user": "https://github.com/williamstein"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_086958.json:
```json
{
    "body": "I get a long doctest failure on t2 and sage.math:\n\n```python\nsage -t -long \"devel/sage/sage/schemes/elliptic_curves/BSD.py\"\n**********************************************************************\nFile \"/mnt/usb1/scratch/mpatel/tmp/sage-4.5.2-fin/devel/sage/sage/schemes/elliptic_curves/BSD.py\", line 383:\n    sage: E.prove_BSD(verbosity=2)               # long time\nExpected:\n    p = 2: True by 2-descent...\n    True for p not in {2, 3} by Kolyvagin....\n    ALERT: p = 3 left in Kolyvagin bound\n        0 <= ord_p(#Sha) <= 2\n        ord_p(#Sha_an) = 2\n    Remaining primes:\n    p = 3: irreducible, surjective, non-split multiplicative\n        (0 <= ord_p <= 2)\n    [3]\nGot:\n    p = 2: True by 2-descent\n    True for p not in {2, 3} by Kolyvagin.\n    Remaining primes:\n    p = 3: irreducible, surjective, non-split multiplicative\n        (0 <= ord_p <= 2)\n        ord_p(#Sha_an) = 2\n    [3]\n**********************************************************************\n1 items had failures:\n   1 of  36 in __main__.example_6\n***Test Failed*** 1 failures.\n```\n\nI'm using 4.5.2 + #9476 + #9247 + #9253 + #9254.  The failure first appears with this ticket.",
    "created_at": "2010-08-08T08:45:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9254",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9254#issuecomment-86958",
    "user": "https://github.com/qed777"
}
```

I get a long doctest failure on t2 and sage.math:

```python
sage -t -long "devel/sage/sage/schemes/elliptic_curves/BSD.py"
**********************************************************************
File "/mnt/usb1/scratch/mpatel/tmp/sage-4.5.2-fin/devel/sage/sage/schemes/elliptic_curves/BSD.py", line 383:
    sage: E.prove_BSD(verbosity=2)               # long time
Expected:
    p = 2: True by 2-descent...
    True for p not in {2, 3} by Kolyvagin....
    ALERT: p = 3 left in Kolyvagin bound
        0 <= ord_p(#Sha) <= 2
        ord_p(#Sha_an) = 2
    Remaining primes:
    p = 3: irreducible, surjective, non-split multiplicative
        (0 <= ord_p <= 2)
    [3]
Got:
    p = 2: True by 2-descent
    True for p not in {2, 3} by Kolyvagin.
    Remaining primes:
    p = 3: irreducible, surjective, non-split multiplicative
        (0 <= ord_p <= 2)
        ord_p(#Sha_an) = 2
    [3]
**********************************************************************
1 items had failures:
   1 of  36 in __main__.example_6
***Test Failed*** 1 failures.
```

I'm using 4.5.2 + #9476 + #9247 + #9253 + #9254.  The failure first appears with this ticket.



---

archive/issue_comments_086959.json:
```json
{
    "body": "Changing status from positive_review to needs_work.",
    "created_at": "2010-08-08T08:45:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9254",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9254#issuecomment-86959",
    "user": "https://github.com/qed777"
}
```

Changing status from positive_review to needs_work.



---

archive/issue_comments_086960.json:
```json
{
    "body": "Attachment [trac_9254.patch](tarball://root/attachments/some-uuid/ticket9254/trac_9254.patch) by @rlmill created at 2010-08-09 05:50:49",
    "created_at": "2010-08-09T05:50:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9254",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9254#issuecomment-86960",
    "user": "https://github.com/rlmill"
}
```

Attachment [trac_9254.patch](tarball://root/attachments/some-uuid/ticket9254/trac_9254.patch) by @rlmill created at 2010-08-09 05:50:49



---

archive/issue_comments_086961.json:
```json
{
    "body": "Updated patch fixes the long doctest failure.",
    "created_at": "2010-08-09T05:52:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9254",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9254#issuecomment-86961",
    "user": "https://github.com/rlmill"
}
```

Updated patch fixes the long doctest failure.



---

archive/issue_comments_086962.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2010-08-09T05:52:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9254",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9254#issuecomment-86962",
    "user": "https://github.com/rlmill"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_086963.json:
```json
{
    "body": "The test now passes on t2 and sage.math.  I'm not a subject expect, but since there are no new technical changes to review, I'm changing the status back to \"positive.\"",
    "created_at": "2010-08-09T08:50:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9254",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9254#issuecomment-86963",
    "user": "https://github.com/qed777"
}
```

The test now passes on t2 and sage.math.  I'm not a subject expect, but since there are no new technical changes to review, I'm changing the status back to "positive."



---

archive/issue_comments_086964.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-08-09T08:50:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9254",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9254#issuecomment-86964",
    "user": "https://github.com/qed777"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_events_009415.json:
```json
{
    "actor": "@qed777",
    "created_at": "2010-08-09T09:50:39Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/9254",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/9254#event-9415"
}
```



---

archive/issue_comments_086965.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-08-09T09:50:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9254",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9254#issuecomment-86965",
    "user": "https://github.com/qed777"
}
```

Resolution: fixed

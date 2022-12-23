# Issue 8749: BSD: doctest failures on solaris (t2)

archive/issues_008749.json:
```json
{
    "body": "Assignee: cremona\n\nCC:  robertwb rlm\n\nWith Sage 4.4.alpha2, I see the following:\n\n```\nFile \"/home/palmieri/t2/sage-4.4.alpha2/devel/sage-main/sage/schemes/elliptic_curves/BSD.py\", line\\\n 304:\n    sage: EllipticCurve('11a').prove_BSD(verbosity=2)\nExpected:\n    p = 2: True by 2-descent\n    True for p not in {2, 5} by Kolyvagin.\n    True for p=5 by Mazur\n    []\nGot:\n    p = 2: True by 2-descent\n    Timeout stopped Heegner index computation...\n    Proceeding to use heegner_index_bound instead.\n    True for p not in {2, 5} by Kolyvagin.\n    True for p=5 by Mazur\n    []\n**********************************************************************\nFile \"/home/palmieri/t2/sage-4.4.alpha2/devel/sage-main/sage/schemes/elliptic_curves/BSD.py\", line\\\n 377:\n    sage: E.prove_BSD(verbosity=2)               # long time\nException raised:\n    Traceback (most recent call last):\n      File \"/home/palmieri/t2/sage-4.4.alpha2/local/bin/ncadoctest.py\", line 1231, in run_one_test\n        self.run_one_example(test, example, filename, compileflags)\n      File \"/home/palmieri/t2/sage-4.4.alpha2/local/bin/sagedoctest.py\", line 38, in run_one_examp\\\nle\n        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)\n      File \"/home/palmieri/t2/sage-4.4.alpha2/local/bin/ncadoctest.py\", line 1172, in run_one_exam\\\nple\n        compileflags, 1) in test.globs\n      File \"<doctest __main__.example_6[22]>\", line 1, in <module>\n        E.prove_BSD(verbosity=Integer(2))               # long time###line 377:\n    sage: E.prove_BSD(verbosity=2)               # long time\n      File \"/home/palmieri/t2/sage-4.4.alpha2/local/lib/python/site-packages/sage/schemes/elliptic\\\n_curves/BSD.py\", line 761, in prove_BSD\n        raise RuntimeError(\"p = %d: ord_p_bound == %d, but sha_an.ord(p) == %d. This appears to be\\\n a counterexample to BSD, but is more likely a bug.\"%(p,ord_p_bound,BSD.sha_an.ord(p)))\n    RuntimeError: p = 3: ord_p_bound == 1, but sha_an.ord(p) == 2. This appears to be a counterexa\\\nmple to BSD, but is more likely a bug.\n**********************************************************************\n1 items had failures:\n   2 of  35 in __main__.example_6\n***Test Failed*** 2 failures.\n```\n\nThe first is a timeout issue of some sort, and perhaps could be fixed by putting in some dots `...` in case the timeout message appears.  (I've also seen more failures of this type from the same file, so ellipses in several places might be needed.  Test on t2 several times to see.)\n\nI have no idea about the second issue.  Presumably it's not a counterexample to BSD.\n\nIssue created by migration from https://trac.sagemath.org/ticket/8749\n\n",
    "created_at": "2010-04-23T05:15:26Z",
    "labels": [
        "elliptic curves",
        "blocker",
        "bug"
    ],
    "title": "BSD: doctest failures on solaris (t2)",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/8749",
    "user": "jhpalmieri"
}
```
Assignee: cremona

CC:  robertwb rlm

With Sage 4.4.alpha2, I see the following:

```
File "/home/palmieri/t2/sage-4.4.alpha2/devel/sage-main/sage/schemes/elliptic_curves/BSD.py", line\
 304:
    sage: EllipticCurve('11a').prove_BSD(verbosity=2)
Expected:
    p = 2: True by 2-descent
    True for p not in {2, 5} by Kolyvagin.
    True for p=5 by Mazur
    []
Got:
    p = 2: True by 2-descent
    Timeout stopped Heegner index computation...
    Proceeding to use heegner_index_bound instead.
    True for p not in {2, 5} by Kolyvagin.
    True for p=5 by Mazur
    []
**********************************************************************
File "/home/palmieri/t2/sage-4.4.alpha2/devel/sage-main/sage/schemes/elliptic_curves/BSD.py", line\
 377:
    sage: E.prove_BSD(verbosity=2)               # long time
Exception raised:
    Traceback (most recent call last):
      File "/home/palmieri/t2/sage-4.4.alpha2/local/bin/ncadoctest.py", line 1231, in run_one_test
        self.run_one_example(test, example, filename, compileflags)
      File "/home/palmieri/t2/sage-4.4.alpha2/local/bin/sagedoctest.py", line 38, in run_one_examp\
le
        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)
      File "/home/palmieri/t2/sage-4.4.alpha2/local/bin/ncadoctest.py", line 1172, in run_one_exam\
ple
        compileflags, 1) in test.globs
      File "<doctest __main__.example_6[22]>", line 1, in <module>
        E.prove_BSD(verbosity=Integer(2))               # long time###line 377:
    sage: E.prove_BSD(verbosity=2)               # long time
      File "/home/palmieri/t2/sage-4.4.alpha2/local/lib/python/site-packages/sage/schemes/elliptic\
_curves/BSD.py", line 761, in prove_BSD
        raise RuntimeError("p = %d: ord_p_bound == %d, but sha_an.ord(p) == %d. This appears to be\
 a counterexample to BSD, but is more likely a bug."%(p,ord_p_bound,BSD.sha_an.ord(p)))
    RuntimeError: p = 3: ord_p_bound == 1, but sha_an.ord(p) == 2. This appears to be a counterexa\
mple to BSD, but is more likely a bug.
**********************************************************************
1 items had failures:
   2 of  35 in __main__.example_6
***Test Failed*** 2 failures.
```

The first is a timeout issue of some sort, and perhaps could be fixed by putting in some dots `...` in case the timeout message appears.  (I've also seen more failures of this type from the same file, so ellipses in several places might be needed.  Test on t2 several times to see.)

I have no idea about the second issue.  Presumably it's not a counterexample to BSD.

Issue created by migration from https://trac.sagemath.org/ticket/8749





---

archive/issue_comments_080043.json:
```json
{
    "body": "Replying to [ticket:8749 jhpalmieri]:\n> (I've also seen more failures of this type from the same file, so ellipses in several places might be needed.  Test on t2 several times to see.)\n\nMore specifically, I just saw this on lines 304, 310, 336, and 418.",
    "created_at": "2010-04-23T17:24:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8749",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8749#issuecomment-80043",
    "user": "jhpalmieri"
}
```

Replying to [ticket:8749 jhpalmieri]:
> (I've also seen more failures of this type from the same file, so ellipses in several places might be needed.  Test on t2 several times to see.)

More specifically, I just saw this on lines 304, 310, 336, and 418.



---

archive/issue_comments_080044.json:
```json
{
    "body": "Attachment",
    "created_at": "2010-04-30T01:44:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8749",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8749#issuecomment-80044",
    "user": "rlm"
}
```

Attachment



---

archive/issue_comments_080045.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-04-30T01:44:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8749",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8749#issuecomment-80045",
    "user": "rlm"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_080046.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-05-01T06:09:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8749",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8749#issuecomment-80046",
    "user": "was"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_080047.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-05-01T06:13:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8749",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8749#issuecomment-80047",
    "user": "was"
}
```

Resolution: fixed



---

archive/issue_comments_080048.json:
```json
{
    "body": "It turns out this patch works on t2, but fails on *everything* else... due to misuse of ...\nThe attached patch fixes this by removing a newline in each ...'d test.",
    "created_at": "2010-05-01T18:43:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8749",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8749#issuecomment-80048",
    "user": "was"
}
```

It turns out this patch works on t2, but fails on *everything* else... due to misuse of ...
The attached patch fixes this by removing a newline in each ...'d test.



---

archive/issue_comments_080049.json:
```json
{
    "body": "Attachment\n\nSecond patch looks good: positive review.",
    "created_at": "2010-05-01T20:30:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8749",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8749#issuecomment-80049",
    "user": "rlm"
}
```

Attachment

Second patch looks good: positive review.



---

archive/issue_comments_080050.json:
```json
{
    "body": "I don't think this is fixed properly - or if it was, a very similar error is now occurring on the same doctest. See  #9127 \n\nDave",
    "created_at": "2010-06-03T12:41:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8749",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8749#issuecomment-80050",
    "user": "drkirkby"
}
```

I don't think this is fixed properly - or if it was, a very similar error is now occurring on the same doctest. See  #9127 

Dave

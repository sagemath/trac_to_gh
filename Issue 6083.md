# Issue 6083: speedup integer division

archive/issues_006083.json:
```json
{
    "body": "Assignee: somebody\n\nremove _sig_on and _sig_off for small operands, specialize for int divisor\n\nIssue created by migration from https://trac.sagemath.org/ticket/6083\n\n",
    "created_at": "2009-05-19T07:35:58Z",
    "labels": [
        "component: basic arithmetic",
        "bug"
    ],
    "title": "speedup integer division",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/6083",
    "user": "https://github.com/robertwb"
}
```
Assignee: somebody

remove _sig_on and _sig_off for small operands, specialize for int divisor

Issue created by migration from https://trac.sagemath.org/ticket/6083





---

archive/issue_comments_048318.json:
```json
{
    "body": "Attachment [6083-integer-div.patch](tarball://root/attachments/some-uuid/ticket6083/6083-integer-div.patch) by @robertwb created at 2009-05-20 03:53:45",
    "created_at": "2009-05-20T03:53:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6083",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6083#issuecomment-48318",
    "user": "https://github.com/robertwb"
}
```

Attachment [6083-integer-div.patch](tarball://root/attachments/some-uuid/ticket6083/6083-integer-div.patch) by @robertwb created at 2009-05-20 03:53:45



---

archive/issue_comments_048319.json:
```json
{
    "body": "I now get one trivial test failure (changed exception message):\n\n\n```\nFile \"/home/fredrik/sage-4.0/devel/sage-mpmath/sage/rings/integer.pyx\", line 2163:\n    sage: z % 0\nExpected:\n    Traceback (most recent call last):\n    ...\n    ZeroDivisionError: Integer modulo by zero\nGot:\n    Traceback (most recent call last):\n      File \"/space/wstein/farm/sage-4.0/local/bin/ncadoctest.py\", line 1231, in run_one_test\n        self.run_one_example(test, example, filename, compileflags)\n      File \"/space/wstein/farm/sage-4.0/local/bin/sagedoctest.py\", line 38, in run_one_example\n        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)\n      File \"/space/wstein/farm/sage-4.0/local/bin/ncadoctest.py\", line 1172, in run_one_example\n        compileflags, 1) in test.globs\n      File \"<doctest __main__.example_46[4]>\", line 1, in <module>\n        z % Integer(0)###line 2163:\n    sage: z % 0\n      File \"integer.pyx\", line 2189, in sage.rings.integer.Integer.__mod__ (sage/rings/integer.c:15033)\n    ZeroDivisionError: other must be nonzero\n```\n\n\nOtherwise, this patch has my approval.",
    "created_at": "2009-06-03T18:43:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6083",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6083#issuecomment-48319",
    "user": "https://github.com/fredrik-johansson"
}
```

I now get one trivial test failure (changed exception message):


```
File "/home/fredrik/sage-4.0/devel/sage-mpmath/sage/rings/integer.pyx", line 2163:
    sage: z % 0
Expected:
    Traceback (most recent call last):
    ...
    ZeroDivisionError: Integer modulo by zero
Got:
    Traceback (most recent call last):
      File "/space/wstein/farm/sage-4.0/local/bin/ncadoctest.py", line 1231, in run_one_test
        self.run_one_example(test, example, filename, compileflags)
      File "/space/wstein/farm/sage-4.0/local/bin/sagedoctest.py", line 38, in run_one_example
        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)
      File "/space/wstein/farm/sage-4.0/local/bin/ncadoctest.py", line 1172, in run_one_example
        compileflags, 1) in test.globs
      File "<doctest __main__.example_46[4]>", line 1, in <module>
        z % Integer(0)###line 2163:
    sage: z % 0
      File "integer.pyx", line 2189, in sage.rings.integer.Integer.__mod__ (sage/rings/integer.c:15033)
    ZeroDivisionError: other must be nonzero
```


Otherwise, this patch has my approval.



---

archive/issue_comments_048320.json:
```json
{
    "body": "Thanks for looking at these. I'll fix this (the original error seems better).",
    "created_at": "2009-06-03T19:00:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6083",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6083#issuecomment-48320",
    "user": "https://github.com/robertwb"
}
```

Thanks for looking at these. I'll fix this (the original error seems better).



---

archive/issue_comments_048321.json:
```json
{
    "body": "This patch looks good. I've added a referee patch that makes a few really minor changes:\n\n* removes the unused `_floordiv` function\n* changes the error messages: they all now say either \"Integer division by zero\" or \"Integer modulo by zero.\" I think these are more informative, and they also now mirror the Python ones (which all say \"integer division or modulus by zero\"). The old ones were of the form `\"other (=%s) must be nonzero\"%other`, and by definition **always** had other equal to 0, so that just seemed silly. \n\nUnless Robert or Fredrik has any objections to the second patch, I'd say this is good to go.",
    "created_at": "2009-06-05T04:47:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6083",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6083#issuecomment-48321",
    "user": "https://github.com/craigcitro"
}
```

This patch looks good. I've added a referee patch that makes a few really minor changes:

* removes the unused `_floordiv` function
* changes the error messages: they all now say either "Integer division by zero" or "Integer modulo by zero." I think these are more informative, and they also now mirror the Python ones (which all say "integer division or modulus by zero"). The old ones were of the form `"other (=%s) must be nonzero"%other`, and by definition **always** had other equal to 0, so that just seemed silly. 

Unless Robert or Fredrik has any objections to the second patch, I'd say this is good to go.



---

archive/issue_comments_048322.json:
```json
{
    "body": "Yep, looks good.",
    "created_at": "2009-06-05T11:15:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6083",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6083#issuecomment-48322",
    "user": "https://github.com/robertwb"
}
```

Yep, looks good.



---

archive/issue_comments_048323.json:
```json
{
    "body": "Unfortunately, this causes a segfault with the 4.0.2.alpha0 singular:\n\n```\n----------------------------------------------------------------------\n\nThe following tests failed:\n\n        sage -t -long devel/sage/sage/rings/polynomial/multi_polynomial_ideal.py # Segfault\n----------------------------------------------------------------------\nTotal time for all tests: 524.4 seconds\nTests failed!\n```\n",
    "created_at": "2009-06-13T21:06:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6083",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6083#issuecomment-48323",
    "user": "https://github.com/ncalexan"
}
```

Unfortunately, this causes a segfault with the 4.0.2.alpha0 singular:

```
----------------------------------------------------------------------

The following tests failed:

        sage -t -long devel/sage/sage/rings/polynomial/multi_polynomial_ideal.py # Segfault
----------------------------------------------------------------------
Total time for all tests: 524.4 seconds
Tests failed!
```




---

archive/issue_comments_048324.json:
```json
{
    "body": "Attachment [trac-6083-referee.patch](tarball://root/attachments/some-uuid/ticket6083/trac-6083-referee.patch) by @craigcitro created at 2009-06-22 07:45:17\n\nIt turns out the segfault was coming from an infinite loop in Cython. The issue was that after the first patch above, doing `Integer % IntegerMod_gmp` would call into the `__mod__` on `IntegerMod_gmp`, which tried to check if something was zero by doing something of the form `Integer % IntegerMod_gmp` ... and repeat ad infinitum. \n\nSo the new patch adds a small snippet to fix this, and a doctest.",
    "created_at": "2009-06-22T07:45:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6083",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6083#issuecomment-48324",
    "user": "https://github.com/craigcitro"
}
```

Attachment [trac-6083-referee.patch](tarball://root/attachments/some-uuid/ticket6083/trac-6083-referee.patch) by @craigcitro created at 2009-06-22 07:45:17

It turns out the segfault was coming from an infinite loop in Cython. The issue was that after the first patch above, doing `Integer % IntegerMod_gmp` would call into the `__mod__` on `IntegerMod_gmp`, which tried to check if something was zero by doing something of the form `Integer % IntegerMod_gmp` ... and repeat ad infinitum. 

So the new patch adds a small snippet to fix this, and a doctest.



---

archive/issue_comments_048325.json:
```json
{
    "body": "Although I have not been following all the details of this one, I applied all patches successfully to 4.1.alpha2 and ran -testall successfully, so I'm giving it a positive review.",
    "created_at": "2009-06-28T13:18:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6083",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6083#issuecomment-48325",
    "user": "https://github.com/JohnCremona"
}
```

Although I have not been following all the details of this one, I applied all patches successfully to 4.1.alpha2 and ran -testall successfully, so I'm giving it a positive review.



---

archive/issue_events_014284.json:
```json
{
    "actor": "https://github.com/rlmill",
    "created_at": "2009-07-04T02:09:23Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/6083",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/6083#event-14284"
}
```



---

archive/issue_comments_048326.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-07-04T02:09:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6083",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6083#issuecomment-48326",
    "user": "https://github.com/rlmill"
}
```

Resolution: fixed

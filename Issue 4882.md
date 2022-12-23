# Issue 4882: ./sage -t sage/sage/rings/polynomial/multi_polynomial_ideal.py M2 failure

archive/issues_004882.json:
```json
{
    "body": "Assignee: tbd\n\nOn Fedora 9, 32 bits:\n\n\n```\nsage -t  \"devel/sage/sage/rings/polynomial/multi_polynomial_ideal.py\"\n**********************************************************************\nFile \"/home/jaap/work/downloads/sage-3.2.2/devel/sage/sage/rings/polynomial/multi_polynomial_ideal.py\", line 58:\n    sage: S.<a,b> = R.quotient((x^2 + y^2, 17))\nExpected:\n    verbose 0 ... Warning: falling back to very slow toy implementation.\nGot nothing\n**********************************************************************\n1 items had failures:\n   1 of  47 in __main__.example_0\n***Test Failed*** 1 failures.\nFor whitespace errors, see the file /home/jaap/downloads/sage-3.2.2/tmp/.doctest_multi_polynomial_ideal.py\n\t [44.6 s]\nexit code: 1024\n \n----------------------------------------------------------------------\nThe following tests failed:\n\n\n\tsage -t  \"devel/sage/sage/rings/polynomial/multi_polynomial_ideal.py\"\nTotal time for all tests: 44.6 seconds\n\n```\n\n\n\nJaap\n\nIssue created by migration from https://trac.sagemath.org/ticket/4882\n\n",
    "created_at": "2008-12-26T17:39:31Z",
    "labels": [
        "algebra",
        "major",
        "bug"
    ],
    "title": "./sage -t sage/sage/rings/polynomial/multi_polynomial_ideal.py M2 failure",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/4882",
    "user": "jsp"
}
```
Assignee: tbd

On Fedora 9, 32 bits:


```
sage -t  "devel/sage/sage/rings/polynomial/multi_polynomial_ideal.py"
**********************************************************************
File "/home/jaap/work/downloads/sage-3.2.2/devel/sage/sage/rings/polynomial/multi_polynomial_ideal.py", line 58:
    sage: S.<a,b> = R.quotient((x^2 + y^2, 17))
Expected:
    verbose 0 ... Warning: falling back to very slow toy implementation.
Got nothing
**********************************************************************
1 items had failures:
   1 of  47 in __main__.example_0
***Test Failed*** 1 failures.
For whitespace errors, see the file /home/jaap/downloads/sage-3.2.2/tmp/.doctest_multi_polynomial_ideal.py
	 [44.6 s]
exit code: 1024
 
----------------------------------------------------------------------
The following tests failed:


	sage -t  "devel/sage/sage/rings/polynomial/multi_polynomial_ideal.py"
Total time for all tests: 44.6 seconds

```



Jaap

Issue created by migration from https://trac.sagemath.org/ticket/4882





---

archive/issue_comments_036996.json:
```json
{
    "body": "Changing assignee from tbd to mabshoff.",
    "created_at": "2008-12-26T17:49:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4882",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4882#issuecomment-36996",
    "user": "mabshoff"
}
```

Changing assignee from tbd to mabshoff.



---

archive/issue_comments_036997.json:
```json
{
    "body": "Changing component from algebra to doctest.",
    "created_at": "2008-12-26T17:49:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4882",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4882#issuecomment-36997",
    "user": "mabshoff"
}
```

Changing component from algebra to doctest.



---

archive/issue_comments_036998.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2008-12-26T17:49:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4882",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4882#issuecomment-36998",
    "user": "mabshoff"
}
```

Changing status from new to assigned.



---

archive/issue_comments_036999.json:
```json
{
    "body": "Attachment",
    "created_at": "2008-12-26T17:49:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4882",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4882#issuecomment-36999",
    "user": "mabshoff"
}
```

Attachment



---

archive/issue_comments_037000.json:
```json
{
    "body": "After the patch:\n\n\n\n```\nsage -t  \"devel/sage/sage/rings/polynomial/multi_polynomial_ideal.py\"\n**********************************************************************\nFile \"/home/jaap/work/downloads/sage-3.2.2/devel/sage/sage/rings/polynomial/multi_polynomial_ideal.py\", line 65:\n    sage: a^2 + b^2 == 0\nException raised:\n    Traceback (most recent call last):\n      File \"/home/jaap/downloads/sage-3.2.2.alpha2/local/bin/ncadoctest.py\", line 1231, in run_one_test\n        self.run_one_example(test, example, filename, compileflags)\n      File \"/home/jaap/downloads/sage-3.2.2.alpha2/local/bin/sagedoctest.py\", line 38, in run_one_example\n        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)\n      File \"/home/jaap/downloads/sage-3.2.2.alpha2/local/bin/ncadoctest.py\", line 1172, in run_one_example\n        compileflags, 1) in test.globs\n      File \"<doctest __main__.example_0[16]>\", line 1, in <module>\n        a**Integer(2) + b**Integer(2) == Integer(0)###line 65:\n    sage: a^2 + b^2 == 0\n    NameError: name 'a' is not defined\n**********************************************************************\nFile \"/home/jaap/work/downloads/sage-3.2.2/devel/sage/sage/rings/polynomial/multi_polynomial_ideal.py\", line 67:\n    sage: a^3 - b^2\nException raised:\n    Traceback (most recent call last):\n      File \"/home/jaap/downloads/sage-3.2.2.alpha2/local/bin/ncadoctest.py\", line 1231, in run_one_test\n        self.run_one_example(test, example, filename, compileflags)\n      File \"/home/jaap/downloads/sage-3.2.2.alpha2/local/bin/sagedoctest.py\", line 38, in run_one_example\n        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)\n      File \"/home/jaap/downloads/sage-3.2.2.alpha2/local/bin/ncadoctest.py\", line 1172, in run_one_example\n        compileflags, 1) in test.globs\n      File \"<doctest __main__.example_0[17]>\", line 1, in <module>\n        a**Integer(3) - b**Integer(2)###line 67:\n    sage: a^3 - b^2\n    NameError: name 'a' is not defined\n**********************************************************************\nFile \"/home/jaap/work/downloads/sage-3.2.2/devel/sage/sage/rings/polynomial/multi_polynomial_ideal.py\", line 69:\n    sage: (a+b)^17\nException raised:\n    Traceback (most recent call last):\n      File \"/home/jaap/downloads/sage-3.2.2.alpha2/local/bin/ncadoctest.py\", line 1231, in run_one_test\n        self.run_one_example(test, example, filename, compileflags)\n      File \"/home/jaap/downloads/sage-3.2.2.alpha2/local/bin/sagedoctest.py\", line 38, in run_one_example\n        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)\n      File \"/home/jaap/downloads/sage-3.2.2.alpha2/local/bin/ncadoctest.py\", line 1172, in run_one_example\n        compileflags, 1) in test.globs\n      File \"<doctest __main__.example_0[18]>\", line 1, in <module>\n        (a+b)**Integer(17)###line 69:\n    sage: (a+b)^17\n    NameError: name 'a' is not defined\n**********************************************************************\nFile \"/home/jaap/work/downloads/sage-3.2.2/devel/sage/sage/rings/polynomial/multi_polynomial_ideal.py\", line 71:\n    sage: S(17) == 0\nException raised:\n    Traceback (most recent call last):\n      File \"/home/jaap/downloads/sage-3.2.2.alpha2/local/bin/ncadoctest.py\", line 1231, in run_one_test\n        self.run_one_example(test, example, filename, compileflags)\n      File \"/home/jaap/downloads/sage-3.2.2.alpha2/local/bin/sagedoctest.py\", line 38, in run_one_example\n        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)\n      File \"/home/jaap/downloads/sage-3.2.2.alpha2/local/bin/ncadoctest.py\", line 1172, in run_one_example\n        compileflags, 1) in test.globs\n      File \"<doctest __main__.example_0[19]>\", line 1, in <module>\n        S(Integer(17)) == Integer(0)###line 71:\n    sage: S(17) == 0\n    NameError: name 'S' is not defined\n**********************************************************************\n1 items had failures:\n   4 of  45 in __main__.example_0\n***Test Failed*** 4 failures.\nFor whitespace errors, see the file /home/jaap/downloads/sage-3.2.2/tmp/.doctest_multi_polynomial_ideal.py\n\t [12.6 s]\nexit code: 1024\n \n\n```\n\n\nNeeds work\n\nJaap",
    "created_at": "2008-12-26T18:55:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4882",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4882#issuecomment-37000",
    "user": "jsp"
}
```

After the patch:



```
sage -t  "devel/sage/sage/rings/polynomial/multi_polynomial_ideal.py"
**********************************************************************
File "/home/jaap/work/downloads/sage-3.2.2/devel/sage/sage/rings/polynomial/multi_polynomial_ideal.py", line 65:
    sage: a^2 + b^2 == 0
Exception raised:
    Traceback (most recent call last):
      File "/home/jaap/downloads/sage-3.2.2.alpha2/local/bin/ncadoctest.py", line 1231, in run_one_test
        self.run_one_example(test, example, filename, compileflags)
      File "/home/jaap/downloads/sage-3.2.2.alpha2/local/bin/sagedoctest.py", line 38, in run_one_example
        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)
      File "/home/jaap/downloads/sage-3.2.2.alpha2/local/bin/ncadoctest.py", line 1172, in run_one_example
        compileflags, 1) in test.globs
      File "<doctest __main__.example_0[16]>", line 1, in <module>
        a**Integer(2) + b**Integer(2) == Integer(0)###line 65:
    sage: a^2 + b^2 == 0
    NameError: name 'a' is not defined
**********************************************************************
File "/home/jaap/work/downloads/sage-3.2.2/devel/sage/sage/rings/polynomial/multi_polynomial_ideal.py", line 67:
    sage: a^3 - b^2
Exception raised:
    Traceback (most recent call last):
      File "/home/jaap/downloads/sage-3.2.2.alpha2/local/bin/ncadoctest.py", line 1231, in run_one_test
        self.run_one_example(test, example, filename, compileflags)
      File "/home/jaap/downloads/sage-3.2.2.alpha2/local/bin/sagedoctest.py", line 38, in run_one_example
        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)
      File "/home/jaap/downloads/sage-3.2.2.alpha2/local/bin/ncadoctest.py", line 1172, in run_one_example
        compileflags, 1) in test.globs
      File "<doctest __main__.example_0[17]>", line 1, in <module>
        a**Integer(3) - b**Integer(2)###line 67:
    sage: a^3 - b^2
    NameError: name 'a' is not defined
**********************************************************************
File "/home/jaap/work/downloads/sage-3.2.2/devel/sage/sage/rings/polynomial/multi_polynomial_ideal.py", line 69:
    sage: (a+b)^17
Exception raised:
    Traceback (most recent call last):
      File "/home/jaap/downloads/sage-3.2.2.alpha2/local/bin/ncadoctest.py", line 1231, in run_one_test
        self.run_one_example(test, example, filename, compileflags)
      File "/home/jaap/downloads/sage-3.2.2.alpha2/local/bin/sagedoctest.py", line 38, in run_one_example
        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)
      File "/home/jaap/downloads/sage-3.2.2.alpha2/local/bin/ncadoctest.py", line 1172, in run_one_example
        compileflags, 1) in test.globs
      File "<doctest __main__.example_0[18]>", line 1, in <module>
        (a+b)**Integer(17)###line 69:
    sage: (a+b)^17
    NameError: name 'a' is not defined
**********************************************************************
File "/home/jaap/work/downloads/sage-3.2.2/devel/sage/sage/rings/polynomial/multi_polynomial_ideal.py", line 71:
    sage: S(17) == 0
Exception raised:
    Traceback (most recent call last):
      File "/home/jaap/downloads/sage-3.2.2.alpha2/local/bin/ncadoctest.py", line 1231, in run_one_test
        self.run_one_example(test, example, filename, compileflags)
      File "/home/jaap/downloads/sage-3.2.2.alpha2/local/bin/sagedoctest.py", line 38, in run_one_example
        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)
      File "/home/jaap/downloads/sage-3.2.2.alpha2/local/bin/ncadoctest.py", line 1172, in run_one_example
        compileflags, 1) in test.globs
      File "<doctest __main__.example_0[19]>", line 1, in <module>
        S(Integer(17)) == Integer(0)###line 71:
    sage: S(17) == 0
    NameError: name 'S' is not defined
**********************************************************************
1 items had failures:
   4 of  45 in __main__.example_0
***Test Failed*** 4 failures.
For whitespace errors, see the file /home/jaap/downloads/sage-3.2.2/tmp/.doctest_multi_polynomial_ideal.py
	 [12.6 s]
exit code: 1024
 

```


Needs work

Jaap



---

archive/issue_comments_037001.json:
```json
{
    "body": "Oops, my bad, A patch on top of that is coming up once sage.math is running again.\n\nCheers,\n\nMichael",
    "created_at": "2008-12-26T19:13:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4882",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4882#issuecomment-37001",
    "user": "mabshoff"
}
```

Oops, my bad, A patch on top of that is coming up once sage.math is running again.

Cheers,

Michael



---

archive/issue_comments_037002.json:
```json
{
    "body": "Attachment",
    "created_at": "2008-12-26T22:26:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4882",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4882#issuecomment-37002",
    "user": "mabshoff"
}
```

Attachment



---

archive/issue_comments_037003.json:
```json
{
    "body": "Jaap,\n\na second patch to be applied on top of the other patch is up and should fix the issues. It even passes doctests now on my test box ;)\n\nCheers,\n\nMichael",
    "created_at": "2008-12-26T22:27:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4882",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4882#issuecomment-37003",
    "user": "mabshoff"
}
```

Jaap,

a second patch to be applied on top of the other patch is up and should fix the issues. It even passes doctests now on my test box ;)

Cheers,

Michael



---

archive/issue_comments_037004.json:
```json
{
    "body": "Now:\n\n```\nsage -t  \"devel/sage/sage/rings/polynomial/multi_polynomial_ideal.py\"\n\t [39.8 s]\n \n----------------------------------------------------------------------\nAll tests passed!\nTotal time for all tests: 39.8 seconds\n\n```\n\n\nCheers,\n\nJaap",
    "created_at": "2008-12-26T22:39:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4882",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4882#issuecomment-37004",
    "user": "jsp"
}
```

Now:

```
sage -t  "devel/sage/sage/rings/polynomial/multi_polynomial_ideal.py"
	 [39.8 s]
 
----------------------------------------------------------------------
All tests passed!
Total time for all tests: 39.8 seconds

```


Cheers,

Jaap



---

archive/issue_comments_037005.json:
```json
{
    "body": "Merged both patches in Sage 3.2.3.final",
    "created_at": "2008-12-26T22:45:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4882",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4882#issuecomment-37005",
    "user": "mabshoff"
}
```

Merged both patches in Sage 3.2.3.final



---

archive/issue_comments_037006.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-12-26T22:45:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4882",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4882#issuecomment-37006",
    "user": "mabshoff"
}
```

Resolution: fixed

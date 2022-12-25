# Issue 2531: pretty-print issue in fractions

archive/issues_002531.json:
```json
{
    "body": "Assignee: @williamstein\n\nCC:  @burcin\n\nSome symbolic fractions are not printed correctly:\n\n```\nsage: print z\n\n                                  arcsin(x)\n                                    -------\n                                       2\n```\n\nOne would expect the '-' bar to start under 'a' on the left.\n\nThis was found from an example in calculus.py:\n\n```\nsage: x = var('x')\nsage: y = x^2\nsage: dy = derivative(y,x)\nsage: z = integral(sqrt(1 + dy^2), x, 0, 2)\nsage: print z\n                     arcsinh(4) + 4 sqrt(17)\n                     ---------------------\n                               4\n```\n\nNote that the actual output I get with 2.10.3 slightly differs:\n\n```\nsage: print z\n\n                           arcsinh(4) + 4 sqrt(17)\n                             ---------------------\n                                       4\n\n```\n\nI wonder why sage -t calculus.py does not point that output difference.\n\nIssue created by migration from https://trac.sagemath.org/ticket/2531\n\n",
    "created_at": "2008-03-15T12:42:31Z",
    "labels": [
        "component: graphics",
        "minor",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-duplicate/invalid/wontfix",
    "title": "pretty-print issue in fractions",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/2531",
    "user": "https://github.com/zimmermann6"
}
```
Assignee: @williamstein

CC:  @burcin

Some symbolic fractions are not printed correctly:

```
sage: print z

                                  arcsin(x)
                                    -------
                                       2
```

One would expect the '-' bar to start under 'a' on the left.

This was found from an example in calculus.py:

```
sage: x = var('x')
sage: y = x^2
sage: dy = derivative(y,x)
sage: z = integral(sqrt(1 + dy^2), x, 0, 2)
sage: print z
                     arcsinh(4) + 4 sqrt(17)
                     ---------------------
                               4
```

Note that the actual output I get with 2.10.3 slightly differs:

```
sage: print z

                           arcsinh(4) + 4 sqrt(17)
                             ---------------------
                                       4

```

I wonder why sage -t calculus.py does not point that output difference.

Issue created by migration from https://trac.sagemath.org/ticket/2531





---

archive/issue_comments_017222.json:
```json
{
    "body": "The issue comes from Maxima using asinh instead of arcsinh.  Thus,  we're simply doing a substitution in the string that Maxima returns.  The testing framework doesn't catch it because it is set to ignore certain whitespace issues.\n\n\nI think a good, and probably not too difficult task would be to have our own native pretty printer.  I believe there is already one in Sympy that we could make use of.",
    "created_at": "2008-03-15T15:12:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2531",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2531#issuecomment-17222",
    "user": "https://github.com/mwhansen"
}
```

The issue comes from Maxima using asinh instead of arcsinh.  Thus,  we're simply doing a substitution in the string that Maxima returns.  The testing framework doesn't catch it because it is set to ignore certain whitespace issues.


I think a good, and probably not too difficult task would be to have our own native pretty printer.  I believe there is already one in Sympy that we could make use of.



---

archive/issue_comments_017223.json:
```json
{
    "body": "Would it be possible to do the substitution asinh -> arcsinh within Maxima, and then calling\nMaxima's pretty printer?",
    "created_at": "2008-03-15T22:34:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2531",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2531#issuecomment-17223",
    "user": "https://github.com/zimmermann6"
}
```

Would it be possible to do the substitution asinh -> arcsinh within Maxima, and then calling
Maxima's pretty printer?



---

archive/issue_comments_017224.json:
```json
{
    "body": "I have no idea how that'd be done.",
    "created_at": "2008-03-15T22:36:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2531",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2531#issuecomment-17224",
    "user": "https://github.com/mwhansen"
}
```

I have no idea how that'd be done.



---

archive/issue_comments_017225.json:
```json
{
    "body": "Since we don't use Maxima's pretty-printing anymore, I'm going to close this as invalid.",
    "created_at": "2009-10-05T07:23:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2531",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2531#issuecomment-17225",
    "user": "https://github.com/mwhansen"
}
```

Since we don't use Maxima's pretty-printing anymore, I'm going to close this as invalid.



---

archive/issue_comments_017226.json:
```json
{
    "body": "Resolution: invalid",
    "created_at": "2009-10-05T07:23:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2531",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2531#issuecomment-17226",
    "user": "https://github.com/mwhansen"
}
```

Resolution: invalid



---

archive/issue_events_005933.json:
```json
{
    "actor": "https://github.com/mwhansen",
    "created_at": "2009-10-05T07:23:38Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/2531",
    "milestone": "sage-duplicate/invalid/wontfix",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/2531#event-5933"
}
```



---

archive/issue_events_005934.json:
```json
{
    "actor": "https://github.com/mwhansen",
    "created_at": "2009-10-05T07:23:38Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/2531",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/2531#event-5934"
}
```

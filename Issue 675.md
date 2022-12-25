# Issue 675: Solaris 10: random_element: "ValueError: denominator must not be 0"

archive/issues_000675.json:
```json
{
    "body": "Assignee: @williamstein\n\nKeywords: Solaris 10\n\n\n```\nFile \"tut.py\", line 1373:\n    : A = M.random_element(density = 0.05)\nException raised:\n    Traceback (most recent call last):\n      File \"/export/home/mabshoff/sage-2.8.4.2/local/lib/python2.5/doctest.py\", line 1212, in __run\n        compileflags, 1) in test.globs\n      File \"<doctest __main__.example_53[1]>\", line 1, in <module>\n        _= A = M.random_element(density = RealNumber('0.05'))###line 1373:\n    : A = M.random_element(density = 0.05)\n      File \"/export/home/mabshoff/sage-2.8.4.2/local/lib/python2.5/site-packages/sage/matrix/matrix_space.py\", line 753, in random_element\n        Z.randomize(density, *args, **kwds)\n      File \"matrix2.pyx\", line 2595, in matrix2.Matrix.randomize\n      File \"/export/home/mabshoff/sage-2.8.4.2/local/lib/python2.5/site-packages/sage/rings/rational_field.py\", line 342, in random_element\n        ZZ.random_element(distribution=distribution)))\n      File \"/export/home/mabshoff/sage-2.8.4.2/local/lib/python2.5/site-packages/sage/rings/rational_field.py\", line 182, in __call__\n        return sage.rings.rational.Rational(x, base)\n      File \"rational.pyx\", line 160, in rational.Rational.__init__\n      File \"rational.pyx\", line 248, in rational.Rational.__set_value\n    ValueError: denominator must not be 0\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/675\n\n",
    "created_at": "2007-09-17T00:38:46Z",
    "labels": [
        "component: packages",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-2.10.1",
    "title": "Solaris 10: random_element: \"ValueError: denominator must not be 0\"",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/675",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```
Assignee: @williamstein

Keywords: Solaris 10


```
File "tut.py", line 1373:
    : A = M.random_element(density = 0.05)
Exception raised:
    Traceback (most recent call last):
      File "/export/home/mabshoff/sage-2.8.4.2/local/lib/python2.5/doctest.py", line 1212, in __run
        compileflags, 1) in test.globs
      File "<doctest __main__.example_53[1]>", line 1, in <module>
        _= A = M.random_element(density = RealNumber('0.05'))###line 1373:
    : A = M.random_element(density = 0.05)
      File "/export/home/mabshoff/sage-2.8.4.2/local/lib/python2.5/site-packages/sage/matrix/matrix_space.py", line 753, in random_element
        Z.randomize(density, *args, **kwds)
      File "matrix2.pyx", line 2595, in matrix2.Matrix.randomize
      File "/export/home/mabshoff/sage-2.8.4.2/local/lib/python2.5/site-packages/sage/rings/rational_field.py", line 342, in random_element
        ZZ.random_element(distribution=distribution)))
      File "/export/home/mabshoff/sage-2.8.4.2/local/lib/python2.5/site-packages/sage/rings/rational_field.py", line 182, in __call__
        return sage.rings.rational.Rational(x, base)
      File "rational.pyx", line 160, in rational.Rational.__init__
      File "rational.pyx", line 248, in rational.Rational.__set_value
    ValueError: denominator must not be 0
```


Issue created by migration from https://trac.sagemath.org/ticket/675





---

archive/issue_comments_003488.json:
```json
{
    "body": "Changing component from packages to doctest.",
    "created_at": "2007-09-17T01:24:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/675",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/675#issuecomment-3488",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Changing component from packages to doctest.



---

archive/issue_comments_003489.json:
```json
{
    "body": "Changing assignee from @williamstein to failure.",
    "created_at": "2007-09-17T01:24:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/675",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/675#issuecomment-3489",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Changing assignee from @williamstein to failure.



---

archive/issue_events_001799.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2008-01-20T20:14:41Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/675",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/675#event-1799"
}
```



---

archive/issue_comments_003490.json:
```json
{
    "body": "This has been fixed in 2.9.x when making sure that 64 bits values in 32 bit mode on Solaris are long long.\n\nCheers,\n\nMichael",
    "created_at": "2008-01-20T20:14:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/675",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/675#issuecomment-3490",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

This has been fixed in 2.9.x when making sure that 64 bits values in 32 bit mode on Solaris are long long.

Cheers,

Michael



---

archive/issue_comments_003491.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-01-20T20:14:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/675",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/675#issuecomment-3491",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed

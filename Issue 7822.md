# Issue 7822: pynac log function cannot handle float arguments <= 0

archive/issues_007822.json:
```json
{
    "body": "Assignee: burcin\n\nCC:  jason\n\nAfter changes in #7490 to sage.symbolic.pynac.py_log, symbolic log function cannot handle float arguments <= 0:\n\n\n```\nsage: from sage.functions.log import function_log\n---------------------------------------------------------------------------\nValueError                                Traceback (most recent call last)\n\n/home/burcin/.sage/temp/karr/16530/_home_burcin__sage_init_sage_0.py in <module>()\n\n/home/burcin/sage/sage-4.3/local/lib/python2.6/site-packages/sage/symbolic/function.so in sage.symbolic.function.GinacFunction.__call__ (sage/symbolic/function.cpp:5305)()\n\n/home/burcin/sage/sage-4.3/local/lib/python2.6/site-packages/sage/symbolic/function.so in sage.symbolic.function.Function.__call__ (sage/symbolic/function.cpp:3560)()\n\n/home/burcin/sage/sage-4.3/local/lib/python2.6/site-packages/sage/symbolic/pynac.so in sage.symbolic.pynac.py_log (sage/symbolic/pynac.cpp:10778)()\n\nValueError: math domain error\n```\n\n\nAttached patch fixes the problem.\n\nIssue created by migration from https://trac.sagemath.org/ticket/7822\n\n",
    "created_at": "2010-01-03T01:10:54Z",
    "labels": [
        "symbolics",
        "major",
        "bug"
    ],
    "title": "pynac log function cannot handle float arguments <= 0",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/7822",
    "user": "burcin"
}
```
Assignee: burcin

CC:  jason

After changes in #7490 to sage.symbolic.pynac.py_log, symbolic log function cannot handle float arguments <= 0:


```
sage: from sage.functions.log import function_log
---------------------------------------------------------------------------
ValueError                                Traceback (most recent call last)

/home/burcin/.sage/temp/karr/16530/_home_burcin__sage_init_sage_0.py in <module>()

/home/burcin/sage/sage-4.3/local/lib/python2.6/site-packages/sage/symbolic/function.so in sage.symbolic.function.GinacFunction.__call__ (sage/symbolic/function.cpp:5305)()

/home/burcin/sage/sage-4.3/local/lib/python2.6/site-packages/sage/symbolic/function.so in sage.symbolic.function.Function.__call__ (sage/symbolic/function.cpp:3560)()

/home/burcin/sage/sage-4.3/local/lib/python2.6/site-packages/sage/symbolic/pynac.so in sage.symbolic.pynac.py_log (sage/symbolic/pynac.cpp:10778)()

ValueError: math domain error
```


Attached patch fixes the problem.

Issue created by migration from https://trac.sagemath.org/ticket/7822





---

archive/issue_comments_067707.json:
```json
{
    "body": "Attachment [trac_7822-py_log.patch](tarball://root/attachments/some-uuid/ticket7822/trac_7822-py_log.patch) by burcin created at 2010-01-03 01:30:15\n\nmake py_log handle float arguments",
    "created_at": "2010-01-03T01:30:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7822",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7822#issuecomment-67707",
    "user": "burcin"
}
```

Attachment [trac_7822-py_log.patch](tarball://root/attachments/some-uuid/ticket7822/trac_7822-py_log.patch) by burcin created at 2010-01-03 01:30:15

make py_log handle float arguments



---

archive/issue_comments_067708.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-01-03T01:31:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7822",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7822#issuecomment-67708",
    "user": "burcin"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_067709.json:
```json
{
    "body": "This looks nice, but causes a serious speed regression:\n\nBEFORE:\n\n```\nsage: %timeit ln(complex(-1))\n10000 loops, best of 3: 29 \u00b5s per loop\nsage: %timeit log(complex(-1))\n10000 loops, best of 3: 43.2 \u00b5s per loop\n```\n\n\nAFTER:\n\n```\nsage: %timeit ln(complex(-1))\n1000 loops, best of 3: 1.47 ms per loop\nsage: %timeit log(complex(-1))\n100 loops, best of 3: 1.47 ms per loop\n```\n\n\nCan this be fixed easily?",
    "created_at": "2010-01-03T05:06:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7822",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7822#issuecomment-67709",
    "user": "jason"
}
```

This looks nice, but causes a serious speed regression:

BEFORE:

```
sage: %timeit ln(complex(-1))
10000 loops, best of 3: 29 µs per loop
sage: %timeit log(complex(-1))
10000 loops, best of 3: 43.2 µs per loop
```


AFTER:

```
sage: %timeit ln(complex(-1))
1000 loops, best of 3: 1.47 ms per loop
sage: %timeit log(complex(-1))
100 loops, best of 3: 1.47 ms per loop
```


Can this be fixed easily?



---

archive/issue_comments_067710.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2010-01-03T05:06:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7822",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7822#issuecomment-67710",
    "user": "jason"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_067711.json:
```json
{
    "body": "Also, there are an awful lot of \"ln\"s when I thought we were trying to get away from those and using \"log\"s.  It makes sense to keep some, but maybe some should be changed to log to show preferred usage?",
    "created_at": "2010-01-13T13:24:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7822",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7822#issuecomment-67711",
    "user": "kcrisman"
}
```

Also, there are an awful lot of "ln"s when I thought we were trying to get away from those and using "log"s.  It makes sense to keep some, but maybe some should be changed to log to show preferred usage?



---

archive/issue_comments_067712.json:
```json
{
    "body": "Attachment [trac_7822-py_log.take2.patch](tarball://root/attachments/some-uuid/ticket7822/trac_7822-py_log.take2.patch) by burcin created at 2010-01-17 01:12:05\n\nsecond try, faster this time",
    "created_at": "2010-01-17T01:12:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7822",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7822#issuecomment-67712",
    "user": "burcin"
}
```

Attachment [trac_7822-py_log.take2.patch](tarball://root/attachments/some-uuid/ticket7822/trac_7822-py_log.take2.patch) by burcin created at 2010-01-17 01:12:05

second try, faster this time



---

archive/issue_comments_067713.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2010-01-17T01:25:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7822",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7822#issuecomment-67713",
    "user": "burcin"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_067714.json:
```json
{
    "body": "attachment:trac_7822-py_log.take2.patch fixes the speed problems, although it is still not as fast as before. It depends on a very small patch to pynac. I will post a pynac package with the fix later this week.\n\nBefore:\n\n\n```\nsage: %timeit t = ln(float(-1))\n1000 loops, best of 3: 285 \u00b5s per loop\nsage: %timeit t = ln(float(1))\n100000 loops, best of 3: 17.5 \u00b5s per loop\nsage: %timeit t = ln(complex(1))\n100000 loops, best of 3: 6.25 \u00b5s per loop\nsage: %timeit t = ln(complex(1,1))\n100000 loops, best of 3: 6.4 \u00b5s per loop\nsage: %timeit t = ln(complex(1,-1))\n100000 loops, best of 3: 6.42 \u00b5s per loop\nsage: %timeit t = ln(complex(0))\n100000 loops, best of 3: 9.24 \u00b5s per loop\nsage: %timeit t = ln(complex(-1))\n100000 loops, best of 3: 6.21 \u00b5s per loop\n```\n\n\nAfter:\n\n\n```\nsage: %timeit t = ln(float(-1))\n100000 loops, best of 3: 15.2 \u00b5s per loop\nsage: %timeit t = ln(float(1))\n100000 loops, best of 3: 13.2 \u00b5s per loop\nsage: %timeit t = ln(complex(1))\n100000 loops, best of 3: 15 \u00b5s per loop\nsage: %timeit t = ln(complex(1,1))\n100000 loops, best of 3: 15.3 \u00b5s per loop\nsage: %timeit t = ln(complex(0))\n100000 loops, best of 3: 15.5 \u00b5s per loop\nsage: %timeit t = ln(complex(-1))\n100000 loops, best of 3: 15.1 \u00b5s per loop\n```\n\n\nRe comment:3:\n\nThe top level log function is a regular python function which handles precision, etc. Calling that in the doctest is not really testing the `Function_log` defined in `sage/functions/log.py`. If we want people to move away from using `ln`, we should deprecate it. Since the last discussion about this topic ended up by concluding we should even support printing `ln` instead of `log`, I don't see that happening soon.",
    "created_at": "2010-01-17T01:25:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7822",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7822#issuecomment-67714",
    "user": "burcin"
}
```

attachment:trac_7822-py_log.take2.patch fixes the speed problems, although it is still not as fast as before. It depends on a very small patch to pynac. I will post a pynac package with the fix later this week.

Before:


```
sage: %timeit t = ln(float(-1))
1000 loops, best of 3: 285 µs per loop
sage: %timeit t = ln(float(1))
100000 loops, best of 3: 17.5 µs per loop
sage: %timeit t = ln(complex(1))
100000 loops, best of 3: 6.25 µs per loop
sage: %timeit t = ln(complex(1,1))
100000 loops, best of 3: 6.4 µs per loop
sage: %timeit t = ln(complex(1,-1))
100000 loops, best of 3: 6.42 µs per loop
sage: %timeit t = ln(complex(0))
100000 loops, best of 3: 9.24 µs per loop
sage: %timeit t = ln(complex(-1))
100000 loops, best of 3: 6.21 µs per loop
```


After:


```
sage: %timeit t = ln(float(-1))
100000 loops, best of 3: 15.2 µs per loop
sage: %timeit t = ln(float(1))
100000 loops, best of 3: 13.2 µs per loop
sage: %timeit t = ln(complex(1))
100000 loops, best of 3: 15 µs per loop
sage: %timeit t = ln(complex(1,1))
100000 loops, best of 3: 15.3 µs per loop
sage: %timeit t = ln(complex(0))
100000 loops, best of 3: 15.5 µs per loop
sage: %timeit t = ln(complex(-1))
100000 loops, best of 3: 15.1 µs per loop
```


Re comment:3:

The top level log function is a regular python function which handles precision, etc. Calling that in the doctest is not really testing the `Function_log` defined in `sage/functions/log.py`. If we want people to move away from using `ln`, we should deprecate it. Since the last discussion about this topic ended up by concluding we should even support printing `ln` instead of `log`, I don't see that happening soon.



---

archive/issue_comments_067715.json:
```json
{
    "body": "New pynac package available here:\n\nhttp://sage.math.washington.edu/home/burcin/pynac/pynac-0.1.11.spkg\n\nA lot of other patches on trac depend on this one. I'd really appreciate a quick review. :)\n\nApply only attachment:trac_7822-py_log.take2.patch",
    "created_at": "2010-01-19T23:31:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7822",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7822#issuecomment-67715",
    "user": "burcin"
}
```

New pynac package available here:

http://sage.math.washington.edu/home/burcin/pynac/pynac-0.1.11.spkg

A lot of other patches on trac depend on this one. I'd really appreciate a quick review. :)

Apply only attachment:trac_7822-py_log.take2.patch



---

archive/issue_comments_067716.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-01-28T21:05:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7822",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7822#issuecomment-67716",
    "user": "kcrisman"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_067717.json:
```json
{
    "body": "All works okay, and after careful checking the patch seems correct, modulo my weak understanding of Cython.  I'll go ahead and put positive review, but someone please stop me if the whole PY_TYPE_CHECK stuff is not right.\n\nTo Burcin: In general, it would be very helpful if you could put a specific link to the changeset in Pynac (in the online hg server) which corresponds to each fix of a Sage issue.",
    "created_at": "2010-01-28T21:05:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7822",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7822#issuecomment-67717",
    "user": "kcrisman"
}
```

All works okay, and after careful checking the patch seems correct, modulo my weak understanding of Cython.  I'll go ahead and put positive review, but someone please stop me if the whole PY_TYPE_CHECK stuff is not right.

To Burcin: In general, it would be very helpful if you could put a specific link to the changeset in Pynac (in the online hg server) which corresponds to each fix of a Sage issue.



---

archive/issue_comments_067718.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-02-18T21:38:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7822",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7822#issuecomment-67718",
    "user": "mvngu"
}
```

Resolution: fixed



---

archive/issue_comments_067719.json:
```json
{
    "body": "Merged [trac_7822-py_log.take2.patch](http://trac.sagemath.org/sage_trac/attachment/ticket/7822/trac_7822-py_log.take2.patch).",
    "created_at": "2010-02-18T21:38:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7822",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7822#issuecomment-67719",
    "user": "mvngu"
}
```

Merged [trac_7822-py_log.take2.patch](http://trac.sagemath.org/sage_trac/attachment/ticket/7822/trac_7822-py_log.take2.patch).

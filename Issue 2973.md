# Issue 2973: RDF doctest failures on arch linux (gcc 4.3)

archive/issues_002973.json:
```json
{
    "body": "Assignee: somebody\n\n\n```\nsage -t  devel/sage/sage/rings/real_double.pyx              **********************************************************************\nFile \"/home/was/build/sage-3.0.rc0/tmp/real_double.py\", line 544:\n    sage: a = -RDF(1)/RDF(0); a.str()\nExpected:\n    '-inf'\nGot:\n    'inf'\n**********************************************************************\nFile \"/home/was/build/sage-3.0.rc0/tmp/real_double.py\", line 979:\n    sage: a.is_positive_infinity()\nExpected:\n    False\nGot:\n    True\n**********************************************************************\nFile \"/home/was/build/sage-3.0.rc0/tmp/real_double.py\", line 991:\n    sage: a.is_negative_infinity()\nExpected:\n    True\nGot:\n    False\n**********************************************************************\n3 items had failures:\n   1 of   6 in __main__.example_35\n   1 of   5 in __main__.example_67\n   1 of   5 in __main__.example_68\n***Test Failed*** 3 failures.\n\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/2973\n\n",
    "created_at": "2008-04-20T21:03:23Z",
    "labels": [
        "basic arithmetic",
        "blocker",
        "bug"
    ],
    "title": "RDF doctest failures on arch linux (gcc 4.3)",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/2973",
    "user": "was"
}
```
Assignee: somebody


```
sage -t  devel/sage/sage/rings/real_double.pyx              **********************************************************************
File "/home/was/build/sage-3.0.rc0/tmp/real_double.py", line 544:
    sage: a = -RDF(1)/RDF(0); a.str()
Expected:
    '-inf'
Got:
    'inf'
**********************************************************************
File "/home/was/build/sage-3.0.rc0/tmp/real_double.py", line 979:
    sage: a.is_positive_infinity()
Expected:
    False
Got:
    True
**********************************************************************
File "/home/was/build/sage-3.0.rc0/tmp/real_double.py", line 991:
    sage: a.is_negative_infinity()
Expected:
    True
Got:
    False
**********************************************************************
3 items had failures:
   1 of   6 in __main__.example_35
   1 of   5 in __main__.example_67
   1 of   5 in __main__.example_68
***Test Failed*** 3 failures.

```


Issue created by migration from https://trac.sagemath.org/ticket/2973





---

archive/issue_comments_020485.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2008-04-20T22:53:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2973",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2973#issuecomment-20485",
    "user": "mabshoff"
}
```

Changing status from new to assigned.



---

archive/issue_comments_020486.json:
```json
{
    "body": "I know how to fix this. Spkg coming up.\n\nCheers,\n\nMichael",
    "created_at": "2008-04-20T22:53:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2973",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2973#issuecomment-20486",
    "user": "mabshoff"
}
```

I know how to fix this. Spkg coming up.

Cheers,

Michael



---

archive/issue_comments_020487.json:
```json
{
    "body": "Changing assignee from somebody to mabshoff.",
    "created_at": "2008-04-20T22:53:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2973",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2973#issuecomment-20487",
    "user": "mabshoff"
}
```

Changing assignee from somebody to mabshoff.



---

archive/issue_comments_020488.json:
```json
{
    "body": "The fix is to use GSL's isinf in all cases and not only on OSX. Hence the diff is minimal in spkg-install. The spkg can be found at\n\nhttp://sage.math.washington.edu/home/mabshoff/release-cycles-3.0/rc1/gsl-1.10.p1.spkg\n\nCheers,\n\nMichael",
    "created_at": "2008-04-21T04:00:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2973",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2973#issuecomment-20488",
    "user": "mabshoff"
}
```

The fix is to use GSL's isinf in all cases and not only on OSX. Hence the diff is minimal in spkg-install. The spkg can be found at

http://sage.math.washington.edu/home/mabshoff/release-cycles-3.0/rc1/gsl-1.10.p1.spkg

Cheers,

Michael



---

archive/issue_comments_020489.json:
```json
{
    "body": "works for me and the changes to the spkg look good.",
    "created_at": "2008-04-21T04:40:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2973",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2973#issuecomment-20489",
    "user": "was"
}
```

works for me and the changes to the spkg look good.



---

archive/issue_comments_020490.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-04-21T04:54:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2973",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2973#issuecomment-20490",
    "user": "mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_020491.json:
```json
{
    "body": "Merged in Sage 3.0.rc1",
    "created_at": "2008-04-21T04:54:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2973",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2973#issuecomment-20491",
    "user": "mabshoff"
}
```

Merged in Sage 3.0.rc1

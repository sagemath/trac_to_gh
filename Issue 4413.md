# Issue 4413: '?' in docstring gets interpreted immediately by the parser

archive/issues_004413.json:
```json
{
    "body": "Assignee: was\n\nThe following code, entered in the command-line interface to Sage, shows the effect:\n\n```\nsage: def foo(x):\n   ....:     '''\n   ....:     Eh?\nObject `Eh` not found.\n   ....:     '''\n   ....:     return x\n   ....: \n```\n\nThe parser appears to act on the '?' right away, rather than wait for the end of the thing being defined (or realizing that '?' in this case is not to be acted on).\n\nThe effect shows up with both single- and double- quotes, and with and without the \"raw\" qualifier (r!''').\n\nThis may be related to Trac#4405.\n\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/4413\n\n",
    "created_at": "2008-10-31T21:05:37Z",
    "labels": [
        "user interface",
        "major",
        "bug"
    ],
    "title": "'?' in docstring gets interpreted immediately by the parser",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/4413",
    "user": "justin"
}
```
Assignee: was

The following code, entered in the command-line interface to Sage, shows the effect:

```
sage: def foo(x):
   ....:     '''
   ....:     Eh?
Object `Eh` not found.
   ....:     '''
   ....:     return x
   ....: 
```

The parser appears to act on the '?' right away, rather than wait for the end of the thing being defined (or realizing that '?' in this case is not to be acted on).

The effect shows up with both single- and double- quotes, and with and without the "raw" qualifier (r!''').

This may be related to Trac#4405.



Issue created by migration from https://trac.sagemath.org/ticket/4413





---

archive/issue_comments_032465.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2009-01-23T13:19:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4413",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4413#issuecomment-32465",
    "user": "mhansen"
}
```

Changing status from new to assigned.



---

archive/issue_comments_032466.json:
```json
{
    "body": "Changing assignee from was to mhansen.",
    "created_at": "2009-01-23T13:19:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4413",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4413#issuecomment-32466",
    "user": "mhansen"
}
```

Changing assignee from was to mhansen.



---

archive/issue_comments_032467.json:
```json
{
    "body": "This is not related to #4405.  In fact, it is an IPython bug.  I've reported it here: http://lists.ipython.scipy.org/pipermail/ipython-dev/2009-January/004812.html",
    "created_at": "2009-01-23T13:19:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4413",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4413#issuecomment-32467",
    "user": "mhansen"
}
```

This is not related to #4405.  In fact, it is an IPython bug.  I've reported it here: http://lists.ipython.scipy.org/pipermail/ipython-dev/2009-January/004812.html



---

archive/issue_comments_032468.json:
```json
{
    "body": "This is fixed in IPython 0.12.  We should close this when #12719 gets closed.",
    "created_at": "2012-03-29T07:46:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4413",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4413#issuecomment-32468",
    "user": "mhansen"
}
```

This is fixed in IPython 0.12.  We should close this when #12719 gets closed.



---

archive/issue_comments_032469.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2012-03-29T07:55:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4413",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4413#issuecomment-32469",
    "user": "kini"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_032470.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2012-03-29T07:56:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4413",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4413#issuecomment-32470",
    "user": "kini"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_032471.json:
```json
{
    "body": "Resolution: duplicate",
    "created_at": "2013-01-25T09:47:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4413",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4413#issuecomment-32471",
    "user": "jdemeyer"
}
```

Resolution: duplicate

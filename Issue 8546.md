# Issue 8546: add section on deprecating functions to developer's guide

archive/issues_008546.json:
```json
{
    "body": "Assignee: mvngu\n\nCC:  @kcrisman\n\nMany functions in the Sage library are deprecated, and we seem to have a standard framework in place for informing users that functions are deprecated, but there is no documentation of this in the developers' guide.\n\nIt seems like the proper way to deprecate a function is like this: if we start with\n\n```\ndef f(x):\n  body of function\n  return something\n```\n\nthen one should change it like so to deprecate it:\n\n```\ndef f(x)\n  from sage.misc.misc import deprecation\n  deprecation(\"f() is deprecated and will be removed in a future version of Sage. Use g() instead.\")\n  body of function\n  return something \n```\n\nOne should also change doctests appropriately; if one had\n\n```\nsage: f(1)\n'foo'\n```\n\nthen it should get changed to\n\n```\nsage: f(1)\ndoctest:...: DeprecationWarning: f() is deprecated and will be removed in a future version of Sage. Use g() instead.\n'foo'\n```\n\nAlso, the documentation should be changed to reflect this! It's a good idea to describe what users should do instead of using the deprecated function, so that it is easy for them to change their code.\n\nIdeally we would also have a policy about how long deprecated functions stay in Sage before being removed, but AFAIK no strong consensus on a time period or specific policy exists. If there is one, it should be put into the developer's guide!\n\nIn any case, it is probably a good idea to specify the date or Sage version in which a function was deprecated (even if it's just \"March 2010\") to give users an idea of how \"stale\" a function is and how close to removal it is. \n\nIssue created by migration from https://trac.sagemath.org/ticket/8546\n\n",
    "created_at": "2010-03-16T03:37:21Z",
    "labels": [
        "component: documentation"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-duplicate/invalid/wontfix",
    "title": "add section on deprecating functions to developer's guide",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/8546",
    "user": "https://github.com/dandrake"
}
```
Assignee: mvngu

CC:  @kcrisman

Many functions in the Sage library are deprecated, and we seem to have a standard framework in place for informing users that functions are deprecated, but there is no documentation of this in the developers' guide.

It seems like the proper way to deprecate a function is like this: if we start with

```
def f(x):
  body of function
  return something
```

then one should change it like so to deprecate it:

```
def f(x)
  from sage.misc.misc import deprecation
  deprecation("f() is deprecated and will be removed in a future version of Sage. Use g() instead.")
  body of function
  return something 
```

One should also change doctests appropriately; if one had

```
sage: f(1)
'foo'
```

then it should get changed to

```
sage: f(1)
doctest:...: DeprecationWarning: f() is deprecated and will be removed in a future version of Sage. Use g() instead.
'foo'
```

Also, the documentation should be changed to reflect this! It's a good idea to describe what users should do instead of using the deprecated function, so that it is easy for them to change their code.

Ideally we would also have a policy about how long deprecated functions stay in Sage before being removed, but AFAIK no strong consensus on a time period or specific policy exists. If there is one, it should be put into the developer's guide!

In any case, it is probably a good idea to specify the date or Sage version in which a function was deprecated (even if it's just "March 2010") to give users an idea of how "stale" a function is and how close to removal it is. 

Issue created by migration from https://trac.sagemath.org/ticket/8546





---

archive/issue_comments_077139.json:
```json
{
    "body": "On sage-devel, Florent Hivert recommends looking at tickets #7515, #7559, and #8073 for information related to this ticket.",
    "created_at": "2010-03-16T08:28:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8546",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8546#issuecomment-77139",
    "user": "https://github.com/dandrake"
}
```

On sage-devel, Florent Hivert recommends looking at tickets #7515, #7559, and #8073 for information related to this ticket.



---

archive/issue_comments_077140.json:
```json
{
    "body": "BTW, the thread on sage-devel is http://groups.google.com/group/sage-devel/browse_thread/thread/b809aff6e97085b9",
    "created_at": "2010-03-16T08:34:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8546",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8546#issuecomment-77140",
    "user": "https://github.com/dandrake"
}
```

BTW, the thread on sage-devel is http://groups.google.com/group/sage-devel/browse_thread/thread/b809aff6e97085b9



---

archive/issue_comments_077141.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2012-06-14T14:40:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8546",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8546#issuecomment-77141",
    "user": "https://github.com/kcrisman"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_077142.json:
```json
{
    "body": "This is superseded by #13109.",
    "created_at": "2012-06-14T14:40:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8546",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8546#issuecomment-77142",
    "user": "https://github.com/kcrisman"
}
```

This is superseded by #13109.



---

archive/issue_comments_077143.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2012-06-14T14:41:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8546",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8546#issuecomment-77143",
    "user": "https://github.com/kcrisman"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_events_008727.json:
```json
{
    "actor": "@jdemeyer",
    "created_at": "2012-06-28T08:34:42Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/8546",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/8546#event-8727"
}
```



---

archive/issue_comments_077144.json:
```json
{
    "body": "Resolution: duplicate",
    "created_at": "2012-06-28T08:34:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8546",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8546#issuecomment-77144",
    "user": "https://github.com/jdemeyer"
}
```

Resolution: duplicate

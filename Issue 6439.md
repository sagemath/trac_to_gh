# Issue 6439: doctests beginning with Sage: are silently ignored

archive/issues_006439.json:
```json
{
    "body": "Assignee: tbd\n\nCC:  @orlitzky\n\nThis doctest is silently ignored:\n\n\n```\nSage: 1+1\n45\n```\n\n\nI.e. no warning is displayed, and doctesting the file it is in produces no failures. This is because I wrote Sage: rather than sage:. I don't now if other capitalizations than \"sage\" should be accepted, but certainly they should not be silently ignored.\n\nI propose to report an error on \"Sage:\" or any other capitalization of that in any context where \"sage:\" would be interpreted as a doctest.\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/6439\n\n",
    "created_at": "2009-06-28T09:45:32Z",
    "labels": [
        "component: doctest coverage",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-duplicate/invalid/wontfix",
    "title": "doctests beginning with Sage: are silently ignored",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/6439",
    "user": "https://trac.sagemath.org/admin/accounts/users/broune"
}
```
Assignee: tbd

CC:  @orlitzky

This doctest is silently ignored:


```
Sage: 1+1
45
```


I.e. no warning is displayed, and doctesting the file it is in produces no failures. This is because I wrote Sage: rather than sage:. I don't now if other capitalizations than "sage" should be accepted, but certainly they should not be silently ignored.

I propose to report an error on "Sage:" or any other capitalization of that in any context where "sage:" would be interpreted as a doctest.


Issue created by migration from https://trac.sagemath.org/ticket/6439





---

archive/issue_comments_051592.json:
```json
{
    "body": "Is this **really** a problem?\n\n1. You shouldn't be re-typing your doctests by hand; you should copy/paste an actual sage session to avoid errors.\n2. This only affects one-line doctests, unless you make the same mistake more than once. For example any lines referencing `t` should fail if your first line is \"Sage: var('t')\".\n3. If there are N tests passing before you add yours, there should be N+1 passing afterwards.\n4. All patches are reviewed and this should certainly catch (3).",
    "created_at": "2011-12-14T20:03:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6439",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6439#issuecomment-51592",
    "user": "https://github.com/orlitzky"
}
```

Is this **really** a problem?

1. You shouldn't be re-typing your doctests by hand; you should copy/paste an actual sage session to avoid errors.
2. This only affects one-line doctests, unless you make the same mistake more than once. For example any lines referencing `t` should fail if your first line is "Sage: var('t')".
3. If there are N tests passing before you add yours, there should be N+1 passing afterwards.
4. All patches are reviewed and this should certainly catch (3).



---

archive/issue_comments_051593.json:
```json
{
    "body": "Yeah, this is developer error, IMO. \"Sage: 1+1\" is not recognized by the doctester as a test input line, and neither is \"Warning: 1+1\" or \"Hello: World\" or any other such examples. We don't (and obviously shouldn't) produce error messages for these other examples, and I see no reason why \"Sage:\" should get special treatment.",
    "created_at": "2012-01-03T23:36:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6439",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6439#issuecomment-51593",
    "user": "https://github.com/kini"
}
```

Yeah, this is developer error, IMO. "Sage: 1+1" is not recognized by the doctester as a test input line, and neither is "Warning: 1+1" or "Hello: World" or any other such examples. We don't (and obviously shouldn't) produce error messages for these other examples, and I see no reason why "Sage:" should get special treatment.



---

archive/issue_comments_051594.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2012-01-04T09:56:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6439",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6439#issuecomment-51594",
    "user": "https://github.com/loefflerd"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_051595.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2012-01-04T09:56:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6439",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6439#issuecomment-51595",
    "user": "https://github.com/loefflerd"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_051596.json:
```json
{
    "body": "Resolution: wontfix",
    "created_at": "2012-01-05T13:37:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6439",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6439#issuecomment-51596",
    "user": "https://github.com/jdemeyer"
}
```

Resolution: wontfix



---

archive/issue_events_006680.json:
```json
{
    "actor": "@jdemeyer",
    "created_at": "2012-01-05T13:37:00Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/6439",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/6439#event-6680"
}
```

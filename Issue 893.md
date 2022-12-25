# Issue 893: 2.8.7-alpha0: doctest failure in const.tex

archive/issues_000893.json:
```json
{
    "body": "Assignee: tba\n\nThere are three failures, but the last two are direct consequences of the first one:\n\n```\nFile \"const.py\", line 749:\n    sage: vals = E.Lseries_values_along_line(1-I, 1+10*I, 100) # critical line\nException raised:\n    Traceback (most recent call last):\n      File \"/home/cwitty/pre-sage/local/lib/python2.5/doctest.py\", line 1212, in\n __run\n        compileflags, 1) in test.globs\n      File \"<doctest __main__.example_22[1]>\", line 1, in <module>\n        vals = E.Lseries_values_along_line(Integer(1)-I, Integer(1)+Integer(10)*\nI, Integer(100)) # critical line###line 749:\n    sage: vals = E.Lseries_values_along_line(1-I, 1+10*I, 100) # critical line\n    AttributeError: 'EllipticCurve_rational_field' object has no attribute 'Lser\nies_values_along_line'\n```\n\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/893\n\n",
    "created_at": "2007-10-13T20:51:36Z",
    "labels": [
        "component: documentation",
        "blocker",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-2.8.7",
    "title": "2.8.7-alpha0: doctest failure in const.tex",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/893",
    "user": "https://trac.sagemath.org/admin/accounts/users/cwitty"
}
```
Assignee: tba

There are three failures, but the last two are direct consequences of the first one:

```
File "const.py", line 749:
    sage: vals = E.Lseries_values_along_line(1-I, 1+10*I, 100) # critical line
Exception raised:
    Traceback (most recent call last):
      File "/home/cwitty/pre-sage/local/lib/python2.5/doctest.py", line 1212, in
 __run
        compileflags, 1) in test.globs
      File "<doctest __main__.example_22[1]>", line 1, in <module>
        vals = E.Lseries_values_along_line(Integer(1)-I, Integer(1)+Integer(10)*
I, Integer(100)) # critical line###line 749:
    sage: vals = E.Lseries_values_along_line(1-I, 1+10*I, 100) # critical line
    AttributeError: 'EllipticCurve_rational_field' object has no attribute 'Lser
ies_values_along_line'
```



Issue created by migration from https://trac.sagemath.org/ticket/893





---

archive/issue_comments_005480.json:
```json
{
    "body": "This function was in 2.8.6 but is no longer in 2.8.7.  Was it deliberately removed?",
    "created_at": "2007-10-13T23:06:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/893",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/893#issuecomment-5480",
    "user": "https://trac.sagemath.org/admin/accounts/users/cwitty"
}
```

This function was in 2.8.6 but is no longer in 2.8.7.  Was it deliberately removed?



---

archive/issue_comments_005481.json:
```json
{
    "body": "This was caused by David Roe's refactoring of the ell_rational_field command.\nNow one does L = E.Lseries(), and there is a method\n    L.values_along_line(...)",
    "created_at": "2007-10-13T23:29:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/893",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/893#issuecomment-5481",
    "user": "https://github.com/williamstein"
}
```

This was caused by David Roe's refactoring of the ell_rational_field command.
Now one does L = E.Lseries(), and there is a method
    L.values_along_line(...)



---

archive/issue_comments_005482.json:
```json
{
    "body": "Attachment [trac893.patch](tarball://root/attachments/some-uuid/ticket893/trac893.patch) by @roed314 created at 2007-10-14 03:08:13\n\nText patch fixing the doctest",
    "created_at": "2007-10-14T03:08:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/893",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/893#issuecomment-5482",
    "user": "https://github.com/roed314"
}
```

Attachment [trac893.patch](tarball://root/attachments/some-uuid/ticket893/trac893.patch) by @roed314 created at 2007-10-14 03:08:13

Text patch fixing the doctest



---

archive/issue_comments_005483.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2007-10-14T22:54:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/893",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/893#issuecomment-5483",
    "user": "https://github.com/williamstein"
}
```

Resolution: fixed



---

archive/issue_events_002474.json:
```json
{
    "actor": "https://github.com/williamstein",
    "created_at": "2007-10-14T22:54:12Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/893",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/893#event-2474"
}
```

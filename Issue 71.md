# Issue 71: Secret transation of .sage to .py causes confusion

archive/issues_000071.json:
```json
{
    "body": "Assignee: somebody\n\nWhen a .sage file is \"load\"ed or \"attach\"ed, it gets translated to a .py file before being processed; the result is a file with different structure than the original.  Any errors are described in terms of the .py file, not the .sage file.  I realize this is a kind of Catch-22, but is there a way to (as the C preprocessor does) keep the .sage line numbers?\n\nOf course this requires that Python have that ability, because it reports the errors.\n\nI suppose the proper solution, given this, is to document the issue.\n\nI think this points up an aspect of a fundamental issue: SAGE is a programming language/system; SAGE is a computer system for mathematicians to use.  I'm not sure how good it can be at both.\n\nIssue created by migration from https://trac.sagemath.org/ticket/71\n\n",
    "created_at": "2006-09-20T21:40:01Z",
    "labels": [
        "basic arithmetic",
        "minor",
        "bug"
    ],
    "title": "Secret transation of .sage to .py causes confusion",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/71",
    "user": "Justin Walker (justin@mac.com)"
}
```
Assignee: somebody

When a .sage file is "load"ed or "attach"ed, it gets translated to a .py file before being processed; the result is a file with different structure than the original.  Any errors are described in terms of the .py file, not the .sage file.  I realize this is a kind of Catch-22, but is there a way to (as the C preprocessor does) keep the .sage line numbers?

Of course this requires that Python have that ability, because it reports the errors.

I suppose the proper solution, given this, is to document the issue.

I think this points up an aspect of a fundamental issue: SAGE is a programming language/system; SAGE is a computer system for mathematicians to use.  I'm not sure how good it can be at both.

Issue created by migration from https://trac.sagemath.org/ticket/71





---

archive/issue_comments_000362.json:
```json
{
    "body": "SAGE can embed the original line numbers in the .py file, and even the original\n.sage lines (before parsing) in the .sage file.  Then the error messages will\nalso list the original line number (and line, if you want) in a comment at the end\nof the line.   In the notebook, at least, it would be easy to postparse the error\nmessages so they refer to the original .sage file.",
    "created_at": "2006-09-21T01:27:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/71",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/71#issuecomment-362",
    "user": "was"
}
```

SAGE can embed the original line numbers in the .py file, and even the original
.sage lines (before parsing) in the .sage file.  Then the error messages will
also list the original line number (and line, if you want) in a comment at the end
of the line.   In the notebook, at least, it would be easy to postparse the error
messages so they refer to the original .sage file.



---

archive/issue_comments_000363.json:
```json
{
    "body": "Changing type from defect to enhancement.",
    "created_at": "2007-01-13T02:15:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/71",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/71#issuecomment-363",
    "user": "was"
}
```

Changing type from defect to enhancement.



---

archive/issue_comments_000364.json:
```json
{
    "body": "This is not a bug.",
    "created_at": "2007-01-13T02:15:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/71",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/71#issuecomment-364",
    "user": "was"
}
```

This is not a bug.



---

archive/issue_comments_000365.json:
```json
{
    "body": "Changing component from basic arithmetic to misc.",
    "created_at": "2009-06-07T13:16:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/71",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/71#issuecomment-365",
    "user": "davidloeffler"
}
```

Changing component from basic arithmetic to misc.



---

archive/issue_comments_000366.json:
```json
{
    "body": "Changing assignee from somebody to cwitty.",
    "created_at": "2009-06-07T13:16:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/71",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/71#issuecomment-366",
    "user": "davidloeffler"
}
```

Changing assignee from somebody to cwitty.



---

archive/issue_comments_000367.json:
```json
{
    "body": "Hi.  This is a REALLY old ticket.  Is the documentation at [the programming tutorial](http://www.sagemath.org/doc/tutorial/programming.html) now sufficient, or should we still keep this ticket around?  I love the idea in William's (six-year-old) comment:1, so we could repurpose this ticket to implement this if desired.  Or, one could just improve the documentation a little to mention that errors refer to lines in the .py file.",
    "created_at": "2013-01-29T20:21:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/71",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/71#issuecomment-367",
    "user": "kcrisman"
}
```

Hi.  This is a REALLY old ticket.  Is the documentation at [the programming tutorial](http://www.sagemath.org/doc/tutorial/programming.html) now sufficient, or should we still keep this ticket around?  I love the idea in William's (six-year-old) comment:1, so we could repurpose this ticket to implement this if desired.  Or, one could just improve the documentation a little to mention that errors refer to lines in the .py file.



---

archive/issue_comments_000368.json:
```json
{
    "body": "Branch pushed to git repo; I updated commit sha1. This was a forced push. New commits:",
    "created_at": "2014-11-20T16:50:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/71",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/71#issuecomment-368",
    "user": "git"
}
```

Branch pushed to git repo; I updated commit sha1. This was a forced push. New commits:



---

archive/issue_comments_000369.json:
```json
{
    "body": "Branch pushed to git repo; I updated commit sha1. This was a forced push. New commits:",
    "created_at": "2014-11-20T20:59:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/71",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/71#issuecomment-369",
    "user": "git"
}
```

Branch pushed to git repo; I updated commit sha1. This was a forced push. New commits:



---

archive/issue_comments_000370.json:
```json
{
    "body": "Branch pushed to git repo; I updated commit sha1. This was a forced push. New commits:",
    "created_at": "2014-11-20T22:17:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/71",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/71#issuecomment-370",
    "user": "git"
}
```

Branch pushed to git repo; I updated commit sha1. This was a forced push. New commits:



---

archive/issue_comments_000371.json:
```json
{
    "body": "Branch pushed to git repo; I updated commit sha1. This was a forced push. New commits:",
    "created_at": "2014-11-21T06:21:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/71",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/71#issuecomment-371",
    "user": "git"
}
```

Branch pushed to git repo; I updated commit sha1. This was a forced push. New commits:



---

archive/issue_comments_000372.json:
```json
{
    "body": "Branch pushed to git repo; I updated commit sha1. This was a forced push. New commits:",
    "created_at": "2014-11-23T10:55:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/71",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/71#issuecomment-372",
    "user": "git"
}
```

Branch pushed to git repo; I updated commit sha1. This was a forced push. New commits:

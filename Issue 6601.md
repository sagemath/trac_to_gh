# Issue 6601: Crash loading rings.polynomial.pbori

archive/issues_006601.json:
```json
{
    "body": "Assignee: tbd\n\nI tried to run a script and python crashed trying to load pbori. Sage_crash_report.txt is attached.\n\nIssue created by migration from https://trac.sagemath.org/ticket/6601\n\n",
    "created_at": "2009-07-23T12:14:56Z",
    "labels": [
        "algebra",
        "major",
        "bug"
    ],
    "title": "Crash loading rings.polynomial.pbori",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/6601",
    "user": "stankewicz"
}
```
Assignee: tbd

I tried to run a script and python crashed trying to load pbori. Sage_crash_report.txt is attached.

Issue created by migration from https://trac.sagemath.org/ticket/6601





---

archive/issue_comments_054029.json:
```json
{
    "body": "Attachment\n\nIt looks like you're using Sage 3.4.1. Would it be possible to try your script with a more recent version of Sage (like 4.1, the most recent as of now) and see whether you still get an error?",
    "created_at": "2009-07-29T00:12:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6601",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6601#issuecomment-54029",
    "user": "wcauchois"
}
```

Attachment

It looks like you're using Sage 3.4.1. Would it be possible to try your script with a more recent version of Sage (like 4.1, the most recent as of now) and see whether you still get an error?



---

archive/issue_comments_054030.json:
```json
{
    "body": "Importing individual modules without initializing sage by doing `import sage.all` is not supported. You should add a line with\n\n\n```\nimport sage.all\n```\n\n\nat the beginning of your script.",
    "created_at": "2010-01-16T23:30:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6601",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6601#issuecomment-54030",
    "user": "burcin"
}
```

Importing individual modules without initializing sage by doing `import sage.all` is not supported. You should add a line with


```
import sage.all
```


at the beginning of your script.



---

archive/issue_comments_054031.json:
```json
{
    "body": "Resolution: invalid",
    "created_at": "2010-01-16T23:30:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6601",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6601#issuecomment-54031",
    "user": "burcin"
}
```

Resolution: invalid

# Issue 2411: Missing references in Sage tutorial

archive/issues_002411.json:
```json
{
    "body": "Assignee: tba\n\nOn the page\n\nhttp://www.sagemath.org/doc/html/tut/node16.html\n\nin the second paragraph the following sentence has problems.\n\n\"Note that the Sage kernel of a matrix $A$ is the ``left kernel'', i.e. the space of vectors 33#1 such that 34#2.\"\n\nI'm not exactly sure what 33#1 and 34#2 should be, but these symbols certainly don't make sense.\n\nIssue created by migration from https://trac.sagemath.org/ticket/2411\n\n",
    "created_at": "2008-03-06T22:36:13Z",
    "labels": [
        "documentation",
        "minor",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.1.2",
    "title": "Missing references in Sage tutorial",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/2411",
    "user": "rhinton"
}
```
Assignee: tba

On the page

http://www.sagemath.org/doc/html/tut/node16.html

in the second paragraph the following sentence has problems.

"Note that the Sage kernel of a matrix $A$ is the ``left kernel'', i.e. the space of vectors 33#1 such that 34#2."

I'm not exactly sure what 33#1 and 34#2 should be, but these symbols certainly don't make sense.

Issue created by migration from https://trac.sagemath.org/ticket/2411





---

archive/issue_comments_016275.json:
```json
{
    "body": "The tex file says:\n\n```\nNote that the \\sage kernel of a matrix $A$ is the ``left kernel'', i.e.\nthe space of vectors $w$ such that $wA=0$.\n```\n\nI assume that ```left kernel''` confuses tex2html, so changing that to emph might fix the issue.\n\nCheers,\n\nMichael",
    "created_at": "2008-03-07T22:27:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2411",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2411#issuecomment-16275",
    "user": "mabshoff"
}
```

The tex file says:

```
Note that the \sage kernel of a matrix $A$ is the ``left kernel'', i.e.
the space of vectors $w$ such that $wA=0$.
```

I assume that ```left kernel''` confuses tex2html, so changing that to emph might fix the issue.

Cheers,

Michael



---

archive/issue_comments_016276.json:
```json
{
    "body": "This was a latex2html issue.  It's been fixed by #3347, so this ticket should be closed.",
    "created_at": "2008-08-25T21:15:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2411",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2411#issuecomment-16276",
    "user": "jhpalmieri"
}
```

This was a latex2html issue.  It's been fixed by #3347, so this ticket should be closed.



---

archive/issue_comments_016277.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-08-25T21:23:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2411",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2411#issuecomment-16277",
    "user": "mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_016278.json:
```json
{
    "body": "Thanks  John. Closed as suggested.\n\nCheers,\n\nMichael",
    "created_at": "2008-08-25T21:23:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2411",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2411#issuecomment-16278",
    "user": "mabshoff"
}
```

Thanks  John. Closed as suggested.

Cheers,

Michael

# Issue 1876: minor typo in reference manual section 8.1.1.2

archive/issues_001876.json:
```json
{
    "body": "Assignee: tba\n\nThe reference manual page at\n\nhttp://www.sagemath.org/doc/html/ref/node44.html\n\nsays\n\n**Note that the character is an escape character in Python, and also a character used by graph6 strings:**\n\nand then later\n\n**In Python, the escaped character is represented by**\n\nProbably there should be a 'slash' and a 'slashslash' there somewhere.\n\nIssue created by migration from https://trac.sagemath.org/ticket/1876\n\n",
    "closed_at": "2008-03-16T08:50:06Z",
    "created_at": "2008-01-21T06:22:45Z",
    "labels": [
        "component: documentation",
        "trivial",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-2.10.4",
    "title": "minor typo in reference manual section 8.1.1.2",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/1876",
    "user": "https://trac.sagemath.org/admin/accounts/users/bober"
}
```
Assignee: tba

The reference manual page at

http://www.sagemath.org/doc/html/ref/node44.html

says

**Note that the character is an escape character in Python, and also a character used by graph6 strings:**

and then later

**In Python, the escaped character is represented by**

Probably there should be a 'slash' and a 'slashslash' there somewhere.

Issue created by migration from https://trac.sagemath.org/ticket/1876





---

archive/issue_comments_011844.json:
```json
{
    "body": "This seems to have gotten fixed. From http://www.sagemath.org/doc/html/ref/node44.html as of 2.10.3:\n\n```\nNote that the \\ character is an escape character in Python, and also a character used by graph6 strings:\n```\nand then\n\n```\nIn Python, the escaped character \\ is represented by \\\\:\n```\n\nCheers,\n\nMichael",
    "created_at": "2008-03-16T08:48:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1876",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1876#issuecomment-11844",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

This seems to have gotten fixed. From http://www.sagemath.org/doc/html/ref/node44.html as of 2.10.3:

```
Note that the \ character is an escape character in Python, and also a character used by graph6 strings:
```
and then

```
In Python, the escaped character \ is represented by \\:
```

Cheers,

Michael



---

archive/issue_events_004526.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2008-03-16T08:50:06Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/1876",
    "milestone": "sage-2.10.4",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/1876#event-4526"
}
```



---

archive/issue_events_004527.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2008-03-16T08:50:06Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/1876",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/1876#event-4527"
}
```



---

archive/issue_comments_011845.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-03-16T08:50:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1876",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1876#issuecomment-11845",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed

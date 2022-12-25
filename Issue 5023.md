# Issue 5023: typo in calculus.py

archive/issues_005023.json:
```json
{
    "body": "Assignee: tba\n\nat line 1372, algorithim should be algorithm\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/5023\n\n",
    "created_at": "2009-01-19T10:34:11Z",
    "labels": [
        "component: documentation",
        "trivial",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.3",
    "title": "typo in calculus.py",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/5023",
    "user": "https://github.com/zimmermann6"
}
```
Assignee: tba

at line 1372, algorithim should be algorithm


Issue created by migration from https://trac.sagemath.org/ticket/5023





---

archive/issue_comments_038183.json:
```json
{
    "body": "Attachment [trac-5023.patch](tarball://root/attachments/some-uuid/ticket5023/trac-5023.patch) by @zimmermann6 created at 2009-01-19 20:54:19",
    "created_at": "2009-01-19T20:54:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5023",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5023#issuecomment-38183",
    "user": "https://github.com/zimmermann6"
}
```

Attachment [trac-5023.patch](tarball://root/attachments/some-uuid/ticket5023/trac-5023.patch) by @zimmermann6 created at 2009-01-19 20:54:19



---

archive/issue_comments_038184.json:
```json
{
    "body": "The attachment fixes the above typo and two more. However for the last one (tahn -> tanh) I am\nconcerned about the fact that there was no doctest for the corresponding function.\n\n```\nsage: a=tanh(2)\nsage: a._algebraic_(QQbar)\n...\nTypeError: Unable to coerce e (<class 'sage.functions.constants.E'>) to Rational\n```\n\nDid I something wrong? If not, a new ticket should be opened.",
    "created_at": "2009-01-19T21:01:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5023",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5023#issuecomment-38184",
    "user": "https://github.com/zimmermann6"
}
```

The attachment fixes the above typo and two more. However for the last one (tahn -> tanh) I am
concerned about the fact that there was no doctest for the corresponding function.

```
sage: a=tanh(2)
sage: a._algebraic_(QQbar)
...
TypeError: Unable to coerce e (<class 'sage.functions.constants.E'>) to Rational
```

Did I something wrong? If not, a new ticket should be opened.



---

archive/issue_comments_038185.json:
```json
{
    "body": "The patch corrected the typos, so a positive review.\n\nBut still\n\n\n```\n[jaap@paix sage-3.3.alpha4]$ ./sage\n----------------------------------------------------------------------\n----------------------------------------------------------------------\n| Sage Version 3.3.alpha5, Release Date: 2009-02-03                  |\n| Type notebook() for the GUI, and license() for information.        |\nsage: a=tanh(2)\n\nsage: a._algebraic_(QQbar)\n---------------------------------------------------------------------------\nTypeError                                 Traceback (most recent call last)\n\n[...]\nTypeError: Unable to coerce e (<class 'sage.functions.constants.E'>) to Rational\n```\n\n\nSomeone more knowledgeable should decide to open a new ticket or not.\n\nJaap",
    "created_at": "2009-02-05T15:29:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5023",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5023#issuecomment-38185",
    "user": "https://github.com/jaapspies"
}
```

The patch corrected the typos, so a positive review.

But still


```
[jaap@paix sage-3.3.alpha4]$ ./sage
----------------------------------------------------------------------
----------------------------------------------------------------------
| Sage Version 3.3.alpha5, Release Date: 2009-02-03                  |
| Type notebook() for the GUI, and license() for information.        |
sage: a=tanh(2)

sage: a._algebraic_(QQbar)
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)

[...]
TypeError: Unable to coerce e (<class 'sage.functions.constants.E'>) to Rational
```


Someone more knowledgeable should decide to open a new ticket or not.

Jaap



---

archive/issue_comments_038186.json:
```json
{
    "body": "I have moved the issue Paul pointed out to #5191 so we can merge the spelling fixes.\n\nCheers,\n\nMichael",
    "created_at": "2009-02-06T00:20:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5023",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5023#issuecomment-38186",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

I have moved the issue Paul pointed out to #5191 so we can merge the spelling fixes.

Cheers,

Michael



---

archive/issue_events_011600.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2009-02-06T22:28:10Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/5023",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/5023#event-11600"
}
```



---

archive/issue_comments_038187.json:
```json
{
    "body": "Merged in Sage 3.3.alpha6.\n\nCheers,\n\nMichael",
    "created_at": "2009-02-06T22:28:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5023",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5023#issuecomment-38187",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged in Sage 3.3.alpha6.

Cheers,

Michael



---

archive/issue_comments_038188.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-02-06T22:28:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5023",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5023#issuecomment-38188",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed

# Issue 4938: Words.count() returns a Python int instead of a Sage Integer

archive/issues_004938.json:
```json
{
    "body": "Assignee: @saliola\n\nCC:  sage-combinat\n\nKeywords: sage-words\n\n\n```\nHi guys,\n\nI sat around and was looking at the new ReST Words documentation and\nnoticed the following:\n\n[5:40pm] mabs: WTF:\n[5:40pm] mabs: sage: Words(7,13).count()\n[5:40pm] mabs: 96889010407L              # 32-bit\n[5:40pm] mabs: 96889010407                # 64-bit\n[5:40pm] mabs: So Words().count() returns a Python int?\n[5:40pm] wstein: ick\n[5:40pm] wstein: That stupid L at theend was suck an annoying decision by Guido.\n\nI would expect that count() returns a Sage Integer since that seems to\nbe the expected result in general. If you agree please open a ticket,\nbut this is not a high priority issue for me.\n\nCheers,\n\nMichael\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/4938\n\n",
    "created_at": "2009-01-04T19:55:25Z",
    "labels": [
        "component: combinatorics",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.4.1",
    "title": "Words.count() returns a Python int instead of a Sage Integer",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/4938",
    "user": "https://github.com/saliola"
}
```
Assignee: @saliola

CC:  sage-combinat

Keywords: sage-words


```
Hi guys,

I sat around and was looking at the new ReST Words documentation and
noticed the following:

[5:40pm] mabs: WTF:
[5:40pm] mabs: sage: Words(7,13).count()
[5:40pm] mabs: 96889010407L              # 32-bit
[5:40pm] mabs: 96889010407                # 64-bit
[5:40pm] mabs: So Words().count() returns a Python int?
[5:40pm] wstein: ick
[5:40pm] wstein: That stupid L at theend was suck an annoying decision by Guido.

I would expect that count() returns a Sage Integer since that seems to
be the expected result in general. If you agree please open a ticket,
but this is not a high priority issue for me.

Cheers,

Michael
```


Issue created by migration from https://trac.sagemath.org/ticket/4938





---

archive/issue_comments_037412.json:
```json
{
    "body": "The problem should be fixed with #5308. So you can close it as a duplicate.\n\nCheers,\n\nFlorent",
    "created_at": "2009-04-02T09:14:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4938",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4938#issuecomment-37412",
    "user": "https://github.com/hivert"
}
```

The problem should be fixed with #5308. So you can close it as a duplicate.

Cheers,

Florent



---

archive/issue_comments_037413.json:
```json
{
    "body": "This ticket can be closed once #5308 is merged.\n\nCheers,\n\nMichael",
    "created_at": "2009-04-05T00:07:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4938",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4938#issuecomment-37413",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

This ticket can be closed once #5308 is merged.

Cheers,

Michael



---

archive/issue_comments_037414.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-04-05T23:54:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4938",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4938#issuecomment-37414",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_037415.json:
```json
{
    "body": "Fixed in Sage 3.4.1.rc1 via #5308.\n\nCheers,\n\nMichael",
    "created_at": "2009-04-05T23:54:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4938",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4938#issuecomment-37415",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Fixed in Sage 3.4.1.rc1 via #5308.

Cheers,

Michael

# Issue 178: Sage()._get() does not return the correct result in some instances

archive/issues_000178.json:
```json
{
    "body": "Assignee: boothby\n\nKeywords: Sage() expect Pexpect\n\nsage: P = Sage()\nsage: P._send('factor(2^250-1)')\nsage: P._get()\n(True, 'factor(2^250-1)\\r\\n251\\r\\n')\nsage: P._get()\n(False, '')\nsage: \n\nThe output from factor(2^250-1) should be:\nsage: factor(2^250-1)\n3 * 11 * 31 * 251 * 601 * 1801 * 4051 * 229668251 * 269089806001 * 4710883168879506001 * 5519485418336288303251\n\nAny idea why it is dropping off chars left and right?\n\nIssue created by migration from https://trac.sagemath.org/ticket/178\n\n",
    "created_at": "2006-12-08T01:17:31Z",
    "labels": [
        "notebook",
        "major",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-1.5",
    "title": "Sage()._get() does not return the correct result in some instances",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/178",
    "user": "@yqiang"
}
```
Assignee: boothby

Keywords: Sage() expect Pexpect

sage: P = Sage()
sage: P._send('factor(2^250-1)')
sage: P._get()
(True, 'factor(2^250-1)\r\n251\r\n')
sage: P._get()
(False, '')
sage: 

The output from factor(2^250-1) should be:
sage: factor(2^250-1)
3 * 11 * 31 * 251 * 601 * 1801 * 4051 * 229668251 * 269089806001 * 4710883168879506001 * 5519485418336288303251

Any idea why it is dropping off chars left and right?

Issue created by migration from https://trac.sagemath.org/ticket/178





---

archive/issue_comments_000820.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2006-12-08T01:31:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/178",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/178#issuecomment-820",
    "user": "@williamstein"
}
```

Resolution: fixed



---

archive/issue_comments_000821.json:
```json
{
    "body": "Input to Sage() is *not* preparsed -- you have to do it.  So 2^250 - 1\nis actually just 251!!  It's \"2 xor 250 minus 1\".",
    "created_at": "2006-12-08T01:31:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/178",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/178#issuecomment-821",
    "user": "@williamstein"
}
```

Input to Sage() is *not* preparsed -- you have to do it.  So 2^250 - 1
is actually just 251!!  It's "2 xor 250 minus 1".

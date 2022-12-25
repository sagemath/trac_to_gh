# Issue 377: major bug in number fields if defining poly has denoms

archive/issues_000377.json:
```json
{
    "body": "Assignee: somebody\n\n\n```\nswas@ubuntu:~$ sage\n----------------------------------------------------------------------\n----------------------------------------------------------------------\n| SAGE Version 2.5.2-alpha, Release Date: 2007-05-20                 |\n| Type notebook() for the GUI, and license() for information.        |\nsage: G.<a> = NumberField(x^3 + 2/3*x + 1)\nsage: a^3 + a\nMulMod: bad args\nAborted\nwas@ubuntu:~$\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/377\n\n",
    "created_at": "2007-05-23T18:35:04Z",
    "labels": [
        "component: basic arithmetic",
        "bug"
    ],
    "title": "major bug in number fields if defining poly has denoms",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/377",
    "user": "https://github.com/williamstein"
}
```
Assignee: somebody


```
swas@ubuntu:~$ sage
----------------------------------------------------------------------
----------------------------------------------------------------------
| SAGE Version 2.5.2-alpha, Release Date: 2007-05-20                 |
| Type notebook() for the GUI, and license() for information.        |
sage: G.<a> = NumberField(x^3 + 2/3*x + 1)
sage: a^3 + a
MulMod: bad args
Aborted
was@ubuntu:~$
```


Issue created by migration from https://trac.sagemath.org/ticket/377





---

archive/issue_comments_001790.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2007-05-31T14:09:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/377",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/377#issuecomment-1790",
    "user": "https://github.com/williamstein"
}
```

Resolution: fixed



---

archive/issue_comments_001791.json:
```json
{
    "body": "Joel mostly fixed this and I finished it off for sage-2.5.4.",
    "created_at": "2007-05-31T14:09:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/377",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/377#issuecomment-1791",
    "user": "https://github.com/williamstein"
}
```

Joel mostly fixed this and I finished it off for sage-2.5.4.

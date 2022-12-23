# Issue 5707: plus signs missing in typesetting of modular symbols

archive/issues_005707.json:
```json
{
    "body": "Assignee: craigcitro\n\nTry this and see no plus signs! Ouch.\n\n```\nsage: x = ModularSymbols(43)(vector([0,0,0,0,1,1,1]))\nsage: show(x.modular_symbol_rep())\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/5707\n\n",
    "created_at": "2009-04-07T21:28:39Z",
    "labels": [
        "modular forms",
        "major",
        "bug"
    ],
    "title": "plus signs missing in typesetting of modular symbols",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/5707",
    "user": "was"
}
```
Assignee: craigcitro

Try this and see no plus signs! Ouch.

```
sage: x = ModularSymbols(43)(vector([0,0,0,0,1,1,1]))
sage: show(x.modular_symbol_rep())
```


Issue created by migration from https://trac.sagemath.org/ticket/5707





---

archive/issue_comments_044595.json:
```json
{
    "body": "Bumping it since according to William this is lower priority.\n\nCheers,\n\nMichael",
    "created_at": "2009-04-08T00:51:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5707",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5707#issuecomment-44595",
    "user": "mabshoff"
}
```

Bumping it since according to William this is lower priority.

Cheers,

Michael



---

archive/issue_comments_044596.json:
```json
{
    "body": "Resolution: duplicate",
    "created_at": "2009-04-12T01:16:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5707",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5707#issuecomment-44596",
    "user": "was"
}
```

Resolution: duplicate



---

archive/issue_comments_044597.json:
```json
{
    "body": "I am closing this since it is easy to fix as part of #5766.",
    "created_at": "2009-04-12T01:16:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5707",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5707#issuecomment-44597",
    "user": "was"
}
```

I am closing this since it is easy to fix as part of #5766.

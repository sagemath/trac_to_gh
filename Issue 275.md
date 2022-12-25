# Issue 275: Maxtrix groups over RR don't get pushed off to GAP properly

archive/issues_000275.json:
```json
{
    "body": "Assignee: @williamstein\n\nKeywords: matrix groups\n\n\n```\nsage: G = SL(2, CC)\nsage: G.gens()\n\nTypeError: Gap produced error output\nVariable: 'Complex' must have a value\n\nSyntax error: ) expected\n$sage17:=SL(2, Complex Field with 53 bits of precision);;\n                           ^\n\n   executing $sage17:=SL(2, Complex Field with 53 bits of precision);;\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/275\n\n",
    "created_at": "2007-02-21T20:34:05Z",
    "labels": [
        "component: algebraic geometry",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-2.8.2",
    "title": "Maxtrix groups over RR don't get pushed off to GAP properly",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/275",
    "user": "https://github.com/bobmoretti"
}
```
Assignee: @williamstein

Keywords: matrix groups


```
sage: G = SL(2, CC)
sage: G.gens()

TypeError: Gap produced error output
Variable: 'Complex' must have a value

Syntax error: ) expected
$sage17:=SL(2, Complex Field with 53 bits of precision);;
                           ^

   executing $sage17:=SL(2, Complex Field with 53 bits of precision);;
```


Issue created by migration from https://trac.sagemath.org/ticket/275





---

archive/issue_comments_001304.json:
```json
{
    "body": "NOTE -- Gap doesn't have a notion of floating point numbers -- so the correct behavior here is to give a good error message.",
    "created_at": "2007-08-18T09:58:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/275",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/275#issuecomment-1304",
    "user": "https://github.com/williamstein"
}
```

NOTE -- Gap doesn't have a notion of floating point numbers -- so the correct behavior here is to give a good error message.



---

archive/issue_comments_001305.json:
```json
{
    "body": "Changing component from algebraic geometry to interfaces.",
    "created_at": "2007-08-18T09:58:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/275",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/275#issuecomment-1305",
    "user": "https://github.com/williamstein"
}
```

Changing component from algebraic geometry to interfaces.



---

archive/issue_events_000292.json:
```json
{
    "actor": "https://github.com/williamstein",
    "created_at": "2007-08-18T20:25:25Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/275",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/275#event-292"
}
```



---

archive/issue_comments_001306.json:
```json
{
    "body": "fixed for sage-2.8.2",
    "created_at": "2007-08-18T20:25:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/275",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/275#issuecomment-1306",
    "user": "https://github.com/williamstein"
}
```

fixed for sage-2.8.2



---

archive/issue_comments_001307.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2007-08-18T20:25:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/275",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/275#issuecomment-1307",
    "user": "https://github.com/williamstein"
}
```

Resolution: fixed

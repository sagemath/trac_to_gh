# Issue 8040: given that m,n are optional inputs to CRT(a,b,m,n), given a,b mod m,n should work

archive/issues_008040.json:
```json
{
    "body": "Assignee: AlexGhitza\n\nI think this should work:\n\n```\nsage: CRT(Mod(3,19), Mod(5, 13))\n...\nValueError: arguments a and b must be coprime\n```\n\n\nThis fix is to check the gcd precondition more carefully. \n\nIssue created by migration from https://trac.sagemath.org/ticket/8040\n\n",
    "created_at": "2010-01-22T15:24:37Z",
    "labels": [
        "basic arithmetic",
        "minor",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-6.4",
    "title": "given that m,n are optional inputs to CRT(a,b,m,n), given a,b mod m,n should work",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/8040",
    "user": "was"
}
```
Assignee: AlexGhitza

I think this should work:

```
sage: CRT(Mod(3,19), Mod(5, 13))
...
ValueError: arguments a and b must be coprime
```


This fix is to check the gcd precondition more carefully. 

Issue created by migration from https://trac.sagemath.org/ticket/8040





---

archive/issue_comments_070271.json:
```json
{
    "body": "I have tried \n\n\n```\nsage: CRT(Mod(3,19), Mod(5, 13))\n```\n\n\nThe error is because of the return type of Mod is sage.rings.finite_rings.integer_mod.IntegerMod_int, not integer which is desire. \n\nif you try this\n\n\n```\nsage: CRT(int(Mod(3,19)), int(Mod(5, 13)))\n```\n\nit's working, is my suggestion right? or am I missing something.\n\nI used Sage version 8.1, which was released on 2017-12-07.\n\nThanks,\\\\\nHarsh",
    "created_at": "2018-03-16T16:55:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8040",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8040#issuecomment-70271",
    "user": "saiharsh"
}
```

I have tried 


```
sage: CRT(Mod(3,19), Mod(5, 13))
```


The error is because of the return type of Mod is sage.rings.finite_rings.integer_mod.IntegerMod_int, not integer which is desire. 

if you try this


```
sage: CRT(int(Mod(3,19)), int(Mod(5, 13)))
```

it's working, is my suggestion right? or am I missing something.

I used Sage version 8.1, which was released on 2017-12-07.

Thanks,\\
Harsh

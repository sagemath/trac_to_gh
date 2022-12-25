# Issue 3740: pickling broken for TensorProductOfCrystals

archive/issues_003740.json:
```json
{
    "body": "Assignee: cwitty\n\nCC:  @mwhansen\n\nI have change the summary of this ticket since the original error is no longer something that happens with the current pickle jar. But as Dan Bump pointed out below:\n\n```\nsage: C = CrystalOfLetters(['A',3])\nsage: v = C.list()[0]\nsage: T = TensorProductOfCrystals(C, C, generators=[[v,v]])\nsage: T == loads(dumps(T))\n```\nraises an exception.\n\nCheers,\n\nMichael\n\nIssue created by migration from https://trac.sagemath.org/ticket/3740\n\n",
    "closed_at": "2009-06-04T20:31:16Z",
    "created_at": "2008-07-29T14:58:24Z",
    "labels": [
        "component: misc",
        "blocker",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-duplicate/invalid/wontfix",
    "title": "pickling broken for TensorProductOfCrystals",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/3740",
    "user": "https://github.com/williamstein"
}
```
Assignee: cwitty

CC:  @mwhansen

I have change the summary of this ticket since the original error is no longer something that happens with the current pickle jar. But as Dan Bump pointed out below:

```
sage: C = CrystalOfLetters(['A',3])
sage: v = C.list()[0]
sage: T = TensorProductOfCrystals(C, C, generators=[[v,v]])
sage: T == loads(dumps(T))
```
raises an exception.

Cheers,

Michael

Issue created by migration from https://trac.sagemath.org/ticket/3740





---

archive/issue_comments_026512.json:
```json
{
    "body": "Presumably the same bug:\n\n```\nsage: C = CrystalOfLetters(['A',3])\nsage: v = C.list()[0]\nsage: T = TensorProductOfCrystals(C, C, generators=[[v,v]])\nsage: T == loads(dumps(T))\n```\n\nReturns an exception.",
    "created_at": "2008-07-30T00:49:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3740",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3740#issuecomment-26512",
    "user": "https://github.com/dwbump"
}
```

Presumably the same bug:

```
sage: C = CrystalOfLetters(['A',3])
sage: v = C.list()[0]
sage: T = TensorProductOfCrystals(C, C, generators=[[v,v]])
sage: T == loads(dumps(T))
```

Returns an exception.



---

archive/issue_comments_026513.json:
```json
{
    "body": "This is no longer valid\n\n```\n----------------------------------------------------------------------\n----------------------------------------------------------------------\nsage: sage: C = CrystalOfLetters(['A',3])\nsage: sage: v = C.list()[0]\nsage: sage: T = TensorProductOfCrystals(C, C, generators=[[v,v]])\nsage: sage: T == loads(dumps(T))\nTrue\nsage: sage: C = CrystalOfLetters(['A',3])\nsage: sage: v = C.list()[0]\nsage: sage: T = TensorProductOfCrystals(C, C, generators=[[v,v]])\nsage: sage: T == loads(dumps(T))\nTrue\nsage: sage: C = CrystalOfLetters(['A',3])\nsage: sage: v = C.list()[0]\nsage: sage: T = TensorProductOfCrystals(C, C, generators=[[v,v]])\nsage: sage: T == loads(dumps(T))\nTrue\n```",
    "created_at": "2009-06-04T20:31:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3740",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3740#issuecomment-26513",
    "user": "https://github.com/mwhansen"
}
```

This is no longer valid

```
----------------------------------------------------------------------
----------------------------------------------------------------------
sage: sage: C = CrystalOfLetters(['A',3])
sage: sage: v = C.list()[0]
sage: sage: T = TensorProductOfCrystals(C, C, generators=[[v,v]])
sage: sage: T == loads(dumps(T))
True
sage: sage: C = CrystalOfLetters(['A',3])
sage: sage: v = C.list()[0]
sage: sage: T = TensorProductOfCrystals(C, C, generators=[[v,v]])
sage: sage: T == loads(dumps(T))
True
sage: sage: C = CrystalOfLetters(['A',3])
sage: sage: v = C.list()[0]
sage: sage: T = TensorProductOfCrystals(C, C, generators=[[v,v]])
sage: sage: T == loads(dumps(T))
True
```



---

archive/issue_events_008569.json:
```json
{
    "actor": "https://github.com/mwhansen",
    "created_at": "2009-06-04T20:31:16Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/3740",
    "milestone": "sage-duplicate/invalid/wontfix",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/3740#event-8569"
}
```



---

archive/issue_events_008570.json:
```json
{
    "actor": "https://github.com/mwhansen",
    "created_at": "2009-06-04T20:31:16Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/3740",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/3740#event-8570"
}
```



---

archive/issue_comments_026514.json:
```json
{
    "body": "Resolution: invalid",
    "created_at": "2009-06-04T20:31:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3740",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3740#issuecomment-26514",
    "user": "https://github.com/mwhansen"
}
```

Resolution: invalid

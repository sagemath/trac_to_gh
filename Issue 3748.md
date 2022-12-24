# Issue 3748: bug in integers modulo n

archive/issues_003748.json:
```json
{
    "body": "Assignee: somebody\n\nthis was reported to me by Emmanuel Thome with Sage 3.0.3:\n\n```\nsage: R=Integers(17^5)\nsage: R\nRing of integers modulo 1419857\nsage: R(17)^5\n1419857\nsage: R(17)^5==0\nFalse\nsage: R(R(17)^5)\n0\n```\n\nClearly R(17)^5 is not in canonical form, which is what we would expect... However:\n\n```\nsage: R(17)*R(17)*R(17)*R(17)*R(17)\n0\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/3748\n\n",
    "created_at": "2008-07-30T15:29:00Z",
    "labels": [
        "basic arithmetic",
        "major",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-duplicate/invalid/wontfix",
    "title": "bug in integers modulo n",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/3748",
    "user": "@zimmermann6"
}
```
Assignee: somebody

this was reported to me by Emmanuel Thome with Sage 3.0.3:

```
sage: R=Integers(17^5)
sage: R
Ring of integers modulo 1419857
sage: R(17)^5
1419857
sage: R(17)^5==0
False
sage: R(R(17)^5)
0
```

Clearly R(17)^5 is not in canonical form, which is what we would expect... However:

```
sage: R(17)*R(17)*R(17)*R(17)*R(17)
0
```


Issue created by migration from https://trac.sagemath.org/ticket/3748





---

archive/issue_comments_026619.json:
```json
{
    "body": "Resolution: duplicate",
    "created_at": "2008-07-30T15:34:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3748",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3748#issuecomment-26619",
    "user": "mabshoff"
}
```

Resolution: duplicate



---

archive/issue_comments_026620.json:
```json
{
    "body": "Hi Paul,\n\nDavid Harvey reported the same problem from sage-devel and already put up a patch that has been positively reviewed patch at #3747. So I am closing this as a duplicate.\n\nCheers,\n\nMichael",
    "created_at": "2008-07-30T15:34:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3748",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3748#issuecomment-26620",
    "user": "mabshoff"
}
```

Hi Paul,

David Harvey reported the same problem from sage-devel and already put up a patch that has been positively reviewed patch at #3747. So I am closing this as a duplicate.

Cheers,

Michael

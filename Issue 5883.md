# Issue 5883: integrate relevant functionality from modular/modsym/p1list.pyx into projective space code

archive/issues_005883.json:
```json
{
    "body": "Assignee: AlexGhitza\n\nKeywords: rational points projective line finite\n\nThere is optimised code in p1list.pyx for creating the list of points on P1 over Z/NZ.  It would be nice to also have this available as, for instance:\n\n\n```\nsage: P1 = ProjectiveSpace(1, Integers(N))\nsage: P1.rational_points()\n```\n\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/5883\n\n",
    "created_at": "2009-04-24T00:23:07Z",
    "labels": [
        "algebraic geometry",
        "minor",
        "enhancement"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-6.4",
    "title": "integrate relevant functionality from modular/modsym/p1list.pyx into projective space code",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/5883",
    "user": "AlexGhitza"
}
```
Assignee: AlexGhitza

Keywords: rational points projective line finite

There is optimised code in p1list.pyx for creating the list of points on P1 over Z/NZ.  It would be nice to also have this available as, for instance:


```
sage: P1 = ProjectiveSpace(1, Integers(N))
sage: P1.rational_points()
```



Issue created by migration from https://trac.sagemath.org/ticket/5883





---

archive/issue_comments_046523.json:
```json
{
    "body": "This can be done independently of, but will greatly benefit from, John's work on #5876.",
    "created_at": "2009-04-24T00:25:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5883",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5883#issuecomment-46523",
    "user": "AlexGhitza"
}
```

This can be done independently of, but will greatly benefit from, John's work on #5876.

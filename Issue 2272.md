# Issue 2272: subgroups of abelian groups have various problems

archive/issues_002272.json:
```json
{
    "body": "Assignee: joyner\n\nWhile nosing around #1284, I ran into some more trouble with subgroups of abelian groups:\n\n\n```\nsage: A = G.subgroup([a])\nsage: G.<a,b> = AbelianGroup(2)\nsage: A = G.subgroup([a])\nsage: a in A   # should return True\nFalse\nsage: A.gens()\n[a]\nsage: A.0      # should return a\nf\n```\n\n\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/2272\n\n",
    "created_at": "2008-02-23T00:49:48Z",
    "labels": [
        "group theory",
        "major",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.0.3",
    "title": "subgroups of abelian groups have various problems",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/2272",
    "user": "AlexGhitza"
}
```
Assignee: joyner

While nosing around #1284, I ran into some more trouble with subgroups of abelian groups:


```
sage: A = G.subgroup([a])
sage: G.<a,b> = AbelianGroup(2)
sage: A = G.subgroup([a])
sage: a in A   # should return True
False
sage: A.gens()
[a]
sage: A.0      # should return a
f
```




Issue created by migration from https://trac.sagemath.org/ticket/2272





---

archive/issue_comments_015066.json:
```json
{
    "body": "I have no idea how to fix this. The __contains__ method on the subclass AbelianGroup_subgroup will default to the parent class if pass or an error is passed. This has messed up every attempt I have made.\nOne issue is that the group is infinite, so perhaps a NotImplementedError makes sense here?",
    "created_at": "2008-02-24T17:11:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2272",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2272#issuecomment-15066",
    "user": "wdj"
}
```

I have no idea how to fix this. The __contains__ method on the subclass AbelianGroup_subgroup will default to the parent class if pass or an error is passed. This has messed up every attempt I have made.
One issue is that the group is infinite, so perhaps a NotImplementedError makes sense here?



---

archive/issue_comments_015067.json:
```json
{
    "body": "The way G.subgroup([a]) is currently written, if you want the generators to have anything other than the default name (f or f1, f2, ...), you must name them explicitly. So, I'm not sure if\n\n```\nsage: A.0      # should return a\nf\n```\n\nis a bug or feature.",
    "created_at": "2008-02-24T18:12:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2272",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2272#issuecomment-15067",
    "user": "wdj"
}
```

The way G.subgroup([a]) is currently written, if you want the generators to have anything other than the default name (f or f1, f2, ...), you must name them explicitly. So, I'm not sure if

```
sage: A.0      # should return a
f
```

is a bug or feature.



---

archive/issue_comments_015068.json:
```json
{
    "body": "See also #3127 and #1849",
    "created_at": "2008-05-07T22:25:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2272",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2272#issuecomment-15068",
    "user": "was"
}
```

See also #3127 and #1849



---

archive/issue_comments_015069.json:
```json
{
    "body": "Patch at #1284 fixes this.",
    "created_at": "2008-05-10T23:36:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2272",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2272#issuecomment-15069",
    "user": "rlm"
}
```

Patch at #1284 fixes this.



---

archive/issue_comments_015070.json:
```json
{
    "body": "Fixed by merging #1284 in Sage 3.0.3.alpha0.",
    "created_at": "2008-05-26T16:43:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2272",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2272#issuecomment-15070",
    "user": "mabshoff"
}
```

Fixed by merging #1284 in Sage 3.0.3.alpha0.



---

archive/issue_comments_015071.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-05-26T16:43:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2272",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2272#issuecomment-15071",
    "user": "mabshoff"
}
```

Resolution: fixed

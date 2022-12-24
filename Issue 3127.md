# Issue 3127: abelian groups (are lame?) -- bug in comparison of subgroups with group

archive/issues_003127.json:
```json
{
    "body": "Assignee: joyner\n\nWARNINGS: \n1. David Roe is recently rumored to be rewriting abelian groups.  \n2. I recently rewrote abelian groups but my patch rotted: #1849\n3. There are other known problems with subgroups of abelian groups: #2272\n\n\nOK, now the bug report.  This is inconsistent and lame:\n\n\n```\nsage: A = AbelianGroup(1,[6])\nsage: A.subgroup(list(A.gens())) == A\nFalse\nsage: A = AbelianGroup(2,[2,3])\nsage: A.subgroup(list(A.gens())) == A\nTrue\n```\n\n\nThis is the original email reporting the bug:\n\n```\nHi there,\n\nWhen I define an abelian group\nA = AbelianGroup(1,[6])\nand then generate a subgroup that actually is the whole group itself,\nand then compare it to the original group:\nA.subgroup(list(A.gens())) == A\nthe result may be either True or False. In this example it is False.\nWhen defining A as\nA = AbelianGroup(2,[3,2])\nit is False as well, but when I define it as\nA = AbelianGroup(2,[2,3])\nit is True.\nMy guess is that this is because comparison of finite Abelian groups\nis implemented using their invariant factors, but when you create the\ngroup using factors that are not in canonical form or not in\nincreasing order, these are used instead of the ordered list of\ninvariant factors anyway.\n\nGreetings,\n\nUtpal Sarkar\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/3127\n\n",
    "created_at": "2008-05-07T22:22:43Z",
    "labels": [
        "group theory",
        "major",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.0.3",
    "title": "abelian groups (are lame?) -- bug in comparison of subgroups with group",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/3127",
    "user": "@williamstein"
}
```
Assignee: joyner

WARNINGS: 
1. David Roe is recently rumored to be rewriting abelian groups.  
2. I recently rewrote abelian groups but my patch rotted: #1849
3. There are other known problems with subgroups of abelian groups: #2272


OK, now the bug report.  This is inconsistent and lame:


```
sage: A = AbelianGroup(1,[6])
sage: A.subgroup(list(A.gens())) == A
False
sage: A = AbelianGroup(2,[2,3])
sage: A.subgroup(list(A.gens())) == A
True
```


This is the original email reporting the bug:

```
Hi there,

When I define an abelian group
A = AbelianGroup(1,[6])
and then generate a subgroup that actually is the whole group itself,
and then compare it to the original group:
A.subgroup(list(A.gens())) == A
the result may be either True or False. In this example it is False.
When defining A as
A = AbelianGroup(2,[3,2])
it is False as well, but when I define it as
A = AbelianGroup(2,[2,3])
it is True.
My guess is that this is because comparison of finite Abelian groups
is implemented using their invariant factors, but when you create the
group using factors that are not in canonical form or not in
increasing order, these are used instead of the ordered list of
invariant factors anyway.

Greetings,

Utpal Sarkar
```


Issue created by migration from https://trac.sagemath.org/ticket/3127





---

archive/issue_comments_021663.json:
```json
{
    "body": "I am working on rewriting, but won't be able to work on it for the next week (I'm at a conference then need to finish a final).  If someone else wants to do something in this direction, let me (or sage-devel) know.",
    "created_at": "2008-05-07T22:30:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3127",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3127#issuecomment-21663",
    "user": "@roed314"
}
```

I am working on rewriting, but won't be able to work on it for the next week (I'm at a conference then need to finish a final).  If someone else wants to do something in this direction, let me (or sage-devel) know.



---

archive/issue_comments_021664.json:
```json
{
    "body": "Is this actually a bug?  It would certainly wrong if the test being\nperformed was isomorphism rather than equality, but I think it is\nactually reasonable for two finite abelian groups to only be reported\nas \"equal\" when they are presented the same way.\n\nHaving said that I agree that is does not look right for a group to have a _subgroup_ which is isomorphic to but not equal to itself.",
    "created_at": "2008-05-08T08:17:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3127",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3127#issuecomment-21664",
    "user": "@JohnCremona"
}
```

Is this actually a bug?  It would certainly wrong if the test being
performed was isomorphism rather than equality, but I think it is
actually reasonable for two finite abelian groups to only be reported
as "equal" when they are presented the same way.

Having said that I agree that is does not look right for a group to have a _subgroup_ which is isomorphic to but not equal to itself.



---

archive/issue_comments_021665.json:
```json
{
    "body": "Will all due respect to myself, I think it is better if someone like David Roe works on this package than the original author, who seems to have created a mess of things:-). Can someone (Michael?) please change the owner from \"joyner\" to \"David Roe\" or whatever abbreviation he likes to use?",
    "created_at": "2008-05-08T11:33:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3127",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3127#issuecomment-21665",
    "user": "@wdjoyner"
}
```

Will all due respect to myself, I think it is better if someone like David Roe works on this package than the original author, who seems to have created a mess of things:-). Can someone (Michael?) please change the owner from "joyner" to "David Roe" or whatever abbreviation he likes to use?



---

archive/issue_comments_021666.json:
```json
{
    "body": "Changing assignee from joyner to @roed314.",
    "created_at": "2008-05-08T11:35:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3127",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3127#issuecomment-21666",
    "user": "mabshoff"
}
```

Changing assignee from joyner to @roed314.



---

archive/issue_comments_021667.json:
```json
{
    "body": "See also #1284.",
    "created_at": "2008-05-09T08:38:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3127",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3127#issuecomment-21667",
    "user": "fwclarke"
}
```

See also #1284.



---

archive/issue_comments_021668.json:
```json
{
    "body": "Patch at #1284 fixes this.",
    "created_at": "2008-05-10T23:36:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3127",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3127#issuecomment-21668",
    "user": "@rlmill"
}
```

Patch at #1284 fixes this.



---

archive/issue_comments_021669.json:
```json
{
    "body": "Fixed by merging #1284 in Sage 3.0.3.alpha0.",
    "created_at": "2008-05-26T16:43:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3127",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3127#issuecomment-21669",
    "user": "mabshoff"
}
```

Fixed by merging #1284 in Sage 3.0.3.alpha0.



---

archive/issue_comments_021670.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-05-26T16:43:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3127",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3127#issuecomment-21670",
    "user": "mabshoff"
}
```

Resolution: fixed

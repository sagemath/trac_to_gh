# Issue 8317: Protecting special names against assignation

archive/issues_008317.json:
```json
{
    "body": "Assignee: olazo\n\nKeywords: assignation,names\n\nI'd like to propose that certain special names should be protected so that they could not become variable names (for example pi, e, and i)\n\nif by accident you assign them like:\n\ne=factorial(10)\n\nand then you need to need to use e with it's standard meaning, like\n\ne^100\n\nyou will have a very hard to spot error ( (factorial(10)^100).\n\nIssue created by migration from https://trac.sagemath.org/ticket/8317\n\n",
    "created_at": "2010-02-21T00:19:55Z",
    "labels": [
        "component: misc",
        "minor",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-wishlist",
    "title": "Protecting special names against assignation",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/8317",
    "user": "https://trac.sagemath.org/admin/accounts/users/olazo"
}
```
Assignee: olazo

Keywords: assignation,names

I'd like to propose that certain special names should be protected so that they could not become variable names (for example pi, e, and i)

if by accident you assign them like:

e=factorial(10)

and then you need to need to use e with it's standard meaning, like

e^100

you will have a very hard to spot error ( (factorial(10)^100).

Issue created by migration from https://trac.sagemath.org/ticket/8317





---

archive/issue_comments_073650.json:
```json
{
    "body": "Changing component from misc to symbolics.",
    "created_at": "2010-02-21T00:26:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8317",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8317#issuecomment-73650",
    "user": "https://trac.sagemath.org/admin/accounts/users/olazo"
}
```

Changing component from misc to symbolics.



---

archive/issue_comments_073651.json:
```json
{
    "body": "his is something that can (and will) be made an optional mode.  We'll have several -- implicit multiplication, automatic variable name creation, and protected names. Having them all on could be useful for people teaching, e.g., calculus labs.   This protected mode, by the way, will in the long run use the same technique as automatic variable name creation: replacing the globals() dictionary by a customized wrapper.  This has a slight performance penalty, so definitely can't be the default.  But it is a fine idea for an optional mode.",
    "created_at": "2010-02-21T01:21:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8317",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8317#issuecomment-73651",
    "user": "https://github.com/williamstein"
}
```

his is something that can (and will) be made an optional mode.  We'll have several -- implicit multiplication, automatic variable name creation, and protected names. Having them all on could be useful for people teaching, e.g., calculus labs.   This protected mode, by the way, will in the long run use the same technique as automatic variable name creation: replacing the globals() dictionary by a customized wrapper.  This has a slight performance penalty, so definitely can't be the default.  But it is a fine idea for an optional mode.



---

archive/issue_comments_073652.json:
```json
{
    "body": "I see that this would be a desirable feature for users of symbolics. I don't think the implementation is related to the symbolics subsystem however. I'm assigning this back to the misc component.",
    "created_at": "2010-04-05T12:38:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8317",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8317#issuecomment-73652",
    "user": "https://github.com/burcin"
}
```

I see that this would be a desirable feature for users of symbolics. I don't think the implementation is related to the symbolics subsystem however. I'm assigning this back to the misc component.



---

archive/issue_comments_073653.json:
```json
{
    "body": "Changing component from symbolics to misc.",
    "created_at": "2010-04-05T12:38:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8317",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8317#issuecomment-73653",
    "user": "https://github.com/burcin"
}
```

Changing component from symbolics to misc.



---

archive/issue_comments_073654.json:
```json
{
    "body": "Changing type from defect to enhancement.",
    "created_at": "2010-04-05T12:38:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8317",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8317#issuecomment-73654",
    "user": "https://github.com/burcin"
}
```

Changing type from defect to enhancement.

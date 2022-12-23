# Issue 576: hard interrupting a Singular calculation does not kill Singular

archive/issues_000576.json:
```json
{
    "body": "Assignee: was\n\nConsider:\n\n\n```\nsage: P = PolynomialRing(QQ,8,'x')\nsage: I = sage.rings.ideal.Cyclic(P)\nsage: I.groebner_basis() # calls Singular and takes a long time\n```\n\n\nNow press Ctrl-C and you'll get:\n\n\n```\nInterrupting Singular...\nInterrupting Singular...\n...\n<type 'exceptions.TypeError'>: Restarting Singular \n(WARNING: all variables defined in previous session are now invalid)\n```\n\n\nSingular supposedly got killed but keeps running in background.\n\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/576\n\n",
    "created_at": "2007-09-03T13:59:11Z",
    "labels": [
        "interfaces",
        "major",
        "bug"
    ],
    "title": "hard interrupting a Singular calculation does not kill Singular",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/576",
    "user": "malb"
}
```
Assignee: was

Consider:


```
sage: P = PolynomialRing(QQ,8,'x')
sage: I = sage.rings.ideal.Cyclic(P)
sage: I.groebner_basis() # calls Singular and takes a long time
```


Now press Ctrl-C and you'll get:


```
Interrupting Singular...
Interrupting Singular...
...
<type 'exceptions.TypeError'>: Restarting Singular 
(WARNING: all variables defined in previous session are now invalid)
```


Singular supposedly got killed but keeps running in background.



Issue created by migration from https://trac.sagemath.org/ticket/576





---

archive/issue_comments_002990.json:
```json
{
    "body": "I think this is fixed in current Sage due to the signal handler rewrite by Gonzalo and William.\n\nCheers,\n\nMichael",
    "created_at": "2007-10-19T18:51:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/576",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/576#issuecomment-2990",
    "user": "mabshoff"
}
```

I think this is fixed in current Sage due to the signal handler rewrite by Gonzalo and William.

Cheers,

Michael



---

archive/issue_comments_002991.json:
```json
{
    "body": "You're right, this is now fixed.",
    "created_at": "2007-10-20T01:07:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/576",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/576#issuecomment-2991",
    "user": "was"
}
```

You're right, this is now fixed.



---

archive/issue_comments_002992.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2007-10-20T01:07:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/576",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/576#issuecomment-2992",
    "user": "was"
}
```

Resolution: fixed

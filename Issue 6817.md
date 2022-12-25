# Issue 6817: [with SPKG, needs review] GLPK for Sage, new version

archive/issues_006817.json:
```json
{
    "body": "Assignee: tbd\n\nCC:  mvngu\n\nNew version of package GLPK for Sage. There is nothing new except that this spkg now embeds the function solveGLPK which was previously included directly into Sage ( stupid, as this is to be an optional package ).\nHence, this code has already been positively reviewed in #6502\n\nAs with package COIN-OR/CBC, the function is now compiled when the package is installed, then loaded by sage.numerical.mip when solve() is called.\n\nThe package can be installed this way\n\n```\nsage -f http://www-sop.inria.fr/members/Nathann.Cohen/glpk-4.38.spkg\n}}]\n\nIssue created by migration from https://trac.sagemath.org/ticket/6817\n\n",
    "created_at": "2009-08-24T09:38:08Z",
    "labels": [
        "component: optional packages"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.1.2",
    "title": "[with SPKG, needs review] GLPK for Sage, new version",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/6817",
    "user": "https://github.com/nathanncohen"
}
```
Assignee: tbd

CC:  mvngu

New version of package GLPK for Sage. There is nothing new except that this spkg now embeds the function solveGLPK which was previously included directly into Sage ( stupid, as this is to be an optional package ).
Hence, this code has already been positively reviewed in #6502

As with package COIN-OR/CBC, the function is now compiled when the package is installed, then loaded by sage.numerical.mip when solve() is called.

The package can be installed this way

```
sage -f http://www-sop.inria.fr/members/Nathann.Cohen/glpk-4.38.spkg
}}]

Issue created by migration from https://trac.sagemath.org/ticket/6817





---

archive/issue_comments_056115.json:
```json
{
    "body": "Changing component from optional packages to packages.",
    "created_at": "2009-08-25T09:01:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6817",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6817#issuecomment-56115",
    "user": "https://github.com/nathanncohen"
}
```

Changing component from optional packages to packages.



---

archive/issue_comments_056116.json:
```json
{
    "body": "Changing assignee from tbd to mabshoff.",
    "created_at": "2009-08-25T09:01:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6817",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6817#issuecomment-56116",
    "user": "https://github.com/nathanncohen"
}
```

Changing assignee from tbd to mabshoff.



---

archive/issue_comments_056117.json:
```json
{
    "body": "I tested this as before (with #6502). It applies fine to 4.1.1.rc2 in an intel macbook running 10..4.11 ( I could not get 4.1.1 to compile from source on that platform), so positive review from me again.",
    "created_at": "2009-08-25T17:51:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6817",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6817#issuecomment-56117",
    "user": "https://github.com/wdjoyner"
}
```

I tested this as before (with #6502). It applies fine to 4.1.1.rc2 in an intel macbook running 10..4.11 ( I could not get 4.1.1 to compile from source on that platform), so positive review from me again.



---

archive/issue_events_016063.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mvngu",
    "created_at": "2009-09-02T16:08:40Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/6817",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/6817#event-16063"
}
```



---

archive/issue_comments_056118.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-09-02T16:08:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6817",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6817#issuecomment-56118",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

Resolution: fixed



---

archive/issue_comments_056119.json:
```json
{
    "body": "ncohen --- In future updates to the GLPK spkg, please put your custom patches, .pyx, or .pxd files under a directory called `patch`.\n\n\n\nMerged the updated spkg in the optional packages repository. See this web page\n\n\n\nhttp://www.sagemath.org/packages/optional/\n\n\n\nThe download link is\n\n\n\nhttp://www.sagemath.org/packages/optional/glpk-4.38.p0.spkg",
    "created_at": "2009-09-02T16:08:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6817",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6817#issuecomment-56119",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

ncohen --- In future updates to the GLPK spkg, please put your custom patches, .pyx, or .pxd files under a directory called `patch`.



Merged the updated spkg in the optional packages repository. See this web page



http://www.sagemath.org/packages/optional/



The download link is



http://www.sagemath.org/packages/optional/glpk-4.38.p0.spkg



---

archive/issue_comments_056120.json:
```json
{
    "body": "Changing component from packages to optional packages.",
    "created_at": "2009-09-03T09:45:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6817",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6817#issuecomment-56120",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

Changing component from packages to optional packages.

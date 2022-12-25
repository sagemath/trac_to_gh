# Issue 4008: [with spkg, needs review] OSX 10.4/5: build python without the OSX specific extensions

archive/issues_004008.json:
```json
{
    "body": "Assignee: mabshoff\n\nThis is a followup to #4407: When we build Python on OSX we per default build extensions that depend on OSX specific frameworks. Those frameworks (especially the IO one) end up pulling in Apple's libpng.dylib which is incompatible with the one we build. Consequently extension linking our libpng.dylib blows up at import time. This is an issue with #3324. Since we are not building the extensions in 64 bit OSX mode this and we have to chose between a working libpng and extension I prefer a working libpng. The spkg at\n\nhttp://sage.math.washington.edu/home/mabshoff/release-cycles-3.1.2/alpha3/python-2.5.2.p5.spkg\n\ndisables the OSX specific python extensions. Builds fine on OSX 10.4 and 10.5 and passes doctests. After applying #3324 the matrix_mod2_dense doctest now also passes.\n\nCheers,\n\nMichael\n\nIssue created by migration from https://trac.sagemath.org/ticket/4008\n\n",
    "created_at": "2008-08-30T23:42:57Z",
    "labels": [
        "component: build",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.1.2",
    "title": "[with spkg, needs review] OSX 10.4/5: build python without the OSX specific extensions",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/4008",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```
Assignee: mabshoff

This is a followup to #4407: When we build Python on OSX we per default build extensions that depend on OSX specific frameworks. Those frameworks (especially the IO one) end up pulling in Apple's libpng.dylib which is incompatible with the one we build. Consequently extension linking our libpng.dylib blows up at import time. This is an issue with #3324. Since we are not building the extensions in 64 bit OSX mode this and we have to chose between a working libpng and extension I prefer a working libpng. The spkg at

http://sage.math.washington.edu/home/mabshoff/release-cycles-3.1.2/alpha3/python-2.5.2.p5.spkg

disables the OSX specific python extensions. Builds fine on OSX 10.4 and 10.5 and passes doctests. After applying #3324 the matrix_mod2_dense doctest now also passes.

Cheers,

Michael

Issue created by migration from https://trac.sagemath.org/ticket/4008





---

archive/issue_comments_028874.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2008-08-30T23:43:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4008",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4008#issuecomment-28874",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Changing status from new to assigned.



---

archive/issue_events_009178.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2008-08-30T23:52:07Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/4008",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/4008#event-9178"
}
```



---

archive/issue_comments_028875.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-08-30T23:52:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4008",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4008#issuecomment-28875",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_028876.json:
```json
{
    "body": "Merged in Sage 3.1.2.alpha3",
    "created_at": "2008-08-30T23:52:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4008",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4008#issuecomment-28876",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged in Sage 3.1.2.alpha3

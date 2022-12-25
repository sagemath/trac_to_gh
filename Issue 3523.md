# Issue 3523: [with spkg; needs review] upgrade flint to 1.0.10

archive/issues_003523.json:
```json
{
    "body": "Assignee: mabshoff\n\nAmong other things, this fixes a MAJOR bug in flint-1.0.6 (in getting coefficients of polys) which would make that version of flint pretty useless.\n\nIssue created by migration from https://trac.sagemath.org/ticket/3523\n\n",
    "created_at": "2008-06-27T14:45:08Z",
    "labels": [
        "component: packages: standard"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.0.4",
    "title": "[with spkg; needs review] upgrade flint to 1.0.10",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/3523",
    "user": "https://github.com/williamstein"
}
```
Assignee: mabshoff

Among other things, this fixes a MAJOR bug in flint-1.0.6 (in getting coefficients of polys) which would make that version of flint pretty useless.

Issue created by migration from https://trac.sagemath.org/ticket/3523





---

archive/issue_comments_024776.json:
```json
{
    "body": "WARNING: current version of package doesn't copy libflint.so over correctly after build on linux, but does on OS X.  On linux you must do\n\n```\n   sage -f -m flint-1.0.10.spkg\n   then copy spkg/build/flint-1.0.10/src/... ?? libflint.so to SAGE_ROOT/local/lib\n```\n",
    "created_at": "2008-06-27T18:37:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3523",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3523#issuecomment-24776",
    "user": "https://github.com/williamstein"
}
```

WARNING: current version of package doesn't copy libflint.so over correctly after build on linux, but does on OS X.  On linux you must do

```
   sage -f -m flint-1.0.10.spkg
   then copy spkg/build/flint-1.0.10/src/... ?? libflint.so to SAGE_ROOT/local/lib
```




---

archive/issue_comments_024777.json:
```json
{
    "body": "I tested the most recent spkg available at the URL listed above, and it works on Mac OSX. I also watched over William's shoulder as he tested it on Linux, so I can say that I've seen it work on two platforms. Note that this ticket is an absolute necessity for both #2357 and #3502, so we should get this merged ASAP.",
    "created_at": "2008-07-01T00:38:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3523",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3523#issuecomment-24777",
    "user": "https://github.com/craigcitro"
}
```

I tested the most recent spkg available at the URL listed above, and it works on Mac OSX. I also watched over William's shoulder as he tested it on Linux, so I can say that I've seen it work on two platforms. Note that this ticket is an absolute necessity for both #2357 and #3502, so we should get this merged ASAP.



---

archive/issue_comments_024778.json:
```json
{
    "body": "Changing priority from major to blocker.",
    "created_at": "2008-07-01T00:38:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3523",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3523#issuecomment-24778",
    "user": "https://github.com/craigcitro"
}
```

Changing priority from major to blocker.



---

archive/issue_comments_024779.json:
```json
{
    "body": "Merged in Sage 3.0.4.alpha2",
    "created_at": "2008-07-01T02:57:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3523",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3523#issuecomment-24779",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged in Sage 3.0.4.alpha2



---

archive/issue_comments_024780.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-07-01T02:57:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3523",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3523#issuecomment-24780",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed



---

archive/issue_events_008039.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2008-07-01T02:57:46Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/3523",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/3523#event-8039"
}
```



---

archive/issue_comments_024781.json:
```json
{
    "body": "The package linked from #2357 modifies the Makefile in FLINT to install the NTL interface. Does this package include those changes? \n\nIt might be a good idea to check this package with the patch from #2357.",
    "created_at": "2008-07-01T08:10:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3523",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3523#issuecomment-24781",
    "user": "https://github.com/burcin"
}
```

The package linked from #2357 modifies the Makefile in FLINT to install the NTL interface. Does this package include those changes? 

It might be a good idea to check this package with the patch from #2357.



---

archive/issue_comments_024782.json:
```json
{
    "body": "No worries -- I've already done that. It works fine.",
    "created_at": "2008-07-01T14:37:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3523",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3523#issuecomment-24782",
    "user": "https://github.com/craigcitro"
}
```

No worries -- I've already done that. It works fine.

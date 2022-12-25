# Issue 4200: Update numpy to 1.2.0

archive/issues_004200.json:
```json
{
    "body": "Assignee: mabshoff\n\nNumpy 1.2.0 came out today.  An updated spkg is here: http://sage.math.washington.edu/home/jason/numpy-1.2.0.spkg\n\nCrazily, apparently some parts of numpy are deprecated and throw warnings, while other parts still use the deprecated functions.  The upshot is that Sage, upon importing scipy, displays several warnings about deprecated numpy stuff.  Also, using numpy, like in the solve_left function, triggers deprecation warnings about other parts of numpy.\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/4200\n\n",
    "created_at": "2008-09-26T04:47:29Z",
    "labels": [
        "component: packages: standard"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.1.3",
    "title": "Update numpy to 1.2.0",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/4200",
    "user": "https://github.com/jasongrout"
}
```
Assignee: mabshoff

Numpy 1.2.0 came out today.  An updated spkg is here: http://sage.math.washington.edu/home/jason/numpy-1.2.0.spkg

Crazily, apparently some parts of numpy are deprecated and throw warnings, while other parts still use the deprecated functions.  The upshot is that Sage, upon importing scipy, displays several warnings about deprecated numpy stuff.  Also, using numpy, like in the solve_left function, triggers deprecation warnings about other parts of numpy.


Issue created by migration from https://trac.sagemath.org/ticket/4200





---

archive/issue_comments_030415.json:
```json
{
    "body": "The problem might just be that we have an old version of scipy, which is triggering these deprecation warnings.",
    "created_at": "2008-09-26T04:51:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4200",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4200#issuecomment-30415",
    "user": "https://github.com/jasongrout"
}
```

The problem might just be that we have an old version of scipy, which is triggering these deprecation warnings.



---

archive/issue_comments_030416.json:
```json
{
    "body": "Hmm, feel like updating scipy then, too? That will be a littl more work since we monkey with various setup.pys, so this spkg might not make it into 3.1.3 :(\n\nCheers,\n\nMichael",
    "created_at": "2008-09-26T04:52:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4200",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4200#issuecomment-30416",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Hmm, feel like updating scipy then, too? That will be a littl more work since we monkey with various setup.pys, so this spkg might not make it into 3.1.3 :(

Cheers,

Michael



---

archive/issue_comments_030417.json:
```json
{
    "body": "Very nice work Jason, I could not have done better myself :)\n\nCheers,\n\nMichael",
    "created_at": "2008-09-27T06:46:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4200",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4200#issuecomment-30417",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Very nice work Jason, I could not have done better myself :)

Cheers,

Michael



---

archive/issue_comments_030418.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-09-27T06:46:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4200",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4200#issuecomment-30418",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed



---

archive/issue_events_004439.json:
```json
{
    "actor": "mabshoff",
    "created_at": "2008-09-27T06:46:39Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/4200",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/4200#event-4439"
}
```



---

archive/issue_comments_030419.json:
```json
{
    "body": "Merged in Sage 3.1.3.alpha2",
    "created_at": "2008-09-27T06:46:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4200",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4200#issuecomment-30419",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged in Sage 3.1.3.alpha2

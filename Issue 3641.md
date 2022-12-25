# Issue 3641: [with spkg, needs review] new Singular upstream release

archive/issues_003641.json:
```json
{
    "body": "Assignee: mabshoff\n\nKeywords: singular\n\n\n```\nTue Nov 27 12:16:36 CET 2007 Singular-3-0-4-1\nChanges with respect to 3-0-4\n- dmod.lib: fixes wrt. nc_algebra and documentation\n- allow assignments like: def l=1,2,3;\n```\n\n\nThe new version also has a memleak we reported eliminated.\n\nIssue created by migration from https://trac.sagemath.org/ticket/3641\n\n",
    "created_at": "2008-07-11T15:30:33Z",
    "labels": [
        "component: packages: standard",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.1.2",
    "title": "[with spkg, needs review] new Singular upstream release",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/3641",
    "user": "https://github.com/malb"
}
```
Assignee: mabshoff

Keywords: singular


```
Tue Nov 27 12:16:36 CET 2007 Singular-3-0-4-1
Changes with respect to 3-0-4
- dmod.lib: fixes wrt. nc_algebra and documentation
- allow assignments like: def l=1,2,3;
```


The new version also has a memleak we reported eliminated.

Issue created by migration from https://trac.sagemath.org/ticket/3641





---

archive/issue_comments_025694.json:
```json
{
    "body": "The new spkg is here:\n\n  http://sage.math.washington.edu/home/malb/spkgs/singular-3-0-4-4-20080711.spkg",
    "created_at": "2008-07-11T15:31:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3641",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3641#issuecomment-25694",
    "user": "https://github.com/malb"
}
```

The new spkg is here:

  http://sage.math.washington.edu/home/malb/spkgs/singular-3-0-4-4-20080711.spkg



---

archive/issue_comments_025695.json:
```json
{
    "body": "Installs fine on my Debian/Linux 64-bit, Core2Duo\n\n\n```\nsage -tp 2 devel/sage/sage/rings\n...\nAll tests passed!\n```\n\n\nSorry, don't have time right now to run the whole test suite.",
    "created_at": "2008-07-11T15:42:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3641",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3641#issuecomment-25695",
    "user": "https://github.com/malb"
}
```

Installs fine on my Debian/Linux 64-bit, Core2Duo


```
sage -tp 2 devel/sage/sage/rings
...
All tests passed!
```


Sorry, don't have time right now to run the whole test suite.



---

archive/issue_comments_025696.json:
```json
{
    "body": "Changing keywords from \"singular\" to \"singular, editor_mabshoff\".",
    "created_at": "2008-08-02T03:11:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3641",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3641#issuecomment-25696",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Changing keywords from "singular" to "singular, editor_mabshoff".



---

archive/issue_comments_025697.json:
```json
{
    "body": "Spkg looks good to me.\n\nCheers,\n\nMichael",
    "created_at": "2008-08-19T22:50:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3641",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3641#issuecomment-25697",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Spkg looks good to me.

Cheers,

Michael



---

archive/issue_comments_025698.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-08-19T23:08:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3641",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3641#issuecomment-25698",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_025699.json:
```json
{
    "body": "Merged in Sage 3.1.2.alpha0",
    "created_at": "2008-08-19T23:08:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3641",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3641#issuecomment-25699",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged in Sage 3.1.2.alpha0



---

archive/issue_events_003860.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2008-08-19T23:08:24Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/3641",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/3641#event-3860"
}
```

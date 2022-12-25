# Issue 4243: [with spkg, needs review] pynac package version bump to 0.1.1

archive/issues_004243.json:
```json
{
    "body": "Assignee: mabshoff\n\nCC:  @williamstein @mwhansen\n\nKeywords: pynac, symbolics\n\nThere is a new version of pynac available. :)\n\nThis version allows setting custom python functions to perform evaluation, numeric evaluation, derivation, series expansion, etc. on symbolic functions.\n\nThe new package is available is here:\n\nhttp://www.risc.jku.at/people/berocal/sage/pynac-0.1.1.spkg\n\nIssue created by migration from https://trac.sagemath.org/ticket/4243\n\n",
    "created_at": "2008-10-04T20:26:25Z",
    "labels": [
        "component: packages: standard"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.2",
    "title": "[with spkg, needs review] pynac package version bump to 0.1.1",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/4243",
    "user": "https://github.com/burcin"
}
```
Assignee: mabshoff

CC:  @williamstein @mwhansen

Keywords: pynac, symbolics

There is a new version of pynac available. :)

This version allows setting custom python functions to perform evaluation, numeric evaluation, derivation, series expansion, etc. on symbolic functions.

The new package is available is here:

http://www.risc.jku.at/people/berocal/sage/pynac-0.1.1.spkg

Issue created by migration from https://trac.sagemath.org/ticket/4243





---

archive/issue_comments_030780.json:
```json
{
    "body": "I updated the package at the address given in the description to correspond to the latest patch added to #4244.\n\nNote that the package will break sage if the patches in #4244 are not applied, since libpynac will complain about missing symbols.",
    "created_at": "2008-10-15T09:14:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4243",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4243#issuecomment-30780",
    "user": "https://github.com/burcin"
}
```

I updated the package at the address given in the description to correspond to the latest patch added to #4244.

Note that the package will break sage if the patches in #4244 are not applied, since libpynac will complain about missing symbols.



---

archive/issue_comments_030781.json:
```json
{
    "body": "Spkg looks good to me. I read Burcin's changes, but having another expert looks over this wouldn't hurt. Either way: damn the torpedoes :)\n\nCheers,\n\nMichael",
    "created_at": "2008-10-18T12:26:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4243",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4243#issuecomment-30781",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Spkg looks good to me. I read Burcin's changes, but having another expert looks over this wouldn't hurt. Either way: damn the torpedoes :)

Cheers,

Michael



---

archive/issue_events_004482.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2008-10-18T13:05:15Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/4243",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/4243#event-4482"
}
```



---

archive/issue_comments_030782.json:
```json
{
    "body": "Merged in Sage 3.2.alpha0",
    "created_at": "2008-10-18T13:05:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4243",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4243#issuecomment-30782",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged in Sage 3.2.alpha0



---

archive/issue_comments_030783.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-10-18T13:05:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4243",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4243#issuecomment-30783",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed

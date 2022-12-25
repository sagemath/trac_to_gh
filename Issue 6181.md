# Issue 6181: The r-2.6.1.p22 spkg was created on OSX hence contains a bunch of crap

archive/issues_006181.json:
```json
{
    "body": "Assignee: mabshoff\n\nIf you extract r-2.6.1.p22.spkg on Linux with \"tar jxvf\" you'll see lots of stuff like this:\n\n\n```\nr-2.6.1.p22/src/src/library/grid/man/grid.layout.Rd\nr-2.6.1.p22/src/src/library/grid/man/._grid.lines.Rd\nr-2.6.1.p22/src/src/library/grid/man/grid.lines.Rd\nr-2.6.1.p22/src/src/library/grid/man/._grid.locator.Rd\nr-2.6.1.p22/src/src/library/grid/man/grid.locator.Rd\nr-2.6.1.p22/src/src/library/grid/man/._grid.ls.Rd\nr-2.6.1.p22/src/src/library/grid/man/grid.ls.Rd\n```\n\n\nThese ._ files are all caused by making the tarball on OS X, and shouldn't be there. \n\nIssue created by migration from https://trac.sagemath.org/ticket/6181\n\n",
    "created_at": "2009-06-02T06:35:41Z",
    "labels": [
        "component: packages: standard",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-duplicate/invalid/wontfix",
    "title": "The r-2.6.1.p22 spkg was created on OSX hence contains a bunch of crap",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/6181",
    "user": "https://github.com/williamstein"
}
```
Assignee: mabshoff

If you extract r-2.6.1.p22.spkg on Linux with "tar jxvf" you'll see lots of stuff like this:


```
r-2.6.1.p22/src/src/library/grid/man/grid.layout.Rd
r-2.6.1.p22/src/src/library/grid/man/._grid.lines.Rd
r-2.6.1.p22/src/src/library/grid/man/grid.lines.Rd
r-2.6.1.p22/src/src/library/grid/man/._grid.locator.Rd
r-2.6.1.p22/src/src/library/grid/man/grid.locator.Rd
r-2.6.1.p22/src/src/library/grid/man/._grid.ls.Rd
r-2.6.1.p22/src/src/library/grid/man/grid.ls.Rd
```


These ._ files are all caused by making the tarball on OS X, and shouldn't be there. 

Issue created by migration from https://trac.sagemath.org/ticket/6181





---

archive/issue_comments_049253.json:
```json
{
    "body": "#6280 is a dup of this.",
    "created_at": "2009-09-16T16:35:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6181",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6181#issuecomment-49253",
    "user": "https://github.com/jasongrout"
}
```

#6280 is a dup of this.



---

archive/issue_comments_049254.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2009-09-16T16:35:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6181",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6181#issuecomment-49254",
    "user": "https://github.com/jasongrout"
}
```

Changing status from new to assigned.



---

archive/issue_comments_049255.json:
```json
{
    "body": "Changing assignee from mabshoff to @jasongrout.",
    "created_at": "2009-09-16T16:35:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6181",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6181#issuecomment-49255",
    "user": "https://github.com/jasongrout"
}
```

Changing assignee from mabshoff to @jasongrout.



---

archive/issue_comments_049256.json:
```json
{
    "body": "Closing this as a duplicate of #6280.",
    "created_at": "2009-10-01T05:51:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6181",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6181#issuecomment-49256",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

Closing this as a duplicate of #6280.



---

archive/issue_comments_049257.json:
```json
{
    "body": "Resolution: duplicate",
    "created_at": "2009-10-01T05:51:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6181",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6181#issuecomment-49257",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

Resolution: duplicate

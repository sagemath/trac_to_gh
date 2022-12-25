# Issue 4040: Update biopython optional package to 1.47

archive/issues_004040.json:
```json
{
    "body": "Assignee: mabshoff\n\nKeywords: biopython, optional packages\n\nJust keeping this package up to date.  Actually 1.48 will be out pretty soon.\n\nIssue created by migration from https://trac.sagemath.org/ticket/4040\n\n",
    "created_at": "2008-09-02T20:32:45Z",
    "labels": [
        "component: packages: optional",
        "minor"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.1.2",
    "title": "Update biopython optional package to 1.47",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/4040",
    "user": "https://trac.sagemath.org/admin/accounts/users/mhampton"
}
```
Assignee: mabshoff

Keywords: biopython, optional packages

Just keeping this package up to date.  Actually 1.48 will be out pretty soon.

Issue created by migration from https://trac.sagemath.org/ticket/4040





---

archive/issue_comments_029083.json:
```json
{
    "body": "First attempt is up at:\n\nhttp://www.d.umn.edu/~mhampton/biopython-1.47.spkg",
    "created_at": "2008-09-02T20:34:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4040",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4040#issuecomment-29083",
    "user": "https://trac.sagemath.org/admin/accounts/users/mhampton"
}
```

First attempt is up at:

http://www.d.umn.edu/~mhampton/biopython-1.47.spkg



---

archive/issue_comments_029084.json:
```json
{
    "body": "I fixed a bunch of issues: \n\n* put the repo back in. *Never* remove the hg repo in an spkg.\n* put back \"exit 1\" in case either one of the python modules fails to build\n* moved setup.py into patches where it belongs\n* checked in all the changes\n* removed OSX crap files, i.e. `._*`\n\nWith those changes I give this spkg at\n\nhttp://sage.math.washington.edu/home/mabshoff/release-cycles-3.1.2/rc0/biopython-1.47.spkg\n\na positive review. Please base future spkgs on this one since I did not increment the patch level.\n\nCheers,\n\nMichael",
    "created_at": "2008-09-04T02:45:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4040",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4040#issuecomment-29084",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

I fixed a bunch of issues: 

* put the repo back in. *Never* remove the hg repo in an spkg.
* put back "exit 1" in case either one of the python modules fails to build
* moved setup.py into patches where it belongs
* checked in all the changes
* removed OSX crap files, i.e. `._*`

With those changes I give this spkg at

http://sage.math.washington.edu/home/mabshoff/release-cycles-3.1.2/rc0/biopython-1.47.spkg

a positive review. Please base future spkgs on this one since I did not increment the patch level.

Cheers,

Michael



---

archive/issue_comments_029085.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-09-04T02:48:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4040",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4040#issuecomment-29085",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed



---

archive/issue_events_004270.json:
```json
{
    "actor": "mabshoff",
    "created_at": "2008-09-04T02:48:07Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/4040",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/4040#event-4270"
}
```



---

archive/issue_comments_029086.json:
```json
{
    "body": "Merged into the optional repo in Sage 3.1.2.rc0.",
    "created_at": "2008-09-04T02:48:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4040",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4040#issuecomment-29086",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged into the optional repo in Sage 3.1.2.rc0.

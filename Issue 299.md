# Issue 299: add make check to all spkg where it is missing

archive/issues_000299.json:
```json
{
    "body": "Assignee: mabshoff\n\nProject:\nGo through every spkg in the SAGE standard distribution and add a file\n\n   spkg-check\n\nthat runs whatever the standard test program is for that package, assuming\nspkg-install has already run successfully.  For example, for many programs\n(e.g., gmp), this will just be:\n\n  make check\n\nor maybe \"make test\".\n\nThe program spkg-check should exit with a 0 code if and only if all tests pass.\n\nThen when building SAGE, if one did something like\n\n   export CHECK=1\n   make\n\nthen all spkg-check's would get run along the way.  The build would take much longer,\nbut would be much more confidence inspiring. \n\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/299\n\n",
    "closed_at": "2008-08-30T07:08:43Z",
    "created_at": "2007-02-27T14:49:57Z",
    "labels": [
        "component: packages: standard"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.1.2",
    "title": "add make check to all spkg where it is missing",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/299",
    "user": "https://github.com/williamstein"
}
```
Assignee: mabshoff

Project:
Go through every spkg in the SAGE standard distribution and add a file

   spkg-check

that runs whatever the standard test program is for that package, assuming
spkg-install has already run successfully.  For example, for many programs
(e.g., gmp), this will just be:

  make check

or maybe "make test".

The program spkg-check should exit with a 0 code if and only if all tests pass.

Then when building SAGE, if one did something like

   export CHECK=1
   make

then all spkg-check's would get run along the way.  The build would take much longer,
but would be much more confidence inspiring. 



Issue created by migration from https://trac.sagemath.org/ticket/299





---

archive/issue_events_000693.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2007-08-21T13:11:57Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/299",
    "milestone": "sage-3.0",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/299#event-693"
}
```



---

archive/issue_comments_001419.json:
```json
{
    "body": "The following come from #153 (which I have just closed as a duplicate)\n\nIt would also be nice to use the \"-t\" flag to run spkg-check when building packages:\n\n```\n  sage -i -t packagename.spkg\n```\n\nCheers,\n\nMichael",
    "created_at": "2007-08-23T11:31:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/299",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/299#issuecomment-1419",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

The following come from #153 (which I have just closed as a duplicate)

It would also be nice to use the "-t" flag to run spkg-check when building packages:

```
  sage -i -t packagename.spkg
```

Cheers,

Michael



---

archive/issue_comments_001420.json:
```json
{
    "body": "Changing assignee from @williamstein to mabshoff.",
    "created_at": "2008-01-26T13:22:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/299",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/299#issuecomment-1420",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Changing assignee from @williamstein to mabshoff.



---

archive/issue_comments_001421.json:
```json
{
    "body": "We now have `SAGE_CHECK` which in case of `SAGE_CHECK==yes` triggers the automated running of `{spkg-check`\n\nCheers,\n\nMichael",
    "created_at": "2008-01-26T13:22:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/299",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/299#issuecomment-1421",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

We now have `SAGE_CHECK` which in case of `SAGE_CHECK==yes` triggers the automated running of `{spkg-check`

Cheers,

Michael



---

archive/issue_comments_001422.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2008-01-26T14:40:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/299",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/299#issuecomment-1422",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Changing status from new to assigned.



---

archive/issue_events_000694.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2008-08-30T07:08:43Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/299",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/299#event-694"
}
```



---

archive/issue_comments_001423.json:
```json
{
    "body": "As far as I know all spkgs now have spkg-checks if applicable. If any spkgs turns out to miss one we need to open a specific ticket for that spkg. Closed.\n\nCheers,\n\nMichael",
    "created_at": "2008-08-30T07:08:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/299",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/299#issuecomment-1423",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

As far as I know all spkgs now have spkg-checks if applicable. If any spkgs turns out to miss one we need to open a specific ticket for that spkg. Closed.

Cheers,

Michael



---

archive/issue_comments_001424.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-08-30T07:08:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/299",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/299#issuecomment-1424",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed

# Issue 993: Pari's gp interpreter has built-in library search path, defeating Sage mechanisms

archive/issues_000993.json:
```json
{
    "body": "Assignee: @williamstein\n\nPari uses \"-rpath\" (or its equivalent) when building gp, to hardcode a library search path.  This search path is used before the $LD_LIBRARY_PATH set by Sage.  The hardcoded search path includes $SAGE_ROOT/local/lib:/usr/lib .\n\nNormally, this is harmless (and perhaps slightly beneficial, since it means you can run $SAGE_ROOT/local/bin/gp directly, without having the SAGE environment variables set).  However, if you move your Sage installation tree, the hardcoded search path ensures that gp will search /usr/lib before the Sage libraries.  If your /usr/lib has libgmp or libpari-gmp libraries, these will be used instead of Sage's versions, leading (in my case) to one actual doctest failure (where the value of gp(log2), as tested in constants.py, was rounded correctly, rather than the slightly incorrect rounding enshrined in the doctest).\n\nIssue created by migration from https://trac.sagemath.org/ticket/993\n\n",
    "created_at": "2007-10-25T05:01:15Z",
    "labels": [
        "component: packages: standard",
        "minor",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-2.8.11",
    "title": "Pari's gp interpreter has built-in library search path, defeating Sage mechanisms",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/993",
    "user": "https://trac.sagemath.org/admin/accounts/users/cwitty"
}
```
Assignee: @williamstein

Pari uses "-rpath" (or its equivalent) when building gp, to hardcode a library search path.  This search path is used before the $LD_LIBRARY_PATH set by Sage.  The hardcoded search path includes $SAGE_ROOT/local/lib:/usr/lib .

Normally, this is harmless (and perhaps slightly beneficial, since it means you can run $SAGE_ROOT/local/bin/gp directly, without having the SAGE environment variables set).  However, if you move your Sage installation tree, the hardcoded search path ensures that gp will search /usr/lib before the Sage libraries.  If your /usr/lib has libgmp or libpari-gmp libraries, these will be used instead of Sage's versions, leading (in my case) to one actual doctest failure (where the value of gp(log2), as tested in constants.py, was rounded correctly, rather than the slightly incorrect rounding enshrined in the doctest).

Issue created by migration from https://trac.sagemath.org/ticket/993





---

archive/issue_comments_006033.json:
```json
{
    "body": "Changing assignee from @williamstein to cwitty.",
    "created_at": "2007-10-25T05:15:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/993",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/993#issuecomment-6033",
    "user": "https://trac.sagemath.org/admin/accounts/users/cwitty"
}
```

Changing assignee from @williamstein to cwitty.



---

archive/issue_comments_006034.json:
```json
{
    "body": "I've put up a new Pari spkg at http://sage.math.washington.edu/home/cwitty/pari-2.3.2.p4.spkg that disables the use of rpath entirely.  (It's been tested on Linux, but not OS X.)  (This spkg also fixes #830.)",
    "created_at": "2007-11-01T06:03:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/993",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/993#issuecomment-6034",
    "user": "https://trac.sagemath.org/admin/accounts/users/cwitty"
}
```

I've put up a new Pari spkg at http://sage.math.washington.edu/home/cwitty/pari-2.3.2.p4.spkg that disables the use of rpath entirely.  (It's been tested on Linux, but not OS X.)  (This spkg also fixes #830.)



---

archive/issue_comments_006035.json:
```json
{
    "body": "I tested this on osx intel and osx ppc and it works.",
    "created_at": "2007-11-01T07:13:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/993",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/993#issuecomment-6035",
    "user": "https://github.com/williamstein"
}
```

I tested this on osx intel and osx ppc and it works.



---

archive/issue_comments_006036.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2007-11-01T10:41:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/993",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/993#issuecomment-6036",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_006037.json:
```json
{
    "body": "applied to 2.8.11.alpha0",
    "created_at": "2007-11-01T10:41:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/993",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/993#issuecomment-6037",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

applied to 2.8.11.alpha0



---

archive/issue_events_002740.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2007-11-01T10:41:21Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/993",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/993#event-2740"
}
```

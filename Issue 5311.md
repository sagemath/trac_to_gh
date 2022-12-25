# Issue 5311: Update to ATLAS 3.8.3 (latest upstream release)

archive/issues_005311.json:
```json
{
    "body": "Assignee: mabshoff\n\nClint writes:\n\n```\nI have released 3.8.3.  This is, of course, mainly a bugfix release.\nHowever, I have also backported some assembly kernels from the 3.9 series\nfor the Core2 and AMD64K10h architectures.  We have architectural defaults\nfor these systems, as well as the new Corei7 (64 bit only).  For Core2-based\nsystems, the speedup is substantial (K10h speedup is modest).\n\nYou should also be aware of one error, *which has not been fixed in 3.8.3*\n  http://math-atlas.sourceforge.net/errata.html#scal0\n\nCheers,\nClint\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/5311\n\n",
    "created_at": "2009-02-19T05:16:09Z",
    "labels": [
        "component: packages: standard",
        "critical",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.3",
    "title": "Update to ATLAS 3.8.3 (latest upstream release)",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/5311",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```
Assignee: mabshoff

Clint writes:

```
I have released 3.8.3.  This is, of course, mainly a bugfix release.
However, I have also backported some assembly kernels from the 3.9 series
for the Core2 and AMD64K10h architectures.  We have architectural defaults
for these systems, as well as the new Corei7 (64 bit only).  For Core2-based
systems, the speedup is substantial (K10h speedup is modest).

You should also be aware of one error, *which has not been fixed in 3.8.3*
  http://math-atlas.sourceforge.net/errata.html#scal0

Cheers,
Clint
```


Issue created by migration from https://trac.sagemath.org/ticket/5311





---

archive/issue_events_012366.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2009-02-20T06:41:37Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/5311",
    "milestone": "sage-3.3",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/5311#event-12366"
}
```



---

archive/issue_comments_040830.json:
```json
{
    "body": "The spkg at\n\n http://sage.math.washington.edu/home/mabshoff/release-cycles-3.3/rc3/atlas-3.8.3.spkg\n\nupdates to ATLAS 3.8.3. The following patches were rebased/changed:\n\n* archinfo_linux.c - only the Itanium hunk is needed\n* archinfo_x86.c - only case 6 PIV hunk is needed\n* Make.top - identical \n* probe_comp.c - needs to be rebased to account for SiCortex fix\n\nOther than that the Core i7 support works, it identifies the Itanium2 boxen on SkyNet correctly (vanilla ATLAS doesn't) and this spkg also fixes #1641.\n\nCheers,\n\nMichael",
    "created_at": "2009-02-20T20:22:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5311",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5311#issuecomment-40830",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

The spkg at

 http://sage.math.washington.edu/home/mabshoff/release-cycles-3.3/rc3/atlas-3.8.3.spkg

updates to ATLAS 3.8.3. The following patches were rebased/changed:

* archinfo_linux.c - only the Itanium hunk is needed
* archinfo_x86.c - only case 6 PIV hunk is needed
* Make.top - identical 
* probe_comp.c - needs to be rebased to account for SiCortex fix

Other than that the Core i7 support works, it identifies the Itanium2 boxen on SkyNet correctly (vanilla ATLAS doesn't) and this spkg also fixes #1641.

Cheers,

Michael



---

archive/issue_comments_040831.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2009-02-20T20:22:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5311",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5311#issuecomment-40831",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Changing status from new to assigned.



---

archive/issue_comments_040832.json:
```json
{
    "body": "Happily installs and runs on 3.3.alpha4 (what I had laying around on the i7 box).  \n\nOther comments recommended by mabshoff: \n\n(12:51:46 PM) mabs: Well, it is a very clean spkg with 3 beautiful commits.\n\n(12:52:06 PM) mabs: This is the best spkg ever. Michael needs to get a gold star :)\n\n(12:52:41 PM) mabs: I tested it widely, so it will work :)\n\nseems about right",
    "created_at": "2009-02-20T20:56:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5311",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5311#issuecomment-40832",
    "user": "https://trac.sagemath.org/admin/accounts/users/ghtdak"
}
```

Happily installs and runs on 3.3.alpha4 (what I had laying around on the i7 box).  

Other comments recommended by mabshoff: 

(12:51:46 PM) mabs: Well, it is a very clean spkg with 3 beautiful commits.

(12:52:06 PM) mabs: This is the best spkg ever. Michael needs to get a gold star :)

(12:52:41 PM) mabs: I tested it widely, so it will work :)

seems about right



---

archive/issue_comments_040833.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-02-20T20:58:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5311",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5311#issuecomment-40833",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_040834.json:
```json
{
    "body": "Merged in Sage 3.3.rc3.\n\nCheers,\n\nMichael",
    "created_at": "2009-02-20T20:58:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5311",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5311#issuecomment-40834",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged in Sage 3.3.rc3.

Cheers,

Michael



---

archive/issue_events_012367.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2009-02-20T20:58:55Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/5311",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/5311#event-12367"
}
```

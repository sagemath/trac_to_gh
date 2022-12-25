# Issue 1626: update lcalc to 20070902

archive/issues_001626.json:
```json
{
    "body": "Assignee: mabshoff\n\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/1626\n\n",
    "created_at": "2007-12-29T04:39:50Z",
    "labels": [
        "component: packages: standard",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.0",
    "title": "update lcalc to 20070902",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/1626",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```
Assignee: mabshoff



Issue created by migration from https://trac.sagemath.org/ticket/1626





---

archive/issue_comments_010330.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2007-12-29T04:39:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1626",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1626#issuecomment-10330",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Changing status from new to assigned.



---

archive/issue_comments_010331.json:
```json
{
    "body": "See also #932 and #449.\n\nCheers,\n\nMichael",
    "created_at": "2008-01-27T17:27:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1626",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1626#issuecomment-10331",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

See also #932 and #449.

Cheers,

Michael



---

archive/issue_comments_010332.json:
```json
{
    "body": "Update it to NOW:\n\n```\nDear Colleagues,\n\nI've released a new version of lcalc.\n\nThis release fixes some bugs (so please update), has improvements to some of the key\nroutines, especially for higher degree L-functions (i.e. deg >=3, and also for Maass forms),\nand better handling of output precision.\n\nThe code can be downloaded from:\nhttp://pmmac03.math.uwaterloo.ca/~mrubinst/L_function_public/CODE/\n\nPlease email me any bugs you notice.\n\nThanks,\n```\n",
    "created_at": "2008-01-27T17:32:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1626",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1626#issuecomment-10332",
    "user": "https://github.com/williamstein"
}
```

Update it to NOW:

```
Dear Colleagues,

I've released a new version of lcalc.

This release fixes some bugs (so please update), has improvements to some of the key
routines, especially for higher degree L-functions (i.e. deg >=3, and also for Maass forms),
and better handling of output precision.

The code can be downloaded from:
http://pmmac03.math.uwaterloo.ca/~mrubinst/L_function_public/CODE/

Please email me any bugs you notice.

Thanks,
```




---

archive/issue_comments_010333.json:
```json
{
    "body": "The latest release is from Feb. 5th, 2008. I did fix some warnings, fixed a Solaris build issue and squashed about 500 lines of warnings. The changes have been send upstream and will hopefully be integrated soon.\n\nCheers,\n\nMichael",
    "created_at": "2008-03-26T00:08:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1626",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1626#issuecomment-10333",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

The latest release is from Feb. 5th, 2008. I did fix some warnings, fixed a Solaris build issue and squashed about 500 lines of warnings. The changes have been send upstream and will hopefully be integrated soon.

Cheers,

Michael



---

archive/issue_comments_010334.json:
```json
{
    "body": "Attachment [lcalc-1.11-constification+solaris.patch](tarball://root/attachments/some-uuid/ticket1626/lcalc-1.11-constification+solaris.patch) by mabshoff created at 2008-03-26 00:08:58",
    "created_at": "2008-03-26T00:08:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1626",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1626#issuecomment-10334",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Attachment [lcalc-1.11-constification+solaris.patch](tarball://root/attachments/some-uuid/ticket1626/lcalc-1.11-constification+solaris.patch) by mabshoff created at 2008-03-26 00:08:58



---

archive/issue_comments_010335.json:
```json
{
    "body": "Attachment [lcalc-1.11-memleak-fixes.patch](tarball://root/attachments/some-uuid/ticket1626/lcalc-1.11-memleak-fixes.patch) by mabshoff created at 2008-03-26 00:09:39",
    "created_at": "2008-03-26T00:09:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1626",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1626#issuecomment-10335",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Attachment [lcalc-1.11-memleak-fixes.patch](tarball://root/attachments/some-uuid/ticket1626/lcalc-1.11-memleak-fixes.patch) by mabshoff created at 2008-03-26 00:09:39



---

archive/issue_comments_010336.json:
```json
{
    "body": "The updated lcalc.spkg has some doctest failures:\n\n```\nsage -t -long devel/sage/sage/lfunctions/lcalc.py\n**********************************************************************\nFile \"/scratch/mabshoff/release-cycle/sage-3.0.alpha5/tmp/lcalc.py\", line 188:\n    sage: E.lseries().values_along_line(0.5, 3, 5)\nExpected:\n    lcalc:  1.5 0 WARNING- we don't have enough Dirichlet coefficients.\n    lcalc:  Will use the maximum possible, though the output will not necessarily be accurate.\n    lcalc:  nan nan\n    [(0, 0.209951303),\n     (0.500000000, -...e-16),\n     (1.00000000, 0.133768433),\n     (2.00000000, 0.552975867)]\nGot:\n    [(0, 0.209951303), (0.500000000, -2.96501173e-16), (1.00000000, 0.133768433), (1.50000000, 0.360092864), (2.00000000, 0.552975867)]\n```\n\nI consider this good news and suggest fixing the doctest.\n\nCheers,\n\nMichael",
    "created_at": "2008-04-14T02:51:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1626",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1626#issuecomment-10336",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

The updated lcalc.spkg has some doctest failures:

```
sage -t -long devel/sage/sage/lfunctions/lcalc.py
**********************************************************************
File "/scratch/mabshoff/release-cycle/sage-3.0.alpha5/tmp/lcalc.py", line 188:
    sage: E.lseries().values_along_line(0.5, 3, 5)
Expected:
    lcalc:  1.5 0 WARNING- we don't have enough Dirichlet coefficients.
    lcalc:  Will use the maximum possible, though the output will not necessarily be accurate.
    lcalc:  nan nan
    [(0, 0.209951303),
     (0.500000000, -...e-16),
     (1.00000000, 0.133768433),
     (2.00000000, 0.552975867)]
Got:
    [(0, 0.209951303), (0.500000000, -2.96501173e-16), (1.00000000, 0.133768433), (1.50000000, 0.360092864), (2.00000000, 0.552975867)]
```

I consider this good news and suggest fixing the doctest.

Cheers,

Michael



---

archive/issue_comments_010337.json:
```json
{
    "body": "Attachment [lcalc-1.11-gcc-4.3-build.patch](tarball://root/attachments/some-uuid/ticket1626/lcalc-1.11-gcc-4.3-build.patch) by mabshoff created at 2008-04-14 03:25:51",
    "created_at": "2008-04-14T03:25:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1626",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1626#issuecomment-10337",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Attachment [lcalc-1.11-gcc-4.3-build.patch](tarball://root/attachments/some-uuid/ticket1626/lcalc-1.11-gcc-4.3-build.patch) by mabshoff created at 2008-04-14 03:25:51



---

archive/issue_comments_010338.json:
```json
{
    "body": "Attachment [trac_1626_lcalc_doctest_fix.patch](tarball://root/attachments/some-uuid/ticket1626/trac_1626_lcalc_doctest_fix.patch) by mabshoff created at 2008-04-14 03:26:19",
    "created_at": "2008-04-14T03:26:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1626",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1626#issuecomment-10338",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Attachment [trac_1626_lcalc_doctest_fix.patch](tarball://root/attachments/some-uuid/ticket1626/trac_1626_lcalc_doctest_fix.patch) by mabshoff created at 2008-04-14 03:26:19



---

archive/issue_comments_010339.json:
```json
{
    "body": "The updated spkg at \n\nhttp://sage.math.washington.edu/home/mabshoff/release-cycles-3.0/alpha5/lcalc-20080205.spkg\n\nfixes a number of issues:\n\n* update to to the latest release\n* fix Solaris build\n* add gcc 4.3 build support\n\nThis ticket also closes #449. For doctests to pass you need to apply trac_1626_lcalc_doctest_fix.patch.\n\nThe other three patches have been send upstream to Mike Rubinstein and will hopefully make it into the next upstream release.\n\nCheers,\n\nMichael",
    "created_at": "2008-04-14T03:28:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1626",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1626#issuecomment-10339",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

The updated spkg at 

http://sage.math.washington.edu/home/mabshoff/release-cycles-3.0/alpha5/lcalc-20080205.spkg

fixes a number of issues:

* update to to the latest release
* fix Solaris build
* add gcc 4.3 build support

This ticket also closes #449. For doctests to pass you need to apply trac_1626_lcalc_doctest_fix.patch.

The other three patches have been send upstream to Mike Rubinstein and will hopefully make it into the next upstream release.

Cheers,

Michael



---

archive/issue_comments_010340.json:
```json
{
    "body": "REPORT:\n\nI have not tried the patch out, but I read everything carefully and it all looks *perfect* to me.",
    "created_at": "2008-04-14T03:37:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1626",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1626#issuecomment-10340",
    "user": "https://github.com/williamstein"
}
```

REPORT:

I have not tried the patch out, but I read everything carefully and it all looks *perfect* to me.



---

archive/issue_comments_010341.json:
```json
{
    "body": "Merged in Sage 3.0.alpha5",
    "created_at": "2008-04-14T03:56:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1626",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1626#issuecomment-10341",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged in Sage 3.0.alpha5



---

archive/issue_comments_010342.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-04-14T03:56:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1626",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1626#issuecomment-10342",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed



---

archive/issue_events_001785.json:
```json
{
    "actor": "mabshoff",
    "created_at": "2008-04-14T03:56:48Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/1626",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/1626#event-1785"
}
```

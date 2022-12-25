# Issue 4711: fix ptest race condition: "file not found"

archive/issues_004711.json:
```json
{
    "body": "Assignee: @garyfurnish\n\n\n```\n\n[10:16pm] mabshoff: gfurnish: just hit another race condition with ptest:\n[10:16pm] mabshoff: sage -t  devel/sage/sage/gsl/gsl_sf_result.pxi\n[10:16pm] mabshoff: Error running /scratch/mabshoff/release-cycle/sage-3.2.2.alpha0/local/bin/sage-doctest, since file gsl_sf_result.pxi does not exist.\n[10:16pm] mabshoff: It is probably the same as the one where the doctest is only half written\n[10:16pm] gfurnish: hm \n[10:17pm] gfurnish: don't touch anything\n[10:17pm] gfurnish: let me look in your directory\n[10:17pm] mabshoff: mk\n[10:17pm] You are now known as mabs|ds0.\n[10:17pm] You are now known as mab|ds9.\n[10:17pm] mab|ds9:\n[10:17pm] gfurnish: nothing in tmp dir?\n[10:18pm] gfurnish: oh nm\n[10:18pm] mab|ds9: The last line of the output was also \"sage -t  devel/sage/sage/gsl/gsl_sf_result.pxi # File not found\"\n[10:18pm] gfurnish: that sounds like a ptest bug.\n[10:19pm] gfurnish: yeah um\n[10:19pm] gfurnish: I know whats causing that problem\n[10:19pm] gfurnish: make a ticket\n[10:20pm] gfurnish: I fixed the bug in pbuild\n[10:20pm] mab|ds9: Is it orthogonal to the other race condition then I assume?\n[10:21pm] gfurnish: I think so\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/4711\n\n",
    "created_at": "2008-12-05T06:24:50Z",
    "labels": [
        "component: build",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.2.2",
    "title": "fix ptest race condition: \"file not found\"",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/4711",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```
Assignee: @garyfurnish


```

[10:16pm] mabshoff: gfurnish: just hit another race condition with ptest:
[10:16pm] mabshoff: sage -t  devel/sage/sage/gsl/gsl_sf_result.pxi
[10:16pm] mabshoff: Error running /scratch/mabshoff/release-cycle/sage-3.2.2.alpha0/local/bin/sage-doctest, since file gsl_sf_result.pxi does not exist.
[10:16pm] mabshoff: It is probably the same as the one where the doctest is only half written
[10:16pm] gfurnish: hm 
[10:17pm] gfurnish: don't touch anything
[10:17pm] gfurnish: let me look in your directory
[10:17pm] mabshoff: mk
[10:17pm] You are now known as mabs|ds0.
[10:17pm] You are now known as mab|ds9.
[10:17pm] mab|ds9:
[10:17pm] gfurnish: nothing in tmp dir?
[10:18pm] gfurnish: oh nm
[10:18pm] mab|ds9: The last line of the output was also "sage -t  devel/sage/sage/gsl/gsl_sf_result.pxi # File not found"
[10:18pm] gfurnish: that sounds like a ptest bug.
[10:19pm] gfurnish: yeah um
[10:19pm] gfurnish: I know whats causing that problem
[10:19pm] gfurnish: make a ticket
[10:20pm] gfurnish: I fixed the bug in pbuild
[10:20pm] mab|ds9: Is it orthogonal to the other race condition then I assume?
[10:21pm] gfurnish: I think so
```


Issue created by migration from https://trac.sagemath.org/ticket/4711





---

archive/issue_comments_035451.json:
```json
{
    "body": "Gary,\n\nit would be excellent if you could make this a priority since I have been hitting this race condition way more often than I used to.\n\nCheers,\n\nMichael",
    "created_at": "2008-12-10T10:04:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4711",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4711#issuecomment-35451",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Gary,

it would be excellent if you could make this a priority since I have been hitting this race condition way more often than I used to.

Cheers,

Michael



---

archive/issue_comments_035452.json:
```json
{
    "body": "Changing priority from major to blocker.",
    "created_at": "2008-12-10T10:04:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4711",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4711#issuecomment-35452",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Changing priority from major to blocker.



---

archive/issue_comments_035453.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2008-12-11T14:14:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4711",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4711#issuecomment-35453",
    "user": "https://github.com/garyfurnish"
}
```

Changing status from new to assigned.



---

archive/issue_comments_035454.json:
```json
{
    "body": "This is fixed by #4699 because previously threads were changing the current directory, and current directory is a per process state and not a per thread state.  By switching to pyprocessing, which uses processes instead of threads, the problem is removed.",
    "created_at": "2008-12-11T14:14:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4711",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4711#issuecomment-35454",
    "user": "https://github.com/garyfurnish"
}
```

This is fixed by #4699 because previously threads were changing the current directory, and current directory is a per process state and not a per thread state.  By switching to pyprocessing, which uses processes instead of threads, the problem is removed.



---

archive/issue_comments_035455.json:
```json
{
    "body": "Fixed by #4699 merged in Sage 3.2.2.alpha2",
    "created_at": "2008-12-11T15:03:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4711",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4711#issuecomment-35455",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Fixed by #4699 merged in Sage 3.2.2.alpha2



---

archive/issue_comments_035456.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-12-11T15:03:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4711",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4711#issuecomment-35456",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed



---

archive/issue_events_004956.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2008-12-11T15:03:51Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/4711",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/4711#event-4956"
}
```

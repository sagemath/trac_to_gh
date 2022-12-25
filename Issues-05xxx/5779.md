# Issue 5779: [with patch, positive review] _fast_floats_'s pow returns garbage for non-integral powers left of zero

archive/issues_005779.json:
```json
{
    "body": "Assignee: @robertwb\n\nCC:  cwitty\n\nI thought we had fixed this via fast_callable, but it is still there:\n\n```\nmabshoff@sage:/scratch/mabshoff/sage-3.4.1.rc3$ ./sage\n----------------------------------------------------------------------\n----------------------------------------------------------------------\nsage: f=x^(1/3)\nsage: f._fast_float_(x)(-1.2)\nnan\nsage: \n```\nThis is exposed via a plotting failure on Solaris where NaNs pop up. Fixing that in the plotting code is a different ticket William will open shortly.\n| Sage Version 3.4.1.rc2, Release Date: 2009-04-10                   |\n| Type notebook() for the GUI, and license() for information.        |\nCheers,\n\nMichael\n\nIssue created by migration from https://trac.sagemath.org/ticket/5779\n\n",
    "closed_at": "2009-04-16T07:41:28Z",
    "created_at": "2009-04-13T20:04:51Z",
    "labels": [
        "component: porting: solaris",
        "critical",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.4.1",
    "title": "[with patch, positive review] _fast_floats_'s pow returns garbage for non-integral powers left of zero",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/5779",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```
Assignee: @robertwb

CC:  cwitty

I thought we had fixed this via fast_callable, but it is still there:

```
mabshoff@sage:/scratch/mabshoff/sage-3.4.1.rc3$ ./sage
----------------------------------------------------------------------
----------------------------------------------------------------------
sage: f=x^(1/3)
sage: f._fast_float_(x)(-1.2)
nan
sage: 
```
This is exposed via a plotting failure on Solaris where NaNs pop up. Fixing that in the plotting code is a different ticket William will open shortly.
| Sage Version 3.4.1.rc2, Release Date: 2009-04-10                   |
| Type notebook() for the GUI, and license() for information.        |
Cheers,

Michael

Issue created by migration from https://trac.sagemath.org/ticket/5779





---

archive/issue_comments_045157.json:
```json
{
    "body": "Changing assignee from mabshoff to @robertwb.",
    "created_at": "2009-04-13T20:05:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5779",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5779#issuecomment-45157",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Changing assignee from mabshoff to @robertwb.



---

archive/issue_comments_045158.json:
```json
{
    "body": "Hmm, the c library is involved here as shown by this on Solaris:\n\n```\n-bash-3.00$ ./sage\n----------------------------------------------------------------------\n----------------------------------------------------------------------\nLoading Sage library. Current Mercurial branch is: main-sol\nsage: f=x^(1/3)\nsage: f._fast_float_(x)(-1.2)\n-NaN\n```\n| Sage Version 3.4.1.rc1, Release Date: 2009-04-05                   |\n| Type notebook() for the GUI, and license() for information.        |\nI am not so sure what is going on or if this is the real issue. I will talk to RobertWB in person about this on the next occasion.\n\nCheers,\n\nMichael",
    "created_at": "2009-04-13T20:13:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5779",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5779#issuecomment-45158",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Hmm, the c library is involved here as shown by this on Solaris:

```
-bash-3.00$ ./sage
----------------------------------------------------------------------
----------------------------------------------------------------------
Loading Sage library. Current Mercurial branch is: main-sol
sage: f=x^(1/3)
sage: f._fast_float_(x)(-1.2)
-NaN
```
| Sage Version 3.4.1.rc1, Release Date: 2009-04-05                   |
| Type notebook() for the GUI, and license() for information.        |
I am not so sure what is going on or if this is the real issue. I will talk to RobertWB in person about this on the next occasion.

Cheers,

Michael



---

archive/issue_comments_045159.json:
```json
{
    "body": "Hmm, the issue here might be plain and simply calling the math libraries pow() function.  So don't invalidate this ticket since we are definitely hitting some issue on Solaris here.\n\nCheers,\n\nMichael",
    "created_at": "2009-04-13T21:53:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5779",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5779#issuecomment-45159",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Hmm, the issue here might be plain and simply calling the math libraries pow() function.  So don't invalidate this ticket since we are definitely hitting some issue on Solaris here.

Cheers,

Michael



---

archive/issue_comments_045160.json:
```json
{
    "body": "I fixed the new fast float (fast callable) not the old one. However, the old one is a simple fix too--I'll post a patch shortly.",
    "created_at": "2009-04-13T22:24:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5779",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5779#issuecomment-45160",
    "user": "https://github.com/robertwb"
}
```

I fixed the new fast float (fast callable) not the old one. However, the old one is a simple fix too--I'll post a patch shortly.



---

archive/issue_comments_045161.json:
```json
{
    "body": "Replying to [comment:4 robertwb]:\n> I fixed the new fast float (fast callable) not the old one. However, the old one is a simple fix too--I'll post a patch shortly. \n\n\nCool, note that #5780 does fix an issue when the axes code in plotting encounters a NaN or Infinity, so you might want to apply that one before doctesting.\n\nCheers,\n\nMichael",
    "created_at": "2009-04-13T22:59:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5779",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5779#issuecomment-45161",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Replying to [comment:4 robertwb]:
> I fixed the new fast float (fast callable) not the old one. However, the old one is a simple fix too--I'll post a patch shortly. 


Cool, note that #5780 does fix an issue when the axes code in plotting encounters a NaN or Infinity, so you might want to apply that one before doctesting.

Cheers,

Michael



---

archive/issue_comments_045162.json:
```json
{
    "body": "Attachment [5779-fast-float-pow.patch](tarball://root/attachments/some-uuid/ticket5779/5779-fast-float-pow.patch) by @robertwb created at 2009-04-16 05:21:10\n\nOK, I did the same thing as for fast_callable.",
    "created_at": "2009-04-16T05:21:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5779",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5779#issuecomment-45162",
    "user": "https://github.com/robertwb"
}
```

Attachment [5779-fast-float-pow.patch](tarball://root/attachments/some-uuid/ticket5779/5779-fast-float-pow.patch) by @robertwb created at 2009-04-16 05:21:10

OK, I did the same thing as for fast_callable.



---

archive/issue_comments_045163.json:
```json
{
    "body": "I am happy with this patch even though it likely introduces a slowdown which I did not measure. Since correctness is more important than speed especially in light of completely wrong results I give this patch a positive review. All doctests do pass, too :)\n\nCheers,\n\nMichael",
    "created_at": "2009-04-16T07:40:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5779",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5779#issuecomment-45163",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

I am happy with this patch even though it likely introduces a slowdown which I did not measure. Since correctness is more important than speed especially in light of completely wrong results I give this patch a positive review. All doctests do pass, too :)

Cheers,

Michael



---

archive/issue_comments_045164.json:
```json
{
    "body": "Merged in Sage 3.4.1.rc3.\n\nCheers,\n\nMichael",
    "created_at": "2009-04-16T07:41:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5779",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5779#issuecomment-45164",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged in Sage 3.4.1.rc3.

Cheers,

Michael



---

archive/issue_events_013566.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2009-04-16T07:41:28Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/5779",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/5779#event-13566"
}
```



---

archive/issue_comments_045165.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-04-16T07:41:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5779",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5779#issuecomment-45165",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed

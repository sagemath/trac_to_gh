# Issue 3239: [with patch; needs review] cygwin polybori -- add Cygwin build support for polybori

archive/issues_003239.json:
```json
{
    "body": "Assignee: mabshoff\n\nCC:  polybori\n\nSee also #3195: add 64 bit OSX build support for polybori\n\nNew spkg here:\n\nhttp://sage.math.washington.edu/home/was/cygwin/polybori-0.3.1.p3.spkg\n\nIssue created by migration from https://trac.sagemath.org/ticket/3239\n\n",
    "created_at": "2008-05-17T17:03:47Z",
    "labels": [
        "component: porting: cygwin",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.0.2",
    "title": "[with patch; needs review] cygwin polybori -- add Cygwin build support for polybori",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/3239",
    "user": "https://github.com/williamstein"
}
```
Assignee: mabshoff

CC:  polybori

See also #3195: add 64 bit OSX build support for polybori

New spkg here:

http://sage.math.washington.edu/home/was/cygwin/polybori-0.3.1.p3.spkg

Issue created by migration from https://trac.sagemath.org/ticket/3239





---

archive/issue_comments_022379.json:
```json
{
    "body": "Attachment [cpu_stats.c.patch](tarball://root/attachments/some-uuid/ticket3239/cpu_stats.c.patch) by mabshoff created at 2008-05-18 13:46:38\n\nCygwin build fix",
    "created_at": "2008-05-18T13:46:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3239",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3239#issuecomment-22379",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Attachment [cpu_stats.c.patch](tarball://root/attachments/some-uuid/ticket3239/cpu_stats.c.patch) by mabshoff created at 2008-05-18 13:46:38

Cygwin build fix



---

archive/issue_comments_022380.json:
```json
{
    "body": "Cygwin python.exe fix",
    "created_at": "2008-05-18T13:47:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3239",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3239#issuecomment-22380",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Cygwin python.exe fix



---

archive/issue_comments_022381.json:
```json
{
    "body": "Attachment [SConstruct.cygwin.patch](tarball://root/attachments/some-uuid/ticket3239/SConstruct.cygwin.patch) by mabshoff created at 2008-05-18 13:49:27\n\nSpkg looks good to me. I checked in some diffs of all the patched files we use on Cygwin. I also attached those files to the ticket and added PolyBoRi to the CC field on this ticket so the changes can get cleaned up and integrated upstream [at least the SConstuct fix must be cleaned up].\n\nIn total: Positive review.\n\nCheers,\n\nMichael",
    "created_at": "2008-05-18T13:49:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3239",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3239#issuecomment-22381",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Attachment [SConstruct.cygwin.patch](tarball://root/attachments/some-uuid/ticket3239/SConstruct.cygwin.patch) by mabshoff created at 2008-05-18 13:49:27

Spkg looks good to me. I checked in some diffs of all the patched files we use on Cygwin. I also attached those files to the ticket and added PolyBoRi to the CC field on this ticket so the changes can get cleaned up and integrated upstream [at least the SConstuct fix must be cleaned up].

In total: Positive review.

Cheers,

Michael



---

archive/issue_comments_022382.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-05-18T13:49:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3239",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3239#issuecomment-22382",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_022383.json:
```json
{
    "body": "Merged in Sage 3.0.2.alpha1",
    "created_at": "2008-05-18T13:49:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3239",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3239#issuecomment-22383",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged in Sage 3.0.2.alpha1



---

archive/issue_events_007280.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2008-05-18T13:49:59Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/3239",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/3239#event-7280"
}
```



---

archive/issue_comments_022384.json:
```json
{
    "body": "Hi Michael,\ncould you check, whether SConstruct.generic.patch does the Job on cygwin? Also, the first part of the cpu_stats.c.patch could be avoided by setting the predefines more sensitive in the construct file. I'll have a look at that issue in the next days.\nBest regards,\n  Alexander",
    "created_at": "2008-05-18T22:56:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3239",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3239#issuecomment-22384",
    "user": "https://trac.sagemath.org/admin/accounts/users/PolyBoRi"
}
```

Hi Michael,
could you check, whether SConstruct.generic.patch does the Job on cygwin? Also, the first part of the cpu_stats.c.patch could be avoided by setting the predefines more sensitive in the construct file. I'll have a look at that issue in the next days.
Best regards,
  Alexander



---

archive/issue_comments_022385.json:
```json
{
    "body": "Replying to [comment:3 PolyBoRi]:\n> Hi Michael,\n> could you check, whether SConstruct.generic.patch does the Job on cygwin? Also, the first part of the cpu_stats.c.patch could be avoided by setting the predefines more sensitive in the construct file. I'll have a look at that issue in the next days.\n> Best regards,\n>   Alexander\n\nHi Alexander,\n\nthat looks like a likely fix. Right now I don't have a Cygwin env setup up to test, but it won't take long. \n\nRe cpu_stats.c: it looks like the sledge hammer approach and we conditionally copy it into the PolyBoRi tree on Cygwin only. Any cleaner solution is appreciated and I plan to write some Win2K+ specific patches that uses the native Windows infrastructure for accounting and memory consumption. I already did so for CoCoALib, so it should be an easy fix.\n\nCheers,\n\nMichael",
    "created_at": "2008-05-18T23:17:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3239",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3239#issuecomment-22385",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Replying to [comment:3 PolyBoRi]:
> Hi Michael,
> could you check, whether SConstruct.generic.patch does the Job on cygwin? Also, the first part of the cpu_stats.c.patch could be avoided by setting the predefines more sensitive in the construct file. I'll have a look at that issue in the next days.
> Best regards,
>   Alexander

Hi Alexander,

that looks like a likely fix. Right now I don't have a Cygwin env setup up to test, but it won't take long. 

Re cpu_stats.c: it looks like the sledge hammer approach and we conditionally copy it into the PolyBoRi tree on Cygwin only. Any cleaner solution is appreciated and I plan to write some Win2K+ specific patches that uses the native Windows infrastructure for accounting and memory consumption. I already did so for CoCoALib, so it should be an easy fix.

Cheers,

Michael



---

archive/issue_comments_022386.json:
```json
{
    "body": "More generic patch, which obsoletes both patches above",
    "created_at": "2008-05-18T23:21:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3239",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3239#issuecomment-22386",
    "user": "https://trac.sagemath.org/admin/accounts/users/PolyBoRi"
}
```

More generic patch, which obsoletes both patches above



---

archive/issue_comments_022387.json:
```json
{
    "body": "Attachment [SConstruct.generic.patch](tarball://root/attachments/some-uuid/ticket3239/SConstruct.generic.patch) by PolyBoRi created at 2008-05-18 23:25:11\n\nHi Michael,\n> that looks like a likely fix. Right now I don't have a Cygwin env setup up to test, but it won't take long. \n> \n> Re cpu_stats.c: it looks like the sledge hammer approach and we conditionally copy it into the PolyBoRi tree on Cygwin only. Any cleaner solution is appreciated and I plan to write some Win2K+ specific patches that uses the native Windows infrastructure for accounting and memory consumption. I already did so for CoCoALib, so it should be an easy fix.\nI've uploaded an extended version of the patch, which should fix both problems from SConstruct, so the cpu_stats.c patch will be obsolete.\n\nBest regards,\n  Alexander",
    "created_at": "2008-05-18T23:25:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3239",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3239#issuecomment-22387",
    "user": "https://trac.sagemath.org/admin/accounts/users/PolyBoRi"
}
```

Attachment [SConstruct.generic.patch](tarball://root/attachments/some-uuid/ticket3239/SConstruct.generic.patch) by PolyBoRi created at 2008-05-18 23:25:11

Hi Michael,
> that looks like a likely fix. Right now I don't have a Cygwin env setup up to test, but it won't take long. 
> 
> Re cpu_stats.c: it looks like the sledge hammer approach and we conditionally copy it into the PolyBoRi tree on Cygwin only. Any cleaner solution is appreciated and I plan to write some Win2K+ specific patches that uses the native Windows infrastructure for accounting and memory consumption. I already did so for CoCoALib, so it should be an easy fix.
I've uploaded an extended version of the patch, which should fix both problems from SConstruct, so the cpu_stats.c patch will be obsolete.

Best regards,
  Alexander

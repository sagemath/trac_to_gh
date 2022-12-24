# Issue 3239: [with patch; needs review] cygwin polybori -- add Cygwin build support for polybori

archive/issues_003239.json:
```json
{
    "body": "Assignee: mabshoff\n\nCC:  polybori\n\nSee also #3195: add 64 bit OSX build support for polybori\n\nNew spkg here:\n\nhttp://sage.math.washington.edu/home/was/cygwin/polybori-0.3.1.p3.spkg\n\nIssue created by migration from https://trac.sagemath.org/ticket/3239\n\n",
    "created_at": "2008-05-17T17:03:47Z",
    "labels": [
        "porting: Cygwin",
        "major",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.0.2",
    "title": "[with patch; needs review] cygwin polybori -- add Cygwin build support for polybori",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/3239",
    "user": "@williamstein"
}
```
Assignee: mabshoff

CC:  polybori

See also #3195: add 64 bit OSX build support for polybori

New spkg here:

http://sage.math.washington.edu/home/was/cygwin/polybori-0.3.1.p3.spkg

Issue created by migration from https://trac.sagemath.org/ticket/3239





---

archive/issue_comments_022426.json:
```json
{
    "body": "Attachment [cpu_stats.c.patch](tarball://root/attachments/some-uuid/ticket3239/cpu_stats.c.patch) by mabshoff created at 2008-05-18 13:46:38\n\nCygwin build fix",
    "created_at": "2008-05-18T13:46:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3239",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3239#issuecomment-22426",
    "user": "mabshoff"
}
```

Attachment [cpu_stats.c.patch](tarball://root/attachments/some-uuid/ticket3239/cpu_stats.c.patch) by mabshoff created at 2008-05-18 13:46:38

Cygwin build fix



---

archive/issue_comments_022427.json:
```json
{
    "body": "Cygwin python.exe fix",
    "created_at": "2008-05-18T13:47:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3239",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3239#issuecomment-22427",
    "user": "mabshoff"
}
```

Cygwin python.exe fix



---

archive/issue_comments_022428.json:
```json
{
    "body": "Attachment [SConstruct.cygwin.patch](tarball://root/attachments/some-uuid/ticket3239/SConstruct.cygwin.patch) by mabshoff created at 2008-05-18 13:49:27\n\nSpkg looks good to me. I checked in some diffs of all the patched files we use on Cygwin. I also attached those files to the ticket and added PolyBoRi to the CC field on this ticket so the changes can get cleaned up and integrated upstream [at least the SConstuct fix must be cleaned up].\n\nIn total: Positive review.\n\nCheers,\n\nMichael",
    "created_at": "2008-05-18T13:49:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3239",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3239#issuecomment-22428",
    "user": "mabshoff"
}
```

Attachment [SConstruct.cygwin.patch](tarball://root/attachments/some-uuid/ticket3239/SConstruct.cygwin.patch) by mabshoff created at 2008-05-18 13:49:27

Spkg looks good to me. I checked in some diffs of all the patched files we use on Cygwin. I also attached those files to the ticket and added PolyBoRi to the CC field on this ticket so the changes can get cleaned up and integrated upstream [at least the SConstuct fix must be cleaned up].

In total: Positive review.

Cheers,

Michael



---

archive/issue_comments_022429.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-05-18T13:49:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3239",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3239#issuecomment-22429",
    "user": "mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_022430.json:
```json
{
    "body": "Merged in Sage 3.0.2.alpha1",
    "created_at": "2008-05-18T13:49:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3239",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3239#issuecomment-22430",
    "user": "mabshoff"
}
```

Merged in Sage 3.0.2.alpha1



---

archive/issue_comments_022431.json:
```json
{
    "body": "Hi Michael,\ncould you check, whether SConstruct.generic.patch does the Job on cygwin? Also, the first part of the cpu_stats.c.patch could be avoided by setting the predefines more sensitive in the construct file. I'll have a look at that issue in the next days.\nBest regards,\n  Alexander",
    "created_at": "2008-05-18T22:56:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3239",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3239#issuecomment-22431",
    "user": "PolyBoRi"
}
```

Hi Michael,
could you check, whether SConstruct.generic.patch does the Job on cygwin? Also, the first part of the cpu_stats.c.patch could be avoided by setting the predefines more sensitive in the construct file. I'll have a look at that issue in the next days.
Best regards,
  Alexander



---

archive/issue_comments_022432.json:
```json
{
    "body": "Replying to [comment:3 PolyBoRi]:\n> Hi Michael,\n> could you check, whether SConstruct.generic.patch does the Job on cygwin? Also, the first part of the cpu_stats.c.patch could be avoided by setting the predefines more sensitive in the construct file. I'll have a look at that issue in the next days.\n> Best regards,\n>   Alexander\n\nHi Alexander,\n\nthat looks like a likely fix. Right now I don't have a Cygwin env setup up to test, but it won't take long. \n\nRe cpu_stats.c: it looks like the sledge hammer approach and we conditionally copy it into the PolyBoRi tree on Cygwin only. Any cleaner solution is appreciated and I plan to write some Win2K+ specific patches that uses the native Windows infrastructure for accounting and memory consumption. I already did so for CoCoALib, so it should be an easy fix.\n\nCheers,\n\nMichael",
    "created_at": "2008-05-18T23:17:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3239",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3239#issuecomment-22432",
    "user": "mabshoff"
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

archive/issue_comments_022433.json:
```json
{
    "body": "More generic patch, which obsoletes both patches above",
    "created_at": "2008-05-18T23:21:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3239",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3239#issuecomment-22433",
    "user": "PolyBoRi"
}
```

More generic patch, which obsoletes both patches above



---

archive/issue_comments_022434.json:
```json
{
    "body": "Attachment [SConstruct.generic.patch](tarball://root/attachments/some-uuid/ticket3239/SConstruct.generic.patch) by PolyBoRi created at 2008-05-18 23:25:11\n\nHi Michael,\n> that looks like a likely fix. Right now I don't have a Cygwin env setup up to test, but it won't take long. \n> \n> Re cpu_stats.c: it looks like the sledge hammer approach and we conditionally copy it into the PolyBoRi tree on Cygwin only. Any cleaner solution is appreciated and I plan to write some Win2K+ specific patches that uses the native Windows infrastructure for accounting and memory consumption. I already did so for CoCoALib, so it should be an easy fix.\nI've uploaded an extended version of the patch, which should fix both problems from SConstruct, so the cpu_stats.c patch will be obsolete.\n\nBest regards,\n  Alexander",
    "created_at": "2008-05-18T23:25:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3239",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3239#issuecomment-22434",
    "user": "PolyBoRi"
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

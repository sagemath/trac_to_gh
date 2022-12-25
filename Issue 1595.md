# Issue 1595: do something about the pari overflow test

archive/issues_001595.json:
```json
{
    "body": "Assignee: failure\n\nThis disturbs people:\n\n```\nsage -t  devel/sage-main/sage/libs/pari/gen.pyx             python(85565) malloc: *** mmap(size=4096000000) failed (error code=12)\n*** error: can't allocate region\n*** set a breakpoint in malloc_error_break to debug\n```\n\n\nThis would disturb people less:\n\n```\n[[The following doctest contains an intentional memory error.]]\nsage -t  devel/sage-main/sage/libs/pari/gen.pyx             python(85565) malloc: *** mmap(size=4096000000) failed (error code=12)\n*** error: can't allocate region\n*** set a breakpoint in malloc_error_break to debug\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/1595\n\n",
    "created_at": "2007-12-24T18:43:56Z",
    "labels": [
        "component: doctest coverage",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.4.1",
    "title": "do something about the pari overflow test",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/1595",
    "user": "https://github.com/williamstein"
}
```
Assignee: failure

This disturbs people:

```
sage -t  devel/sage-main/sage/libs/pari/gen.pyx             python(85565) malloc: *** mmap(size=4096000000) failed (error code=12)
*** error: can't allocate region
*** set a breakpoint in malloc_error_break to debug
```


This would disturb people less:

```
[[The following doctest contains an intentional memory error.]]
sage -t  devel/sage-main/sage/libs/pari/gen.pyx             python(85565) malloc: *** mmap(size=4096000000) failed (error code=12)
*** error: can't allocate region
*** set a breakpoint in malloc_error_break to debug
```


Issue created by migration from https://trac.sagemath.org/ticket/1595





---

archive/issue_comments_010121.json:
```json
{
    "body": "The issue has been added to the FAQ. It might be easiest to direct stderr to some file. That way people should never see the offending message.\n\nCheers,\n\nMichael",
    "created_at": "2007-12-25T09:33:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1595",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1595#issuecomment-10121",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

The issue has been added to the FAQ. It might be easiest to direct stderr to some file. That way people should never see the offending message.

Cheers,

Michael



---

archive/issue_comments_010122.json:
```json
{
    "body": "Changing type from defect to enhancement.",
    "created_at": "2009-01-22T18:24:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1595",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1595#issuecomment-10122",
    "user": "https://github.com/aghitza"
}
```

Changing type from defect to enhancement.



---

archive/issue_comments_010123.json:
```json
{
    "body": "On OSX 10.5 64 bit, FreeBSD 7 as well as Solaris Sparc this overflow test leads to a segfault/failed test. I am not sure what to do with this test since the fact that it worked purely depends on the OS behavior for large allocs. \n\nMaybe making it \"optional -- large\" or \"optional -- $SOME_OS_LIST\" would be a way out of this. Anyway, there seems to be no reliable way to test the allocation of huge amounts of memory and expect the Sage session to survive.\n\nCheers,\n\nMichael",
    "created_at": "2009-02-08T03:18:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1595",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1595#issuecomment-10123",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

On OSX 10.5 64 bit, FreeBSD 7 as well as Solaris Sparc this overflow test leads to a segfault/failed test. I am not sure what to do with this test since the fact that it worked purely depends on the OS behavior for large allocs. 

Maybe making it "optional -- large" or "optional -- $SOME_OS_LIST" would be a way out of this. Anyway, there seems to be no reliable way to test the allocation of huge amounts of memory and expect the Sage session to survive.

Cheers,

Michael



---

archive/issue_comments_010124.json:
```json
{
    "body": "Attachment [gen.patch](tarball://root/attachments/some-uuid/ticket1595/gen.patch) by @williamstein created at 2009-04-08 00:57:43",
    "created_at": "2009-04-08T00:57:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1595",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1595#issuecomment-10124",
    "user": "https://github.com/williamstein"
}
```

Attachment [gen.patch](tarball://root/attachments/some-uuid/ticket1595/gen.patch) by @williamstein created at 2009-04-08 00:57:43



---

archive/issue_comments_010125.json:
```json
{
    "body": "Positive review.\n\nCheers,\n\nMichael",
    "created_at": "2009-04-08T01:04:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1595",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1595#issuecomment-10125",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Positive review.

Cheers,

Michael



---

archive/issue_comments_010126.json:
```json
{
    "body": "Oops, change the summary, too.\n\nCheers,\n\nMichael",
    "created_at": "2009-04-08T04:29:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1595",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1595#issuecomment-10126",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Oops, change the summary, too.

Cheers,

Michael



---

archive/issue_comments_010127.json:
```json
{
    "body": "Ooops, this patch needs to be rebased for 3.4.1.rc1 - new patch coming up in the morning.\n\nCheers,\n\nMichael",
    "created_at": "2009-04-08T10:46:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1595",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1595#issuecomment-10127",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Ooops, this patch needs to be rebased for 3.4.1.rc1 - new patch coming up in the morning.

Cheers,

Michael



---

archive/issue_comments_010128.json:
```json
{
    "body": "Attachment [trac_1595-rebase.patch](tarball://root/attachments/some-uuid/ticket1595/trac_1595-rebase.patch) by mabshoff created at 2009-04-09 02:22:50\n\nMerged trac_1595-rebase.patch in Sage 3.4.1.rc2.\n\nCheers,\n\nMichael",
    "created_at": "2009-04-09T02:22:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1595",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1595#issuecomment-10128",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Attachment [trac_1595-rebase.patch](tarball://root/attachments/some-uuid/ticket1595/trac_1595-rebase.patch) by mabshoff created at 2009-04-09 02:22:50

Merged trac_1595-rebase.patch in Sage 3.4.1.rc2.

Cheers,

Michael



---

archive/issue_events_001753.json:
```json
{
    "actor": "mabshoff",
    "created_at": "2009-04-09T02:22:50Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/1595",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/1595#event-1753"
}
```



---

archive/issue_comments_010129.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-04-09T02:22:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1595",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1595#issuecomment-10129",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed

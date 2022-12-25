# Issue 2099: Make sage-test execute multiple doctests in parallel

archive/issues_002099.json:
```json
{
    "body": "Assignee: @ncalexan\n\nCC:  ncalexander@gmail.com\n\nKeywords: sage test doctest multiple parallel\n\nIt would greatly speed testing if `sage-test` doctested multiple files in parallel.\n\nIssue created by migration from https://trac.sagemath.org/ticket/2099\n\n",
    "created_at": "2008-02-08T04:40:23Z",
    "labels": [
        "component: doctest coverage"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-2.10.3",
    "title": "Make sage-test execute multiple doctests in parallel",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/2099",
    "user": "https://github.com/ncalexan"
}
```
Assignee: @ncalexan

CC:  ncalexander@gmail.com

Keywords: sage test doctest multiple parallel

It would greatly speed testing if `sage-test` doctested multiple files in parallel.

Issue created by migration from https://trac.sagemath.org/ticket/2099





---

archive/issue_comments_013548.json:
```json
{
    "body": "Mike Abshoff suggested a short document explaining how the current doctesting system is organized.  I have attached a preliminary version of this document.",
    "created_at": "2008-02-08T04:41:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2099",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2099#issuecomment-13548",
    "user": "https://github.com/ncalexan"
}
```

Mike Abshoff suggested a short document explaining how the current doctesting system is organized.  I have attached a preliminary version of this document.



---

archive/issue_comments_013549.json:
```json
{
    "body": "Attachment [sage-doctesting.tex](tarball://root/attachments/some-uuid/ticket2099/sage-doctesting.tex) by @ncalexan created at 2008-02-08 04:42:45",
    "created_at": "2008-02-08T04:42:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2099",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2099#issuecomment-13549",
    "user": "https://github.com/ncalexan"
}
```

Attachment [sage-doctesting.tex](tarball://root/attachments/some-uuid/ticket2099/sage-doctesting.tex) by @ncalexan created at 2008-02-08 04:42:45



---

archive/issue_comments_013550.json:
```json
{
    "body": "Attachment [ncalexan-parallel-testing-1.hg](tarball://root/attachments/some-uuid/ticket2099/ncalexan-parallel-testing-1.hg) by @ncalexan created at 2008-02-09 02:36:00",
    "created_at": "2008-02-09T02:36:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2099",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2099#issuecomment-13550",
    "user": "https://github.com/ncalexan"
}
```

Attachment [ncalexan-parallel-testing-1.hg](tarball://root/attachments/some-uuid/ticket2099/ncalexan-parallel-testing-1.hg) by @ncalexan created at 2008-02-09 02:36:00



---

archive/issue_comments_013551.json:
```json
{
    "body": "The patch `ncalexan-parallel-testing-1.hg` applies to `hg_scripts` in `local/bin`.",
    "created_at": "2008-02-09T02:36:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2099",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2099#issuecomment-13551",
    "user": "https://github.com/ncalexan"
}
```

The patch `ncalexan-parallel-testing-1.hg` applies to `hg_scripts` in `local/bin`.



---

archive/issue_comments_013552.json:
```json
{
    "body": "Attachment [2099-ncalexan-parallel-testing-2.hg](tarball://root/attachments/some-uuid/ticket2099/2099-ncalexan-parallel-testing-2.hg) by @ncalexan created at 2008-02-10 11:05:16",
    "created_at": "2008-02-10T11:05:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2099",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2099#issuecomment-13552",
    "user": "https://github.com/ncalexan"
}
```

Attachment [2099-ncalexan-parallel-testing-2.hg](tarball://root/attachments/some-uuid/ticket2099/2099-ncalexan-parallel-testing-2.hg) by @ncalexan created at 2008-02-10 11:05:16



---

archive/issue_comments_013553.json:
```json
{
    "body": "`2099-ncalexan-parallel-testing-2.hg` should not depend on the earlier bundle.\n\nThis is a work in progress bundle that improves option parsing and makes 'test via make' the only option.  It improves `sage-doctest` slightly and tries to write a `Makefile.doctest` that can be run via command-line `make`.\n\nUse two dashes (`--`) for options.\n\nOutput is not yet collated.  Timeouts are not yet implemented.",
    "created_at": "2008-02-10T11:07:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2099",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2099#issuecomment-13553",
    "user": "https://github.com/ncalexan"
}
```

`2099-ncalexan-parallel-testing-2.hg` should not depend on the earlier bundle.

This is a work in progress bundle that improves option parsing and makes 'test via make' the only option.  It improves `sage-doctest` slightly and tries to write a `Makefile.doctest` that can be run via command-line `make`.

Use two dashes (`--`) for options.

Output is not yet collated.  Timeouts are not yet implemented.



---

archive/issue_comments_013554.json:
```json
{
    "body": "Attachment [2099-ncalexan-parallel-testing-3.hg](tarball://root/attachments/some-uuid/ticket2099/2099-ncalexan-parallel-testing-3.hg) by @ncalexan created at 2008-02-15 01:36:35\n\n`2099-ncalexan-parallel-testing-3.hg` should not depend on earlier bundles.\n\nThis is a work in progress bundle that adds\n* working per-test timeouts\n* parsing SAGE_DOCTEST_OPTIONAL, _LONG, _TIMEOUT from the environment\n* output via -o OUTFILE\n* improves handling of sage-doctest crashing\n\n\n```\n[5:25pm] ncalexan: mabshoff: I have parallel testing with output and timeout working, or mostly working.\n[5:25pm] mabshoff: ncalexan: cool\n[5:26pm] ncalexan: mabshoff: I can't think of a way to get partial output correct.  You can display it while it comes, but if you don't wait until the entire test is done, you won't get the sorted output.\n[5:26pm] ncalexan: I'll post another bundle.\n[5:26pm] ncalexan: Use -v for verbose, -q for quiet, -o OUTFILE.\n[5:26pm] ncalexan: (All to sage-test or sage -t)\n```\n",
    "created_at": "2008-02-15T01:36:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2099",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2099#issuecomment-13554",
    "user": "https://github.com/ncalexan"
}
```

Attachment [2099-ncalexan-parallel-testing-3.hg](tarball://root/attachments/some-uuid/ticket2099/2099-ncalexan-parallel-testing-3.hg) by @ncalexan created at 2008-02-15 01:36:35

`2099-ncalexan-parallel-testing-3.hg` should not depend on earlier bundles.

This is a work in progress bundle that adds
* working per-test timeouts
* parsing SAGE_DOCTEST_OPTIONAL, _LONG, _TIMEOUT from the environment
* output via -o OUTFILE
* improves handling of sage-doctest crashing


```
[5:25pm] ncalexan: mabshoff: I have parallel testing with output and timeout working, or mostly working.
[5:25pm] mabshoff: ncalexan: cool
[5:26pm] ncalexan: mabshoff: I can't think of a way to get partial output correct.  You can display it while it comes, but if you don't wait until the entire test is done, you won't get the sorted output.
[5:26pm] ncalexan: I'll post another bundle.
[5:26pm] ncalexan: Use -v for verbose, -q for quiet, -o OUTFILE.
[5:26pm] ncalexan: (All to sage-test or sage -t)
```




---

archive/issue_comments_013555.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2008-03-02T23:05:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2099",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2099#issuecomment-13555",
    "user": "https://github.com/garyfurnish"
}
```

Changing status from new to assigned.



---

archive/issue_comments_013556.json:
```json
{
    "body": "Changing assignee from @ncalexan to @garyfurnish.",
    "created_at": "2008-03-02T23:05:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2099",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2099#issuecomment-13556",
    "user": "https://github.com/garyfurnish"
}
```

Changing assignee from @ncalexan to @garyfurnish.



---

archive/issue_comments_013557.json:
```json
{
    "body": "This creates sage-ptest for parallel test.  The first argument is equivalent to -j (the number of parallel tests to run).  The rest of the arguments are as normal.",
    "created_at": "2008-03-03T02:13:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2099",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2099#issuecomment-13557",
    "user": "https://github.com/garyfurnish"
}
```

This creates sage-ptest for parallel test.  The first argument is equivalent to -j (the number of parallel tests to run).  The rest of the arguments are as normal.



---

archive/issue_comments_013558.json:
```json
{
    "body": "sage-ptest",
    "created_at": "2008-03-03T02:14:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2099",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2099#issuecomment-13558",
    "user": "https://github.com/garyfurnish"
}
```

sage-ptest



---

archive/issue_comments_013559.json:
```json
{
    "body": "Attachment [trac_2999.patch](tarball://root/attachments/some-uuid/ticket2099/trac_2999.patch) by mabshoff created at 2008-03-03 04:53:22\n\ntrac_2999.patch replaces all the other patches (with the exception of a minimal fix to `sage -test`. I give it a positive review.\n\nCheers,\n\nMichael",
    "created_at": "2008-03-03T04:53:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2099",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2099#issuecomment-13559",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Attachment [trac_2999.patch](tarball://root/attachments/some-uuid/ticket2099/trac_2999.patch) by mabshoff created at 2008-03-03 04:53:22

trac_2999.patch replaces all the other patches (with the exception of a minimal fix to `sage -test`. I give it a positive review.

Cheers,

Michael



---

archive/issue_comments_013560.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-03-03T04:55:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2099",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2099#issuecomment-13560",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed



---

archive/issue_events_002259.json:
```json
{
    "actor": "mabshoff",
    "created_at": "2008-03-03T04:55:40Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/2099",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/2099#event-2259"
}
```



---

archive/issue_comments_013561.json:
```json
{
    "body": "Merged in Sage 2.10.3.rc1",
    "created_at": "2008-03-03T04:55:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2099",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2099#issuecomment-13561",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged in Sage 2.10.3.rc1

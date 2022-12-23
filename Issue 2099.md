# Issue 2099: Make sage-test execute multiple doctests in parallel

archive/issues_002099.json:
```json
{
    "body": "Assignee: ncalexan\n\nCC:  ncalexander@gmail.com\n\nKeywords: sage test doctest multiple parallel\n\nIt would greatly speed testing if `sage-test` doctested multiple files in parallel.\n\nIssue created by migration from https://trac.sagemath.org/ticket/2099\n\n",
    "created_at": "2008-02-08T04:40:23Z",
    "labels": [
        "doctest coverage",
        "major",
        "enhancement"
    ],
    "title": "Make sage-test execute multiple doctests in parallel",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/2099",
    "user": "ncalexan"
}
```
Assignee: ncalexan

CC:  ncalexander@gmail.com

Keywords: sage test doctest multiple parallel

It would greatly speed testing if `sage-test` doctested multiple files in parallel.

Issue created by migration from https://trac.sagemath.org/ticket/2099





---

archive/issue_comments_013579.json:
```json
{
    "body": "Mike Abshoff suggested a short document explaining how the current doctesting system is organized.  I have attached a preliminary version of this document.",
    "created_at": "2008-02-08T04:41:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2099",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2099#issuecomment-13579",
    "user": "ncalexan"
}
```

Mike Abshoff suggested a short document explaining how the current doctesting system is organized.  I have attached a preliminary version of this document.



---

archive/issue_comments_013580.json:
```json
{
    "body": "Attachment",
    "created_at": "2008-02-08T04:42:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2099",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2099#issuecomment-13580",
    "user": "ncalexan"
}
```

Attachment



---

archive/issue_comments_013581.json:
```json
{
    "body": "Attachment",
    "created_at": "2008-02-09T02:36:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2099",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2099#issuecomment-13581",
    "user": "ncalexan"
}
```

Attachment



---

archive/issue_comments_013582.json:
```json
{
    "body": "The patch `ncalexan-parallel-testing-1.hg` applies to `hg_scripts` in `local/bin`.",
    "created_at": "2008-02-09T02:36:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2099",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2099#issuecomment-13582",
    "user": "ncalexan"
}
```

The patch `ncalexan-parallel-testing-1.hg` applies to `hg_scripts` in `local/bin`.



---

archive/issue_comments_013583.json:
```json
{
    "body": "Attachment",
    "created_at": "2008-02-10T11:05:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2099",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2099#issuecomment-13583",
    "user": "ncalexan"
}
```

Attachment



---

archive/issue_comments_013584.json:
```json
{
    "body": "`2099-ncalexan-parallel-testing-2.hg` should not depend on the earlier bundle.\n\nThis is a work in progress bundle that improves option parsing and makes 'test via make' the only option.  It improves `sage-doctest` slightly and tries to write a `Makefile.doctest` that can be run via command-line `make`.\n\nUse two dashes (`--`) for options.\n\nOutput is not yet collated.  Timeouts are not yet implemented.",
    "created_at": "2008-02-10T11:07:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2099",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2099#issuecomment-13584",
    "user": "ncalexan"
}
```

`2099-ncalexan-parallel-testing-2.hg` should not depend on the earlier bundle.

This is a work in progress bundle that improves option parsing and makes 'test via make' the only option.  It improves `sage-doctest` slightly and tries to write a `Makefile.doctest` that can be run via command-line `make`.

Use two dashes (`--`) for options.

Output is not yet collated.  Timeouts are not yet implemented.



---

archive/issue_comments_013585.json:
```json
{
    "body": "Attachment\n\n`2099-ncalexan-parallel-testing-3.hg` should not depend on earlier bundles.\n\nThis is a work in progress bundle that adds\n* working per-test timeouts\n* parsing SAGE_DOCTEST_OPTIONAL, _LONG, _TIMEOUT from the environment\n* output via -o OUTFILE\n* improves handling of sage-doctest crashing\n\n\n```\n[5:25pm] ncalexan: mabshoff: I have parallel testing with output and timeout working, or mostly working.\n[5:25pm] mabshoff: ncalexan: cool\n[5:26pm] ncalexan: mabshoff: I can't think of a way to get partial output correct.  You can display it while it comes, but if you don't wait until the entire test is done, you won't get the sorted output.\n[5:26pm] ncalexan: I'll post another bundle.\n[5:26pm] ncalexan: Use -v for verbose, -q for quiet, -o OUTFILE.\n[5:26pm] ncalexan: (All to sage-test or sage -t)\n```\n",
    "created_at": "2008-02-15T01:36:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2099",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2099#issuecomment-13585",
    "user": "ncalexan"
}
```

Attachment

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

archive/issue_comments_013586.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2008-03-02T23:05:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2099",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2099#issuecomment-13586",
    "user": "gfurnish"
}
```

Changing status from new to assigned.



---

archive/issue_comments_013587.json:
```json
{
    "body": "Changing assignee from ncalexan to gfurnish.",
    "created_at": "2008-03-02T23:05:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2099",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2099#issuecomment-13587",
    "user": "gfurnish"
}
```

Changing assignee from ncalexan to gfurnish.



---

archive/issue_comments_013588.json:
```json
{
    "body": "This creates sage-ptest for parallel test.  The first argument is equivalent to -j (the number of parallel tests to run).  The rest of the arguments are as normal.",
    "created_at": "2008-03-03T02:13:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2099",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2099#issuecomment-13588",
    "user": "gfurnish"
}
```

This creates sage-ptest for parallel test.  The first argument is equivalent to -j (the number of parallel tests to run).  The rest of the arguments are as normal.



---

archive/issue_comments_013589.json:
```json
{
    "body": "sage-ptest",
    "created_at": "2008-03-03T02:14:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2099",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2099#issuecomment-13589",
    "user": "gfurnish"
}
```

sage-ptest



---

archive/issue_comments_013590.json:
```json
{
    "body": "Attachment\n\ntrac_2999.patch replaces all the other patches (with the exception of a minimal fix to `sage -test`. I give it a positive review.\n\nCheers,\n\nMichael",
    "created_at": "2008-03-03T04:53:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2099",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2099#issuecomment-13590",
    "user": "mabshoff"
}
```

Attachment

trac_2999.patch replaces all the other patches (with the exception of a minimal fix to `sage -test`. I give it a positive review.

Cheers,

Michael



---

archive/issue_comments_013591.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-03-03T04:55:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2099",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2099#issuecomment-13591",
    "user": "mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_013592.json:
```json
{
    "body": "Merged in Sage 2.10.3.rc1",
    "created_at": "2008-03-03T04:55:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2099",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2099#issuecomment-13592",
    "user": "mabshoff"
}
```

Merged in Sage 2.10.3.rc1
